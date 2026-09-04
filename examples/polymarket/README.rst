Polymarket examples
===================

Notebooks adapted from the mileswangs/pm-hftbacktest overlay:

* ``endline.ipynb`` — endgame / certainty-zone style strategy sketch
* ``reverse.ipynb`` — reverse-style sketch

They expect Polymarket L2 / trade data (for example from pmdata.dev) and use
``BacktestAssetPoly``, ``polymarket_to_hbt``, ``binary_fee_model``, and
``PolyAssetRecord``.

Upstream CEX tutorials remain in the parent ``examples/`` directory.
