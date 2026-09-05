# ADR review manifest — hftbacktest-verify-ci-baseline

## In-force sources read

| Source | Relevance |
|---|---|
| I1.md Act-on #2 / A4 recommended base | Min GHA cargo lib + test_polymarket (± fmt); presence ≠ green |
| tip `openspec/specs/verify-levers/spec.md` | Seeded R-VER-01..03 |
| S7 / S8 reports | Local PASS Metadata; no verify GHA Static |
| UPSTREAM.md token note | Drift CI deferred; workflow scope Metadata park |

## Change-local decisions

| Decision | Durable new repo ADR? | Status | Notes |
|---|---|---|---|
| Minimum verify GHA: cargo lib + targeted test_polymarket (± fmt) | No — change-local | **Accepted** (I1) | A4 O1 (+ O2 optional) |
| Honest rustc pin (≥ needs; note py s3 skew vs MSRV 1.91.1) | No — change-local | **Accepted** (I1) | Do not claim MSRV-only green for py job |
| Keep discover out until fixture policy fixed | No — change-local | **Accepted** (I1) | S7 named ERROR |
| Workflow presence ≠ CI green | No — change-local | **Accepted** (I1) | Unavailable until real runs |
| Defer coverage / CodeQL Rust / drift GHA | No — change-local | **Accepted** (I1) | Parks / first-missing named |

## Must not

Invent check-run PASS in proposal evidence. Do not ADR-require collector/connector CI for product boundary.
