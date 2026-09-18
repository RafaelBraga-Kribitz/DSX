# Examples: warehouse_humanoid_tco

Reference implementation in this repo. Use as template, not universal schema.

## File map

| Path | Role |
|------|------|
| `exports/tableau_public/build_twb.py` | TWB/TWBX generator (~1100 lines) |
| `exports/tableau_public/build_extracts.py` | Hyper extract builder |
| `exports/tableau_public/warehouse_humanoid_tco.twb` | Generated workbook |
| `exports/tableau_public/warehouse_humanoid_tco.twbx` | Packaged for Tableau Public |
| `exports/tableau_public/_twb_refs/*.twb` | Extracted community patterns (gitignored) |
| `exports/tableau_public/tableau_dashboard_wireframe_tco.html` | Layout wireframe |
| `docs/TABLEAU_PUBLIC_SETUP.md` | Manual setup guide (pre-generator) |

## Datasources

| ID | CSV | Worksheets |
|----|-----|------------|
| `federated.tco` | tco_scenarios.csv | KPIs, NPV Ranking, Cost Composition, Payback |
| `federated.sim` | simulation_runs.csv | Throughput Distribution, Workforce Utilization |
| `federated.cap` | humanoid_capabilities_summary.csv | Cycle Time *, Capability Highlight Table |

## Worksheets implemented

| Sheet | Pattern |
|-------|---------|
| KPI Winner / NPV / Payback | Shape + customized-label + winner filter |
| NPV Ranking | Bar + Is Winner color |
| Cost Composition | Measure Names pivot + Multiple Values cols |
| Payback Analysis | Circle + constant ref line 2.0 + scenario filter |
| Throughput Distribution | Box plot ref line + jitter + constant 949 |
| Workforce Utilization | Measure Names rows + Multiple Values color |
| Cycle Time Percentiles | Dual-axis GanttBar + Circle dumbbell |
| Cycle Time Range | GanttBar spread |
| Capability Highlight Table | Measure Names cols + Multiple Values text/color |

## Dashboards

- **D1 Executive TCO**: KPI row, NPV + Cost, Payback, filter action from NPV Ranking
- **D2 Simulation Validation**: Throughput + Utilization
- **D3 Capabilities Explorer**: Percentiles + Range + Highlight table

## Iteration history (lessons)

1. **Initial generator**: KPI cards, dashboards, filter actions from reference TWBX extraction.
2. **Load error fix**: `[:Measure Values]` → `[Multiple Values]`; extract relation child added.
3. **Measure Names fix**: Raw `[field]` members → `[federated.*].[sum:field:qk]` (and `avg:` where appropriate).
4. **Result**: Workbook opens in Desktop; payback KPI still empty (known unknown).

## Build commands

```bash
cd exports/tableau_public
python3 build_twb.py
python3 ../../.cursor/skills/tableau-dashboard-builder/scripts/validate_twb.py \
  warehouse_humanoid_tco.twb warehouse_humanoid_tco.twbx
```

## Reference TWBX sources used

- Dashboard Filter Actions.twbx — highlight table, Measure Names + Multiple Values
- Reference Line.twbx — constant reference lines
- Visualizing Distributions (#VizOfTheDay).twbx — box plot + jitter
- JITTER AND BOX PLOT FOR BUSINESS.twbx — jitter LOD pattern
- Customer_Dashboards_filters_actions.twbx — filter actions, KPI formatting

Extract with:

```bash
python3 scripts/extract_twb_refs.py --scan "exports/tableau_public/*.twbx" --out exports/tableau_public/_twb_refs/
```

## Payback Display calc (investigate empty KPI)

```tableau
IF [payback_years]=0 THEN NULL ELSE [payback_years] END
```

Winner filter restricts KPI Payback to `S-hybrid-amr` only. Verify CSV `payback_years` for that scenario is non-null and non-zero.
