# Query Execution Plan Analysis *AI Prompt *

Analyze this query's execution plan and identify optimization opportunities. Database: {{database}} Query: {{query}} Table sizes: {{table_sizes}} Current runtime: {{runtime}} 1.... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze this query's execution plan and identify optimization opportunities.

Database: {{database}}
Query: {{query}}
Table sizes: {{table_sizes}}
Current runtime: {{runtime}}

1. Reading the EXPLAIN output (PostgreSQL):
 Run: EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) <query>;

 Key nodes to identify:
 - Seq Scan: reading all rows — acceptable for small tables, problematic for large ones
 - Index Scan: using an index — usually good
 - Index Only Scan: no heap access needed (covering index) — best case
 - Hash Join / Merge Join: efficient for large joins
 - Nested Loop: efficient when inner side is small or indexed; slow for large outer sets
 - Sort: expensive on large datasets if no index supports the ORDER BY
 - Hash Aggregate: GROUP BY without index; may spill to disk if hash table exceeds work_mem

2. Cost interpretation:
 - Cost is in arbitrary units (not milliseconds)
 - cost=startup..total: startup is cost to return first row; total is cost for all rows
 - Rows: estimated row count (if vastly different from actual: statistics are stale → ANALYZE)
 - Buffers hit=N: N pages from buffer cache (fast); Buffers read=N: N pages from disk (slow)

3. Common anti-patterns and fixes:

 Seq scan on a large table:
 Fix: add an index on the filter column

 Bad row estimate (actual >> estimated):
 Fix: ANALYZE the table; consider statistics targets: ALTER TABLE orders ALTER COLUMN status SET STATISTICS 500;

 Nested Loop on large tables:
 Fix: ensure join columns are indexed; consider enable_nestloop=off temporarily to force hash join

 Sort without index:
 Fix: add index matching the ORDER BY columns (with the same sort direction)

 Function on indexed column (prevents index use):
 WHERE LOWER(email) = 'test@example.com' -- cannot use index on email
 Fix: use a functional index: CREATE INDEX ON users (LOWER(email));

4. Work memory for sorts and hash joins:
 SET work_mem = '256MB'; -- only for the current session, for a specific expensive query
 Large sorts and hash aggregates may spill to disk if work_mem is too low.
 Check: 'Batches: 4' in hash join node means memory spilled to disk.

Return: annotated EXPLAIN output, identified bottlenecks, specific fixes with DDL/SQL, and expected improvement. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin query optimization work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Query Optimization or the wider Database Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Reading the EXPLAIN output (PostgreSQL):, Seq Scan: reading all rows — acceptable for small tables, problematic for large ones, Index Scan: using an index — usually good. The final answer should stay clear, actionable, and easy to review inside a query optimization workflow for database engineer work. 

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

Once you have the first result, continue deeper with related prompts in Query Optimization.
