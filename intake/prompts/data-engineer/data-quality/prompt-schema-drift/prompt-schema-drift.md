# Schema Drift Detection *AI Prompt *

This prompt catches upstream schema changes before they cause silent data corruption or pipeline failures. It is useful for pipelines that depend on external systems, files, or APIs where fields can appear, disappear, or change type unexpectedly. The answer should distinguish between informative drift and truly breaking changes. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement automated schema drift detection to catch upstream schema changes before they break the pipeline.

1. Schema snapshot:
 - After each successful run, save the source schema to a metadata table: column_name, data_type, is_nullable, ordinal_position, table_name, snapshot_date
 - Schema fingerprint: compute a hash of the sorted column list and types — quick change detection

2. Drift detection (run before each pipeline execution):
 Compare current source schema against the last known good schema:
 - NEW columns: column exists in current schema but not in snapshot
 - REMOVED columns: column exists in snapshot but not in current schema
 - TYPE CHANGES: column exists in both but data type has changed
 - RENAME: column removed and new column added with similar name — flag as possible rename
 - REORDERING: column ordinal positions changed (matters for positional file formats like CSV)

3. Severity classification:
 - BREAKING changes (block pipeline):
 - Removed column that is used downstream
 - Type change that is not backwards compatible (VARCHAR to INT)
 - WARNING changes (log and continue):
 - New column added (schema evolution — may need to add to downstream tables)
 - Type widening (INT to BIGINT, VARCHAR(50) to VARCHAR(255))
 - INFO:
 - Ordinal position change only
 - New column not used downstream

4. Automated response:
 - BREAKING: halt the pipeline, alert on-call, create a ticket
 - WARNING: continue pipeline, send a non-urgent notification to data team
 - Update the schema snapshot only after a successful run

Return: schema snapshot table DDL, drift detection query, severity classification logic, and alert templates. 
```

## When to use this prompt 
Use case 01 
When pipelines depend on upstream schemas that can change without notice. 
Use case 02 
When CSV, JSON, API, or database schemas must be monitored automatically. 
Use case 03 
When you need a pre-run schema gate before transformation starts. 
Use case 04 
When different drift types require different alerting and blocking behavior. 

## What the AI should return 

Return the schema snapshot metadata design, drift-detection query or algorithm, severity classification rules, and automated response flow. Include examples of new columns, removed columns, incompatible type changes, and likely renames. The result should specify exactly when to halt the pipeline and when to continue with warnings. 

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
