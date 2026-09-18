# Slow Query Analysis *AI Prompt *

Identify and fix slow queries in this database. Database: {{database}} Monitoring tool: {{tool}} (pg_stat_statements, slow query log, pgBadger, DataDog) Problem symptoms: {{symp... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Identify and fix slow queries in this database.

Database: {{database}}
Monitoring tool: {{tool}} (pg_stat_statements, slow query log, pgBadger, DataDog)
Problem symptoms: {{symptoms}}

1. Find slowest queries with pg_stat_statements:
 SELECT query,
 calls,
 mean_exec_time,
 total_exec_time,
 stddev_exec_time,
 rows / calls AS avg_rows
 FROM pg_stat_statements
 ORDER BY total_exec_time DESC
 LIMIT 20;

 Focus on: highest total_exec_time (biggest impact on the system overall), not just highest mean.

2. Find queries with high variance (stddev >> mean):
 -- These queries are sometimes fast, sometimes very slow (plan instability)
 SELECT query, mean_exec_time, stddev_exec_time,
 stddev_exec_time / NULLIF(mean_exec_time, 0) AS cv
 FROM pg_stat_statements
 WHERE calls > 100
 ORDER BY cv DESC;

3. Slow query log:
 log_min_duration_statement = 1000 -- log all queries > 1 second
 pgBadger: parse PostgreSQL logs into an HTML report with top slow queries, lock waits, and error counts

4. Common slow query patterns:

 N+1 queries: app issues 1 query to get N records, then N queries for details
 Fix: rewrite as a single JOIN query

 Missing index on WHERE / JOIN column:
 Fix: EXPLAIN ANALYZE the query; add index on the Seq Scan column

 Returning too many rows:
 Fix: add LIMIT; use pagination (keyset pagination is faster than OFFSET for large pages)

 Implicit type cast prevents index use:
 WHERE user_id = '12345' -- user_id is INTEGER; string causes type cast → no index
 Fix: match parameter type to column type

 Large IN (...) clause:
 WHERE id IN (1,2,3,...,10000) -- creates a large OR condition
 Fix: use a temporary table or VALUES() with JOIN instead

5. Auto_explain for plan logging:
 LOAD 'auto_explain';
 SET auto_explain.log_min_duration = 1000;
 SET auto_explain.log_analyze = true;
 -- Logs the execution plan for every query > 1 second

Return: slow query identification queries, pattern diagnosis for each slow query, fix recommendations, and auto_explain configuration. 
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

The AI should return a structured result that covers the main requested outputs, such as Find slowest queries with pg_stat_statements:, Find queries with high variance (stddev >> mean):, Slow query log:. The final answer should stay clear, actionable, and easy to review inside a query optimization workflow for database engineer work. 

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
