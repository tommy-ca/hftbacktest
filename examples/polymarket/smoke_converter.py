"""Offline smoke for polymarket_to_hbt (no network, no native backtest run)."""

from __future__ import annotations

import numpy as np

from hftbacktest import (
    BUY_EVENT,
    DEPTH_SNAPSHOT_EVENT,
    EXCH_EVENT,
    LOCAL_EVENT,
    SELL_EVENT,
    TRADE_EVENT,
    polymarket_to_hbt,
)


def main() -> None:
    data = polymarket_to_hbt(
        {
            "market_slug": ["m"],
            "timestamp": [1_000],
            "local_timestamp": [1_100],
            "event_type": ["book"],
            "ask_prices": [[0.6]],
            "ask_sizes": [[10.0]],
            "bid_prices": [[0.4]],
            "bid_sizes": [[10.0]],
            "best_ask": [0.6],
            "best_bid": [0.4],
            "pc_price": [None],
            "pc_size": [None],
            "pc_side": [None],
            "new_tick_size": [None],
            "winning_outcome": [None],
        },
        trade_df={
            "timestamp": [1_500],
            "local_timestamp": [1_550],
            "outcome": ["Yes"],
            "price": [0.7],
            "size": [3.0],
            "side": ["BUY"],
        },
    )
    event_mask = np.uint64(~(EXCH_EVENT | LOCAL_EVENT) & np.iinfo(np.uint64).max)
    base_ev = data["ev"] & event_mask
    assert len(data) > 0
    assert np.any(base_ev == (DEPTH_SNAPSHOT_EVENT | BUY_EVENT))
    assert np.any(base_ev == (DEPTH_SNAPSHOT_EVENT | SELL_EVENT))
    assert np.any(base_ev == (TRADE_EVENT | BUY_EVENT))
    print(f"ok: {len(data)} events")


if __name__ == "__main__":
    main()
