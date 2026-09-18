# Tool-Specific Implementation *AI Prompts *

3 Data Visualization Specialist prompts in Tool-Specific Implementation. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate levels and 3 single prompts. 

## AI prompts in Tool-Specific Implementation 
3 prompts Intermediate Single prompt 01 
### Power BI Best Practices 

Apply Power BI best practices to build a robust, performant report. Report goal: {{goal}} Data model: {{data_model}} Power BI version / license: {{license}} 1. Data model best p... 
Prompt text Apply Power BI best practices to build a robust, performant report.

Report goal: {{goal}}
Data model: {{data_model}}
Power BI version / license: {{license}}

1. Data model best practices:
 - Star schema: always model as star schema — fact tables with foreign keys to dimension tables. Never use flat tables with denormalized data.
 - Relationships: one-to-many only in the model — many-to-many relationships cause performance problems. Resolve many-to-many with a bridge table.
 - Import vs DirectQuery: use Import mode for anything not requiring < 1-hour freshness. DirectQuery limits DAX features and is slow.
 - Composite model: use when some tables must be real-time (DirectQuery) and others can be imported.

2. DAX best practices:
 - Use variables (VAR ... RETURN): improves readability and performance by evaluating an expression only once
 - Avoid CALCULATE inside iterators (SUMX, COUNTX): nested iteration is slow
 - Time intelligence: always use a proper Date table marked as Date table in the model
 - Measures vs calculated columns: always prefer measures for aggregations. Calculated columns are stored in memory; measures compute on demand.

3. Report design:
 - Page tabs: meaningful names, not 'Page 1, Page 2'
 - Slicer placement: top or left of page, never inside the report body
 - Visual interactions: configure interactions explicitly — by default every visual cross-filters every other
 - Bookmarks: use bookmarks for show/hide panels, not for navigation (navigation pages are better)
 - Tooltips: create tooltip pages for rich hover details

4. Performance optimization:
 - Turn off 'Auto date/time': in Options > Data load. Auto date creates hidden date tables for every date column — major performance killer.
 - Reduce cardinality: avoid high-cardinality text columns in the fact table. Use integer keys and dimension tables.
 - Disable cross-highlighting on visuals not requiring it: each cross-highlight = a DAX query
 - Use Performance Analyzer (View > Performance Analyzer) to identify slow visuals

5. Governance:
 - Deployment pipelines: use Dev → Test → Production pipeline for enterprise reports
 - Row-level security (RLS): implement in the model, not in the report layer
 - Naming conventions: [Measure Name], d_DimensionTable, f_FactTable

Return: data model validation checklist, DAX pattern examples for this use case, performance optimization steps, and naming conventions. Copy prompt Open prompt details Intermediate Single prompt 02 
### Python Visualization Code 

