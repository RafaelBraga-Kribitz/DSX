# Database Engineer *AI Prompts *

Database Engineer AI prompt library with 18 prompts in 6 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 6 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Database Engineer prompt categories 
6 categories 
### Migration and Upgrades 

AI prompts for migration and upgrade workflows including compatibility planning, phased rollout, rollback strategy, and operational risk control. 
4 prompts Data Migration Pipeline Database Version Upgrade → 
### Schema Design 

AI prompts for schema design including normalization tradeoffs, entity relationships, indexing implications, and analytics-friendly modeling decisions. 
4 prompts Indexing Strategy Multi-Tenancy Patterns → 
### Performance Tuning 

AI prompts for database and query performance tuning, including indexing strategy, execution-plan analysis, and workload-specific optimization. 
3 prompts Connection Pooling with PgBouncer PostgreSQL Configuration Tuning → 
### Query Optimization 

AI prompts for query optimization including execution plan analysis, indexing recommendations, and cost-aware SQL refactoring. 
3 prompts Deadlock and Lock Analysis Query Execution Plan Analysis → 
### Replication and HA 

AI prompts for replication and high-availability database design including failover planning, consistency tradeoffs, and resilience testing. 
2 prompts Backup and Recovery Strategy Replication Setup → 
### Security 

AI prompts for data and database security including access control, secrets handling, threat mitigation, and secure operational practices. 
2 prompts Database Security Hardening Row-Level Security and Data Access Control → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 18 Migration and Upgrades 4 Schema Design 4 Performance Tuning 3 Query Optimization 3 Replication and HA 2 Security 2 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **18 **of 18 prompts 
## Migration and Upgrades 
4 prompt s Migration and Upgrades Intermediate Prompt 01 
### Data Migration Pipeline 
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

Return: batch migration script, dual-write pattern, validation queries, and rollback procedure. Copy prompt View page Show more ↓ Migration and Upgrades Advanced Prompt 02 
### Database Version Upgrade 
Plan a major PostgreSQL version upgrade for this production system.

Current version: {{current_version}}
Target version: {{target_version}}
Database size: {{size}}
RPO: {{rpo}}
Upgrade method: {{method}} (pg_upgrade, logical replication, dump/restore)

1. Upgrade methods comparison:

 pg_upgrade (in-place, fast):
 - Upgrades the data directory in-place (or with hard links for near-instant speed)
 - Downtime: 5-30 minutes for most databases
 - Process: pg_upgrade --old-datadir --new-datadir --old-bindir --new-bindir --link
 - Requires: stop the old cluster, upgrade, start the new cluster
 - Rollback: keep the old data directory until validated (can revert in minutes)

 Logical replication (minimal downtime):
 - Set up logical replication from old version to new version instance
 - Wait for replicas to catch up, then switch over
 - Cutover window: 30-60 seconds (stop app, wait for lag to drain, update connection string)
 - Limitation: logical replication does not replicate DDL or sequences automatically

 Dump and restore (safest, most downtime):
 - pg_dump → transfer → pg_restore on new version
 - Downtime: proportional to database size (hours for large databases)
 - Best for: small databases or when a long maintenance window is acceptable

2. Pre-upgrade checklist:
 ☐ Test on a clone: run the upgrade on a copy of production first
 ☐ Review extension compatibility: all extensions must have versions for the target PostgreSQL version
 ☐ Check pg_upgrade --check: dry run without actually upgrading
 ☐ Verify application compatibility: any deprecated functions or behaviors in the new version?
 ☐ Update statistics: run ANALYZE on the new cluster after pg_upgrade before opening to traffic
 ☐ Rebuild indexes: pg_upgrade preserves indexes but recommend REINDEX for safety

3. Cutover plan:
 T-2h: disable application writes (maintenance mode)
 T-1h: final sync check if using logical replication
 T-0: run pg_upgrade; start new cluster; verify; update connection strings
 T+15m: re-enable application writes; monitor for errors
 T+24h: if stable, remove old cluster and backup files

4. Rollback plan:
 - Keep old cluster stopped but intact for 24 hours post-upgrade
 - Rollback: stop new cluster, restart old cluster, update connection strings

