## ADDED Requirements

### Requirement: R-UP-01 Upstream Source And Baseline Pin

Feature: Upstream identity
Rule: Fork of nkaz001/hftbacktest with documented baseline tip pin.

`UPSTREAM.md` SHALL name upstream `https://github.com/nkaz001/hftbacktest` and
record a baseline tip / pin SHA for the overlay reapply point. Reviewers MUST
treat an outdated pin as hygiene debt, not invent sync PASS.

#### Scenario: UPSTREAM.md names source and pin

- **GIVEN** tip `UPSTREAM.md`
- **WHEN** Source and Baseline tip lines are read
- **THEN** upstream repo URL and a baseline tip SHA are present
- **AND** nearest tags for rust/py versions are documented

### Requirement: R-UP-02 Overlay Stays Additive

Feature: Overlay commit hygiene
Rule: Polymarket deltas stay reviewable additive surface.

Overlay commits SHALL remain reviewable as additive product surface (converter,
fee variant, stats helpers, examples, docs). Authors MUST NOT flatten Polymarket
deltas into silent edits of unrelated upstream files beyond the fee model /
bindings already touched.

#### Scenario: Additive overlay rule is documented

- **GIVEN** tip `UPSTREAM.md` Rebase hygiene and Relationship sections
- **WHEN** a change proposes overlay edits
- **THEN** the change MUST keep overlay commits identifiable and additive
- **AND** MUST NOT silently replace the full tree with pm-hftbacktest

### Requirement: R-UP-03 Drift Script Is The Local Probe

Feature: Upstream drift probe
Rule: `scripts/check-upstream-drift.sh` is the documented local drift check.

Operators SHALL use `scripts/check-upstream-drift.sh` to report commits on
`upstream/master` not in `HEAD`. Wiring that script into CI is optional and
MUST NOT be claimed as PASS in this baseline without evidence.

#### Scenario: Drift script exists at tip

- **GIVEN** tip path `scripts/check-upstream-drift.sh`
- **WHEN** the script is present and referenced from `UPSTREAM.md`
- **THEN** local drift probing is documented
- **AND** CI integration of the script is recorded as optional / not claimed green
