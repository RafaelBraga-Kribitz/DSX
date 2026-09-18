# Data Warehouse Patterns *AI Prompts *

8 Data Engineer prompts in Data Warehouse Patterns. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 6 single prompts · 1 chain · 1 template. 

## AI prompts in Data Warehouse Patterns 
8 prompts Advanced Single prompt 01 
### Data Vault Design 

This prompt designs a Data Vault 2.0 model for integrating multiple source systems while preserving history and supporting scalable loading. It is useful when the integration problem is complex, source systems are heterogeneous, and auditability matters. The output should clearly separate Hubs, Links, Satellites, and optional Business Vault structures. 
Prompt text Design a Data Vault 2.0 model for integrating {{num_sources}} source systems on the entity: {{core_entity}}.

1. Hub table:
 - One Hub per core business entity (Customer, Product, Order, etc.)
 - Columns: hash_key (PK, SHA-256 of business key), business_key, load_date, record_source
 - No descriptive attributes — Hubs contain only the business key
 - Business key: the natural identifier used by the business (customer_id, order_number)
 - Hash key: deterministic hash of the business key — enables parallel loading without sequences

2. Satellite tables:
 - One or more Satellites per Hub, each containing descriptive attributes from one source
 - Columns: hash_key (FK to Hub), load_date, load_end_date (NULL = current), record_source, + descriptive columns
 - Split Satellites by: rate of change (fast-changing vs slow-changing attributes separate), source system, sensitivity level
 - load_end_date pattern: NULL for current record, populated when a new record supersedes it

3. Link tables:
 - Represent many-to-many relationships between Hubs
 - Columns: link_hash_key (PK), hash_key_hub_a (FK), hash_key_hub_b (FK), load_date, record_source
 - Never delete from Links — relationships are historical facts

4. Business Vault:
 - Computed Satellites: derived business rules applied on top of raw Vault
 - Bridge tables: pre-joined structures for performance
 - Point-in-time (PIT) tables: snapshot of active satellite records at each date — avoids complex timestamp joins in queries

5. Loading patterns:
 - Hubs: INSERT new business keys only (never update)
 - Satellites: INSERT new records; close previous record by setting load_end_date
 - Links: INSERT new relationships only
 - All loads are insert-only — no updates, no deletes

Return: Hub, Satellite, and Link DDLs, loading SQL for each component, and PIT table design. Copy prompt Open prompt details Intermediate Single prompt 02 
### Fact Table Loading Pattern 

This prompt designs a safe and repeatable fact-loading pattern for analytical tables. It focuses on surrogate key resolution, late-arriving dimensions, partition-based loading, audit metadata, and pre/post-load validation. It is ideal for teams that want disciplined warehouse loading patterns rather than one-off ETL code. 
Prompt text Implement a robust fact table loading pattern for {{fact_table}} using a {{loading_strategy}} approach.