Return: upgrade method recommendation, step-by-step plan, pre-upgrade checklist, cutover procedure, and rollback plan. Copy prompt View page Show more ↓ Migration and Upgrades Advanced Chain 03 
### Full Database Engineering Chain 
Step 1: Schema design - design the normalized relational schema for the domain. Define primary keys, foreign keys, and data types. Create an ERD. Identify tables requiring partitioning based on expected data volume.
Step 2: Indexing strategy - analyze the query workload. Design B-tree, partial, and covering indexes for the top 10 query patterns. Identify unused index candidates. Document the index maintenance plan.
Step 3: Security hardening - configure pg_hba.conf for certificate or SCRAM authentication. Define the role hierarchy. Enable RLS for multi-tenant tables. Configure pgaudit for compliance logging.
Step 4: Performance configuration - tune postgresql.conf for the server specs (shared_buffers, work_mem, random_page_cost). Configure PgBouncer for connection pooling. Set autovacuum parameters for high-write tables.
Step 5: Replication and HA - configure streaming replication. Set up Patroni for automatic failover. Configure WAL archiving for PITR. Define the backup schedule using pgBackRest.
Step 6: Monitoring - deploy pg_stat_statements for slow query identification. Set up pg_stat_replication lag monitoring. Configure autovacuum bloat alerts. Integrate with the organization's observability stack.
Step 7: Migration and change management - define the zero-downtime migration procedure for schema changes. Create a runbook for major version upgrades. Establish the PR review checklist for database changes. Copy prompt View page Show more ↓ Migration and Upgrades Intermediate Prompt 04 
### Zero-Downtime Schema Migration 
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

Return: step-by-step migration plan for the specific change, DDL statements, rollback procedure, and validation steps. Copy prompt View page Show more ↓ 
## Schema Design 
4 prompt s Schema Design Intermediate Prompt 01 
### Indexing Strategy 
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

Return: index recommendations per query pattern, DDL for each index, covering index opportunities, and maintenance schedule. Copy prompt View page Show more ↓ Schema Design Intermediate Prompt 02 
### Multi-Tenancy Patterns 
Design a multi-tenancy data isolation strategy for this SaaS application.

Isolation requirement: {{isolation}} (full isolation / logical isolation / row-level)
Expected tenants: {{tenant_count}}
Tenant size variation: {{size_variation}} (all small / some enterprise / highly variable)
Database: {{database}}

1. Multi-tenancy patterns:

 Pattern A — Separate database per tenant:
 - Maximum isolation: each tenant has their own database instance
 - Pros: complete data isolation, independent backups, custom configurations per tenant
 - Cons: expensive (one DB instance per tenant), complex management at scale
 - Use for: high-compliance tenants (financial, healthcare), large enterprise customers

 Pattern B — Separate schema per tenant:
 - Each tenant gets a PostgreSQL schema within a shared database
 - Each schema has identical table structures
 - search_path = tenant_xyz_schema; routes queries to the right schema
 - Pros: strong logical isolation, easy schema-level backup, easier to customize per tenant
 - Cons: schema proliferation beyond ~1000 schemas becomes slow

 Pattern C — Row-level security (shared tables):
 - All tenants share the same tables; a tenant_id column identifies rows
 - PostgreSQL Row Level Security enforces isolation at the database level
 - Pros: simple schema, scales to millions of tenants, efficient
 - Cons: a bug in the RLS policy could expose cross-tenant data

2. Row-Level Security implementation:
 ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

 CREATE POLICY tenant_isolation ON orders
 USING (tenant_id = current_setting('app.current_tenant_id')::UUID);

 -- Set in the application before every query:
 SET app.current_tenant_id = 'tenant-uuid-here';

3. Hybrid approach:
 - Free tier / SMB: shared tables with RLS (Pattern C)
 - Enterprise / high-compliance: dedicated schema or database (Pattern A or B)
 - Migrate enterprise tenants to dedicated instances on request

4. Index strategy for shared tables:
 - Always include tenant_id as the first column of every index
 - CREATE INDEX ON orders (tenant_id, created_at);
 - Without this, queries for one tenant scan all tenants' data

Return: pattern recommendation, RLS policy DDL, index strategy, and hybrid architecture for mixed tenant tiers. Copy prompt View page Show more ↓ Schema Design Advanced Prompt 03 
### Partitioning Strategy 
Design a table partitioning strategy for this large table.

