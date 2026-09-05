## Context

hftbacktest tip `0e2488bf` is a public fork of `nkaz001/hftbacktest` with an
additive Polymarket backtest overlay and no OpenSpec tree. The maintain-audit
program (Wave 0–5) requires `schema: intent-driven` before swarm/arena/I1/propose
for SOLID/KISS/DRY/YAGNI Act-on clusters. Live Polymarket connector and inventing
CI green are standing Must-nots.

## Goals / Non-Goals

**Goals.**
- Install intent-driven schema + skills; activate via `openspec/config.yaml`.
- Seed Static-honesty specs for `product-boundary`, `upstream-hygiene`,
  `polymarket-overlay`, `verify-levers` from PRODUCT / UPSTREAM / DEVELOPMENT.
- Complete propose artifacts that `openspec validate --type change --strict`
  accepts.
- Keep overlay additive; document verify levers without inventing CI PASS.

**Non-Goals.**
- Enable live connectors or Polymarket live connector.
- Rewrite the HftBacktest engine.
- Invent CI green / live PASS receipts.
- Start Wave-1 S1–S10 swarm.
- Merge this PR (Horizon eng-lead owns merge).
- Flatten overlay into silent upstream edits.

## Decisions

1. **Project-local schema install (Option A).** Copy `intent-driven` into
   `openspec/schemas/intent-driven/` and skills into `.agents/skills/` per
   AGENT_INSTALL.md so the repo is self-contained.
2. **Static honesty seeds.** Canonical `openspec/specs/<capability>/spec.md`
   record tip behaviour only; Probe labels Static / Metadata / Unavailable —
   never invented live/CI PASS.
3. **Bootstrap land = install.** This PR ships `openspec/` (+ skills, `.worktrees/`
   gitignore). Change folder remains for archive after eng-lead merge + Todd go
   archive cadence; non-bootstrap product apply is STOP'd.
4. **Honesty rules in config.** Mirror polie probe/honesty patterns adapted to
   hftbacktest PRODUCT/UPSTREAM/DEVELOPMENT (no polie live dials).

### Alternatives rejected

- Bootstrap that enables live connectors — rejected (Wave-0 Must not).
- CloudAgent apply — rejected (brief: No CloudAgent).
- Inventing CI Runtime PASS without Probe — rejected (standing orders).
- Waiting to seed only after Wave-1 inventory — rejected (Wave-0 blocking).

## C4 (context)

```text
[Operator/Todd] -> [Wave-0 Heavilifter worktree]
                 -> openspec/config.yaml (intent-driven)
                 -> openspec/specs/{product-boundary,upstream-hygiene,
                      polymarket-overlay,verify-levers}
                 -> openspec/changes/hftbacktest-openspec-bootstrap/*
[Later waves]   -> swarm/arena/I1 -> Act-on proposes (separate changes)
[Parks]         -> live Polymarket connector, invent CI green (Unavailable/Must-not)
```

## Risks

- Writers treat seeded specs as license to claim live/CI-ready — mitigate with
  explicit non-goal scenarios and tasks MUST NOT.
- Archive conflict if ADDED duplicates already-seeded requirement IDs —
  mitigate in archive: confirm seed≡delta identity per openspec-git-discipline.
- Overlay flatten into upstream — mitigate via `upstream-hygiene` + config rules.

## Migration

Docs/tooling only. No runtime migration. No crate/Python API change.

## Open Questions

None for Wave-0. Upstream sync cadence, CI minimum, and overlay SOLID splits
remain Wave 1–4 questions.
