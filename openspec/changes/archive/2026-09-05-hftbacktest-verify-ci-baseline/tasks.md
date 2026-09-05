# Tasks: hftbacktest-verify-ci-baseline

> Schema: intent-driven. Propose → offline verify → **STOP** → Todd-go apply → archive.
> Tip: `fdc5b7d2d909b93727020450908d65211d9f0dc7`. Workflow presence ≠ green. Soft-after overlay-solid-dry.

## 0. Preconditions (read-only)

- [x] 0.1 Tip SHA Probe: `fdc5b7d2d909b93727020450908d65211d9f0dc7`
- [x] 0.2 Re-read `openspec/specs/verify-levers/spec.md`, I1.md, A4.md, S7/S8
- [x] 0.3 Parks held: invent CI green (Must-not); CI token/`workflow` scope (Metadata — may gate apply)
- [x] 0.4 Soft-after note: if `hftbacktest-overlay-solid-dry` adds dual-settlement tests, py job must run `test_polymarket`

## 1. Propose atoms (Wave 4 — Planner)

Depends: §0

- [x] 1.1 `proposal.md` — Probe Evidence Record (Static absence; Metadata S7; Unavailable green)
- [x] 1.2 `specs/verify-levers/spec.md` — ADDED/MODIFIED requirements
- [x] 1.3 `design.md` — job shape / pin / discover defer
- [x] 1.4 `adr.md` — Accepted min GHA + honesty locks
- [x] 1.5 Spec refs: tip verify-levers R-VER-01..03

## 2. Validate --strict (offline — before any apply)

Depends: §1 complete

- [x] 2.1 `/home/box/bin/openspec validate --type change --strict hftbacktest-verify-ci-baseline`
- [x] 2.2 Probe honesty: no invented badge/check PASS in proposal
- [x] 2.3 Confirm Must-nots: discover out; no collector/connector CI; no drift GHA; no coverage/CodeQL Rust claim

## 3. STOP handoff

Depends: §2 green

- [x] 3.1 Hand Horizon `openspec/changes/hftbacktest-verify-ci-baseline/`
- [x] 3.2 Ledger: propose VERIFIED; token park may gate Wave-5
- [x] 3.3 **STOP** — no apply until Todd go (+ park exit if required)

## 4. Apply (Wave 5 — later workers; gated on Todd go)

Depends: Todd go + §2 green + token/`workflow` park exit if needed

- [x] 4.1 Workflow YAML authored (rust-lib + targeted `test_polymarket` after maturin); body at `artifacts/verify.yml`. **Park:** push into `.github/workflows/` blocked — OAuth App lacks `workflow` scope (Metadata; named in UPSTREAM/S10). Not invent green.
- [x] 4.2 Optional `cargo fmt --check` **deferred**: tip has widespread rustfmt drift (connector/examples/lib); adding the gate would invent permanent red without a separate format Act-on — honesty over invent-green
- [x] 4.3 Document honest rustc pin (≥ crate needs; note py `s3` skew vs MSRV 1.91.1) and libclang for default `live`
- [x] 4.4 Keep discover path OUT of the workflow
- [x] 4.5 Soft-after #1: confirm py-overlay job runs dual-settlement tests if present under `test_polymarket`
- [x] 4.6 Merge delta into canonical `openspec/specs/verify-levers/spec.md`
- [x] 4.7 MUST NOT: invent badge/check PASS; claim workflow presence = green; wire drift/coverage/CodeQL Rust; require collector/connector CI
- [x] 4.8 After real runs exist, Probe may cite check-run URLs — until then results remain Unavailable for "green"

## 5. Archive

Depends: §4 complete

- [x] 5.1 Archive per openspec-git-discipline
- [x] 5.2 Update ledger; reaffirm invent-CI-green Must-not