Table: {{table}} with estimated {{row_count}} rows, growing at {{growth_rate}}
Query patterns: {{query_patterns}} (always filter by date? by region? by tenant?)
Database: {{database}}

1. Partitioning methods:

 Range partitioning (most common for time-series data):
 - Partition by date range: one partition per month or per year
 - Queries filtering by date only scan relevant partitions (partition pruning)
 - CREATE TABLE orders_2024_q1 PARTITION OF orders
 FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');

 List partitioning:
 - Partition by discrete values: country, region, status, tenant_id
 - FOR VALUES IN ('US', 'CA')
 - Use when: queries always filter on a low-cardinality categorical column

 Hash partitioning:
 - Distribute rows evenly across N partitions based on a hash of a key
 - FOR VALUES WITH (MODULUS 8, REMAINDER 0)
 - Use when: no natural range or list key but want to distribute I/O load

2. PostgreSQL declarative partitioning:
 CREATE TABLE orders (
 order_id BIGINT,
 order_date DATE NOT NULL,
 ...
 ) PARTITION BY RANGE (order_date);

 Automating partition creation:
 - pg_partman: automatically creates and maintains time-based partitions
 - Configure: retention period, pre-creation interval, maintenance job

3. Partition pruning:
 - The planner must be able to eliminate partitions from the query plan
 - Partition pruning requires: the filter condition uses the partition key column directly
 - Verify: EXPLAIN shows 'Partitions: 1 (of N)' rather than scanning all partitions

4. Global indexes on partitioned tables:
 - PostgreSQL: no global indexes across all partitions; each partition has its own indexes
 - Unique constraints must include the partition key
 - Workaround for cross-partition uniqueness: application-level enforcement or a separate lookup table

5. Partition maintenance:
 - Detach old partitions for archival: ALTER TABLE orders DETACH PARTITION orders_2020;
 - Archive to cold storage, then DROP TABLE orders_2020;
 - Automate with pg_partman or a scheduled maintenance procedure

Return: partitioning DDL, partition pruning verification, pg_partman configuration, and maintenance/archival plan. Copy prompt View page Show more ↓ Schema Design Beginner Prompt 04 
### Relational Schema Design 
Design a normalized relational schema for this domain.

Domain: {{domain}}
Entities described: {{entities}}
Key relationships: {{relationships}}
Database: {{database}} (PostgreSQL, MySQL, SQL Server, Oracle)

1. Normalization levels:

 1NF (First Normal Form):
 - Atomic values: no repeating groups, no arrays in columns
 - Each column holds a single value
 - Example violation: storing 'tag1,tag2,tag3' in a tags column

 2NF (Second Normal Form):
 - Must be in 1NF
 - No partial dependencies: every non-key column depends on the WHOLE primary key
 - Applies to tables with composite primary keys

 3NF (Third Normal Form):
 - Must be in 2NF
 - No transitive dependencies: non-key columns should not depend on other non-key columns
 - Example violation: storing both zip_code and city in the same table (city depends on zip)

 BCNF (Boyce-Codd Normal Form):
 - Stricter version of 3NF; every determinant must be a candidate key
 - Required for mission-critical schemas

2. Primary key strategy:
 - Surrogate key: auto-incrementing integer or UUID — decouples business logic from identity
 - Natural key: use when the business key is stable and unique (e.g. ISO country code)
 - Composite key: for junction tables (order_id + product_id as PK in order_items)
 - UUID vs SERIAL: UUID is globally unique (good for distributed systems); SERIAL is faster for single-DB

3. Foreign key design:
 - Always create FK constraints: enforces referential integrity at the database level
 - ON DELETE behavior: RESTRICT (default, safest), CASCADE (auto-delete children), SET NULL
 - Index all FK columns: queries joining on FK columns need indexes

4. Column data types:
 - Prefer: TIMESTAMP WITH TIME ZONE (not WITHOUT), NUMERIC for money (not FLOAT), TEXT over VARCHAR(n) in Postgres
 - Avoid: storing dates as VARCHAR, using FLOAT for currency

