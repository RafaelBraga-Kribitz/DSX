"""Shared pinned counts for the zero-mint tripwire tests.

These numbers are deliberate tripwires, not facts derived at run time. Each one
is asserted by more than one test module, and each is meant to turn the suite red
when something is added or removed without a conscious decision:

- A new finding code (a "mint") must bump ``EXPECTED_CATALOGUE_TOTAL`` here, in
  the same change that adds the code to ``references/finding-codes.md`` and to
  ``_MINTED_CODES`` in ``tests/test_finding_catalogue_invariant.py``.
- A new ``dsx-*`` skill must bump ``DSX_SKILL_COUNT`` here, in the same change
  that registers it in ``capabilities/dsx/capability.json``.
- ``SNAPSHOT_TOTAL`` is the size of the byte-frozen Phase-12 snapshot
  (``tests/fixtures/finding-codes-phase12.md``). It never changes.

Editing these in lockstep with a mint or a new skill is the intended
maintenance cost: it forces the change to be deliberate. Keeping them in one
place means one edit instead of three files.

The leading underscore keeps this module out of ``unittest discover``'s
``test*.py`` pattern (the same convention as ``tests/_trail_seed.py``).
"""

from __future__ import annotations

# Codes in references/finding-codes.md: the Phase-12 snapshot's 256 plus the 23
# additive mints listed in tests/test_finding_catalogue_invariant.py::_MINTED_CODES.
EXPECTED_CATALOGUE_TOTAL = 279

# Codes in the byte-frozen Phase-12 snapshot. Never changes (D-08).
SNAPSHOT_TOTAL = 256

# dsx-* skills under skills/ and in capabilities/dsx/capability.json: 13 through
# Phase 14, plus dsx-reproduce (Phase 16). The using-dsx entry skill is not counted.
DSX_SKILL_COUNT = 14