Write production-quality Python visualization code for this chart. Chart type: {{chart_type}} Data: {{data_description}} Library preference: {{library}} (matplotlib, seaborn, pl... 
Prompt text Write production-quality Python visualization code for this chart.

Chart type: {{chart_type}}
Data: {{data_description}}
Library preference: {{library}} (matplotlib, seaborn, plotly, altair, bokeh)
Output format: {{output}} (static PNG/PDF, interactive HTML, Jupyter notebook)

1. Library selection guide:

 Matplotlib:
 - Best for: publication-quality static charts, full control over every element
 - Pros: complete control, widely supported, PDF/SVG export
 - Cons: verbose API, interactive features require additional work

 Seaborn:
 - Best for: statistical charts (distributions, regressions, heatmaps)
 - Pros: high-level API, beautiful defaults, statistical integration
 - Cons: built on matplotlib, limited interactivity

 Plotly:
 - Best for: interactive web-based charts
 - Pros: interactive by default, Plotly Express high-level API, Dash integration
 - Cons: larger files, not ideal for publication

 Altair:
 - Best for: declarative grammar-of-graphics style charts
 - Pros: concise code, vega-altair grammar, responsive
 - Cons: data size limit in browser (5000 rows default)

2. Code standards:
 - Use matplotlib style sheets or seaborn themes for consistent styling
 - Set figure size explicitly: fig, ax = plt.subplots(figsize=(10, 6))
 - Use clear variable names that match the data (not ax1, ax2)
 - Add docstring explaining what the function produces
 - Save with appropriate DPI: plt.savefig('chart.png', dpi=300, bbox_inches='tight')

3. Accessibility in code:
 - Set colorblind-safe palette: plt.rcParams['axes.prop_cycle'] = cycler(color=okabe_ito_palette)
 - Add alt text for web outputs
 - Ensure minimum font sizes: plt.rcParams['font.size'] = 12

4. Reusable function template:
 Write the chart as a function that accepts data and styling parameters:
 def create_[chart_name](data, title, color_col=None, highlight=None, save_path=None):
 'Creates a [description] chart from the provided DataFrame.'
 ...
 return fig, ax

5. For this specific chart:
 - Import statements needed
 - Data preparation steps
 - Chart creation code with full styling
 - Annotation code
 - Save/display code

Return: complete, runnable Python code with comments, color palette definition, and example usage. Copy prompt Open prompt details Intermediate Single prompt 03 
### Tableau Best Practices 

Apply Tableau-specific best practices to build a high-quality, performant visualization. Visualization goal: {{goal}} Data source: {{data_source}} Tableau version: {{version}} 1... 
Prompt text Apply Tableau-specific best practices to build a high-quality, performant visualization.

Visualization goal: {{goal}}
Data source: {{data_source}}
Tableau version: {{version}}

1. Data source best practices:
 - Extract vs live connection: use extract (.hyper) for anything not requiring real-time updates. Extract = 10–100× faster than live connections to most databases.
 - Data modeling in Tableau: use relationships (not joins) for multi-table data sources in Tableau 2020.2+. Relationships avoid row duplication from joins.
 - Calculated fields: compute in the data source (database/ETL) when possible. Tableau calculated fields that run on every row are slow.
 - LOD expressions: use for aggregations at a different level of detail than the viz. FIXED LOD does not respect dimension filters — use INCLUDE/EXCLUDE for filter-sensitive aggregations.

2. Performance best practices:
 - Limit mark count: < 5,000 marks for smooth interaction. > 50,000 marks = investigate alternatives (aggregation, sampling).
 - Filter order: context filters first → dimension filters → measure filters. Context filters run before the rest, dramatically reducing query scope.
 - Dashboard loading: disable 'Automatically update' for slow dashboards; provide a 'Run' button.
 - Hide unused fields: remove fields from the data source that are not used in the workbook.

3. Formatting standards:
 - Remove borders from all worksheets embedded in dashboards
 - Set background to 'None' on worksheets; control background at the dashboard layout level
 - Use Layout Containers (horizontal/vertical) to control spacing and alignment
 - Font: set a single font in Format > Workbook for consistency
 - Tooltip: customize all tooltips — default tooltips show field names (ugly)

4. Color in Tableau:
 - Use a custom color palette: Tableau's default palette is acceptable but not brand-aligned
 - For sequential palettes: use ColorBrewer palettes imported as custom palettes
 - Diverging palettes: always set the midpoint explicitly (not the data average unless that is meaningful)

5. Publishing and access:
 - Add descriptions to all worksheets and dashboards (used in Tableau Server search)
 - Tag dashboards by business domain for discoverability
 - Set refresh schedule to match data update frequency (not default 'never')

6. Calculated field documentation:
 - Add a comment to every complex calculated field explaining what it computes and why
 - Format: // Revenue excl. returns = gross revenue less refunds processed in the same period

Return: implementation checklist, LOD expression examples for this use case, performance configuration, and formatting specification. Copy prompt Open prompt details 
## Recommended Tool-Specific Implementation workflow 
1 
### Power BI Best Practices 

Start with a focused prompt in Tool-Specific Implementation so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Python Visualization Code 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Tableau Best Practices 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
