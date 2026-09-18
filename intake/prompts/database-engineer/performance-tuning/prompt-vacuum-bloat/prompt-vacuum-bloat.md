# VACUUM and Bloat Management *AI Prompt *

Manage table and index bloat and configure VACUUM for this PostgreSQL database. Database: {{database}} High-write tables: {{tables}} Current bloat symptoms: {{symptoms}} (slow q... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Manage table and index bloat and configure VACUUM for this PostgreSQL database.

Database: {{database}}
High-write tables: {{tables}}
Current bloat symptoms: {{symptoms}} (slow queries, large table size, high dead tuple count)

1. Why bloat occurs:
 PostgreSQL uses MVCC (Multi-Version Concurrency Control): UPDATE and DELETE do not modify rows in place — they mark old versions as dead and insert new versions. Dead tuples accumulate until VACUUM reclaims them.

2. Measuring bloat:
 -- Dead tuple count per table
 SELECT relname, n_dead_tup, n_live_tup,
 ROUND(n_dead_tup::NUMERIC / NULLIF(n_live_tup,0) * 100, 2) AS dead_pct
 FROM pg_stat_user_tables
 ORDER BY n_dead_tup DESC
 LIMIT 20;

 -- Estimated table bloat (pgstattuple extension)
 SELECT * FROM pgstattuple('orders');

3. Autovacuum tuning:
 Default thresholds trigger VACUUM when: dead_tuples > 20% of table size.
 For large tables this is too infrequent — 20% of 100M rows = 20M dead tuples before VACUUM runs.

 Tune per high-write table:
 ALTER TABLE orders SET (
 autovacuum_vacuum_scale_factor = 0.01, -- trigger at 1% dead tuples
 autovacuum_analyze_scale_factor = 0.005,
 autovacuum_vacuum_cost_delay = 2 -- less aggressive I/O throttling for this table
 );

4. Manual VACUUM for immediate relief:
 VACUUM (ANALYZE, VERBOSE) orders; -- reclaim space, update statistics
 VACUUM (FULL) orders; -- full rewrite, reclaims max space (EXCLUSIVE LOCK)
 -- Use FULL only during maintenance windows; it blocks all access

5. pg_repack for VACUUM FULL without downtime:
 pg_repack -t orders --no-order
 - Rebuilds the table in the background without blocking reads or writes
 - Requires the pg_repack extension

6. Index bloat:
 -- Bloated indexes (indexes larger than the data they reference)
 SELECT indexname, pg_size_pretty(pg_relation_size(indexrelid)) AS index_size
 FROM pg_stat_user_indexes
 ORDER BY pg_relation_size(indexrelid) DESC;

 REINDEX INDEX CONCURRENTLY idx_orders_customer;
 -- Rebuilds the index without locking

Return: bloat measurement queries, autovacuum tuning per table, VACUUM schedule, and pg_repack plan for maintenance-free compaction. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin performance tuning work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Performance Tuning or the wider Database Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Why bloat occurs:, Measuring bloat:, Autovacuum tuning:. The final answer should stay clear, actionable, and easy to review inside a performance tuning workflow for database engineer work. 

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

Once you have the first result, continue deeper with related prompts in Performance Tuning.
