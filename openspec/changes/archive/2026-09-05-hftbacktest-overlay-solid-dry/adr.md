# ADR review manifest — hftbacktest-overlay-solid-dry

## In-force sources read

| Source | Relevance |
|---|---|
| I1.md Act-on #1 / A2 recommended base | Locked keep-dual + keep-in-host + dismiss fee extract |
| tip `openspec/specs/polymarket-overlay/spec.md` | Seeded R-POLY-01..03; deltas ADDED against these |
| tip `PRODUCT.md` / `UPSTREAM.md` | Overlay surface + additive rule |
| S4 / S5 reports | Static dual settlement + fee formula multi-surface |

## Change-local decisions

| Decision | Durable new repo ADR? | Status | Notes |
|---|---|---|---|
| Keep dual settlement (converter resolve-book ∧ PolyAssetRecord/fix_record_prices) as intentional primary+safety-net | No — change-local | **Accepted** (I1) | Document + test; do not unify blindly |
| Keep-in-host stats helpers in `stats.py` | No — change-local | **Accepted** (I1) | Split only if later rebase pain > doc cost |
| Keep converter file + `BinaryFeeModel` on existing `FeeModel` (no fee crate) | No — change-local | **Accepted** (I1) | A2 O4 dismiss extract |
| Fee-formula prose sync checklist across Rust/PyO3/README | No — change-local | **Accepted** | Hygiene when docs touched |

## Must not

Invent repo-root `adr/NNNN` for these locks unless later proven cross-change durable. Do not ADR-accept live Polymarket connector or invent CI green.