5. Schema documentation:
 - Add comments to every table and column: COMMENT ON TABLE orders IS '...';
 - Maintain an ERD (Entity Relationship Diagram) in draw.io or dbdiagram.io

Return: normalized schema DDL, primary and foreign key definitions, index recommendations, and ERD description. Copy prompt View page Show more ↓ 
## Performance Tuning 
3 prompt s Performance Tuning Advanced Prompt 01 
### Connection Pooling with PgBouncer 
Configure PgBouncer connection pooling for this PostgreSQL deployment.

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

Return: pgbouncer.ini configuration, pool size calculation, mode recommendation, and monitoring setup. Copy prompt View page Show more ↓ Performance Tuning Intermediate Prompt 02 
### PostgreSQL Configuration Tuning 
Tune PostgreSQL configuration parameters for this server and workload.

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

Return: postgresql.conf settings for the given server spec and workload, PgBouncer configuration, and autovacuum tuning. Copy prompt View page Show more ↓ Performance Tuning Intermediate Prompt 03 
### VACUUM and Bloat Management 
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

Return: bloat measurement queries, autovacuum tuning per table, VACUUM schedule, and pg_repack plan for maintenance-free compaction. Copy prompt View page Show more ↓ 
## Query Optimization 
3 prompt s Query Optimization Advanced Prompt 01 
### Deadlock and Lock Analysis 
Diagnose and resolve lock contention and deadlocks in this database.

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

Return: lock diagnosis queries, deadlock root cause analysis, prevention strategies, and lock timeout configuration. Copy prompt View page Show more ↓ Query Optimization Intermediate Prompt 02 
### Query Execution Plan Analysis 
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

Return: annotated EXPLAIN output, identified bottlenecks, specific fixes with DDL/SQL, and expected improvement. Copy prompt View page Show more ↓ Query Optimization Intermediate Prompt 03 
### Slow Query Analysis 
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

Return: slow query identification queries, pattern diagnosis for each slow query, fix recommendations, and auto_explain configuration. Copy prompt View page Show more ↓ 
## Replication and HA 
2 prompt s Replication and HA Advanced Prompt 01 
### Backup and Recovery Strategy 
Design a backup and recovery strategy for this production database.

Database size: {{size}}
RPO: {{rpo}}
RTO: {{rto}}
Retention requirement: {{retention}} (30 days, 7 years for compliance, etc.)
Database: {{database}}

1. Backup types:

 Full backup:
 - Complete copy of the database
 - Slow to create and restore; self-contained
 - Frequency: weekly or daily depending on RPO

 Incremental backup:
 - Only changes since the last full or incremental backup
 - Fast to create; requires chaining backups for restore
 - pgBackRest and Barman support incremental PostgreSQL backups

 WAL archiving (point-in-time recovery):
 - Archive every WAL segment to S3/GCS/Azure Blob
 - Enables recovery to any point in time within the archive window
 - Combined with a base backup: recover to any second
 - archive_mode = on; archive_command = 'pgbackrest --stanza=main archive-push %p'

2. pgBackRest configuration:
 stanza: production
 repo1-path: /var/lib/pgbackrest
 repo1-retention-full: 4 # keep 4 full backups
 repo1-s3-bucket: company-db-backups

 Schedule:
 - Full backup: weekly (Sunday 02:00)
 - Differential backup: daily (02:00 Mon-Sat)
 - WAL archiving: continuous

3. Recovery time estimate:
 - Full restore: depends on backup size and network bandwidth
 - PITR: restore the base backup + replay WAL up to the target time
 - Test restore time regularly: log the time taken in the DR runbook

4. Backup validation (critical — most organizations skip this):
 - Monthly automated restore test: restore to a staging instance, run integrity checks
 - pg_restore --list: verify backup catalog is intact
 - SELECT COUNT(*) on key tables after restore
 - Log validation results; alert if restore fails

5. Offsite and immutable backups:
 - Store backups in a separate cloud region from the primary database
 - Enable S3 Object Lock (WORM) for compliance retention requirements
 - Encrypt backups at rest and in transit

Return: backup schedule, pgBackRest configuration, PITR setup, restore time estimate, and validation automation plan. Copy prompt View page Show more ↓ Replication and HA Intermediate Prompt 02 
### Replication Setup 
Design a replication and high-availability setup for this PostgreSQL database.

