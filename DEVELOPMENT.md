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

# Polymarket overlay notes

- Converter and stats helpers need `polars` (already a core dependency).
- Overlay examples: `examples/polymarket/`.
- Product boundary: `PRODUCT.md`. Upstream pin: `UPSTREAM.md`.
