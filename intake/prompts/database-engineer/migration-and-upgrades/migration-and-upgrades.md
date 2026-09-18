# Migration and Upgrades *AI Prompts *

4 Database Engineer prompts in Migration and Upgrades. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts · 1 chain. 

## AI prompts in Migration and Upgrades 
4 prompts Intermediate Single prompt 01 
### Data Migration Pipeline 

Design a safe, reversible data migration pipeline for this schema change or data movement. Migration: {{migration_description}} (e.g. split a table, merge schemas, move to new d... 
Prompt text Design a safe, reversible data migration pipeline for this schema change or data movement.

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

Return: batch migration script, dual-write pattern, validation queries, and rollback procedure. Copy prompt Open prompt details Advanced Single prompt 02 
### Database Version Upgrade 

Plan a major PostgreSQL version upgrade for this production system. Current version: {{current_version}} Target version: {{target_version}} Database size: {{size}} RPO: {{rpo}}... 
Prompt text Plan a major PostgreSQL version upgrade for this production system.

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

Return: upgrade method recommendation, step-by-step plan, pre-upgrade checklist, cutover procedure, and rollback plan. Copy prompt Open prompt details Advanced Chain 03 
### Full Database Engineering Chain 

Step 1: Schema design - design the normalized relational schema for the domain. Define primary keys, foreign keys, and data types. Create an ERD. Identify tables requiring parti... 
Prompt text Step 1: Schema design - design the normalized relational schema for the domain. Define primary keys, foreign keys, and data types. Create an ERD. Identify tables requiring partitioning based on expected data volume.
Step 2: Indexing strategy - analyze the query workload. Design B-tree, partial, and covering indexes for the top 10 query patterns. Identify unused index candidates. Document the index maintenance plan.
Step 3: Security hardening - configure pg_hba.conf for certificate or SCRAM authentication. Define the role hierarchy. Enable RLS for multi-tenant tables. Configure pgaudit for compliance logging.
Step 4: Performance configuration - tune postgresql.conf for the server specs (shared_buffers, work_mem, random_page_cost). Configure PgBouncer for connection pooling. Set autovacuum parameters for high-write tables.
Step 5: Replication and HA - configure streaming replication. Set up Patroni for automatic failover. Configure WAL archiving for PITR. Define the backup schedule using pgBackRest.
Step 6: Monitoring - deploy pg_stat_statements for slow query identification. Set up pg_stat_replication lag monitoring. Configure autovacuum bloat alerts. Integrate with the organization's observability stack.
Step 7: Migration and change management - define the zero-downtime migration procedure for schema changes. Create a runbook for major version upgrades. Establish the PR review checklist for database changes. Copy prompt Open prompt details Intermediate Single prompt 04 
### Zero-Downtime Schema Migration 

Design a zero-downtime schema migration strategy for this production database. Change type: {{change}} (add column, rename column, change type, add index, split table) Table siz... 
Prompt text Design a zero-downtime schema migration strategy for this production database.

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

Return: step-by-step migration plan for the specific change, DDL statements, rollback procedure, and validation steps. Copy prompt Open prompt details 
## Recommended Migration and Upgrades workflow 
1 
### Data Migration Pipeline 

Start with a focused prompt in Migration and Upgrades so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Database Version Upgrade 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Full Database Engineering Chain 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Zero-Downtime Schema Migration 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
