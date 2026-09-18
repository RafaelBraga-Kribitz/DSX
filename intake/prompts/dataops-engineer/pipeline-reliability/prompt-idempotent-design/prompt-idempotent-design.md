# Idempotent Pipeline Design *AI Prompt *

Design idempotent data pipelines that can be safely re-run without producing duplicate or incorrect data. Pipeline type: {{pipeline_type}} (ELT, streaming, batch scoring) Storag... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design idempotent data pipelines that can be safely re-run without producing duplicate or incorrect data.

Pipeline type: {{pipeline_type}} (ELT, streaming, batch scoring)
Storage target: {{target}} (database table, S3, data warehouse)
Re-run scenarios: {{scenarios}} (duplicate events, partial failure, backfill)

1. Idempotency definition:
 A pipeline is idempotent if running it multiple times with the same input produces the same output as running it once.
 All production pipelines should be idempotent to allow safe retries and backfills.

2. Techniques for idempotency:

 UPSERT (INSERT OR UPDATE):
 - Use MERGE or ON CONFLICT for database targets
 - Requires a unique key per record
 - Safe to run multiple times: existing rows are updated, new rows are inserted

 Delete + reinsert for partitioned tables:
 - Delete all rows for the partition being processed, then re-insert
 - DELETE FROM orders WHERE date = '2024-01-15'; followed by INSERT
 - Atomic if done in a single transaction

 Deduplication after load:
 - Load all records including duplicates into a staging table
 - Final table: SELECT DISTINCT ON (primary_key) ... ORDER BY updated_at DESC

 S3 key naming for idempotency:
 - Use deterministic paths: s3://bucket/year=2024/month=01/day=15/run_id=20240115T120000Z/
 - Overwriting the same S3 key produces a deterministic result
 - Avoid: appending to existing files (non-idempotent)

3. Partitioned backfill:
 - Process one time partition per pipeline run
 - Parameter: execution_date → determines which partition to process
 - Backfill: run the pipeline for each historical date partition
 - Airflow: dbt run --vars '{"execution_date": "2024-01-15"}'

4. Testing idempotency:
 - Run the pipeline twice for the same input date
 - Verify: row count is the same after the second run
 - Verify: no duplicate rows in the output (run unique test on primary key)

Return: idempotency technique for each storage target, backfill pattern, partition-based processing, and idempotency test design. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin pipeline reliability work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Pipeline Reliability or the wider DataOps Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Idempotency definition:, Techniques for idempotency:, Use MERGE or ON CONFLICT for database targets. The final answer should stay clear, actionable, and easy to review inside a pipeline reliability workflow for dataops engineer work. 

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

Once you have the first result, continue deeper with related prompts in Pipeline Reliability.
