## Context

Documented verify levers exist; tip has no GHA job running them. A4 recommends O1 minimum (± O2 fmt). I1 Act-on #2 proposes one PR/push workflow with honest toolchain notes. Soft-after overlay-solid-dry: job must run new dual-settlement tests if they land in `test_polymarket`.

## Goals / Non-Goals

**Goals.**

- Propose one PR/push workflow with rust-lib + py-overlay jobs (and optional format).
- Honest rustc pin and libclang documentation for CI/DEVELOPMENT consumers.
- Keep discover path out of minimum CI until fixture policy fixed.
- Explicit honesty: workflow file ≠ green checks.

**Non-Goals.**

- Invent badge/check PASS; collector/connector CI farms; drift-script GHA; coverage numbers; CodeQL Rust matrix; release-python/PyPI secret changes; claiming MSRV-only green while py job needs newer rustc.

## Decisions

1. **Job shape (A4 O1 + optional O2).**  
   - `rust-lib`: toolchain ≥ crate needs + libclang note; `cargo test -p hftbacktest --lib`.  
   - `py-overlay`: venv + `maturin develop -m py-hftbacktest/Cargo.toml` + targeted `test_polymarket` only.  
   - Optional same change: `cargo fmt --check` (rustfmt.toml exists).
2. **Rustc pin honesty.** Pin ≥ what jobs need; document MSRV 1.91.1 vs py `s3`/AWS skew (S7 Metadata). Do not silently claim MSRV-only matrix green for the py job.
3. **Discover deferred.** Do not wire full unittest discover until `tmp_20240501.npz` policy fixed.
4. **Soft-after #1.** If overlay-solid-dry adds dual-settlement tests under `test_polymarket`, py-overlay job runs them automatically via the same target.
5. **Presence ≠ green.** Spec MUST forbid inventing PASS from workflow file alone.
6. **Park.** Token/`workflow` scope may gate apply — named Metadata, not invented.

### Alternatives rejected

- Defer all new GHA (A4 O4) — rejected; first-missing verify CI is Act-on.
- Full ROADMAP CI (coverage, CodeQL Rust, drift) — rejected; breadth before baseline.
- Wire discover now — rejected; named fixture ERROR (S7).

## Risks

- Token park blocks Wave-5 apply — mitigate by naming park in tasks; propose still completes.
- Toolchain skew surprises contributors — mitigate with pin notes + DEVELOPMENT footnotes (sibling docs change).
- Writers claim CI green after merging YAML — mitigate with R-VER honesty requirements.

## Migration

Propose-only now. Apply (Todd go + park exit): add workflow YAML; document pin/libclang; do not assert green until real check runs. Soft coordinate with overlay-solid-dry test landings.

## Open Questions

- Exact rustc version string for py-overlay job (1.94.1+ vs pin to 1.98.x used in S7) — resolve at apply with lockfile resolution, document chosen pin.
- Whether fmt lives in same workflow file or separate job — prefer same change per I1 optional O2.
