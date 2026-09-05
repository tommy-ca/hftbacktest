## Context

Fork tip `fdc5b7d2` is an upstream HftBacktest identity plus Polymarket **backtest** overlay. Wave-1 S4/S5 and arena A2 established: converter and fee boundaries are SRP/OCP-clean; dual settlement (converter resolve book ∧ stats snap) is intentional primary+safety-net; stats overlay lives in host `stats.py`; fee formula prose is restated in multiple surfaces. I1 Act-on #1 proposes docs/tests/checklist — not module surgery.

## Goals / Non-Goals

**Goals.**

- Document dual settlement as intentional primary+safety-net in overlay specs and (on apply) converter/stats docs.
- Require scenario coverage in `test_polymarket` (or adjacent Static tests) for resolve-book ∧ snap agreement / safety-net behavior.
- Keep converter file + `BinaryFeeModel` on `FeeModel`; keep stats helpers in host `stats.py`.
- Provide a fee-formula prose sync checklist for Rust / PyO3 / README when those docs are touched.

**Non-Goals.**

- Fee crate extract; unify dual paths without strong tests; stats module split; live Polymarket connector; invent CI green; product apply in propose phase; upstream-sync Act-on.

## Decisions

1. **Keep dual settlement.** Do not collapse to converter-only or stats-only. Document + strengthen tests (A2 O3 dismiss unify; I1 lock).
2. **Keep-in-host stats.** `fix_record_prices`, `Stats.earn`, `PolyAssetRecord` remain in `py-hftbacktest/hftbacktest/stats/stats.py` unless later rebase pain > doc cost (A2 O1; I1).
3. **Keep converter + fee trait extend.** No fee crate (A2 O4 dismiss).
4. **Fee-formula sync is checklist hygiene**, not a single-source codegen invent.
5. **Change-local ADR only** for keep-dual / keep-in-host; do not invent repo-root `adr/NNNN` unless later proven durable.

### Alternatives rejected

- Unify dual settlement into one path — rejected (loses safety net; A2 O3).
- Split `stats/polymarket.py` now — rejected (rebase pain not proven; A2 O2 deferred).
- Extract fee crate — rejected (YAGNI; OCP already clean).

## Risks

- Dual-path drift if one side changes settlement semantics without tests — mitigate with scenario matrix in apply.
- Writers treat ADDED requirements as license for live connector or CI invent — mitigate with Must-not in tasks/proposal.
- Soft-after for CI change: new dual-settlement tests must be runnable by targeted `test_polymarket` job.

## Migration

Propose-only now. Apply (Wave-5, Todd go): doc dual settlement; strengthen `test_polymarket` scenarios; run fee-formula sync checklist where docs touched; merge delta into canonical `polymarket-overlay` spec. No runtime migration of engine crates.

## Open Questions

- Exact scenario matrix shape (agreement vs deliberate disagreement cases) — resolve in apply with Static fixtures; no invent LIVE.
- Whether fee-formula checklist lives in DEVELOPMENT vs change tasks only — prefer DEVELOPMENT footnote or overlay README highlight on apply if docs touched.
