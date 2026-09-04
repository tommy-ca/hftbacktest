Polymarket examples
===================

Notebooks adapted from the mileswangs/pm-hftbacktest overlay:

* ``endline.ipynb`` — endgame / certainty-zone style strategy sketch
* ``reverse.ipynb`` — reverse-style sketch

They expect Polymarket L2 / trade data (for example from pmdata.dev) and use
``BacktestAssetPoly``, ``polymarket_to_hbt``, ``binary_fee_model``, and
``PolyAssetRecord``.

Upstream CEX tutorials remain in the parent ``examples/`` directory.


Fees and settlement stats
-------------------------

* ``binary_fee_model(maker_rate, taker_rate)`` charges
  ``qty * rate * price * (1 - price)``. Negative rates are rebates (credit).
* ``Stats.earn`` is last equity after fee (``equity_wo_fee - fee``). Mark-to-
  settlement assumptions: resolve books in ``polymarket_to_hbt`` plus the
  ``PolyAssetRecord`` / ``fix_record_prices`` snap; see those docstrings.
