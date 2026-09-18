# Data Migration Pipeline *AI Prompt *

Design a safe, reversible data migration pipeline for this schema change or data movement. Migration: {{migration_description}} (e.g. split a table, merge schemas, move to new d... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a safe, reversible data migration pipeline for this schema change or data movement.

Migration: {{migration_description}} (e.g. split a table, merge schemas, move to new database)
Data volume: {{volume}}
Max downtime: {{max_downtime}}
Database: {{database}}

1. Migration principles:
 - Never modify data in place without a backup
 - Test in staging with a production-size data clone first
 - Build in a rollback path for every step
 - Migrate data in small batches, not one massive transaction

2. Batch migration pattern:
 DO $$
 DECLARE
 batch_size INT := 10000;
 last_id BIGINT := 0;
 max_id BIGINT;
 BEGIN
 SELECT MAX(id) INTO max_id FROM source_table;
 WHILE last_id < max_id LOOP
 INSERT INTO target_table
 SELECT ... FROM source_table
 WHERE id > last_id AND id <= last_id + batch_size;
 last_id := last_id + batch_size;
 PERFORM pg_sleep(0.1); -- throttle to avoid I/O saturation
 END LOOP;
 END $$;

3. Online migration with dual-write:
 Phase 1: Add new table/column; application writes to both old and new
 Phase 2: Backfill old data from old to new in batches
 Phase 3: Verify consistency (compare row counts and key values)
 Phase 4: Switch reads to new structure; stop writing to old
 Phase 5: Remove old structure after validation period

4. Validation queries:
 -- Row count match
 SELECT (
 (SELECT COUNT(*) FROM source_table) =
 (SELECT COUNT(*) FROM target_table)
 ) AS counts_match;

 -- Checksum of key columns
 SELECT MD5(STRING_AGG(id::text || amount::text, ',' ORDER BY id))
 FROM source_table;

5. Emergency rollback:
 - Keep the old table or column intact until migration is fully validated
 - Use a feature flag to switch between old and new data paths
 - Drop old structures only after: 24h monitoring, zero errors, stakeholder sign-off

Return: batch migration script, dual-write pattern, validation queries, and rollback procedure. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin migration and upgrades work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Migration and Upgrades or the wider Database Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Migration principles:, Never modify data in place without a backup, Test in staging with a production-size data clone first. The final answer should stay clear, actionable, and easy to review inside a migration and upgrades workflow for database engineer work. 

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

Once you have the first result, continue deeper with related prompts in Migration and Upgrades.
