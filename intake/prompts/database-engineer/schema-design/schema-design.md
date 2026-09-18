# Schema Design *AI Prompts *

4 Database Engineer prompts in Schema Design. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 4 single prompts. 

## AI prompts in Schema Design 
4 prompts Intermediate Single prompt 01 
### Indexing Strategy 

Design an indexing strategy for this table and query workload. Table: {{table_name}} with {{row_count}} rows Query patterns: {{query_patterns}} (filter columns, join columns, so... 
Prompt text Design an indexing strategy for this table and query workload.

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

Return: index recommendations per query pattern, DDL for each index, covering index opportunities, and maintenance schedule. Copy prompt Open prompt details Intermediate Single prompt 02 
### Multi-Tenancy Patterns 

Design a multi-tenancy data isolation strategy for this SaaS application. Isolation requirement: {{isolation}} (full isolation / logical isolation / row-level) Expected tenants:... 
Prompt text Design a multi-tenancy data isolation strategy for this SaaS application.

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

Return: pattern recommendation, RLS policy DDL, index strategy, and hybrid architecture for mixed tenant tiers. Copy prompt Open prompt details Advanced Single prompt 03 
### Partitioning Strategy 

Design a table partitioning strategy for this large table. Table: {{table}} with estimated {{row_count}} rows, growing at {{growth_rate}} Query patterns: {{query_patterns}} (alw... 
Prompt text Design a table partitioning strategy for this large table.

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

Return: partitioning DDL, partition pruning verification, pg_partman configuration, and maintenance/archival plan. Copy prompt Open prompt details Beginner Single prompt 04 
### Relational Schema Design 

Design a normalized relational schema for this domain. Domain: {{domain}} Entities described: {{entities}} Key relationships: {{relationships}} Database: {{database}} (PostgreSQ... 
Prompt text Design a normalized relational schema for this domain.

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

Return: normalized schema DDL, primary and foreign key definitions, index recommendations, and ERD description. Copy prompt Open prompt details 
## Recommended Schema Design workflow 
1 
### Indexing Strategy 

Start with a focused prompt in Schema Design so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Multi-Tenancy Patterns 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Partitioning Strategy 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Relational Schema Design 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
