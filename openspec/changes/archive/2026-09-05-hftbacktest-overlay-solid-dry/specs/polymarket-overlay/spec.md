## ADDED Requirements

### Requirement: R-POLY-04 Dual Settlement Is Intentional Primary And Safety-Net

Feature: Dual settlement honesty
Rule: Converter resolve-book and PolyAssetRecord/fix_record_prices remain dual by design.

The Polymarket backtest overlay SHALL treat converter resolve-book injection (primary path that encodes terminal 0/1 book behavior at resolution) **and** settlement-aware stats helpers (`PolyAssetRecord`, `fix_record_prices`, and related earn/equity helpers) as an intentional **primary + safety-net** dual settlement design. Authors MUST NOT unify these paths into a single converter-only or stats-only path without an Act-on change that adds strong scenario coverage proving equivalent terminal mid/equity behavior. Documentation touched by overlay Act-on SHALL name both paths and their roles. This requirement MUST NOT claim Polymarket live connector support or invent LIVE PASS.

#### Scenario: Dual paths remain named primary and safety-net

- **GIVEN** tip converter resolve-book helpers and `PolyAssetRecord`/`fix_record_prices` both exist on tip `fdc5b7d2`
- **AND** I1/A2 lock keep-dual settlement
- **WHEN** overlay settlement behavior is documented or refactored
- **THEN** both paths remain present unless a later Act-on with strong tests explicitly collapses them
- **AND** docs name primary (converter resolve-book) and safety-net (stats snap) roles
- **AND** no LIVE / Polymarket live connector claim is introduced

#### Scenario: Blind unify without tests is forbidden

- **GIVEN** dual settlement is locked keep-dual
- **WHEN** a change proposes removing resolve-book injection or removing stats snap without scenario coverage
- **THEN** the change MUST be rejected or revised to retain dual paths or to ship equivalent tests first
- **AND** "DRY cleanup" alone is not sufficient justification

### Requirement: R-POLY-05 Dual Settlement Scenario Coverage In test_polymarket

Feature: Overlay test coverage
Rule: test_polymarket (or adjacent Static tests) must cover dual-settlement scenarios.

Overlay verify SHALL include scenario coverage for dual settlement in `py-hftbacktest/tests/test_polymarket.py` or adjacent Static unit tests under the documented targeted Python lever. Coverage MUST exercise that resolve-book and snap paths both affect terminal mid/equity semantics in the documented safety-net design (agreement cases at minimum; deliberate disagreement/regression cases when fixtures allow). Authors MUST NOT invent CI green from local PASS alone. Discover-path fixture gaps (`tmp_20240501.npz`) MUST NOT block the targeted overlay lever.

#### Scenario: Targeted test_polymarket covers dual settlement

- **GIVEN** documented lever `python -m unittest py-hftbacktest.tests.test_polymarket` (after maturin/venv as in DEVELOPMENT.md)
- **WHEN** dual-settlement Act-on apply completes
- **THEN** at least one scenario asserts resolve-book primary behavior
- **AND** at least one scenario asserts stats snap / `PolyAssetRecord` safety-net behavior (or their documented interaction)
- **AND** results are reported as local/Metadata verify evidence — not invented GitHub Actions PASS

#### Scenario: Discover fixture gap does not redefine overlay lever

- **GIVEN** full unittest discover may ERROR on missing `tmp_20240501.npz` (S7)
- **WHEN** dual-settlement coverage is required
- **THEN** the required lever remains the targeted `test_polymarket` path
- **AND** discover fixture policy stays Deferred / out of this requirement's scope

### Requirement: R-POLY-06 Keep Converter File Fee Trait And Host Stats

Feature: Overlay module boundaries
Rule: Keep converter file, BinaryFeeModel on FeeModel, and host stats.py helpers.

The overlay SHALL keep Polymarket conversion in `py-hftbacktest/hftbacktest/data/utils/polymarket.py`, keep `BinaryFeeModel` as an extension of the existing `FeeModel` trait (Rust + thin PyO3 binding), and keep settlement-aware stats helpers hosted in `py-hftbacktest/hftbacktest/stats/stats.py`. Authors MUST NOT extract a separate fee crate in this change. Authors MUST NOT split stats overlay into a new module solely for SRP cosmetics without documented rebase-pain evidence exceeding doc cost. Thin PyO3 `binary_fee_model` slice MUST remain additive.

#### Scenario: Boundaries stay keep-in-host

- **GIVEN** A2/I1 locks keep converter + fee trait extend + keep-in-host stats
- **WHEN** overlay-solid-dry apply lands
- **THEN** converter remains a dedicated file
- **AND** `BinaryFeeModel` remains on existing `FeeModel` (no fee crate)
- **AND** `fill_record_prices` / `PolyAssetRecord` / related helpers remain in host `stats.py`
- **AND** no second preset class is introduced

### Requirement: R-POLY-07 Fee Formula Prose Sync Checklist

Feature: Fee formula documentation hygiene
Rule: When fee docs are touched, sync Rust / PyO3 / README prose.

When Act-on work touches fee-formula documentation in Rust (`fee.rs` / model docs), PyO3 binding docs/comments, or README overlay fee highlights, authors SHALL run a sync checklist so the stated binary fee formula remains consistent across those surfaces. The checklist MUST be documentary (no invented codegen SoT required). This requirement MUST NOT invent CI PASS for fee tests or claim live trading fee behavior beyond backtest overlay.

#### Scenario: Touched fee docs stay consistent

- **GIVEN** fee-formula prose exists in Rust and is restated in PyO3 and/or README overlay
- **WHEN** any of those surfaces is edited in an overlay Act-on
- **THEN** authors complete a fee-formula sync checklist across the touched surfaces
- **AND** remaining surfaces are either updated or explicitly noted as unchanged-but-consistent
- **AND** no CI green or LIVE PASS is claimed from the checklist alone

## MODIFIED Requirements

<!-- None. R-POLY-01..03 on tip remain in force unchanged; this change ADDS dual-settlement / boundary / checklist requirements. -->
