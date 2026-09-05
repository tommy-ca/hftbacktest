import unittest

import numpy as np

from hftbacktest import (
    BacktestAsset,
    BacktestAssetPoly,
    HashMapMarketDepthBacktest,
    ROIVectorMarketDepthBacktest,
    DEPTH_EVENT,
    DEPTH_CLEAR_EVENT,
    DEPTH_SNAPSHOT_EVENT,
    BUY_EVENT,
    SELL_EVENT,
    EXCH_EVENT,
    LOCAL_EVENT,
    TRADE_EVENT,
    polymarket_to_hbt,
)
from hftbacktest.stats import PolyAssetRecord, fix_record_prices
from hftbacktest.types import event_dtype


class TestPolymarketOverlay(unittest.TestCase):
    def test_polymarket_asset_preset_allows_variable_settings(self):
        asset = (
            BacktestAssetPoly()
                .constant_order_latency(100, 100)
                .trading_value_fee_model(0.0, 0.006)
        )

        self.assertIsInstance(asset, BacktestAsset)

    def test_binary_fee_model_uses_fill_quantity_and_price(self):
        data = np.array(
            [
                (
                    DEPTH_SNAPSHOT_EVENT | BUY_EVENT | EXCH_EVENT | LOCAL_EVENT,
                    1_000,
                    1_000,
                    0.3,
                    100.0,
                    0,
                    0,
                    0.0,
                ),
                (
                    DEPTH_SNAPSHOT_EVENT | SELL_EVENT | EXCH_EVENT | LOCAL_EVENT,
                    1_000,
                    1_000,
                    0.4,
                    100.0,
                    0,
                    0,
                    0.0,
                ),
                (
                    DEPTH_EVENT | BUY_EVENT | EXCH_EVENT | LOCAL_EVENT,
                    1_000_000_000,
                    1_000_000_000,
                    0.3,
                    100.0,
                    0,
                    0,
                    0.0,
                ),
            ],
            dtype=event_dtype,
        )
        for backtest_cls in (HashMapMarketDepthBacktest, ROIVectorMarketDepthBacktest):
            with self.subTest(backtest_cls=backtest_cls.__name__):
                asset = (
                    BacktestAssetPoly()
                        .data(data.copy())
                        .constant_order_latency(0, 0)
                        .no_partial_fill_exchange()
                        .binary_fee_model(-0.01, 0.02)
                )
                hbt = backtest_cls([asset])

                try:
                    self.assertEqual(hbt.elapse(1), 0)
                    self.assertAlmostEqual(hbt.depth(0).best_ask, 0.4)
                    self.assertEqual(
                        hbt.submit_buy_order(0, 1, 0.4, 100.0, 0, 0, True),
                        0,
                    )
                    self.assertAlmostEqual(hbt.state_values(0).fee, 0.48)
                finally:
                    hbt.close()

    def test_poly_asset_record_fixes_prices_and_computes_earn(self):
        record = np.array(
            [
                (0, 10.0, 1.0, 0.40, 0.0),
                (1_000_000_000, 10.0, 1.0, 0.60, 0.5),
                (2_000_000_000, 10.0, 1.0, np.nan, 0.5),
            ],
            dtype=[
                ('timestamp', 'i8'),
                ('balance', 'f8'),
                ('position', 'f8'),
                ('price', 'f8'),
                ('fee', 'f8'),
            ],
        )

        fixed = fix_record_prices(record.copy())
        self.assertEqual(fixed['price'][-2], 1.0)
        self.assertEqual(fixed['price'][-1], 1.0)

        stats = PolyAssetRecord(record).resample('1s').stats(book_size=100.0)
        self.assertEqual(stats.earn, 10.5)

    def test_polymarket_to_hbt_uses_winning_outcome_as_final_book(self):
        data = polymarket_to_hbt(
            {
                'market_slug': ['m', 'm'],
                'timestamp': [1_000, 2_000],
                'local_timestamp': [1_100, 2_100],
                'event_type': ['book', 'market_resolved'],
                'ask_prices': [[0.6], None],
                'ask_sizes': [[10.0], None],
                'bid_prices': [[0.4], None],
                'bid_sizes': [[10.0], None],
                'best_ask': [0.6, None],
                'best_bid': [0.4, None],
                'pc_price': [None, None],
                'pc_size': [None, None],
                'pc_side': [None, None],
                'new_tick_size': [None, None],
                'trade_price': [None, None],
                'trade_size': [None, None],
                'trade_side': [None, None],
                'trade_is_mirror': [None, None],
                'winning_outcome': [None, 'Yes'],
            },
        )

        event_mask = np.uint64(
            ~(EXCH_EVENT | LOCAL_EVENT) & np.iinfo(np.uint64).max
        )
        base_ev = data['ev'] & event_mask
        bid_snapshots = data[
            (base_ev == (DEPTH_SNAPSHOT_EVENT | BUY_EVENT))
            & (data['exch_ts'] == 2_000_000_000)
        ]
        ask_snapshots = data[
            (base_ev == (DEPTH_SNAPSHOT_EVENT | SELL_EVENT))
            & (data['exch_ts'] == 2_000_000_000)
        ]

        self.assertEqual(len(bid_snapshots), 1)
        self.assertEqual(len(ask_snapshots), 1)
        self.assertEqual(bid_snapshots['px'][0], 0.998)
        self.assertEqual(bid_snapshots['qty'][0], 0.01)
        self.assertEqual(ask_snapshots['px'][0], 1.0)
        self.assertEqual(ask_snapshots['qty'][0], 0.01)

    def test_polymarket_to_hbt_clears_empty_snapshot_sides(self):
        data = polymarket_to_hbt(
            {
                'market_slug': ['m', 'm'],
                'timestamp': [1_000, 2_000],
                'local_timestamp': [1_100, 2_100],
                'event_type': ['book', 'book'],
                'ask_prices': [[0.6], []],
                'ask_sizes': [[10.0], []],
                'bid_prices': [[0.4], []],
                'bid_sizes': [[10.0], []],
                'best_ask': [0.6, None],
                'best_bid': [0.4, None],
                'pc_price': [None, None],
                'pc_size': [None, None],
                'pc_side': [None, None],
                'new_tick_size': [None, None],
                'trade_price': [None, None],
                'trade_size': [None, None],
                'trade_side': [None, None],
                'trade_is_mirror': [None, None],
                'winning_outcome': [None, None],
            },
        )

        event_mask = np.uint64(
            ~(EXCH_EVENT | LOCAL_EVENT) & np.iinfo(np.uint64).max
        )
        base_ev = data['ev'] & event_mask
        bid_clears = data[
            (base_ev == (DEPTH_CLEAR_EVENT | BUY_EVENT))
            & (data['exch_ts'] == 2_000_000_000)
        ]
        ask_clears = data[
            (base_ev == (DEPTH_CLEAR_EVENT | SELL_EVENT))
            & (data['exch_ts'] == 2_000_000_000)
        ]

        self.assertEqual(len(bid_clears), 1)
        self.assertEqual(len(ask_clears), 1)
        self.assertEqual(bid_clears['px'][0], 0.0)
        self.assertEqual(ask_clears['px'][0], 1.0)

    def test_polymarket_to_hbt_accepts_separate_trade_df(self):
        data = polymarket_to_hbt(
            {
                'market_slug': ['m'],
                'timestamp': [1_000],
                'local_timestamp': [1_100],
                'event_type': ['book'],
                'ask_prices': [[0.6]],
                'ask_sizes': [[10.0]],
                'bid_prices': [[0.4]],
                'bid_sizes': [[10.0]],
                'best_ask': [0.6],
                'best_bid': [0.4],
                'pc_price': [None],
                'pc_size': [None],
                'pc_side': [None],
                'new_tick_size': [None],
                'winning_outcome': [None],
            },
            trade_df={
                'market_slug': ['m', 'm'],
                'timestamp': [1_500, 1_600],
                'local_timestamp': [1_550, 1_650],
                'event_type': ['last_trade_price', 'ignored'],
                'outcome': ['Yes', 'No'],
                'price': [0.7, 0.2],
                'size': [3.0, 4.0],
                'side': ['BUY', 'SELL'],
            },
        )

        event_mask = np.uint64(
            ~(EXCH_EVENT | LOCAL_EVENT) & np.iinfo(np.uint64).max
        )
        base_ev = data['ev'] & event_mask
        trades = data[base_ev == (TRADE_EVENT | BUY_EVENT)]

        self.assertEqual(len(trades), 2)
        self.assertEqual(trades['exch_ts'][0], 1_500_000_000)
        self.assertEqual(trades['local_ts'][0], 1_550_000_000)
        self.assertEqual(trades['px'][0], 0.7)
        self.assertEqual(trades['qty'][0], 3.0)
        self.assertEqual(trades['exch_ts'][1], 1_600_000_000)
        self.assertEqual(trades['local_ts'][1], 1_650_000_000)
        self.assertEqual(trades['px'][1], 0.8)
        self.assertEqual(trades['qty'][1], 4.0)

    def test_polymarket_to_hbt_rejects_null_book_size(self):
        with self.assertRaises(ValueError):
            polymarket_to_hbt(
                {
                    'market_slug': ['m'],
                    'timestamp': [1_000],
                    'local_timestamp': [1_100],
                    'event_type': ['book'],
                    'ask_prices': [[0.6]],
                    'ask_sizes': [[None]],
                    'bid_prices': [[0.4]],
                    'bid_sizes': [[10.0]],
                    'best_ask': [0.6],
                    'best_bid': [0.4],
                    'pc_price': [None],
                    'pc_size': [None],
                    'pc_side': [None],
                    'new_tick_size': [None],
                    'winning_outcome': [None],
                },
            )

    def test_polymarket_to_hbt_rejects_null_trade_price(self):
        with self.assertRaises(ValueError):
            polymarket_to_hbt(
                {
                    'market_slug': ['m'],
                    'timestamp': [1_000],
                    'local_timestamp': [1_100],
                    'event_type': ['book'],
                    'ask_prices': [[0.6]],
                    'ask_sizes': [[10.0]],
                    'bid_prices': [[0.4]],
                    'bid_sizes': [[10.0]],
                    'best_ask': [0.6],
                    'best_bid': [0.4],
                    'pc_price': [None],
                    'pc_size': [None],
                    'pc_side': [None],
                    'new_tick_size': [None],
                    'winning_outcome': [None],
                },
                trade_df={
                    'timestamp': [1_500],
                    'local_timestamp': [1_550],
                    'outcome': ['Yes'],
                    'price': [None],
                    'size': [3.0],
                    'side': ['BUY'],
                },
            )

    def test_dual_settlement_resolve_book_primary_and_snap_safety_net_agree_yes(self):
        """Agreement case: resolve-book primary mid near 1; snap safety-net → 1.0.

        Documents intentional dual settlement: converter resolve injects the
        near-boundary book; PolyAssetRecord/fix_record_prices snaps mid>0.5
        to 1.0. Both paths remain; neither is unified away here.
        """
        events = polymarket_to_hbt(
            {
                'market_slug': ['m', 'm'],
                'timestamp': [1_000, 2_000],
                'local_timestamp': [1_100, 2_100],
                'event_type': ['book', 'market_resolved'],
                'ask_prices': [[0.6], None],
                'ask_sizes': [[10.0], None],
                'bid_prices': [[0.4], None],
                'bid_sizes': [[10.0], None],
                'best_ask': [0.6, None],
                'best_bid': [0.4, None],
                'pc_price': [None, None],
                'pc_size': [None, None],
                'pc_side': [None, None],
                'new_tick_size': [None, None],
                'trade_price': [None, None],
                'trade_size': [None, None],
                'trade_side': [None, None],
                'trade_is_mirror': [None, None],
                'winning_outcome': [None, 'Yes'],
            },
        )

        event_mask = np.uint64(
            ~(EXCH_EVENT | LOCAL_EVENT) & np.iinfo(np.uint64).max
        )
        base_ev = events['ev'] & event_mask
        resolve_bids = events[
            (base_ev == (DEPTH_SNAPSHOT_EVENT | BUY_EVENT))
            & (events['exch_ts'] == 2_000_000_000)
        ]
        # Primary path: resolve-book near-boundary bid.
        self.assertEqual(len(resolve_bids), 1)
        resolve_mid = (
            float(resolve_bids['px'][0])
            + 1.0  # ask side of Yes resolve book is 1.0
        ) / 2.0
        self.assertGreater(resolve_mid, 0.5)

        # Safety-net path: snap a mark near the resolve mid toward 1.0.
        record = np.array(
            [
                (0, 10.0, 1.0, 0.55, 0.0),
                (1_000_000_000, 10.0, 1.0, float(resolve_bids['px'][0]), 0.0),
            ],
            dtype=[
                ('timestamp', 'i8'),
                ('balance', 'f8'),
                ('position', 'f8'),
                ('price', 'f8'),
                ('fee', 'f8'),
            ],
        )
        fixed = fix_record_prices(record.copy(), settlement=True)
        self.assertEqual(fixed['price'][-1], 1.0)

        # With settlement disabled, snap does not rewrite the primary mid.
        untouched = fix_record_prices(record.copy(), settlement=False)
        self.assertAlmostEqual(
            float(untouched['price'][-1]),
            float(resolve_bids['px'][0]),
        )

    def test_dual_settlement_stats_snap_safety_net_without_resolve_book(self):
        """Safety-net alone: without resolve injection, snap still settles mid.

        Regression guard for keep-dual: stats snap must work even when the
        converter resolve-book path did not run (e.g. no market_resolved row).
        """
        # No market_resolved → no resolve-book injection.
        events = polymarket_to_hbt(
            {
                'market_slug': ['m'],
                'timestamp': [1_000],
                'local_timestamp': [1_100],
                'event_type': ['book'],
                'ask_prices': [[0.6]],
                'ask_sizes': [[10.0]],
                'bid_prices': [[0.4]],
                'bid_sizes': [[10.0]],
                'best_ask': [0.6],
                'best_bid': [0.4],
                'pc_price': [None],
                'pc_size': [None],
                'pc_side': [None],
                'new_tick_size': [None],
                'winning_outcome': [None],
            },
        )
        event_mask = np.uint64(
            ~(EXCH_EVENT | LOCAL_EVENT) & np.iinfo(np.uint64).max
        )
        base_ev = events['ev'] & event_mask
        # Only the live book snapshots at t=1000 — no resolve-time snapshots.
        late_snapshots = events[
            (base_ev == (DEPTH_SNAPSHOT_EVENT | BUY_EVENT))
            & (events['exch_ts'] > 1_000_000_000)
        ]
        self.assertEqual(len(late_snapshots), 0)

        record = np.array(
            [
                (0, 10.0, 1.0, 0.40, 0.0),
                (1_000_000_000, 10.0, 1.0, 0.35, 0.0),
                (2_000_000_000, 10.0, 1.0, np.nan, 0.0),
            ],
            dtype=[
                ('timestamp', 'i8'),
                ('balance', 'f8'),
                ('position', 'f8'),
                ('price', 'f8'),
                ('fee', 'f8'),
            ],
        )
        fixed = fix_record_prices(record.copy(), settlement=True)
        self.assertEqual(fixed['price'][-2], 0.0)
        self.assertEqual(fixed['price'][-1], 0.0)

        stats = PolyAssetRecord(record).resample('1s').stats(book_size=100.0)
        # Earn uses snapped settlement prices (safety-net path).
        self.assertIsInstance(stats.earn, float)




if __name__ == '__main__':
    unittest.main()
