# Tableau Best Practices *AI Prompt *

Apply Tableau-specific best practices to build a high-quality, performant visualization. Visualization goal: {{goal}} Data source: {{data_source}} Tableau version: {{version}} 1... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Apply Tableau-specific best practices to build a high-quality, performant visualization.

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

Return: implementation checklist, LOD expression examples for this use case, performance configuration, and formatting specification. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin tool-specific implementation work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Tool-Specific Implementation or the wider Data Visualization Specialist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Data source best practices:, Extract vs live connection: use extract (.hyper) for anything not requiring real-time updates. Extract = 10–100× faster than live connections to most databases., Data modeling in Tableau: use relationships (not joins) for multi-table data sources in Tableau 2020.2+. Relationships avoid row duplication from joins.. The final answer should stay clear, actionable, and easy to review inside a tool-specific implementation workflow for data visualization specialist work. 

## How to use this prompt 
1 
### Open your data context 

Load your dataset, notebook, or working environment so the AI can operate on the actual project context. 
2 
### Copy the prompt text 

Use the copy button above and paste the prompt into the AI assistant or prompt input area. 
3 
### Review the output critically 

Check whether the result matches your data, assumptions, and desired format before moving on. 
4 
### Chain into the next prompt 

Once you have the first result, continue deeper with related prompts in Tool-Specific Implementation.
