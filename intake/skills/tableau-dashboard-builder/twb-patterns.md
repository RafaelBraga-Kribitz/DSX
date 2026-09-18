# TWB XML Patterns

Validated against Tableau Desktop 2024.1 / workbook version 18.1. Prefer copying from reference TWBs over inventing tags.

## Field reference helpers

```python
def fq(ds: str, field: str) -> str:
    return f"[{ds}].{field}"

def mq(ds: str) -> str:
    return f"[{ds}].[Multiple Values]"

def mn_member(ds: str, column_instance: str) -> str:
    inst = column_instance if column_instance.startswith("[") else f"[{column_instance}]"
    return f"&quot;{fq(ds, inst)}&quot;"
```

## Column instances

Every field used on shelves/filters needs a `<column-instance>` in worksheet `<datasource-dependencies>`:

```xml
<column-instance column='[npv_eur]' derivation='Sum' name='[sum:npv_eur:qk]' pivot='key' type='quantitative' />
<column-instance column='[Scenario Label]' derivation='None' name='[none:Scenario Label:nk]' pivot='key' type='nominal' />
<column-instance column='[Payback Display]' derivation='User' name='[usr:Payback Display:qk]' pivot='key' type='quantitative' />
```

Derivation prefixes: `none:` (dimension), `sum:`, `avg:`, `usr:` (calculated), suffix `:nk` nominal, `:qk` quantitative, `:ok` ordinal.

## Measure Names filter (pivot / highlight table / stacked measures)

Members MUST be fully qualified column instances:

```xml
<filter class='categorical' column='[federated.tco].[:Measure Names]'>
  <groupfilter function='union' user:ui-domain='database' user:ui-marker='enumerate'>
    <groupfilter function='member' level='[:Measure Names]' member='&quot;[federated.tco].[sum:total_capex_eur:qk]&quot;' />
    <groupfilter function='member' level='[:Measure Names]' member='&quot;[federated.tco].[sum:total_opex_5yr_eur_pv:qk]&quot;' />
  </groupfilter>
</filter>
<slices>
  <column>[federated.tco].[:Measure Names]</column>
</slices>
```

Palette buckets use the same member strings:

```xml
<encoding attr='color' field='[federated.tco].[:Measure Names]' type='palette'>
  <map to='#4A7FB5'><bucket>&quot;[federated.tco].[sum:total_capex_eur:qk]&quot;</bucket></map>
</encoding>
```

## Measure Values → Multiple Values

For cols shelf or text/color encodings on unpivoted measures:

```xml
<cols>[federated.tco].[Multiple Values]</cols>
<text column='[federated.cap].[Multiple Values]' />
```

Dual-axis dumbbell-style:

```xml
<cols>([federated.cap].[sum:cycle_time_p50:qk] + [federated.cap].[Multiple Values])</cols>
```

## Hyper extract block

```xml
<extract count='-1' enabled='true' units='records'>
  <connection authentication='auth-none' author-locale='en_US' class='hyper'
    dbname='Data/Extracts/tco_scenarios.hyper' default-settings='hyper'
    schema='Extract' tablename='Extract'>
    <relation name='Extract' table='[Extract].[Extract]' type='table' />
  </connection>
</extract>
```

Hyper file must use schema `Extract`, table `Extract` (create via `tableauhyperapi`).

## KPI card (Shape mark + customized label)

```xml
<mark class='Shape' />
<encodings>
  <text column='[federated.tco].[sum:npv_eur:qk]' />
</encodings>
<customized-label>
  <formatted-text>
    <run fontcolor='#475960' fontsize='11'>5-year NPV</run>
    <run>Æ&#10;</run>
    <run bold='true' fontsize='20'><![CDATA[<[federated.tco].[sum:npv_eur:qk]>]]></run>
  </formatted-text>
</customized-label>
<style>
  <style-rule element='mark'>
    <format attr='shape' value='Custom Shape/Empty.png' />
    <format attr='mark-labels-show' value='true' />
  </style-rule>
</style>
```

Filter to single row (e.g. winner scenario) via categorical filter + `<slices>`.

## Reference line (constant)

```xml
<reference-line axis-column='[federated.tco].[usr:Payback Display:qk]'
  enable-instant-analytics='true' formula='constant' id='refline0'
  label='2yr target' label-type='custom' scope='per-table' value='2.0'
  value-column='[federated.tco].[usr:Payback Display:qk]' z-order='1' />
```

Style via `<style-rule element='refline'>` with matching `id='refline0'`.

## Box plot + jitter

- Box plot: `<reference-line ... formula='average' ... boxplot-whisker-type='standard' />` on measure axis.
- Jitter: calculated field `random()`, LOD encoding + jitter on rows shelf:
  `([none:Scenario Label:nk] + [sum:Calculation_jitter:qk])`
- Constant benchmark: second `<reference-line formula='constant' value='949.0' />`

## Dual-axis Gantt + Circle (dumbbell / range)

Two panes, second with `y-index='1'`:

```xml
<pane id='1'><mark class='GanttBar' />
  <encodings><size column='[sum:Calculation_pspread:qk]' /></encodings>
</pane>
<pane id='2' y-index='1'><mark class='Circle' />
  <encodings><color column='[:Measure Names]' /></encodings>
</pane>
```

## Dashboard filter action

```xml
<actions>
  <action caption='Filter Cost by Scenario' name='[Action1]'>
    <activation auto-clear='true' type='on-select' />
    <source dashboard='D1 Executive TCO' type='sheet' worksheet='NPV Ranking' />
    <command command='tsc:tsl-filter'>
      <param name='special-fields' value='all' />
      <param name='target' value='D1 Executive TCO' />
    </command>
  </action>
</actions>
```

## Dashboard layout (layout-flow)

```xml
<dashboard name='D1 Executive TCO'>
  <size maxheight='900' maxwidth='1200' minheight='900' minwidth='1200' />
  <zones>
    <zone type-v2='layout-basic'>
      <zone param='vert' type-v2='layout-flow'>
        <zone type-v2='text'>...</zone>
        <zone name='KPI Winner' />  <!-- sheet zone -->
      </zone>
    </zone>
  </zones>
</dashboard>
```

## TWBX packaging

```python
with zipfile.ZipFile(twbx_path, "w") as archive:
    archive.write(twb_path, arcname=twb_path.name)
    for hyper in extract_dir.glob("*.hyper"):
        archive.write(hyper, arcname=f"Data/Extracts/{hyper.name}")
```