RPO requirement: {{rpo}} (maximum acceptable data loss)
RTO requirement: {{rto}} (maximum acceptable downtime)
Read scaling needed: {{read_scaling}} (yes/no)
Cloud provider: {{cloud}}

1. Replication types:

 Physical (streaming) replication:
 - Copies WAL (Write-Ahead Log) byte-for-byte from primary to standby
 - Standby is an exact replica at the byte level
 - Synchronous mode: primary waits for standby to confirm WAL receipt before committing (RPO = 0)
 - Asynchronous mode: primary does not wait (small data loss risk; better performance)

 Logical replication:
 - Replicates logical changes (INSERT/UPDATE/DELETE) via the publication/subscription model
 - Can replicate specific tables or schemas
 - Allows different PostgreSQL versions between publisher and subscriber
 - Use for: selective replication, zero-downtime migrations, cross-version upgrades

2. Synchronous vs asynchronous:
 synchronous_standby_names = 'ANY 1 (standby1, standby2)'
 - Synchronous: guarantees RPO=0 but adds latency to every write
 - Asynchronous: no write latency penalty; potential for a small amount of data loss
 - Choice: financial / healthcare data → synchronous; acceptable small RPO → asynchronous

3. Automatic failover with Patroni:
 - Patroni: open-source HA solution using etcd/Consul/ZooKeeper for leader election
 - Automatically promotes the most up-to-date standby when the primary fails
 - Provides: REST API for cluster status, automatic primary registration with load balancer
 - Managed alternatives: AWS RDS Multi-AZ, GCP Cloud SQL HA, Azure Flexible Server

4. Read replica routing:
 - Direct read-heavy queries (reporting, analytics) to standby replicas
 - Use PgBouncer or application-level routing to send reads to replicas
 - Caution: replica lag means reads may see slightly stale data

5. Monitoring replication lag:
 SELECT
 client_addr,
 state,
 sent_lsn,
 replay_lsn,
 (sent_lsn - replay_lsn) AS lag_bytes
 FROM pg_stat_replication;
 Alert if lag_bytes > threshold.

Return: replication architecture for the given RPO/RTO, synchronous vs async decision, Patroni configuration, and lag monitoring. Copy prompt View page Show more ↓ 
## Security 
2 prompt s Security Intermediate Prompt 01 
### Database Security Hardening 
Harden this database deployment against common security threats.

Database: {{database}}
Environment: {{environment}} (cloud, on-premise, containerized)
Compliance: {{compliance}} (SOC 2, HIPAA, PCI-DSS, GDPR)

1. Authentication:
 - Disable password authentication over TCP; use certificate-based or IAM authentication
 - PostgreSQL: configure pg_hba.conf to require scram-sha-256 (not md5) for all connections
 - Require TLS for all connections: ssl = on; ssl_cert_file; ssl_key_file
 - Rotate database passwords on a schedule (90 days maximum)

2. Least-privilege role model:
 - Application user: SELECT/INSERT/UPDATE/DELETE on specific schemas only; no DDL
 - Read-only user: SELECT only on production tables (for reporting tools)
 - Migration user: DDL rights only during deployment windows; revoke after
 - DBA user: full access; requires MFA; every action logged

 CREATE ROLE app_user LOGIN PASSWORD '...';
 GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;
 REVOKE ALL ON ALL TABLES IN SCHEMA pg_catalog FROM app_user;

3. Network security:
 - Database not reachable from the public internet: place in a private subnet
 - Firewall rule: only application servers and VPN hosts can reach the database port
 - VPC/network-level isolation: separate database VPC from web tier

4. Encryption:
 - In-transit: TLS required for all connections (no cleartext allowed)
 - At-rest: OS-level encryption (dm-crypt/LUKS, cloud-provider disk encryption)
 - Column-level: for PII columns, consider pgcrypto or application-level encryption
 pgp_sym_encrypt(ssn::text, key) AS encrypted_ssn

5. Audit logging:
 - pgaudit extension: logs all DDL and DML at the statement level
 - log_statement = 'ddl': log all DDL even without pgaudit
 - Ship logs to SIEM (Splunk, Elastic) for anomaly detection
 - Alert on: login failures, privilege escalation, bulk SELECT on sensitive tables