1. Pre-load validation:
 - Check source row count vs expected range (alert if < 80% or > 120% of yesterday's count)
 - Verify all required foreign keys exist in their dimension tables (referential integrity check)
 - Check for duplicate natural keys in the incoming batch
 - Validate numeric measure ranges (no negative revenue, no impossible quantities)

2. Surrogate key lookup:
 - Never store natural keys in the fact table — always look up the surrogate key from the dimension
 - For each foreign key: JOIN to dimension on natural key WHERE is_current = TRUE
 - For late-arriving dimensions: look up the surrogate key valid at the event time (point-in-time lookup)
 - Late-arriving facts: if the dimension record did not exist at event time, use a 'unknown' placeholder record (surrogate_key = -1)

3. Incremental load to fact table:
 - Partition by date and load one partition at a time
 - Use INSERT OVERWRITE for the current partition (idempotent, safe to re-run)
 - Never UPDATE rows in a fact table — append or overwrite partitions only

4. Post-load validation:
 - Row count reconciliation: source count = fact table insert count
 - Measure totals reconciliation: SUM(revenue) in source = SUM(revenue) in fact for the loaded date
 - No NULL surrogate keys in the output (all dimension lookups resolved)

5. Audit columns:
 - Add to every fact table: load_timestamp, pipeline_run_id, source_system

Return: pre-load validation queries, surrogate key lookup logic, incremental load SQL, and post-load reconciliation queries. Copy prompt Open prompt details Intermediate Single prompt 03 
### Medallion Architecture Design 

This prompt defines Bronze, Silver, and Gold layers in a way that clarifies what belongs in each layer and what quality expectations apply. It is useful when building a lakehouse or modern warehouse platform that needs both raw replayability and curated business-ready outputs. The response should emphasize responsibilities, retention, access, and lineage across layers. 
Prompt text Design a medallion (Bronze / Silver / Gold) architecture for this data platform.

Data sources: {{source_systems}}
Consumers: {{downstream_consumers}}
Platform: {{platform}}

1. Bronze layer (raw ingest):
 - Store data exactly as received from the source — no transformation, no business logic
 - Schema: source columns + metadata columns (ingested_at, source_file, pipeline_run_id)
 - File format: Parquet or Delta (preserve original data types)
 - Partitioning: by ingestion date (not event date — you want to find what was loaded when)
 - Retention: keep all data indefinitely — Bronze is your audit trail and replay source
 - Access: restricted to data engineers only

2. Silver layer (cleansed, conformed):
 - Clean and standardize: fix types, normalize casing, handle nulls, apply business rules
 - Deduplicate: one row per natural key per valid state
 - Conform: common naming conventions, standard date formats, unified entity IDs across sources
 - Add: valid_from / valid_to for SCD2 entities, data quality score per row
 - Partitioning: by event date (not ingestion date) for time-series data
 - Access: data engineers and data scientists

3. Gold layer (business-ready):
 - Aggregated, joined, and modeled for specific use cases: star schemas, wide flat tables, aggregated metrics
 - Optimized for query performance: partitioned, clustered, materialized
 - Documented: every table and column has a business description
 - Access: analysts, BI tools, applications

4. Cross-layer governance:
 - Lineage: track which Gold tables derive from which Silver, which derives from which Bronze
 - SLA: Bronze = 30 min from source, Silver = 1 hour, Gold = 2 hours
 - Testing: Bronze (schema only), Silver (schema + row counts + nulls), Gold (schema + business rules + reconciliation)

Return: layer definitions, DDL templates for each layer, lineage tracking approach, and SLA commitments. Copy prompt Open prompt details Intermediate Single prompt 04 
### Partitioning Strategy 

This prompt helps choose partitioning and clustering based on real query behavior and platform-specific capabilities. It is aimed at improving scan efficiency, cost, and maintainability rather than blindly partitioning by date. The answer should connect the physical design to workload patterns and platform constraints. 
Prompt text Design the optimal partitioning and clustering strategy for this data warehouse table.

Table: {{table_name}}
Approximate size: {{table_size}}
Query patterns: {{query_patterns}}
Warehouse platform: {{platform}} (BigQuery / Snowflake / Redshift / Databricks / Trino)

1. Partitioning:
 - Partition by the column most frequently used in WHERE filters
 - For time-series data: partition by date (daily partitions for tables < 1TB, monthly for larger)
 - For non-time data: partition by a low-cardinality column (region, status, product_category)
 - Avoid over-partitioning: partitions should be > 100MB each to avoid small-file problems
 - Avoid under-partitioning: each partition should be a meaningful data subset to skip files effectively

2. Clustering / sort keys:
 - After partitioning, cluster by the next most common filter column (e.g. customer_id, product_id)
 - Cluster by columns used in JOIN conditions to collocate related rows
 - For Snowflake: choose cluster keys with high cardinality and low correlation with insert order
 - For BigQuery: cluster up to 4 columns in order of filter frequency
 - For Redshift: SORTKEY on the main time column, DISTKEY on the most common join key

3. Partition pruning validation:
 - Write a test query using EXPLAIN to confirm partition pruning is occurring
 - Alert if a query scans > {{max_scan_ratio}}% of partitions (indicates missing partition filter)

4. Maintenance:
 - For Delta/Iceberg: OPTIMIZE (compaction) and VACUUM (remove deleted files) on a schedule
 - For Redshift: VACUUM and ANALYZE after large loads
 - Monitor partition statistics: flag partitions with unusually high or low row counts

Return: partitioning and clustering DDL, partition pruning test query, and maintenance schedule. Copy prompt Open prompt details Advanced Single prompt 05 
### Query Performance Tuning 

This prompt tunes a slow warehouse query methodically by analyzing the execution plan and then rewriting the most expensive parts. It is helpful when teams need to bring query latency down while also reducing scanned data and compute cost. The answer should prioritize changes with the biggest likely payoff first. 
Prompt text Tune this slow data warehouse query for performance.

Query: {{slow_query}}
Current runtime: {{current_runtime}}
Target runtime: {{target_runtime}}
Platform: {{platform}}

Work through these optimizations in order:

1. Execution plan analysis:
 - Run EXPLAIN ANALYZE (or platform equivalent)
 - Identify the most expensive operations: full table scans, hash joins on large tables, sorts on large datasets
 - Check estimated vs actual row counts — large divergence indicates stale statistics

2. Filter pushdown:
 - Ensure WHERE clause filters on partitioned/clustered columns appear as early as possible
 - Check if filters are being applied before or after a JOIN — move them before the JOIN
 - Replace HAVING with WHERE where possible (filter before aggregation)

3. Join optimization:
 - Order JOINs from smallest to largest result set
 - Use broadcast/replicate hint for small dimension tables
 - Check for accidental cartesian products (missing JOIN conditions)
 - Replace correlated subqueries with JOINs or window functions

4. Aggregation optimization:
 - Pre-aggregate before joining to reduce row count going into the join
 - Use approximate aggregations (APPROX_COUNT_DISTINCT) where exact precision is not required
 - Push GROUP BY to a subquery before the outer SELECT

5. Materialization:
 - If this query runs frequently: materialize it as a table and schedule refresh
 - Create a summary table at the right grain to avoid full re-aggregation each time

6. Statistics:
 - Run ANALYZE TABLE to refresh statistics if the query plan looks wrong
 - Check column statistics: histograms for skewed columns, NDV for join columns

Return: annotated execution plan, specific rewrites for each optimization applied, and before/after runtime comparison. Copy prompt Open prompt details Beginner Template 06 
### Slowly Changing Dimension 

This prompt builds a Type 2 Slowly Changing Dimension pattern for attributes that require full history. It is useful when descriptive records such as customers, products, or account metadata change over time and reporting must reflect both current and historical truth. The answer should separate tracked and non-tracked changes clearly. 
Prompt text Implement a Type 2 Slowly Changing Dimension (SCD2) for the table {{dim_table}} in {{database_type}}.

Natural key: {{natural_key}}
Tracked attributes (trigger new version): {{tracked_columns}}
Non-tracked attributes (overwrite in place): {{non_tracked_columns}}

1. Table design:
 - Add columns: surrogate_key (BIGINT IDENTITY), valid_from (DATE), valid_to (DATE), is_current (BOOLEAN)
 - valid_to for current rows = '9999-12-31' (sentinel value)
 - is_current = TRUE for current rows (redundant but improves query performance)

2. Initial load: INSERT all rows with valid_from = first_seen_date, valid_to = '9999-12-31', is_current = TRUE

3. Incremental merge logic:
 For each incoming row:
 a. NEW RECORD (natural key not in dim): INSERT with valid_from = today, valid_to = '9999-12-31', is_current = TRUE
 b. CHANGED RECORD (tracked columns differ from current version):
 - UPDATE existing current row: valid_to = today - 1, is_current = FALSE
 - INSERT new row: valid_from = today, valid_to = '9999-12-31', is_current = TRUE
 c. UNCHANGED RECORD: no action
 d. DELETED RECORD (exists in dim but not in source): optionally set is_current = FALSE

4. Point-in-time query:
 SELECT * FROM {{dim_table}} WHERE {{natural_key}} = 'X' AND valid_from <= '{{as_of_date}}' AND valid_to > '{{as_of_date}}'

5. Current records query:
 SELECT * FROM {{dim_table}} WHERE is_current = TRUE
 (Always faster than the date range query — index on is_current)

6. Non-tracked attribute updates: UPDATE current row in-place, no new version needed

Return: CREATE TABLE DDL, MERGE statement, point-in-time query, and current records query. Copy prompt Open prompt details Beginner Single prompt 07 
### Star Schema Design 

This prompt designs a dimensional model centered on a business process and the questions analysts need to answer. It helps define grain, measures, dimensions, hierarchies, and surrogate keys in a way that supports performant analytics. The output should be practical enough to guide implementation, not just conceptual modeling. 
Prompt text Design a star schema for this business process: {{business_process}}

Source data: {{source_tables}}
Key business questions to answer: {{business_questions}}

1. Fact table design:
 - Identify the grain: what does one row represent? (e.g. one order line, one daily session, one claim)
 - State the grain explicitly — this is the most important design decision
 - Numeric measures: what is being measured? (revenue, quantity, duration, count)
 - Additive vs semi-additive vs non-additive measures:
 - Additive: sum across all dimensions (revenue, quantity)
 - Semi-additive: can sum across some dimensions but not time (account balance)
 - Non-additive: cannot sum at all (ratios, percentages — store numerator and denominator instead)
 - Foreign keys: one surrogate key per dimension
 - Degenerate dimensions: order_number, invoice_number (store in fact, no separate dim)

2. Dimension tables:
 - For each dimension: list the descriptive attributes
 - Surrogate key (integer) as primary key — never use the source system natural key as PK
 - Include the source natural key as an attribute for traceability
 - Slowly changing dimension type per attribute: Type 1 (overwrite), Type 2 (version), Type 3 (keep prior)

3. Dimension hierarchies:
 - Identify rollup hierarchies within each dimension (product → category → department)
 - Flatten hierarchy into the dimension table (denormalized) for query performance

4. Date dimension:
 - Always include a date dimension — never join on raw date columns
 - Generate one row per day for a 10-year range minimum
 - Include: date_key, full_date, year, quarter, month, week, day_of_week, is_weekend, is_holiday, fiscal_period

Return: fact table DDL, dimension table DDLs, date dimension generation SQL, and ER diagram (text). Copy prompt Open prompt details Advanced Chain 08 
### Warehouse Design Chain 

This prompt walks through complete warehouse design, from business questions and source profiling to physical design, loading, testing, and documentation. It is meant for end-to-end modeling efforts where tables, pipelines, and consumers must align. The output should feel like a warehouse design blueprint rather than a disconnected set of notes. 
Prompt text Step 1: Requirements — identify the business processes to model, the grain of each fact table, the key business questions to answer, and the consumers (BI tools, DS teams, apps).
Step 2: Source analysis — profile each source table: row counts, key columns, update patterns, data quality issues, and join relationships. Identify integration challenges (different customer IDs across systems).
Step 3: Dimensional model design — design the star schema(s): fact tables with grain and measures, dimension tables with attributes and SCD type per column. Draw the ER diagram.
Step 4: Physical design — choose partitioning, clustering, file format, and materialization strategy for each table. Estimate storage size and query cost at expected query volume.
Step 5: Loading design — design the loading pattern for each table: full load vs incremental vs SCD2 merge. Write the key SQL statements.
Step 6: Testing plan — define data quality tests for each table: row count checks, uniqueness, not-null, referential integrity, and business rule validation.
Step 7: Document the warehouse design: data model diagram, table catalog (name, description, grain, owner), loading schedule, SLA, and known limitations. Copy prompt Open prompt details 
## Recommended Data Warehouse Patterns workflow 
1 
### Data Vault Design 

Start with a focused prompt in Data Warehouse Patterns so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Fact Table Loading Pattern 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Medallion Architecture Design 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Partitioning Strategy 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
