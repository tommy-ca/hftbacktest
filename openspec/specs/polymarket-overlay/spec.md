# polymarket-overlay Specification

## Purpose

Document tip-honest Polymarket backtest overlay surface from `PRODUCT.md` /
`UPSTREAM.md`. Static honesty only — backtest overlay, not live connector.

## Requirements

### Requirement: R-POLY-01 BacktestAssetPoly Preset Contract

Feature: Asset preset
Rule: `BacktestAssetPoly` fixes ROI [0,1], tick/lot 0.001, risk-adverse queue.

`BacktestAssetPoly` SHALL fix ROI `[0, 1]`, tick/lot `0.001`, and the
risk-adverse queue model at construction. Latency, fee model, exchange fill
model, and data SHALL remain chainable. There MUST NOT be a second preset class
for ROI overrides — use plain `BacktestAsset` with explicit ROI bounds.

#### Scenario: Preset defaults match PRODUCT.md

- **GIVEN** tip `PRODUCT.md` BacktestAssetPoly preset section and
  `py-hftbacktest/hftbacktest/__init__.py`
- **WHEN** `BacktestAssetPoly` construction defaults are inspected
- **THEN** ROI `[0, 1]`, tick/lot `0.001`, and risk-adverse queue are fixed at construction
- **AND** no second preset class is introduced for ROI overrides

### Requirement: R-POLY-02 Binary Fee And Stats Helpers Are Overlay Surface

Feature: Fee and stats overlay
Rule: BinaryFeeModel and settlement-aware stats helpers are additive overlay.

The overlay SHALL include `BinaryFeeModel` (Rust + PyO3 binding), Polymarket
converter utilities, and settlement-aware stats helpers (`PolyAssetRecord`,
`fix_record_prices`, `earn`) as documented in `UPSTREAM.md`.

#### Scenario: Overlay files named in UPSTREAM.md

- **GIVEN** tip `UPSTREAM.md` Polymarket overlay list
- **WHEN** overlay surface is enumerated
- **THEN** converter, `BacktestAssetPoly`, BinaryFeeModel, stats helpers, and
  `examples/polymarket/` are included
- **AND** live Polymarket connector is not listed as overlay surface

### Requirement: R-POLY-03 No Live Polymarket Connector Claim

Feature: Live connector boundary
Rule: Live Polymarket connector remains out of scope.

This baseline MUST NOT claim a Polymarket live connector, live trading
readiness, or invent LIVE PASS for Polymarket order placement.

#### Scenario: Live connector remains non-goal

- **GIVEN** tip `PRODUCT.md` and program standing orders
- **WHEN** a reviewer checks for Polymarket live connector support
- **THEN** the baseline records it as out of scope / non-goal
- **AND** no LIVE / production-ready receipt is invented
