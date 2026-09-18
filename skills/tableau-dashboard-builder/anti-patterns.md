# Tableau TWB Anti-Patterns

Each entry: symptom → bad pattern → fix.

## Wrong Measure Values pseudo-field

**Symptom**: Warning "There is no field named ':Measure Values'"; internal errors A1232EF3 / DF4A1293.

**Bad**:
```xml
<cols>[federated.tco].[:Measure Values]</cols>
<text column='[federated.cap].[:Measure Values]' />
```

**Fix**: Use `[datasource].[Multiple Values]` everywhere Measure Values appears on shelves or encodings.

---

## Raw Measure Names filter members

**Symptom**: "There is no field named '[total_capex_eur]'" (or `[n_episodes]`, etc.); Tableau removes fields from worksheet.

**Bad**:
```xml
<groupfilter function='member' level='[:Measure Names]' member='&quot;[total_capex_eur]&quot;' />
```

**Fix**: Use fully qualified column instance:
```xml
member='&quot;[federated.tco].[sum:total_capex_eur:qk]&quot;'
```

Same rule applies to palette `<bucket>` values in color encodings.

---

## Sparse Hyper extract connection

**Symptom**: Workbook fails to load extracts; SQL connection errors.

**Bad**:
```xml
<connection class='hyper' dbname='...' schema='Extract' tablename='Extract' />
```

**Fix**: Add `authentication`, `author-locale`, `default-settings='hyper'` and inner relation:
```xml
<relation name='Extract' table='[Extract].[Extract]' type='table' />
```

---

## Missing column-instance in worksheet deps

**Symptom**: Field exists in datasource but worksheet cannot resolve shelf reference.

**Bad**: Reference `[sum:npv_eur:qk]` on cols without matching `<column-instance>` in that worksheet's `<datasource-dependencies>`.

**Fix**: Duplicate required columns + column-instances in each worksheet's dependency block (Tableau expects per-worksheet deps).

---

## Missing `<slices>` for filtered dimensions

**Symptom**: Filter applies inconsistently or action filters behave oddly.

**Fix**: After categorical filters on dimensions or Measure Names, add matching `<slices><column>...</column></slices>`.

---

## Malformed except/union filters

**Symptom**: TWB parse errors or filters ignored.

**Bad**: Invalid `except` groupfilter syntax.

**Fix**: Use `union` with explicit `member` entries for include lists (see payback scenario filter pattern in examples).

---

## Hand-editing generated TWB without updating generator

**Symptom**: Fixes work once, regress on next `build_twb.py` run.

**Fix**: Change generator only; TWB is output artifact.

---

## Claiming success from XML parse alone

**Symptom**: "Fixed" workbook still blank or wrong in Desktop.

**Fix**: Run `validate_twb.py` AND manual Desktop QA checklist (see workflow.md).

---

## Absolute paths in generator

**Symptom**: TWB works on one machine, breaks on another.

**Bad**: Hard-coded `/Users/...` in CSV directory connections.

**Fix**: Use relative paths or `Path(__file__).resolve().parent` for packaged TWBX.

---

## Hyper schema mismatch

**Symptom**: Extract connection fails silently.

**Bad**: Default `public` schema or wrong table name in Hyper file.

**Fix**: Create schema `Extract`, table `Extract`; match TWB connection attributes.
