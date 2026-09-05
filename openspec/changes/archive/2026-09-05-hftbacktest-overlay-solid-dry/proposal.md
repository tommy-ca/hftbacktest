## Why

Tip `fdc5b7d2` Polymarket backtest overlay already has cohesive SRP boundaries (converter file, `BinaryFeeModel` on `FeeModel`, thin PyO3 slice) and intentional dual settlement (converter resolve-book ∧ `PolyAssetRecord`/`fix_record_prices`). Arena A2 / I1 locked **keep dual** + **keep-in-host stats** and dismissed fee-crate extract and blind unify. Without OpenSpec deltas, Wave-5 writers may collapse the safety net, split stats without rebase-pain evidence, or invent CI/LIVE PASS while touching fee-formula prose. This change documents and requires scenario coverage only.

## What Changes

- Grow `polymarket-overlay` so dual settlement is explicit primary+safety-net with `test_polymarket` (or adjacent Static) scenario coverage requirements.
- Lock keep-converter-file + `BinaryFeeModel` on existing `FeeModel`; lock keep-in-host stats helpers in `stats.py`.
- Add fee-formula prose sync checklist across Rust / PyO3 / README where docs are touched.
- Do **not** extract a fee crate; do **not** unify dual paths without strong tests; do **not** split stats; do **not** invent live connector or CI green.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `polymarket-overlay`: dual-settlement documentation + scenario coverage; keep converter/fee/host-stats; fee-formula sync hygiene.

## Impact

Spec + design + tasks for later Wave-5 apply (docs/tests/checklist). No engine product apply in propose. Parks (live Polymarket connector, invent CI green) remain Unavailable / Must-not. Soft dependency for change #2: if dual-settlement tests land, CI job must run them.

## Probe Evidence Record

- Evidence label: `Static`
  - Query: Overlay SRP/OCP boundaries and dual settlement coupling
  - Path: `py-hftbacktest/hftbacktest/data/utils/polymarket.py`; `hftbacktest/src/backtest/models/fee.rs`; `py-hftbacktest/hftbacktest/stats/stats.py`; `py-hftbacktest/src/lib.rs`
  - Command: Wave-1 S4/S5 file reads at tip `fdc5b7d2d909b93727020450908d65211d9f0dc7`
  - Result summary: Converter cohesive (~305); `BinaryFeeModel` OCP-clean on `FeeModel`; stats host ~534 with overlay helpers; dual resolve-book ∧ snap both affect terminal mid/equity; fee formula restated in Rust/PyO3/README.
  - Conclusion: Document + test dual path; keep host modules; sync checklist — no fee crate / no blind unify.

- Evidence label: `Metadata`
  - Query: Local verify levers for overlay tests
  - Path: `DEVELOPMENT.md`; `py-hftbacktest/tests/test_polymarket.py`
  - Command: S7 Runtime cited as prior verify (26 cargo lib PASS; 8 test_polymarket PASS)
  - Result summary: Targeted overlay tests exist and passed locally after maturin/venv; not CI green.
  - Conclusion: Strengthen dual-settlement scenarios against existing lever; do not invent CI PASS.

- Evidence label: `Unavailable`
  - Query: Polymarket live connector / invent CI green
  - Path: PRODUCT / S10 parks
  - Result summary: Parks held; no LIVE / CI PASS receipts.
  - Conclusion: Must-not invent; out of this change.

- Evidence label: `Static` / `Metadata`
  - Query: I1 / A2 locked decisions
  - Path: `orchestrate/.../i1/I1.md`; `arena/A2.md`
  - Result summary: Keep dual; keep-in-host stats; dismiss fee extract and unify-without-tests.
  - Conclusion: Change-local ADR captures locks; no new repo-root adr/NNNN unless later durable.
