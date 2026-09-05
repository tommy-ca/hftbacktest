# Tasks: hftbacktest-overlay-solid-dry

> Schema: intent-driven. Propose → offline verify → **STOP** → Todd-go apply → archive.
> Tip: `fdc5b7d2d909b93727020450908d65211d9f0dc7`. No invent LIVE / CI PASS. No product apply until Todd go.

## 0. Preconditions (read-only)

- [x] 0.1 Tip SHA Probe: worktree at `fdc5b7d2d909b93727020450908d65211d9f0dc7` (or newer with same parks)
- [x] 0.2 Re-read seeded `openspec/specs/polymarket-overlay/spec.md`, I1.md, A2.md, S4/S5
- [x] 0.3 Parks held: live Polymarket connector (Unavailable); invent CI green (Must-not)
- [x] 0.4 Confirm propose-only — no engine code edits in this phase

## 1. Propose atoms (Wave 4 — Planner)

Depends: §0

- [x] 1.1 `proposal.md` — Why / What / Capabilities / Impact / Probe Evidence Record
- [x] 1.2 `specs/polymarket-overlay/spec.md` — ADDED requirements + scenarios
- [x] 1.3 `design.md` — Context / Goals / Decisions / Risks / Migration
- [x] 1.4 `adr.md` — change-local Accepted locks (keep-dual; keep-in-host; no fee crate)
- [x] 1.5 Spec refs checklist:
  - [x] tip `openspec/specs/polymarket-overlay/spec.md` (R-POLY-01..03 remain in force)
  - [x] I1 Act-on #1 / A2 base

## 2. Validate --strict (offline — before any apply)

Depends: §1 complete

- [x] 2.1 `/home/box/bin/openspec validate --type change --strict hftbacktest-overlay-solid-dry`
- [x] 2.2 Probe labels honest — Static/Metadata/Unavailable only; no invented CI/LIVE PASS
- [x] 2.3 Confirm Must-nots present in proposal/tasks (fee crate; unify without tests; stats split; live; invent CI)

## 3. STOP handoff

Depends: §2 green

- [x] 3.1 Hand Horizon path: `openspec/changes/hftbacktest-overlay-solid-dry/`
- [x] 3.2 Ledger: propose VERIFIED; parks parked; soft-note for verify-ci-baseline if new tests land
- [x] 3.3 **STOP** — no apply until Todd go

## 4. Apply (Wave 5 — later workers; gated on Todd go)

Depends: Todd go + §2 green

- [x] 4.1 Document dual settlement (converter resolve-book ∧ `PolyAssetRecord`/`fix_record_prices`) as intentional primary+safety-net in converter/stats docs as touched
- [x] 4.2 Strengthen `test_polymarket` (or adjacent Static) scenarios for dual-settlement coverage per ADDED requirements
- [x] 4.3 Fee-formula prose sync checklist across Rust / PyO3 / README where those docs are touched
- [x] 4.4 Merge delta into canonical `openspec/specs/polymarket-overlay/spec.md`
- [x] 4.5 Re-run local levers: `cargo test -p hftbacktest --lib`; targeted `python -m unittest …test_polymarket` — treat as Metadata levers, **not** invent CI green
- [x] 4.6 MUST NOT: fee crate extract; unify dual paths without tests; stats split; live connector; invent CI PASS

## 5. Archive

Depends: §4 complete

- [x] 5.1 Archive per openspec-git-discipline after apply lands
- [x] 5.2 Update orchestrate ledger; reaffirm parks / no LIVE invent
