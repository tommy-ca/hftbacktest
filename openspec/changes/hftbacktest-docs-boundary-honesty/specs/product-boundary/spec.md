## ADDED Requirements

### Requirement: R-BOUND-04 README Dual Audience Honesty

Feature: Docs honesty — README
Rule: Clarify fork overlay audience vs retained upstream chrome.

README documentation SHALL make the dual audience explicit: (1) fork consumers of the Polymarket **backtest** overlay and tommy-ca fork identity, and (2) retained upstream HftBacktest Key Features / tutorials / historical chrome (including nkaz001-oriented clone or badge links where not yet safely retargeted). Authors MAY annotate upstream chrome as upstream identity and MAY retarget clone/badge URLs to the fork **only where Static evidence supports the retarget** (e.g. fork repo URL). Authors MUST NOT wipe upstream tutorials wholesale. Authors MUST NOT claim a Polymarket live connector. Authors MUST NOT invent CI green via badge retarget when fork Actions lack evidenced passing verify checks.

#### Scenario: Overlay vs upstream chrome are distinguishable

- **GIVEN** tip README includes an overlay section naming Polymarket backtest overlay and also retains upstream Key Features / nkaz001-oriented links (S9)
- **WHEN** docs-boundary-honesty apply lands
- **THEN** a reader can distinguish fork overlay claims from retained upstream chrome
- **AND** upstream tutorials are not wiped
- **AND** no Polymarket live connector is claimed

#### Scenario: Badge or clone retarget stays evidence-honest

- **GIVEN** some README badges/links still point at `nkaz001/hftbacktest`
- **WHEN** authors retarget or annotate those links
- **THEN** retargets are limited to destinations with Static/Metadata honesty
- **AND** authors do not invent fork CI/RTD green solely by pointing a badge at the fork

### Requirement: R-BOUND-05 DEVELOPMENT Toolchain Footnotes

Feature: Docs honesty — DEVELOPMENT
Rule: Document libclang and rustc>MSRV for py s3.

`DEVELOPMENT.md` SHALL footnote that default Rust features including `live` may require libclang/bindgen for iceoryx2, and that building the Python binding with the `s3` feature may require a rustc newer than the crate MSRV `1.91.1` when current AWS crates resolve above MSRV. These footnotes are Static/Metadata honesty for local levers. They MUST NOT be phrased as invent CI green or as Polymarket live readiness.

#### Scenario: Footnotes name libclang and s3 rustc skew

- **GIVEN** S7 Metadata showed libclang need for default `live` and rustc skew for py `s3`
- **WHEN** DEVELOPMENT is updated under this change
- **THEN** libclang (or equivalent) is noted for default-feature Rust builds
- **AND** rustc>MSRV possibility for py `s3` is noted
- **AND** footnotes do not claim GitHub Actions PASS

### Requirement: R-BOUND-06 Docs Must Not Invent Live Or CI Green Or Fork-Done ROADMAP

Feature: Docs honesty — standing must-nots
Rule: Docs grafts stay tip-honest on live, CI, and ROADMAP.

Documentation Act-on under this change MUST NOT claim Polymarket live trading or live connector readiness, MUST NOT claim CI green / production-ready verify PASS without Probe evidence, MUST NOT wipe upstream tutorials to force a fork-only narrative, and MUST NOT promote upstream `ROADMAP.md` live/connector checkboxes as fork delivery complete. Soft-after overlay-solid-dry: if README overlay settlement or fee prose is edited, wording SHALL stay consistent with dual settlement as intentional primary+safety-net.

#### Scenario: Standing docs must-nots hold

- **GIVEN** PRODUCT non-goals and program Must-nots (no invent LIVE/CI green)
- **WHEN** README / DEVELOPMENT / related docs grafts are reviewed
- **THEN** no Polymarket live claim is introduced
- **AND** no CI green is invented
- **AND** upstream tutorials remain unless a separate owner Act-on says otherwise
- **AND** ROADMAP live items are not presented as fork-done PASS

#### Scenario: Soft-after dual-settlement wording

- **GIVEN** `hftbacktest-overlay-solid-dry` documents dual settlement primary+safety-net
- **AND** README overlay settlement/fee prose may be touched
- **WHEN** docs-boundary-honesty apply edits that prose
- **THEN** wording remains consistent with keep-dual primary+safety-net
- **AND** does not imply unify-without-tests or live connector behavior

## MODIFIED Requirements

<!-- None required. R-BOUND-01..03 remain in force; this change ADDS docs-honesty requirements. -->
