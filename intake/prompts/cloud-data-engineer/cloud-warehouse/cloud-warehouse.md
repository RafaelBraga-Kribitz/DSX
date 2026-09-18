# Cloud Warehouse *AI Prompts *

3 Cloud Data Engineer prompts in Cloud Warehouse. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts. 

## AI prompts in Cloud Warehouse 
3 prompts Intermediate Single prompt 01 
### BigQuery Optimization 

Optimize BigQuery performance and cost for this workload. Workload: {{workload}} Current monthly cost: {{current_cost}} Query patterns: {{query_patterns}} Data volume: {{volume}... 
Prompt text Optimize BigQuery performance and cost for this workload.

Workload: {{workload}}
Current monthly cost: {{current_cost}}
Query patterns: {{query_patterns}}
Data volume: {{volume}}

1. BigQuery cost model:
 - On-demand: $5 per TB of data scanned (minimize bytes read)
 - Flat-rate / capacity pricing: reserved slot commitments for predictable workloads
 - Storage: $0.02/GB for active, $0.01/GB for long-term (not modified for 90 days)

2. Reducing bytes scanned:
 - Partition tables by date:
 PARTITION BY DATE(event_timestamp)
 Queries with WHERE event_date BETWEEN ... AND ... only scan relevant partitions

 - Cluster by frequently filtered columns:
 CLUSTER BY user_id, product_category
 Improves scan efficiency for queries filtering on these columns

 - Use INFORMATION_SCHEMA to find expensive queries:
 SELECT total_bytes_billed/POW(1024,3) AS gb_billed, query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 ORDER BY total_bytes_billed DESC LIMIT 20;

3. Schema design for BigQuery:
 - Prefer denormalized (nested and repeated) schemas over normalized schemas
 - Use STRUCT and ARRAY columns to store related data in one row
 - Avoids expensive cross-shard joins on normalized data
 - Nested repeated fields are stored in columnar format → efficient for column scans

4. Materialized views:
 CREATE MATERIALIZED VIEW daily_revenue AS
 SELECT DATE(order_date) AS d, SUM(amount) AS revenue
 FROM orders GROUP BY 1;
 - BigQuery automatically refreshes within 5 minutes of base table changes
 - Queries on the base table can transparently use the materialized view

5. Slot utilization:
 - Monitor: INFORMATION_SCHEMA.JOBS_TIMELINE for slot hours
 - Identify: queries with high slot_ms = compute-intensive (add partitioning)
 - BI Engine: in-memory acceleration for Looker and Looker Studio

Return: partitioning and clustering DDL, cost investigation queries, materialized view setup, and schema design recommendation. Copy prompt Open prompt details Advanced Single prompt 02 
### Redshift Architecture and Tuning 

Design and optimize a Redshift deployment for this workload. Workload: {{workload}} Data volume: {{volume}} Query patterns: {{query_patterns}} Cluster type: {{cluster_type}} (pr... 
Prompt text Design and optimize a Redshift deployment for this workload.

Workload: {{workload}}
Data volume: {{volume}}
Query patterns: {{query_patterns}}
Cluster type: {{cluster_type}} (provisioned vs Serverless)

1. Redshift Serverless vs Provisioned:
 Serverless: auto-scales, pay per compute-second, no cluster management
 - Use for: unpredictable workloads, intermittent usage, cost optimization
 Provisioned: fixed cluster, predictable performance and cost
 - Use for: consistent heavy workloads, >$500/month sustained use

2. Table design:
 Distribution styles:
 - DISTSTYLE KEY (column): rows with the same key on the same slice — use for large JOIN tables
 - DISTSTYLE EVEN: round-robin — use for large tables with no clear join key
 - DISTSTYLE ALL: copy to every slice — use for small dimension tables (< 1M rows)

 Sort keys:
 - COMPOUND SORTKEY (col1, col2): range scan optimization on ordered columns (date)
 - INTERLEAVED SORTKEY: equal weight to all sort key columns — use for multiple filter patterns

3. COPY command for loading:
 COPY orders FROM 's3://bucket/data/orders/'
 IAM_ROLE 'arn:aws:iam::123456789:role/RedshiftRole'
 FORMAT AS PARQUET;
 - Use PARQUET (fastest) or CSV with GZIP compression
 - Parallel loading: split files into 1× number of slices for maximum parallelism

4. Vacuuming:
 VACUUM orders TO 100 PERCENT BOOST;
 -- Reclaims space from deleted rows and re-sorts unsorted rows
 -- Schedule weekly; automatic vacuum may not keep up with high-write tables

5. WLM (Workload Management):
 - Define query queues by user group or query group
 - Short query acceleration (SQA): auto-routes short queries to a fast lane
 - Concurrency scaling: auto-adds read capacity during peak periods

Return: distribution and sort key design, COPY command, vacuum schedule, and WLM configuration. Copy prompt Open prompt details Intermediate Single prompt 03 
### Snowflake Architecture and Best Practices 

Design and optimize a Snowflake deployment for this organization. Workload: {{workload}} (ELT, mixed, analytics, ML feature store) Team: {{team}} (data engineers, analysts, data... 
Prompt text Design and optimize a Snowflake deployment for this organization.

Workload: {{workload}} (ELT, mixed, analytics, ML feature store)
Team: {{team}} (data engineers, analysts, data scientists)
Data volume: {{volume}}
Cost target: {{cost_target}}

1. Snowflake architecture concepts:
 - Separation of storage and compute: storage billed per TB, compute per second
 - Virtual warehouses: compute clusters that scale independently
 - Databases → Schemas → Tables: same as traditional databases
 - Zero-copy cloning: instant clone of any table/schema/database for testing or branching

2. Virtual warehouse strategy:
 - One warehouse per workload type (not per team):
 LOADING_WH (X-Large): bulk data loading, ELT
 ANALYTICS_WH (Small-Medium): analyst queries
 TRANSFORM_WH (Medium): dbt runs
 ML_WH (Large): data science ad-hoc
 - Auto-suspend: 60 seconds (analysts), 300 seconds (loading)
 - Auto-resume: always enabled
 - Multi-cluster warehouses: for concurrent analyst workloads

3. Cost optimization:
 - Monitor: QUERY_HISTORY view for expensive queries
 - Use result cache: same query within 24h returns the cached result (free)
 - Use CLUSTERING KEYS on large tables filtered by a column:
 ALTER TABLE orders CLUSTER BY (TO_DATE(order_date));
 - Use SEARCH OPTIMIZATION for high-cardinality point lookups
 - Tag warehouses with resource monitors to cap monthly spend

4. Snowflake roles hierarchy:
 ACCOUNTADMIN → SYSADMIN → custom roles
 - SYSADMIN: creates databases, warehouses
 - Custom roles: ANALYST_ROLE (SELECT), ENGINEER_ROLE (DML + DDL on own schema), LOADER_ROLE (COPY INTO)
 - Follow least-privilege; never use ACCOUNTADMIN for day-to-day operations

5. Data sharing:
 - Share data with other Snowflake accounts without copying (live read access)
 - CREATE SHARE; GRANT SELECT ON TABLE TO SHARE; ADD ACCOUNT TO SHARE
 - Use for: sharing data products with customers, cross-department data sharing

Return: warehouse configuration, role hierarchy DDL, clustering key recommendations, cost monitoring queries, and data sharing setup. Copy prompt Open prompt details 
## Recommended Cloud Warehouse workflow 
1 
### BigQuery Optimization 

Start with a focused prompt in Cloud Warehouse so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Redshift Architecture and Tuning 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Snowflake Architecture and Best Practices 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
