# ADR review manifest — hftbacktest-docs-boundary-honesty

## In-force sources read

| Source | Relevance |
|---|---|
| I1.md Act-on #3 / A3 / S9 | README chrome + DEVELOPMENT footnotes; no LIVE/CI invent |
| tip `openspec/specs/product-boundary/spec.md` | Seeded R-BOUND-01..03 |
| PRODUCT.md / UPSTREAM.md | Supported surface + skip list |
| S7 Metadata toolchain skew | Footnote evidence |

## Change-local decisions

| Decision | Durable new repo ADR? | Status | Notes |
|---|---|---|---|
| README dual-audience: annotate/retarget where safe; keep upstream chrome identifiable | No — change-local | **Accepted** (I1) | Do not wipe tutorials |
| DEVELOPMENT footnotes: libclang + rustc>MSRV for py s3 | No — change-local | **Accepted** (I1) | Honesty, not CI green |
| Do not claim Polymarket live or CI green in docs grafts | No — change-local | **Accepted** (I1) | Standing Must-not |
| Do not promote ROADMAP live as fork done | No — change-local | **Accepted** (I1) | Upstream wishlist |

## Must not

Invent repo-root ADR that declares LIVE PASS or CI green. Do not ADR-delete collector/connector ambient members.