6. SQL injection prevention:
 - Always use parameterized queries in the application — never string interpolation
 - Row-level security (RLS): enforce multi-tenant data isolation at the database level

Return: pg_hba.conf config, role hierarchy DDL, network security rules, encryption approach, and audit log configuration. Copy prompt View page Show more ↓ Security Advanced Prompt 02 
### Row-Level Security and Data Access Control 
Implement row-level security (RLS) and fine-grained data access control for this multi-tenant or sensitive data use case.

Use case: {{use_case}} (multi-tenant SaaS, per-department data, financial data with role-based access)
Database: {{database}}
Roles needed: {{roles}}

1. Enable and create RLS policies:
 ALTER TABLE orders ENABLE ROW LEVEL SECURITY;
 ALTER TABLE orders FORCE ROW LEVEL SECURITY; -- applies to table owners too

 Tenant isolation policy:
 CREATE POLICY tenant_isolation ON orders
 FOR ALL
 TO app_user
 USING (tenant_id = current_setting('app.current_tenant')::UUID)
 WITH CHECK (tenant_id = current_setting('app.current_tenant')::UUID);

 USING: controls SELECT/UPDATE/DELETE visibility
 WITH CHECK: controls INSERT/UPDATE values (prevents writing to wrong tenant)

2. Role-based policies:
 -- Managers can see all orders; staff can only see their own
 CREATE POLICY manager_access ON orders
 FOR SELECT TO manager_role
 USING (TRUE);

 CREATE POLICY staff_access ON orders
 FOR SELECT TO staff_role
 USING (assigned_rep_id = current_user);

3. Sensitive column masking (alternative: column privileges):
 REVOKE SELECT ON employees FROM analyst_role;
 CREATE VIEW employees_masked AS
 SELECT employee_id, name, department,
 LEFT(salary::text, 2) || '***' AS salary_masked
 FROM employees;
 GRANT SELECT ON employees_masked TO analyst_role;

4. Audit logging with RLS:
 -- Log when RLS blocks a query (for compliance)
 CREATE EXTENSION IF NOT EXISTS pgaudit;
 SET pgaudit.log = 'read,write';

5. Performance impact:
 - RLS adds a predicate to every query (effectively a WHERE clause)
 - The predicate must use indexed columns to avoid full table scans
 - Always: CREATE INDEX ON orders (tenant_id) before enabling RLS
 - Test: verify EXPLAIN shows Index Scan with the RLS predicate applied

Return: RLS policy DDL for each role and use case, column masking approach, index requirements, and performance validation queries. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
- Terms of Service 
- Privacy Policy 
- AI Policy 
- Licenses 
### AI Data Analysis Examples 

- LLM Benchmark on AI Data Analysis 
- Air Passengers Forecast 
- Iris Classification 
- Customer Churn Prediction 
- Energy Consumption Forecast 
### Resources 

- Example Python notebooks 
- Fix ModuleNotFoundError 
- Glossary 
- Brand 
- Answers 
- ML Algorithm Comparison 
- Research 
- Solutions 
### Products 

- MLJAR Studio 
- MLJAR AutoML 
- AI Data Analyst 
- AutoLab Experiments 
- Mercury 
### Tutorials 

- AutoML in Python: Beginner Tutorial with House Prices 
### Open Source 

- MLJAR AutoML 
- Mercury 
- More ... 
### AI Prompts 

- Prompts for Data Professionals 
- Data Analyst prompts 
- Business Analyst prompts 
- Data Scientist prompts 
- ML Engineer prompts 
- Data Engineer prompts 
- MLOps prompts 
### Compare 

- MLJAR Studio vs Julius 
- MLJAR Studio vs H2O 
- MLJAR Studio vs DataRobot 
- MLJAR Studio vs Jupyter 
- MLJAR Studio vs ChatGPT 
- MLJAR Studio vs Cursor 
### Company 

- Contact us 
- Services 
- About us 
- Blog Made by MLJAR. All rights reserved. Created in 🇵🇱 We ❤ you! 
We collect traffic information to improve the site. 

Data is collected in a privacy-friendly way (IP anonymization, no ads, no cross-site tracking). 
Analytics are only enabled if you accept. 
Read Privacy Policy Reject Accept
