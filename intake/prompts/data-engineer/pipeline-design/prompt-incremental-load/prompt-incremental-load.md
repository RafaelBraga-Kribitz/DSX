# Incremental Load Design *AI Prompt *

This prompt designs a dependable incremental loading strategy with explicit handling for watermarks, upserts, deletes, replay, and schema drift. It is aimed at pipelines that must run repeatedly without duplicates, data loss, or hard-to-debug edge cases. The output should emphasize deterministic windows and operational safety. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a robust incremental data load pattern for this source table.

Source: {{source_table}} in {{source_db}}
Target: {{target_table}} in {{target_db}}
Update pattern: {{update_pattern}} (append-only / append-and-update / full CRUD)

1. Watermark management:
 - Store the last successful watermark (max updated_at or max id) in a dedicated metadata table
 - Watermark must be committed only after successful write to target — never before
 - Handle clock skew: use watermark = max(updated_at) - safety_margin (e.g. 5 minutes) to catch late-arriving rows

2. Incremental query:
 - SELECT * FROM source WHERE updated_at > {{last_watermark}} AND updated_at <= {{current_run_time}}
 - Use a closed upper bound (current run time) to make the window deterministic and replayable
 - Add an ORDER BY to ensure consistent extraction order

3. Merge/upsert to target:
 - Use MERGE statement (or equivalent) matching on primary key
 - Handle inserts (new rows), updates (changed rows), and optionally soft deletes (is_deleted flag)
 - Never use INSERT blindly — always upsert to maintain idempotency

4. Hard delete handling:
 - If source supports deletes and CDC is not available: run a full key scan periodically (e.g. daily) and soft-delete rows absent from source
 - Add deleted_at and is_current columns to target table

5. Backfill procedure:
 - To re-process a date range: set watermark back to range start and re-run
 - Ensure the merge logic is idempotent so backfill does not create duplicates

6. Schema change handling:
 - Before each run, compare source schema to last known schema
 - Alert on new, removed, or type-changed columns before proceeding

Return: watermark table DDL, incremental query, merge statement, delete handling, and backfill procedure. 
```

## When to use this prompt 
Use case 01 
When moving from full refreshes to incremental processing. 
Use case 02 
When building pipelines for mutable source tables. 
Use case 03 
When you need safe backfills and replayable extraction windows. 
Use case 04 
When source deletes or schema changes must be handled explicitly. 

## What the AI should return 

Return the full incremental design: metadata table DDL, watermark logic, extraction query, merge or upsert statement, delete-handling approach, and backfill procedure. Explain how idempotency is preserved and where late-arriving data is handled. Include failure scenarios to watch for and how the design mitigates them. 

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

Once you have the first result, continue deeper with related prompts in Pipeline Design.
