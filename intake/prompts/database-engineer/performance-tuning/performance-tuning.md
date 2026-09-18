# Performance Tuning *AI Prompts *

3 Database Engineer prompts in Performance Tuning. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts. 

## AI prompts in Performance Tuning 
3 prompts Advanced Single prompt 01 
### Connection Pooling with PgBouncer 

Configure PgBouncer connection pooling for this PostgreSQL deployment. Max connections PostgreSQL can handle: {{max_connections}} Application connection demand: {{app_connection... 
Prompt text Configure PgBouncer connection pooling for this PostgreSQL deployment.

Max connections PostgreSQL can handle: {{max_connections}}
Application connection demand: {{app_connections}} (peak concurrent connections from app servers)
Workload: {{workload}} (short OLTP transactions vs long-running analytics queries)

1. Why connection pooling:
 - Each PostgreSQL connection consumes ~5-10MB RAM and a process
 - With 500 app server threads each holding an open connection → 500 Postgres processes → OOM
 - PgBouncer maintains a small pool of actual database connections; app connections are multiplexed

2. Pooling modes:

 Session pooling:
 - App connection holds a server connection for its entire lifetime
 - No statement restriction; full PostgreSQL feature support
 - Limited benefit: only helps when connections are idle for long periods

 Transaction pooling (recommended for most OLTP apps):
 - App connection holds a server connection only during a transaction
 - Server connection returned to pool after COMMIT/ROLLBACK
 - 100x reduction in required server connections for typical apps
 - Restriction: prepared statements and advisory locks do not work in transaction mode
 Fix: use named prepared statements via protocol-level support (pgBouncer >= 1.21)

 Statement pooling:
 - Server connection returned after every single statement
 - Most aggressive pooling; does not support multi-statement transactions
 - Use only for read-only single-statement workloads

3. pgbouncer.ini configuration:
 [databases]
 production = host=localhost port=5432 dbname=production

 [pgbouncer]
 pool_mode = transaction
 max_client_conn = 2000
 default_pool_size = 25 # = max_connections / number_of_databases
 min_pool_size = 5
 reserve_pool_size = 5
 server_idle_timeout = 600
 client_idle_timeout = 0

4. Monitoring PgBouncer:
 Connect to the PgBouncer admin: psql -p 6432 pgbouncer
 SHOW POOLS; -- active/waiting clients, server connections
 SHOW STATS; -- requests per second, average query time
 Alert on: cl_waiting > 0 for more than 5 seconds (connection queue building up)

5. PgBouncer in Kubernetes:
 - Deploy as a sidecar or as a shared deployment per database cluster
 - Use environment variable injection for credentials (never hardcode passwords)

Return: pgbouncer.ini configuration, pool size calculation, mode recommendation, and monitoring setup. Copy prompt Open prompt details Intermediate Single prompt 02 
### PostgreSQL Configuration Tuning 

Tune PostgreSQL configuration parameters for this server and workload. Server specs: {{specs}} (RAM, CPU cores, disk type) Workload type: {{workload}} (OLTP, OLAP, mixed, write-... 
Prompt text Tune PostgreSQL configuration parameters for this server and workload.

Server specs: {{specs}} (RAM, CPU cores, disk type)
Workload type: {{workload}} (OLTP, OLAP, mixed, write-heavy)
PostgreSQL version: {{version}}

1. Memory configuration:

 shared_buffers:
 - PostgreSQL's main cache for data pages
 - Set to: 25% of total RAM
 - 32GB RAM → shared_buffers = 8GB

 effective_cache_size:
 - Estimate of total memory available for caching (OS + shared_buffers)
 - Set to: 75% of total RAM (helps the planner make better decisions)
 - Does NOT allocate memory; it's a planning hint

 work_mem:
 - Memory per sort / hash operation (not per connection!)
 - Formula: (Total RAM - shared_buffers) / (max_connections * average_parallel_queries * 2)
 - OLTP: 4-16MB; OLAP: 64-256MB
 - Too high with many connections = OOM; too low = spills to disk

 maintenance_work_mem:
 - Memory for VACUUM, CREATE INDEX, ALTER TABLE
 - Set to: 256MB - 1GB (operations run one at a time)

2. WAL and checkpoints:

 wal_buffers: 64MB (or auto-tuned by default)

 checkpoint_completion_target: 0.9
 - Spread checkpoint I/O over 90% of the checkpoint interval (reduces I/O spikes)

 max_wal_size: 4GB (default 1GB)
 - Allow larger WAL between checkpoints for write-heavy workloads

 wal_level: replica (minimum for streaming replication)

3. Connection management:
 max_connections: 100-200 (not more; use PgBouncer for connection pooling)
 PgBouncer pool_size = 10-20 × CPU cores

4. Query planner:
 random_page_cost: 1.1 for SSD (default 4.0 is for spinning disk)
 effective_io_concurrency: 200 for SSD (default 1)

5. Autovacuum tuning for high-write tables:
 ALTER TABLE orders SET (
 autovacuum_vacuum_scale_factor = 0.01,
 autovacuum_analyze_scale_factor = 0.005
 );
 - Default 20% threshold is too high for large tables; trigger more frequently

Return: postgresql.conf settings for the given server spec and workload, PgBouncer configuration, and autovacuum tuning. Copy prompt Open prompt details Intermediate Single prompt 03 
### VACUUM and Bloat Management 

Manage table and index bloat and configure VACUUM for this PostgreSQL database. Database: {{database}} High-write tables: {{tables}} Current bloat symptoms: {{symptoms}} (slow q... 
Prompt text Manage table and index bloat and configure VACUUM for this PostgreSQL database.

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

Return: bloat measurement queries, autovacuum tuning per table, VACUUM schedule, and pg_repack plan for maintenance-free compaction. Copy prompt Open prompt details 
## Recommended Performance Tuning workflow 
1 
### Connection Pooling with PgBouncer 

Start with a focused prompt in Performance Tuning so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### PostgreSQL Configuration Tuning 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### VACUUM and Bloat Management 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
