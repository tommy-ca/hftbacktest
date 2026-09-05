## Why

Tip `fdc5b7d2` has local verify levers documented in DEVELOPMENT.md / OpenSpec `verify-levers`, and Wave-1 S7 exercised them (cargo lib 26 PASS; targeted test_polymarket 8 PASS). S8 shows no build/test/format GHA — only CodeQL (Python), release-python, stale. Arena A4 / I1 lock Act-on minimum verify CI. Without a propose change, Wave-5 may invent badge PASS, wire discover (fixture ERROR), silently claim MSRV-only green despite py `s3` rustc skew, or expand into coverage/CodeQL Rust/drift GHA before baseline exists.

## What Changes

- Grow `verify-levers` so one PR/push GitHub Actions workflow is the proposed first-missing baseline: (1) `cargo test -p hftbacktest --lib` (2) targeted `python -m unittest …test_polymarket` after maturin/venv; optional `cargo fmt --check` in the same change.
- Require honest rustc pin (≥ crate needs; note py `s3` skew vs MSRV 1.91.1) and libclang note for default `live` feature.
- Keep full unittest discover **out** until `tmp_20240501.npz` fixture policy is fixed.
- Soft-after #1: if dual-settlement tests land in `test_polymarket`, the py-overlay job MUST run them.
- Do **not** invent badge/check PASS; do **not** require collector/connector CI; do **not** wire drift GHA; do **not** claim coverage/CodeQL Rust; do **not** claim workflow presence = green.
- Park: CI token / `workflow` scope may gate Wave-5 apply.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `verify-levers`: minimum verify GHA shape; rustc/libclang honesty; discover deferred; workflow ≠ green.

## Impact

Propose workflow + pin notes for later apply. No claim that tip CI is green today. Soft dependency on `hftbacktest-overlay-solid-dry` if new dual-settlement tests land. Token/`workflow` Metadata park may block apply until owner provisions.

## Probe Evidence Record

- Evidence label: `Static`
  - Query: Tip `.github/workflows/` inventory vs ROADMAP build/test/format
  - Path: `.github/workflows/` (`codeql.yml`, `release-python.yml`, `stale.yml`); `ROADMAP.md` L54–56
  - Command: S8 inventory at tip `fdc5b7d2`
  - Result summary: No build/test/format GHA; CodeQL Python-only; ROADMAP wishlist unchecked.
  - Conclusion: First-missing = minimum verify workflow for documented levers.

- Evidence label: `Metadata`
  - Query: Local lever results (not CI)
  - Path: S7 report; DEVELOPMENT.md
  - Command: Wave-1 Runtime cited — cargo lib 26 PASS; test_polymarket 8 PASS; discover 1 ERROR missing npz
  - Result summary: Levers work locally after rustc/libclang/maturin setup; py `s3` needed rustc ≥1.94.1 / succeeded 1.98.1 vs crate MSRV 1.91.1.
  - Conclusion: Document honest pin; keep discover out; do not invent CI PASS from S7.

- Evidence label: `Unavailable`
  - Query: GitHub Actions check-run green / badge PASS for this fork
  - Path: Actions conclusions
  - Result summary: No verify workflow; must-not invent green.
  - Conclusion: After apply, Runtime check-run URLs may be cited; until then Unavailable.

- Evidence label: `Metadata`
  - Query: Token / workflow scope park
  - Path: UPSTREAM.md L55–56; S10; A4
  - Result summary: Adding workflows may need owner `workflow` scope / Actions write policy.
  - Conclusion: Park may gate Wave-5 apply of this change.
