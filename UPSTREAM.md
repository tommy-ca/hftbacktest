# Upstream

## Source

- Upstream repo: https://github.com/nkaz001/hftbacktest
- This GitHub repository (`tommy-ca/hftbacktest`) **is a fork of** `nkaz001/hftbacktest` (default branch `master`).
- Baseline tip when the Polymarket overlay was reapplied: `5f3ec40b2afb764e0fea112f941ed85523ef4e88`
- Nearest tags: `rust-v0.9.4` / `py-v2.4.4` at `a244a14250b42d97fc305569c93c4117cd5e1dff`

## Polymarket overlay provenance

Product deltas were adapted from the vendored Polymarket port:

- https://github.com/mileswangs/pm-hftbacktest
- Optional working fork used during hygiene: https://github.com/tommy-ca/pm-hftbacktest

That port is a full-tree copy of upstream with Polymarket additions. This fork
keeps upstream identity and reapplies **only** the Polymarket product overlay as
additive commits (not a full tree replace).

## Relationship

Inherited from upstream: core backtest engine, depth processors, live IPC,
`collector`, and CEX `connector` (Binance / Bybit / Hyperliquid paths).

Polymarket overlay (additions / changes on this branch):

- `py-hftbacktest/hftbacktest/data/utils/polymarket.py`
- `py-hftbacktest/hftbacktest/__init__.py` (`BacktestAssetPoly`, `init_orderbook`, `polymarket_to_hbt`)
- `py-hftbacktest/hftbacktest/stats/stats.py` (`PolyAssetRecord`, `fix_record_prices`, `earn`)
- `hftbacktest/src/backtest/models/fee.rs` + `models/mod.rs` (`BinaryFeeModel`)
- `py-hftbacktest/src/lib.rs` (PyO3 `binary_fee_model`)
- `examples/polymarket/`, README overlay section, `PRODUCT.md`, `DEVELOPMENT.md`, `NOTICE`

Skipped from pm (intentionally left upstream / not copied):

- Package rename to PyPI `pm-hftbacktest` / version `1.0.9` (this fork keeps `hftbacktest` / `2.4.4`)
- Dropping the py crate `s3` feature
- Replacing root README / deleting upstream `examples/` tutorials
- CEX collector/connector diffs (none required for BinaryFee)
- Agent-only noise (`.DS_Store`)
