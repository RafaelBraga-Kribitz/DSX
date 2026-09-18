# Known Unknowns

What headless validation and programmatic TWB generation cannot guarantee.

## Visual fidelity

| Known | Unknown |
|-------|---------|
| XML parses; anti-patterns absent | Chart matches reference TWB pixel-for-pixel |
| TWBX contains required files | Box plot / jitter / dumbbell render identically to reference |
| Field references resolve in XML | Color palettes, fonts, mark sizes match design intent |

**Mitigation**: Compare side-by-side in Tableau Desktop; keep reference TWBX library.

## Tableau version sensitivity

- Generator targets `source-build='2024.1'`, `version='18.1'`.
- Older/newer Desktop may rewrite XML on save.
- Unknown: forward compatibility with Tableau 2025+ without re-extraction of patterns.

**Mitigation**: Document target version in generator; re-validate after Tableau upgrade.

## Payback period empty (warehouse_humanoid_tco)

- Workbook loads after Measure Names / Multiple Values fixes.
- **KPI Payback** and possibly **Payback Analysis** may still show empty values in Desktop.
- Likely causes (unverified): `Payback Display` calc nulling `payback_years=0`, winner-only filter too restrictive, Shape mark label formatting, aggregation with single filtered row.

**Mitigation**: Diagnose in Desktop (show underlying data on sheet); do not mark payback viz as done until values visible.

## KPI Shape marks

- `Custom Shape/Empty.png` dependency may vary by Tableau install.
- Unknown whether Shape KPI pattern works in Tableau Public web viewer same as Desktop.

## Random jitter reproducibility

- `random()` calc produces non-deterministic jitter each refresh.
- Acceptable for exploration; unknown impact on published snapshot aesthetics.

## Filter actions scope

- Generated action filters entire dashboard (`special-fields=all`).
- Unknown: multi-dashboard stories, URL actions, set actions — not yet encoded in generator.

## Reference TWB extraction quality

- Extracted `_twb_refs/` may be gitignored; not all community TWBX use identical XML dialect.
- Pattern from one workbook may need datasource-id substitution.

## Tableau Public constraints

- Requires Hyper extracts embedded in TWBX (confirmed).
- Unknown: file size limits, calc complexity limits, refresh behavior for generated workbooks.

## Error code mapping

| Code | Confirmed association | Unconfirmed |
|------|----------------------|-------------|
| DF4A1293 | Malformed pseudo-fields / extract metadata | All other triggers |
| A1232EF3 | "not a sql data connection" with bad field refs | — |

Treat error codes as hints; fix concrete XML evidence first.

## When to stop automating

- Highly custom interactivity (parameters driving reference lines, set actions).
- Maps, polygons, advanced analytics not present in reference set.
- Production polish requiring Desktop manual formatting pass.
