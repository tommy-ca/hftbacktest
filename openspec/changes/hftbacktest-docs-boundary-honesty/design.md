## Context

S9 / A3 / I1 Act-on #3: graftable docs honesty. Product boundary remains engine + Polymarket backtest overlay. README retains upstream identity chrome while overlay section speaks fork truth — dual audience needs clarification, not a rewrite that flattens upstream tutorials.

## Goals / Non-Goals

**Goals.**

- Clarify README dual audience: fork overlay / tommy-ca vs retained upstream Key Features + nkaz001 badges (annotate or retarget where safe).
- Add DEVELOPMENT footnotes: libclang for default `live`; py `s3` may need rustc newer than crate MSRV 1.91.1.
- Keep docs claims aligned with PRODUCT non-goals (no Polymarket live; no invent CI green).

**Non-Goals.**

- Claim Polymarket live; claim CI green; wipe upstream tutorials; promote ROADMAP live checkboxes as fork done; delete ambient collector/connector; engine code edits; invent LIVE PASS.

## Decisions

1. **Dual-audience README strategy.** Prefer annotate / clarify (fork consumers read overlay + tommy-ca identity; upstream Key Features retained as upstream chrome) and retarget clone/badge URLs where safe — not a full README replace.
2. **DEVELOPMENT footnotes.** libclang + rustc>MSRV for `s3` as Static/Metadata honesty from S7 — not a CI green claim.
3. **ROADMAP.** Leave as inherited upstream wishlist; annotate only if needed to prevent fork-done misread — do not rewrite as delivered.
4. **Soft-after #1.** If README overlay fee/settlement prose is touched, keep dual-settlement wording consistent with overlay-solid-dry.
5. **Capability scope.** Prefer `product-boundary` only for this graft (README + DEVELOPMENT are boundary/docs honesty).

### Alternatives rejected

- Wipe upstream Key Features / tutorials — rejected (UPSTREAM skip list / A3).
- Retarget every badge blindly without checking fork Actions truth — rejected (would invent CI/RTD green).
- Promote live ROADMAP items as fork Act-on done — rejected (PRODUCT + parks).

## Risks

- Over-editing README breaks upstream sync conflict surface — mitigate with minimal annotate/retarget.
- Badge retarget to tommy-ca where Actions still lack verify workflow — mitigate: retarget only where truth holds; otherwise annotate upstream-vs-fork.
- Soft wording drift vs overlay-solid-dry — mitigate with apply checklist task.

## Migration

Propose-only. Apply (Todd go): README annotate/retarget; DEVELOPMENT footnotes; merge product-boundary delta. No runtime migration.

## Open Questions

- Which badges are safe to retarget vs annotate-as-upstream — decide at apply with Static fork Actions inventory (still no invent green).
