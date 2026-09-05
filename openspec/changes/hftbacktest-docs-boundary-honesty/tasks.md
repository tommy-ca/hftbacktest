# Tasks: hftbacktest-docs-boundary-honesty

> Schema: intent-driven. Propose → offline verify → **STOP** → Todd-go apply → archive.
> Tip: `fdc5b7d2d909b93727020450908d65211d9f0dc7`. Docs graft only. Soft-after overlay-solid-dry for settlement wording.

## 0. Preconditions (read-only)

- [x] 0.1 Tip SHA Probe: `fdc5b7d2d909b93727020450908d65211d9f0dc7`
- [x] 0.2 Re-read `openspec/specs/product-boundary/spec.md`, I1.md, A3.md, S9, DEVELOPMENT.md, README.rst overlay
- [x] 0.3 Parks held: live Polymarket connector; invent CI green
- [x] 0.4 Soft-after: dual-settlement wording consistency if README overlay settlement/fee prose touched

## 1. Propose atoms (Wave 4 — Planner)

Depends: §0

- [x] 1.1 `proposal.md` — Probe Evidence Record
- [x] 1.2 `specs/product-boundary/spec.md` — ADDED docs-honesty requirements
- [x] 1.3 `design.md`
- [x] 1.4 `adr.md` — Accepted dual-audience + footnotes locks
- [x] 1.5 Spec refs: tip product-boundary R-BOUND-01..03

## 2. Validate --strict (offline — before any apply)

Depends: §1 complete

- [x] 2.1 `/home/box/bin/openspec validate --type change --strict hftbacktest-docs-boundary-honesty`
- [ ] 2.2 Probe honesty: no LIVE/CI invent in proposal
- [ ] 2.3 Confirm Must-nots: no tutorial wipe; no ROADMAP live-as-done; no Polymarket live claim

## 3. STOP handoff

Depends: §2 green

- [ ] 3.1 Hand Horizon `openspec/changes/hftbacktest-docs-boundary-honesty/`
- [ ] 3.2 Ledger: propose VERIFIED; parks parked
- [ ] 3.3 **STOP** — no apply until Todd go

## 4. Apply (Wave 5 — later workers; gated on Todd go)

Depends: Todd go + §2 green

- [ ] 4.1 Clarify README dual audience: fork overlay / tommy-ca vs retained upstream Key Features + nkaz001 badges (annotate or retarget where safe)
- [ ] 4.2 DEVELOPMENT footnotes: libclang for default `live`; py `s3` may need rustc newer than crate MSRV 1.91.1
- [ ] 4.3 Soft-after #1: if README overlay settlement/fee prose touched, align with dual-settlement primary+safety-net wording
- [ ] 4.4 Merge delta into canonical `openspec/specs/product-boundary/spec.md`
- [ ] 4.5 MUST NOT: claim Polymarket live; claim CI green; wipe upstream tutorials; promote ROADMAP live checkboxes as fork done

## 5. Archive

Depends: §4 complete

- [ ] 5.1 Archive per openspec-git-discipline
- [ ] 5.2 Update ledger; reaffirm no LIVE/CI invent
