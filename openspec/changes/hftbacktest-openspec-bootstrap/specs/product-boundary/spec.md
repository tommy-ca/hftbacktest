## ADDED Requirements

### Requirement: R-BOUND-01 Supported Surface Is Engine Plus Overlay

Feature: Product boundary
Rule: Fork supports upstream engine identity plus Polymarket backtest overlay only.

The supported surface SHALL be (1) the upstream HftBacktest engine with the same
`hftbacktest` import and core APIs, and (2) the Polymarket backtest overlay
(converter, asset presets, binary fee model, settlement-aware stats helpers,
and `examples/polymarket/`).

#### Scenario: Supported surface matches PRODUCT.md

- **GIVEN** tip `PRODUCT.md` Supported surface section
- **WHEN** a reviewer enumerates product claims
- **THEN** only upstream engine + Polymarket backtest overlay are listed as supported
- **AND** no Polymarket live connector is claimed as supported

### Requirement: R-BOUND-02 Non-Goals Stay Non-Goals

Feature: Explicit non-product surfaces
Rule: collector, connector, and live Polymarket connector are not this fork's product surface.

`collector/`, `connector/`, and a live Polymarket connector MUST NOT be treated
as supported Polymarket product surface unless a later Act-on change with owner
go explicitly promotes them.

#### Scenario: Non-goals named at baseline

- **GIVEN** tip `PRODUCT.md` Not a Polymarket product surface list
- **WHEN** OpenSpec baseline is seeded
- **THEN** `collector/`, `connector/`, and live Polymarket connector are recorded as non-goals
- **AND** no LIVE / production-ready receipt is invented for them

### Requirement: R-BOUND-03 Import Identity Matches Upstream

Feature: Import coexistence
Rule: Python import module remains `hftbacktest`; do not collide with `pm-hftbacktest`.

The Python import module SHALL remain `hftbacktest`. Publishing or installing a
conflicting `pm-hftbacktest` identity alongside this fork in one environment is
out of scope for this baseline and MUST NOT be claimed as required.

#### Scenario: Import name is hftbacktest

- **GIVEN** tip `PRODUCT.md` Import coexistence section
- **WHEN** package identity is inspected
- **THEN** the documented import module is `hftbacktest`
- **AND** dual-install with `pm-hftbacktest` is documented as a collision to avoid
