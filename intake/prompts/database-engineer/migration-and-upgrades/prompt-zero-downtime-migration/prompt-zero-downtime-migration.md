# Zero-Downtime Schema Migration *AI Prompt *

Design a zero-downtime schema migration strategy for this production database. Change type: {{change}} (add column, rename column, change type, add index, split table) Table siz... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a zero-downtime schema migration strategy for this production database.

Change type: {{change}} (add column, rename column, change type, add index, split table)
Table size: {{table_size}} (rows, approximate GB)
Database: {{database}}
Max acceptable downtime: {{max_downtime}}

1. Safe operations (instant, no lock):
 - Adding a column with a default value (PostgreSQL 11+)
 - Adding a NOT NULL column with a default (PostgreSQL 11+)
 - Adding a foreign key with NOT VALID (deferred validation)
 - Creating an index CONCURRENTLY
 - Dropping an index CONCURRENTLY

2. Dangerous operations (requires full table lock):
 - Changing a column type (ALTER COLUMN ... TYPE)
 - Adding a NOT NULL constraint to an existing column
 - Setting a default that requires table rewrite
 - Adding a UNIQUE constraint (without using CONCURRENTLY)

3. Add column with default (zero-downtime, PostgreSQL 11+):
 ALTER TABLE orders ADD COLUMN is_flagged BOOLEAN DEFAULT FALSE;
 - In PostgreSQL 11+: this is instant (the default is stored in the catalog, not written to each row)
 - In PostgreSQL < 11: causes a full table rewrite — use a nullable column first, then backfill

4. Add index concurrently:
 CREATE INDEX CONCURRENTLY idx_orders_customer ON orders (customer_id);
 - Does not hold a full table lock; runs in the background
 - Takes longer than a regular CREATE INDEX (2-3x)
 - May fail if there are duplicate violations; check pg_index.indisvalid after completion

5. Expand-contract pattern for column renames:
 Phase 1 (expand): Add new column, populate via trigger and backfill
 Phase 2 (contract): Update app to write to new column, stop writing to old
 Phase 3 (cleanup): Drop old column after verifying no reads remain

6. pg_repack for table rewrites online:
 - Rebuilds bloated or modified tables without a full lock
 - Useful for: changing column types, removing table bloat
 - Requires: pg_repack extension installed

Return: step-by-step migration plan for the specific change, DDL statements, rollback procedure, and validation steps. 
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

The AI should return a structured result that covers the main requested outputs, such as Safe operations (instant, no lock):, Adding a column with a default value (PostgreSQL 11+), Adding a NOT NULL column with a default (PostgreSQL 11+). The final answer should stay clear, actionable, and easy to review inside a migration and upgrades workflow for database engineer work. 

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
