#!/usr/bin/env bash
# Report commits on upstream/master that are not in HEAD (fork drift).
# Usage: scripts/check-upstream-drift.sh [upstream-remote]
set -euo pipefail

UPSTREAM_REMOTE="${1:-upstream}"
UPSTREAM_URL="${UPSTREAM_URL:-https://github.com/nkaz001/hftbacktest.git}"

if ! git remote get-url "$UPSTREAM_REMOTE" >/dev/null 2>&1; then
  echo "Adding remote '$UPSTREAM_REMOTE' -> $UPSTREAM_URL"
  git remote add "$UPSTREAM_REMOTE" "$UPSTREAM_URL"
fi

echo "Fetching $UPSTREAM_REMOTE ..."
git fetch "$UPSTREAM_REMOTE" master --quiet

RANGE="${UPSTREAM_REMOTE}/master"
COUNT="$(git rev-list --count "HEAD..${RANGE}" 2>/dev/null || echo 0)"
PIN="$(git rev-parse --short=12 "${RANGE}")"

echo "Upstream tip: ${PIN} (${RANGE})"
echo "Commits on upstream/master not in HEAD: ${COUNT}"

if [[ "$COUNT" -eq 0 ]]; then
  echo "No drift. Fork HEAD contains upstream/master."
  exit 0
fi

echo
echo "Newest first (up to 30):"
git log --oneline -30 "HEAD..${RANGE}"
echo
echo "Policy: rebase or merge upstream regularly; keep Polymarket overlay"
echo "commits identifiable. Update the pin line in UPSTREAM.md after each sync."
exit 0
