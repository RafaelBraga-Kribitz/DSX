# Full SQL Development Chain *AI Prompt *

Step 1: Requirements analysis - translate the analytical requirement into precise SQL semantics. Define the grain of the output, identify the tables needed, and map each column... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Requirements analysis - translate the analytical requirement into precise SQL semantics. Define the grain of the output, identify the tables needed, and map each column in the output to its source column and any required transformations.
Step 2: Query architecture - decide whether to use a single query, CTEs, or multiple queries. Identify window functions, aggregations, or recursive CTEs needed. Sketch the logical flow before writing SQL.
Step 3: Write the query - implement the query using CTEs for each logical step. Add clear comments on each CTE's purpose. Use explicit JOINs (no implicit joins). Handle NULLs explicitly with COALESCE where appropriate.
Step 4: Correctness validation - test with known inputs and expected outputs. Verify: row count matches expectation, aggregations handle NULLs correctly, deduplication is correct, date range logic is inclusive/exclusive as intended.
Step 5: Performance review - run EXPLAIN ANALYZE. Check for Seq Scans on large tables. Identify missing indexes. Rewrite any correlated subqueries as JOINs. Check for implicit type conversions.
Step 6: Documentation - add a header comment with: purpose, inputs, outputs, business rules applied, known limitations, and author. Add inline comments for complex logic. Document any assumptions about data quality.
Step 7: Optimization and handoff - propose indexes needed for production performance. If the query is recurrent, recommend materializing as a view or a scheduled table. Provide a test dataset for regression testing. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin advanced sql work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Advanced SQL or the wider SQL Developer library. 

## What the AI should return 

The AI should return a structured result that is directly usable in a advanced sql workflow, with explicit outputs, readable formatting, and enough clarity to support the next step in sql developer work. 

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

Once you have the first result, continue deeper with related prompts in Advanced SQL.
