# Tasks: hftbacktest-openspec-bootstrap

> Schema: intent-driven. Session-sized.
> Wave-0 OpenSpec bootstrap only. MUST NOT enable live connectors.
> MUST NOT invent CI green / Polymarket live PASS.
> MUST NOT rewrite engine. MUST NOT start Wave-1 swarm.
> Bootstrap apply = install itself. STOP before non-bootstrap product apply.

## 0. Preconditions (read-only)

- [x] 0.1 Tip SHA Probe: `0e2488bf9c8dc40acbf6e1255d91585e0549bffc` (floor ≥ required)
- [x] 0.2 Confirm no prior `openspec/` on tip before this branch
- [x] 0.3 Worktree: `/workspace/hftbacktest/.worktrees/chore/hftbacktest-openspec-bootstrap`
      on branch `chore/hftbacktest-openspec-bootstrap`
- [x] 0.4 Probe PRODUCT.md / UPSTREAM.md / DEVELOPMENT.md + workflows inventory

## 1. Propose atoms (Wave 0) — bootstrap land

Depends: §0

- [x] 1.1 Install intent-driven per AGENT_INSTALL.md (schema + skills)
- [x] 1.2 `openspec/config.yaml` with `schema: intent-driven` + honesty rules
- [x] 1.3 Seed `openspec/specs/{product-boundary,upstream-hygiene,polymarket-overlay,verify-levers}/`
- [x] 1.4 `proposal.md` — Probe evidence recorded (Static / Metadata / Unavailable)
- [x] 1.5 Delta specs with `## ADDED` + `#### Scenario:`
- [x] 1.6 `design.md`
- [x] 1.7 `adr.md`
- [x] 1.8 `.openspec.yaml` (schema: intent-driven)

## 2. Verify atoms (offline — before any non-bootstrap product apply)

Depends: §1 complete

- [x] 2.1 Ensure `openspec` on PATH (`/home/box/.local/bin`)
- [x] 2.2 `openspec schema validate` (intent-driven)
- [x] 2.3 `openspec validate --type change --strict hftbacktest-openspec-bootstrap`
- [x] 2.4 Fix propose artifacts until strict passes
- [x] 2.5 Confirm no engine/live-connector edits; no invented CI/live PASS

## 3. Hand-off (stop)

Depends: §2 green

- [x] 3.1 Commit conventional: `chore(openspec): Wave-0 intent-driven bootstrap`
- [x] 3.2 Push + open ready PR to `master` (propose/bootstrap only)
- [x] 3.3 Update orch ledger/README with PR URL
- [x] 3.4 Hand Horizon eng-lead the PR — **DO NOT merge** from executor
- [x] 3.5 **STOP** — no Wave-1 swarm; no non-bootstrap product apply until Todd go

## 4. Apply atoms (non-bootstrap — gated; not this Wave-0 session)

Depends: Todd go + separate Act-on changes

- [ ] 4.1 No non-bootstrap product apply in this change
- [ ] 4.2 MUST NOT enable live connectors; MUST NOT invent CI/live PASS
- [ ] 4.3 MUST NOT rewrite engine outside future tasked Act-on changes

## 5. Archive

Depends: eng-lead merge of this bootstrap PR + program archive cadence

- [ ] 5.1 Archive per openspec-git-discipline after merge on tip
- [ ] 5.2 Reaffirm overlay additive + no live connector; ping Horizon for Wave-1
