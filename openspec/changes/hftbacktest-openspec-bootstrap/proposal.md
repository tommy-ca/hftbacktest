## Why

`tommy-ca/hftbacktest` tip `0e2488bf` has no OpenSpec tree. Wave-0 must arm
`schema: intent-driven` and seed Static-honesty baselines for product boundary,
upstream hygiene, Polymarket backtest overlay, and verify levers before
maintain-audit swarm/arena/propose. Without this bootstrap, later waves cannot
use propose→validate→apply discipline. This change records tip honesty only —
it does not enable live connectors, rewrite the engine, or invent CI green /
Polymarket live PASS.

## What Changes

- Install project-local `intent-driven` schema under `openspec/schemas/intent-driven/`
  and companion skills under `.agents/skills/`.
- Add `openspec/config.yaml` with `schema: intent-driven` and honesty rules
  (no invent live/CI PASS; overlay additive per `UPSTREAM.md`).
- Seed minimal `openspec/specs/` for `product-boundary`, `upstream-hygiene`,
  `polymarket-overlay`, and `verify-levers` from `PRODUCT.md` / `UPSTREAM.md` /
  `DEVELOPMENT.md` (Static honesty only).
- Land this propose change `hftbacktest-openspec-bootstrap` (proposal → specs →
  design → adr → tasks). Bootstrap apply = the install itself (config + seed
  canonical specs + change folder).
- Do **not** enable live connectors; do **not** rewrite the engine; do **not**
  invent CI green or Polymarket live connector PASS; do **not** start Wave-1 swarm.

## Capabilities

### New Capabilities

- `product-boundary`: Supported surface = upstream engine + Polymarket backtest
  overlay; collector/connector/live Polymarket connector remain non-goals;
  import identity stays `hftbacktest`.
- `upstream-hygiene`: Upstream source + baseline pin; additive overlay commits;
  `scripts/check-upstream-drift.sh` as local drift probe (CI wiring optional).
- `polymarket-overlay`: `BacktestAssetPoly` preset contract; BinaryFeeModel +
  stats helpers + examples; no live Polymarket connector claim.
- `verify-levers`: Documented Rust/Python verify commands; CI gaps Act-on/Defer
  only — never invented green.

### Modified Capabilities

None (greenfield OpenSpec tree).

## Impact

OpenSpec tooling and documentation only (`openspec/`, `.agents/skills/`,
`.gitignore` worktree ignore). No engine behaviour change. No live connector.
No invent CI PASS. Overlay remains additive per `UPSTREAM.md`.

## Probe Evidence Record

- Evidence label: `Static`
  - Query: Tip SHA and OpenSpec absence
  - Path: repo root / `openspec/` (absent at tip)
  - Command: `git rev-parse HEAD` → `0e2488bf9c8dc40acbf6e1255d91585e0549bffc`; confirm no `openspec/` on `origin/master`
  - Result summary: Tip matches required floor (≥ `0e2488bf`); no OpenSpec tree before this change.
  - Conclusion: Wave-0 bootstrap required.

- Evidence label: `Static`
  - Query: Product supported surface and non-goals
  - Path: `PRODUCT.md`
  - Command: read Supported surface / Not a Polymarket product surface / Import coexistence
  - Result summary: Engine + Polymarket backtest overlay supported; collector/connector/live Polymarket connector non-goals; import `hftbacktest`.
  - Conclusion: Seed `product-boundary` Static honesty.

- Evidence label: `Static`
  - Query: Upstream pin and additive overlay rules
  - Path: `UPSTREAM.md`, `scripts/check-upstream-drift.sh`
  - Command: read Source / Baseline tip / Rebase hygiene; confirm drift script exists
  - Result summary: Upstream nkaz001/hftbacktest; baseline tip `5f3ec40...`; overlay list named; drift script present; CI wiring optional.
  - Conclusion: Seed `upstream-hygiene`; no invent sync/CI PASS.

- Evidence label: `Static`
  - Query: Overlay surface (`BacktestAssetPoly`, BinaryFeeModel)
  - Path: `PRODUCT.md`, `UPSTREAM.md`, `py-hftbacktest/hftbacktest/__init__.py`, `hftbacktest/src/backtest/models/fee.rs`
  - Command: rg `BacktestAssetPoly|BinaryFeeModel`
  - Result summary: Preset and BinaryFeeModel present; examples under `examples/polymarket/`; live connector not in overlay list.
  - Conclusion: Seed `polymarket-overlay`; no live PASS.

- Evidence label: `Static`
  - Query: Verify levers
  - Path: `DEVELOPMENT.md`
  - Command: read Build and Test section
  - Result summary: `cargo test -p hftbacktest --lib`; unittest discover + `test_polymarket`; maturin develop preferred.
  - Conclusion: Seed `verify-levers` as documented levers only.

- Evidence label: `Metadata`
  - Query: Tip CI workflow inventory
  - Path: `.github/workflows/`
  - Command: `ls .github/workflows/`
  - Result summary: `codeql.yml`, `release-python.yml`, `stale.yml` present — no full build/test/format matrix claimed.
  - Conclusion: CI gaps for maintain-audit are Act-on/Defer later; MUST NOT invent CI green in bootstrap.

- Evidence label: `Unavailable`
  - Query: Polymarket live connector / live trading readiness
  - Path: `PRODUCT.md` non-goals
  - Result summary: Live Polymarket connector out of scope; no owner go to promote.
  - Conclusion: Park; never invent LIVE receipts in bootstrap.
