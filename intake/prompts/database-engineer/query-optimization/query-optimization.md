# Query Optimization *AI Prompts *

3 Database Engineer prompts in Query Optimization. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts. 

## AI prompts in Query Optimization 
3 prompts Advanced Single prompt 01 
### Deadlock and Lock Analysis 

Diagnose and resolve lock contention and deadlocks in this database. Database: {{database}} Application pattern: {{pattern}} (OLTP, batch processing, mixed) Lock issue: {{issue_... 
Prompt text Diagnose and resolve lock contention and deadlocks in this database.

Database: {{database}}
Application pattern: {{pattern}} (OLTP, batch processing, mixed)
Lock issue: {{issue_description}}

1. How deadlocks occur:
 Transaction A: locks row 1, waits for row 2
 Transaction B: locks row 2, waits for row 1
 → Neither can proceed; the database detects and rolls back one transaction.

2. Diagnosing locks in PostgreSQL:

 Active locks:
 SELECT pid, locktype, relation::regclass, mode, granted, query
 FROM pg_locks
 JOIN pg_stat_activity USING (pid)
 WHERE NOT granted;

 Blocking queries:
 SELECT blocking.pid AS blocking_pid, blocked.pid AS blocked_pid,
 blocking.query AS blocking_query, blocked.query AS blocked_query
 FROM pg_stat_activity blocked
 JOIN pg_stat_activity blocking
 ON blocking.pid = ANY(pg_blocking_pids(blocked.pid))
 WHERE blocked.wait_event_type = 'Lock';

3. Deadlock prevention strategies:

 Consistent lock ordering:
 - Always acquire locks in the same order across all transactions
 - If Transaction A locks customer then order, Transaction B must also lock customer then order

 Minimize lock duration:
 - Do expensive computation BEFORE the transaction, not inside it
 - Hold locks for as short a time as possible

 Use SELECT FOR UPDATE SKIP LOCKED for queue patterns:
 SELECT * FROM job_queue
 WHERE status = 'pending'
 ORDER BY created_at
 LIMIT 1
 FOR UPDATE SKIP LOCKED;
 - Workers pick uncontested jobs without blocking each other

 Reduce transaction scope:
 - Do not perform external API calls inside a transaction
 - Commit early; reopen if needed

4. Lock timeout:
 SET lock_timeout = '5s';
 - Prevents long lock waits from cascading into system-wide slowdowns
 - Raises LockNotAvailable exception; handle in the application with retry logic

5. Advisory locks:
 - Application-level locks without database row locking
 - SELECT pg_advisory_xact_lock(hashtext('job_processing_' || job_id::text));
 - Useful for: distributed mutual exclusion, serializing concurrent background jobs

Return: lock diagnosis queries, deadlock root cause analysis, prevention strategies, and lock timeout configuration. Copy prompt Open prompt details Intermediate Single prompt 02 
### Query Execution Plan Analysis 

Analyze this query's execution plan and identify optimization opportunities. Database: {{database}} Query: {{query}} Table sizes: {{table_sizes}} Current runtime: {{runtime}} 1.... 
Prompt text Analyze this query's execution plan and identify optimization opportunities.

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

Return: annotated EXPLAIN output, identified bottlenecks, specific fixes with DDL/SQL, and expected improvement. Copy prompt Open prompt details Intermediate Single prompt 03 
### Slow Query Analysis 

Identify and fix slow queries in this database. Database: {{database}} Monitoring tool: {{tool}} (pg_stat_statements, slow query log, pgBadger, DataDog) Problem symptoms: {{symp... 
Prompt text Identify and fix slow queries in this database.

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

Return: slow query identification queries, pattern diagnosis for each slow query, fix recommendations, and auto_explain configuration. Copy prompt Open prompt details 
## Recommended Query Optimization workflow 
1 
### Deadlock and Lock Analysis 

Start with a focused prompt in Query Optimization so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Query Execution Plan Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Slow Query Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
