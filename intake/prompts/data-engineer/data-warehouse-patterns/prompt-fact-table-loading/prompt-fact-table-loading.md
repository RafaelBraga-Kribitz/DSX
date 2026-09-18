# Fact Table Loading Pattern *AI Prompt *

This prompt designs a safe and repeatable fact-loading pattern for analytical tables. It focuses on surrogate key resolution, late-arriving dimensions, partition-based loading, audit metadata, and pre/post-load validation. It is ideal for teams that want disciplined warehouse loading patterns rather than one-off ETL code. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement a robust fact table loading pattern for {{fact_table}} using a {{loading_strategy}} approach.

1. Pre-load validation:
 - Check source row count vs expected range (alert if < 80% or > 120% of yesterday's count)
 - Verify all required foreign keys exist in their dimension tables (referential integrity check)
 - Check for duplicate natural keys in the incoming batch
 - Validate numeric measure ranges (no negative revenue, no impossible quantities)

2. Surrogate key lookup:
 - Never store natural keys in the fact table — always look up the surrogate key from the dimension
 - For each foreign key: JOIN to dimension on natural key WHERE is_current = TRUE
 - For late-arriving dimensions: look up the surrogate key valid at the event time (point-in-time lookup)
 - Late-arriving facts: if the dimension record did not exist at event time, use a 'unknown' placeholder record (surrogate_key = -1)

3. Incremental load to fact table:
 - Partition by date and load one partition at a time
 - Use INSERT OVERWRITE for the current partition (idempotent, safe to re-run)
 - Never UPDATE rows in a fact table — append or overwrite partitions only

4. Post-load validation:
 - Row count reconciliation: source count = fact table insert count
 - Measure totals reconciliation: SUM(revenue) in source = SUM(revenue) in fact for the loaded date
 - No NULL surrogate keys in the output (all dimension lookups resolved)

5. Audit columns:
 - Add to every fact table: load_timestamp, pipeline_run_id, source_system

Return: pre-load validation queries, surrogate key lookup logic, incremental load SQL, and post-load reconciliation queries. 
```

## When to use this prompt 
Use case 01 
When implementing a new fact table in a warehouse. 
Use case 02 
When loading events or transactions into partitioned analytical tables. 
Use case 03 
When referential integrity and reconciliation are important. 
Use case 04 
When you need a reusable load pattern with validation built in. 

## What the AI should return 

Return pre-load validation queries, surrogate-key lookup logic, partition load SQL, post-load reconciliation checks, and audit-column guidance. Explain how late-arriving facts and dimensions are handled and what should happen when lookups fail. The output should be implementation-oriented and safe to rerun. 

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

Once you have the first result, continue deeper with related prompts in Data Warehouse Patterns.
