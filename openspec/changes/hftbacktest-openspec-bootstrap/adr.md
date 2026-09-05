# ADR review manifest — hftbacktest-openspec-bootstrap

## In-force ADRs read

| ADR | Relevance |
|---|---|
| _(none at tip)_ | `adr/` absent on `0e2488bf`; no in-force ADR set constrains Wave-0 |

## Change-local decisions

| Decision | Durable new repo ADR? | Notes |
|---|---|---|
| Activate OpenSpec `schema: intent-driven` for hftbacktest | Optional later ADR | Captured in `openspec/config.yaml` + this change; may mint `adr/0001-openspec-intent-driven.md` on archive if desired |
| Seed Static-honesty baselines; no live connector / invent CI green in bootstrap | No (spec + tasks MUST NOT) | PRODUCT/UPSTREAM/DEVELOPMENT remain tip truth |
| Overlay stays additive per UPSTREAM.md | No (spec + config rules) | Hygiene debt, not invent sync PASS |

## Must not

- Create an ADR that enables live connectors or claims Polymarket live / CI PASS.
- Supersede imaginary ADRs.
- Treat Wave-1 swarm start as implied by this bootstrap.
