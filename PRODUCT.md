# Product boundary

## Supported surface

This fork supports:

1. **Upstream HftBacktest engine** — same import (`hftbacktest`), same core APIs.
2. **Polymarket backtest overlay** — converter, asset presets, binary fee model,
   settlement-aware stats helpers, and examples under `examples/polymarket/`.

Not a Polymarket product surface:

- `collector/` — upstream CEX market-data binaries
- `connector/` — upstream live exchange gateway + iceoryx
- Live Polymarket connector — out of scope

## Import coexistence

- Python import module: **`hftbacktest`** (matches upstream).
- PyPI project name on this fork remains **`hftbacktest`** for identity with upstream.
- A separate published package named `pm-hftbacktest` (mileswangs) also imports
  as `hftbacktest`. Do **not** install both in one environment; they collide on
  the import path. Prefer this fork **or** the pm package, not both.

## Version map

| Layer | This fork (overlay on upstream tip) | Upstream tags | mileswangs/pm-hftbacktest (reference) |
| --- | --- | --- | --- |
| Python package | `2.4.4` (keeps upstream) | `py-v2.4.4` | `1.0.9` (`pm-hftbacktest`) |
| Rust crate | `0.9.4` | `rust-v0.9.4` | `0.9.4` |
| Upstream tip pin | `5f3ec40...` | tag + tip fix | undeclared copy of ~same tree |

Overlay features are additive relative to upstream `2.4.4` / `0.9.4`.


## BacktestAssetPoly preset

`BacktestAssetPoly` fixes ROI `[0, 1]`, tick/lot `0.001`, and the risk-adverse
queue model at construction. Latency, fee model, exchange fill model, and data
stay chainable.

To override queue or tick while keeping the same ROI bounds, use plain
`BacktestAsset` and set `roi_lb(0.0)` / `roi_ub(1.0)` yourself (plus the tick,
lot, and queue model you want). No second preset class.

## BacktestAssetPoly preset

`BacktestAssetPoly` fixes ROI bounds (`0.0`–`1.0`), tick/lot (`0.001`), and
`risk_adverse_queue_model` at construction. Data, latency, and fee model stay
chainable.

To override queue or tick/lot, use plain `BacktestAsset` with the same ROI
bounds (`roi_lb(0.0)`, `roi_ub(1.0)`) and set the models you need. There is no
second preset class.
