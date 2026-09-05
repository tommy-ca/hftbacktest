# Build and Test

Prefer an editable install of the Python extension:

1. Create/activate a venv under `py-hftbacktest/` if needed.
2. From the repo root: `maturin develop -m py-hftbacktest/Cargo.toml`
3. Run Rust tests: `cargo test -p hftbacktest --lib`
4. Run Python tests:

   ```
   PYTHONPATH="$PWD/py-hftbacktest:$PWD/py-hftbacktest/tests" \
     python -m unittest discover -s py-hftbacktest/tests -p "test_*.py"
   ```

   Targeted overlay tests: `python -m unittest py-hftbacktest.tests.test_polymarket`

`maturin develop` places the built extension where Python can import it on
Linux, macOS, and Windows. Manual copy of the built artifact is a fallback
only if needed: Linux `.so`, macOS `.dylib`, Windows `.pyd`.

# Toolchain footnotes (honesty — not CI green)

- **Crate MSRV** is `rust-version = "1.91.1"` in `hftbacktest/Cargo.toml`.
  `cargo test -p hftbacktest --lib` is expected to work at that pin (or newer).
- **Default Rust features include `live`** (iceoryx2). Building the default
  feature set typically needs **libclang / clang** for bindgen. Install
  platform libclang (e.g. `libclang-dev` + `clang` on Debian/Ubuntu) or trim
  features if you are not exercising live IPC.
- **Python binding `s3` skew:** `py-hftbacktest` depends on `hftbacktest` with
  features `backtest` + `s3`. Current AWS crate resolution may require a
  **rustc newer than MSRV 1.91.1** (observed ≥ 1.94.1; local probe succeeded on
  1.98.1). Do not silently claim MSRV-only green for `maturin develop` / py
  overlay jobs.
- **Verify CI:** Minimum workflow body is authored at
  `openspec/changes/hftbacktest-verify-ci-baseline/artifacts/verify.yml`
  (rust-lib + targeted `test_polymarket`; discover OUT). Landing into
  `.github/workflows/verify.yml` is gated by the Metadata park: GitHub OAuth
  token needs **`workflow` scope** (see `UPSTREAM.md`). **Workflow presence
  is not CI green** — treat Actions check-run evidence separately; local PASS
  remains Metadata until Runtime check runs exist. Full unittest **discover**
  stays out of minimum CI until the `tmp_20240501.npz` fixture policy is fixed.

# Polymarket overlay notes

- Converter and stats helpers need `polars` (already a core dependency).
- Overlay examples: `examples/polymarket/`.
- Product boundary: `PRODUCT.md`. Upstream pin: `UPSTREAM.md`.
- **Dual settlement (intentional primary + safety-net):** converter
  resolve-book injection is primary; `PolyAssetRecord` / `fix_record_prices`
  snap is the stats-side safety net. Keep both unless a later Act-on with
  strong tests collapses them. Covered by targeted `test_polymarket`.

## Fee-formula prose sync checklist

When Act-on work touches fee-formula documentation, sync these surfaces so the
binary fee formula stays consistent (`quantity * fee_rate * price * (1 - price)`):

1. Rust: `hftbacktest/src/backtest/models/fee.rs` (`BinaryFeeModel` docs)
2. PyO3: `py-hftbacktest/src/lib.rs` (`binary_fee_model` docs)
3. README overlay highlight: `README.rst` (`binary_fee_model` bullet)

Checklist is documentary hygiene only — not CI green and not live trading fee
behavior beyond the backtest overlay. No fee crate extract.
