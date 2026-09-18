# Power BI Best Practices *AI Prompt *

Apply Power BI best practices to build a robust, performant report. Report goal: {{goal}} Data model: {{data_model}} Power BI version / license: {{license}} 1. Data model best p... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Apply Power BI best practices to build a robust, performant report.

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

Return: data model validation checklist, DAX pattern examples for this use case, performance optimization steps, and naming conventions. 
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

The AI should return a structured result that covers the main requested outputs, such as Data model best practices:, Star schema: always model as star schema — fact tables with foreign keys to dimension tables. Never use flat tables with denormalized data., Relationships: one-to-many only in the model — many-to-many relationships cause performance problems. Resolve many-to-many with a bridge table.. The final answer should stay clear, actionable, and easy to review inside a tool-specific implementation workflow for data visualization specialist work. 

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
