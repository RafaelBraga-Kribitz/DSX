# Tableau Dashboard Builder Workflow

## Phase 1: Intake

1. **Data sources**: List CSVs or tables, column names, types, row counts.
2. **Dashboard intent**: Worksheets, chart types, KPIs, filters, actions, layout.
3. **Target platform**: Tableau Public (requires Hyper extracts in TWBX) vs Desktop-only.
4. **Reference workbooks**: Collect working `.twbx` files that implement similar patterns.

## Phase 2: Reference extraction

```bash
python3 scripts/extract_twb_refs.py --scan "*.twbx" --out _twb_refs/
```

Search extracted TWBs for the pattern you need (grep `reference-line`, `Multiple Values`, `tsc:tsl-filter`, etc.). Copy XML structure; do not guess tag names.

## Phase 3: Data preparation

- Ensure CSV headers match datasource `<column>` definitions in TWB.
- For Tableau Public: build `.hyper` files with schema `Extract`, table `Extract` via `tableauhyperapi`.
- Map business labels via calculated fields (`CASE [id] WHEN ...`) in datasource or worksheet deps.

## Phase 4: TWB generation

Recommended structure (Python generator):

| Module | Responsibility |
|--------|----------------|
| Helpers | `fq(ds, field)`, `mq(ds)` for Multiple Values, `mn_member(ds, inst)` for Measure Names |
| Datasources | CSV connection + columns + calcs + `<extract>` block |
| Worksheets | `<view>`, filters, panes, rows/cols, encodings |
| Dashboards | `layout-flow` zones, text zones, sheet zones |
| Actions | `<actions>` filter-action blocks |
| Windows | Dashboard + hidden worksheet window entries |
| main() | build extracts → write TWB → zip TWBX |

Regenerate after every XML change:

```bash
cd exports/tableau_public && python3 build_twb.py
```

## Phase 5: Headless validation

```bash
python3 scripts/validate_twb.py warehouse_humanoid_tco.twb warehouse_humanoid_tco.twbx
```

All checks must pass before opening in Tableau Desktop.

## Phase 6: Manual Tableau Desktop QA

Checklist (record pass/fail per sheet):

- [ ] Workbook opens without field-removal warnings
- [ ] No internal errors (DF4A1293, A1232EF3)
- [ ] Each worksheet shows expected marks (not blank)
- [ ] KPI cards display values (watch for empty payback / null handling)
- [ ] Filter actions work (source sheet → target dashboard)
- [ ] Reference lines visible at expected values
- [ ] Colors/legends match intent

Treat Desktop warnings as root-cause evidence. Map warning field names back to generator output.

## Phase 7: Iterate

1. Fix generator, not hand-edited TWB (unless prototyping).
2. Re-run build + validate.
3. Re-open TWBX in Desktop.
4. Document new anti-patterns in [anti-patterns.md](anti-patterns.md) if discovered.
