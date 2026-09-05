## ADDED Requirements

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

Tip `.github/workflows/` presence or absence MUST be Probe-labeled honestly.
Authors MUST NOT invent CI green for build/test/format coverage that is not
evidenced. Expanding CI is a later Act-on or Defer with first-missing named.

#### Scenario: Baseline does not invent CI green

- **GIVEN** tip `.github/workflows/` inventory at OpenSpec baseline
- **WHEN** verify/CI claims are reviewed
- **THEN** only documented local levers are treated as known verify paths
- **AND** any CI gap is labeled Metadata/Unavailable or deferred — never invented PASS
