# Row Count Reconciliation *AI Prompt *

This prompt builds a reconciliation framework around row counts across extraction, transformation, and load stages. It is intended to make completeness issues visible quickly and consistently, especially in ETL and CDC pipelines. The focus is on metadata capture, tolerance-based comparisons, and operational alerting. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a row count reconciliation framework to verify data completeness across pipeline stages.

1. Count capture at each stage:
 - Extract: rows read from source
 - After filter: rows meeting extraction criteria
 - After transformation: rows output from each major transformation step
 - Load: rows written to target
 - Store all counts in a reconciliation metadata table: pipeline_run_id, stage, table_name, row_count, timestamp

2. Reconciliation checks:
 - Source to target: abs(source_count - target_count) / source_count < {{tolerance}} (e.g. 0.001 = 0.1% tolerance)
 - Explain expected differences: deduplication, filtering, and type-specific exclusions
 - For CDC pipelines: verify inserts + updates + deletes = total source changes

3. Historical comparison:
 - Compare today's count to the same day last week (day-of-week adjusted)
 - Alert if count differs by more than 2σ from the rolling 30-day average for that day
 - Hard alert if count is 0 (empty load — almost always a pipeline error)

4. Metadata table DDL:
 ```sql
 CREATE TABLE pipeline_reconciliation (
 run_id VARCHAR,
 pipeline_name VARCHAR,
 stage VARCHAR,
 table_name VARCHAR,
 expected_count BIGINT,
 actual_count BIGINT,
 variance_pct DECIMAL(10,4),
 status VARCHAR, -- PASS / WARN / FAIL
 run_timestamp TIMESTAMP
 )
 ```

5. Alerting:
 - FAIL: variance > {{fail_threshold}}% → block downstream, page on-call
 - WARN: variance > {{warn_threshold}}% → log warning, notify data team
 - PASS: variance within tolerance → log and continue

Return: reconciliation metadata table DDL, count capture code, comparison queries, and alerting logic. 
```

## When to use this prompt 
Use case 01 
When you need stage-by-stage completeness checks in a pipeline. 
Use case 02 
When row loss or duplication is a recurring concern. 
Use case 03 
When building metadata-driven observability for ETL jobs. 
Use case 04 
When downstream execution should depend on reconciliation status. 

## What the AI should return 

Return metadata table DDL, count-capture logic for each stage, comparison queries, status rules, and alerting behavior. Explain which count differences are expected versus suspicious, and how CDC-specific reconciliation should work. The output should support implementation as an operational control. 

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

Once you have the first result, continue deeper with related prompts in Data Quality.
