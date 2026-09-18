# Indexing Strategy *AI Prompt *

Design an indexing strategy for this table and query workload. Table: {{table_name}} with {{row_count}} rows Query patterns: {{query_patterns}} (filter columns, join columns, so... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design an indexing strategy for this table and query workload.

Table: {{table_name}} with {{row_count}} rows
Query patterns: {{query_patterns}} (filter columns, join columns, sort columns, aggregations)
Database: {{database}}
Write vs read ratio: {{write_read_ratio}}

1. Index types:

 B-tree (default):
 - Best for: equality (=), range (<, >, BETWEEN), ORDER BY, most queries
 - Used for: 95% of indexes; the safe default

 Hash:
 - Only equality lookups (=); faster than B-tree for pure equality at high cardinality
 - PostgreSQL: hash indexes are now WAL-logged (safe); MySQL: InnoDB does not support hash

 GIN (Generalized Inverted Index):
 - For: full-text search, JSONB containment (@>), array operators (@>, &&)
 - Slower to build and update; fast for containment queries

 GiST:
 - For: geometric data, range types (tsrange, daterange), PostGIS

 Partial index:
 - Index only a subset of rows matching a WHERE condition
 - CREATE INDEX ON orders (customer_id) WHERE status = 'active';
 - Much smaller and faster than a full index when only a small fraction of rows match

 Covering index (INCLUDE clause):
 - Include additional columns in the index leaf nodes
 - Allows index-only scans (no heap access needed)
 - CREATE INDEX ON orders (customer_id) INCLUDE (order_amount, created_at);

2. Composite index column order:
 - Put the most selective column first
 - Put range conditions last
 - An index on (a, b, c) supports queries filtering on a, a+b, or a+b+c; not on b or c alone

3. Index bloat and maintenance:
 - REINDEX or VACUUM on PostgreSQL to reclaim dead index space
 - Monitor index size and usage: pg_stat_user_indexes (use_count = 0 → unused index)
 - Unused indexes hurt write performance with no read benefit — drop them

4. Write performance trade-off:
 - Each index slows INSERT, UPDATE, DELETE
 - High write ratio: minimize indexes to only the most critical
 - Read-heavy OLAP tables: more indexes acceptable

Return: index recommendations per query pattern, DDL for each index, covering index opportunities, and maintenance schedule. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin schema design work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Schema Design or the wider Database Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Index types:, Best for: equality (=), range (<, >, BETWEEN), ORDER BY, most queries, Used for: 95% of indexes; the safe default. The final answer should stay clear, actionable, and easy to review inside a schema design workflow for database engineer work. 

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

Once you have the first result, continue deeper with related prompts in Schema Design.
