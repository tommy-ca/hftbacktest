# verify-levers Specification

## Purpose

Document tip-honest verify commands from `DEVELOPMENT.md`. Static honesty only —
document the levers; do not invent CI green or claim full coverage PASS.

## Requirements

### Requirement: R-VER-01 Rust Lib Test Lever

Feature: Rust verify
Rule: Documented Rust lib test command is the offline Rust lever.

The documented Rust verify lever SHALL be `cargo test -p hftbacktest --lib`.
This baseline MUST NOT invent a green CI receipt for that command without a
Probe result from this change's Runtime evidence.

#### Scenario: DEVELOPMENT.md names Rust lever

- **GIVEN** tip `DEVELOPMENT.md`
- **WHEN** Rust test instructions are read
- **THEN** `cargo test -p hftbacktest --lib` is documented
- **AND** no invented CI PASS is recorded in this baseline

### Requirement: R-VER-02 Python Unittest Lever Including Overlay

Feature: Python verify
Rule: Documented unittest discover + targeted overlay test path.

Python verify SHALL document unittest discover under `py-hftbacktest/tests` and
the targeted overlay path `python -m unittest py-hftbacktest.tests.test_polymarket`
(with `PYTHONPATH` as in `DEVELOPMENT.md`). Editable install via
`maturin develop -m py-hftbacktest/Cargo.toml` is the preferred setup path.

#### Scenario: DEVELOPMENT.md names Python levers

- **GIVEN** tip `DEVELOPMENT.md`
- **WHEN** Python test instructions are read
- **THEN** unittest discover and `test_polymarket` targeted path are documented
- **AND** `maturin develop` is the preferred editable install path

### Requirement: R-VER-03 CI Gaps Are Act-On Or Defer Not Invented Green

Feature: CI honesty
Rule: Tip CI workflows may be incomplete; gaps need Act-on/Defer with evidence.

Tip `.github/workflows/` presence or absence MUST be Probe-labeled honestly. Authors MUST NOT invent CI green for build/test/format coverage that is not evidenced. Expanding CI beyond the minimum verify baseline (R-VER-04) is a later Act-on or Defer with first-missing named. The minimum verify workflow Act-on does **not** by itself constitute green evidence (see R-VER-06).

#### Scenario: Baseline does not invent CI green

- **GIVEN** tip `.github/workflows/` inventory at OpenSpec baseline
- **WHEN** verify/CI claims are reviewed
- **THEN** only documented local levers are treated as known verify paths until Runtime check runs exist
- **AND** any CI gap is labeled Metadata/Unavailable or deferred — never invented PASS
- **AND** proposing or landing R-VER-04 workflow YAML is not treated as invent PASS

#### Scenario: First-missing Act-on is minimum verify GHA

- **GIVEN** S8 Static shows no build/test/format GHA for verify levers
- **WHEN** Wave-4/5 plans CI Act-on
- **THEN** the first-missing Act-on is the minimum workflow in R-VER-04
- **AND** coverage / CodeQL Rust / drift GHA remain Deferred unless separately promoted

### Requirement: R-VER-04 Minimum Verify GitHub Actions Workflow

Feature: Verify CI baseline
Rule: Propose one PR/push workflow running cargo lib + targeted test_polymarket.

The fork SHALL propose (and on Todd-go apply, may add) one pull_request/push GitHub Actions workflow that runs at least: (1) `cargo test -p hftbacktest --lib` and (2) targeted `python -m unittest py-hftbacktest.tests.test_polymarket` after documented maturin/venv setup (`maturin develop -m py-hftbacktest/Cargo.toml` preferred). Optional same change: `cargo fmt --check`. The workflow MUST NOT wire full unittest discover until the `tmp_20240501.npz` fixture policy is fixed. The workflow MUST NOT require collector or connector test farms for product-boundary compliance. Soft-after overlay dual-settlement tests: if new dual-settlement scenarios land under `test_polymarket`, job (2) MUST run them via that same target.

#### Scenario: Minimum jobs map to documented levers

- **GIVEN** DEVELOPMENT.md / R-VER-01 / R-VER-02 name cargo lib and targeted test_polymarket
- **AND** tip lacks build/test/format GHA (S8 Static)
- **WHEN** verify-ci-baseline apply adds the minimum workflow
- **THEN** the workflow includes a rust-lib job running `cargo test -p hftbacktest --lib`
- **AND** the workflow includes a py-overlay job running targeted `test_polymarket` after maturin/venv
- **AND** full unittest discover is not required in the minimum workflow

#### Scenario: Soft-after dual-settlement tests

- **GIVEN** `hftbacktest-overlay-solid-dry` may add dual-settlement scenarios to `test_polymarket`
- **WHEN** the py-overlay CI job runs
- **THEN** those scenarios are executed as part of the targeted unittest module
- **AND** no separate invent-green claim is made solely because the job exists

#### Scenario: Optional format gate

- **GIVEN** `rustfmt.toml` exists on tip and A4 O2 is optional
- **WHEN** authors include format in this change
- **THEN** the gate is `cargo fmt --check` (or equivalent documented command)
- **AND** clippy/coverage/CodeQL Rust remain out of minimum unless a later Act-on promotes them

### Requirement: R-VER-05 Honest Rustc Pin And Libclang Notes

Feature: CI toolchain honesty
Rule: Document rustc pin and libclang; note py s3 skew vs MSRV.

CI and related DEVELOPMENT notes for the verify baseline SHALL document an honest rustc pin that is ≥ what the jobs need. Authors MUST note that crate MSRV `1.91.1` may be insufficient for the Python binding build when `s3`/AWS crates resolve to versions requiring newer rustc (S7 Metadata skew). Default Rust features including `live` (iceoryx2) SHALL note libclang/bindgen prerequisites. Authors MUST NOT silently claim MSRV-only green for a py-overlay job that required a newer toolchain.

#### Scenario: Pin and libclang are documented

- **GIVEN** S7 observed MSRV 1.91.1 for crate lib tests and newer rustc for maturin/`s3`
- **WHEN** verify-ci-baseline workflow or DEVELOPMENT footnotes are written
- **THEN** rustc pin for each job is stated honestly
- **AND** libclang (or feature trim) is noted for default `live` builds
- **AND** py `s3` skew vs MSRV is named rather than hidden

### Requirement: R-VER-06 Workflow Presence Is Not CI Green

Feature: CI honesty
Rule: Adding a workflow file does not invent PASS.

Authors MUST NOT treat the presence of a verify workflow file, YAML merge, or badge markup as evidence of passing GitHub Actions checks. Until real check-run evidence exists, CI green for these levers remains **Unavailable**. Local S7 PASS remains Metadata evidence of levers only — not fork CI PASS. Expanding to coverage, CodeQL Rust, or drift-script GHA is Deferred and MUST NOT be claimed in this change. CI token / `workflow` scope Metadata park MAY gate Wave-5 apply and MUST be named when blocking.

#### Scenario: No invent green from workflow file

- **GIVEN** a verify workflow may be proposed or merged
- **WHEN** status is reported before real Actions check runs
- **THEN** CI green is Unavailable / not claimed
- **AND** local lever PASS is not re-labeled as CI PASS
- **AND** token/`workflow` park is named if apply cannot proceed
