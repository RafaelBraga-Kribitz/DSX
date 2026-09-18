# Data Engineer *AI Prompts *

Data Engineer AI prompt library with 35 prompts in 5 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 5 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Data Engineer prompt categories 
5 categories 
### Pipeline Design 

AI prompts for data pipeline design, ETL and ELT processes, orchestration, ingestion, and end-to-end data workflows. 
10 prompts Backfill Strategy DAG Design for Airflow → 
### Data Quality 

AI prompts for data quality checks, validation rules, audits, constraints, and monitoring data reliability in production systems. 
8 prompts Data Lineage Tracking Data Quality Framework Chain → 
### Data Warehouse Patterns 

AI prompts for data warehouse design, dimensional modeling, data marts, slowly changing dimensions, and analytical architecture. 
8 prompts Data Vault Design Fact Table Loading Pattern → 
### Data Contracts 

AI prompts for data contracts, schema validation, data expectations, interface definitions, and upstream-downstream reliability. 
5 prompts Breaking Change Migration Contract Validation Pipeline → 
### Infrastructure and Platform 

AI prompts for data and ML infrastructure, platform architecture, orchestration, scalability, and system reliability design. 
4 prompts Compute Sizing Guide Data Lake File Format Selection → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 35 Pipeline Design 10 Data Quality 8 Data Warehouse Patterns 8 Data Contracts 5 Infrastructure and Platform 4 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **35 **of 35 prompts 
## Pipeline Design 
10 prompt s Pipeline Design Advanced Prompt 01 
### Backfill Strategy 
Design a safe, efficient backfill strategy for re-processing historical data in this pipeline.

Pipeline: {{pipeline_description}}
Data range to backfill: {{date_range}}
Estimated data volume: {{volume}}
Downstream dependencies: {{downstream_tables}}

1. Backfill isolation:
 - Never write backfill output to the production table directly during processing
 - Write to a staging table or partition-isolated location first
 - Swap into production atomically after validation

2. Partitioned backfill approach:
 - Process one date partition at a time to limit blast radius
 - Use a date loop: for each date in the range, submit an independent job
 - Parallelism: how many partitions can safely run in parallel without overloading the source system or cluster?
 - Checkpoint completed partitions: re-running the backfill skips already-completed dates

3. Source system protection:
 - Throttle extraction queries to avoid overwhelming the source (use LIMIT/offset pagination or time-boxed micro-batches)
 - Schedule backfill during low-traffic hours if source is OLTP
 - Use read replicas if available

4. Downstream impact management:
 - Notify downstream consumers before starting the backfill
 - If downstream tables are materialized from this table, suspend their refresh until backfill is complete
 - After backfill: re-run downstream tables in dependency order

5. Validation before cutover:
 - Row count: does the backfilled output match expected counts?
 - Key uniqueness: no duplicate primary keys in the output
 - Metric spot check: compare aggregated metrics for a sample of dates to the source system

6. Rollback plan:
 - If validation fails: what is the procedure to restore the previous state?

Return: backfill execution script, validation checks, downstream notification template, and rollback procedure. Copy prompt View page Show more ↓ Pipeline Design Beginner Prompt 02 
### DAG Design for Airflow 
Design and implement an Airflow DAG for this pipeline.

Pipeline requirements: {{pipeline_requirements}}
Schedule: {{schedule}}
Dependencies: {{upstream_dependencies}}

1. DAG structure best practices:
 - Use @dag decorator with explicit schedule, catchup=False, and max_active_runs=1
 - Set meaningful dag_id, description, and tags
 - Define default_args with retries=3, retry_delay=timedelta(minutes=5), retry_exponential_backoff=True
 - Set execution_timeout per task to prevent hung tasks from blocking slots

2. Task design:
 - Keep tasks small and single-responsibility (one logical operation per task)
 - Use TaskFlow API (@task decorator) for Python tasks — cleaner than PythonOperator
 - Use KubernetesPodOperator for heavy workloads — isolates dependencies and resources
 - Avoid pulling large datasets into Airflow worker memory — use Spark/dbt/SQL for heavy transforms

3. Dependencies and branching:
 - Define task dependencies with >> and << operators
 - Use BranchPythonOperator for conditional logic
 - Use TriggerDagRunOperator for cross-DAG dependencies (prefer sensors for blocking waits)

4. Idempotency:
 - All tasks must be safely re-runnable
 - Use execution_date in file paths and table partition filters to scope each run

5. Alerting:
 - on_failure_callback: send Slack alert with DAG name, task, execution_date, and log URL
 - SLA miss callback: alert if DAG does not complete within SLA

6. Testing:
 - Unit test task logic separately from the DAG
 - Use airflow dags test dag_id execution_date for local DAG runs

Return: complete DAG code with all operators, dependencies, and alerting. Copy prompt View page Show more ↓ Pipeline Design Intermediate Prompt 03 
### dbt Project Structure 
Design the dbt project structure for a data warehouse with {{num_source_systems}} source systems.

1. Directory structure:
```
models/
 staging/ # 1:1 with source tables, light cleaning only
 source_a/
 source_b/
 intermediate/ # Business logic, joining staging models
 marts/
 core/ # Shared dimension and fact tables
 finance/ # Domain-specific marts
 marketing/
tests/
 generic/ # Custom generic tests
 singular/ # One-off data quality tests
macros/
seeds/
snapshots/
```

2. Model naming conventions:
 - Staging: stg_{source}__{entity} (e.g. stg_salesforce__accounts)
 - Intermediate: int_{entity}_{verb} (e.g. int_orders_pivoted)
 - Marts: {entity} or dim_{entity} / fct_{entity}

3. Materialization strategy:
 - Staging: view (always fresh, no storage cost)
 - Intermediate: ephemeral or table depending on complexity
 - Marts: table or incremental depending on size and freshness requirements

4. Sources configuration (sources.yml):
 - Define all source tables with freshness checks
 - freshness: warn_after: {count: 12, period: hour}, error_after: {count: 24, period: hour}

5. Model configuration (schema.yml):
 - Document every model and column
 - Apply generic tests: unique, not_null, accepted_values, relationships

6. Incremental models:
 - Use unique_key for merge strategy
 - Filter with is_incremental() macro: WHERE updated_at > (SELECT MAX(updated_at) FROM {{ this }})
 - Handle late-arriving data with a lookback window

7. CI/CD integration:
 - dbt build --select state:modified+ on PRs (only changed models and their downstream)
 - dbt test --select source:* for source freshness checks

Return: directory structure, naming convention guide, materialization decision matrix, and CI/CD integration config. Copy prompt View page Show more ↓ Pipeline Design Intermediate Prompt 04 
### Incremental Load Design 
Design a robust incremental data load pattern for this source table.

Source: {{source_table}} in {{source_db}}
Target: {{target_table}} in {{target_db}}
Update pattern: {{update_pattern}} (append-only / append-and-update / full CRUD)

1. Watermark management:
 - Store the last successful watermark (max updated_at or max id) in a dedicated metadata table
 - Watermark must be committed only after successful write to target — never before
 - Handle clock skew: use watermark = max(updated_at) - safety_margin (e.g. 5 minutes) to catch late-arriving rows

2. Incremental query:
 - SELECT * FROM source WHERE updated_at > {{last_watermark}} AND updated_at <= {{current_run_time}}
 - Use a closed upper bound (current run time) to make the window deterministic and replayable
 - Add an ORDER BY to ensure consistent extraction order

3. Merge/upsert to target:
 - Use MERGE statement (or equivalent) matching on primary key
 - Handle inserts (new rows), updates (changed rows), and optionally soft deletes (is_deleted flag)
 - Never use INSERT blindly — always upsert to maintain idempotency

4. Hard delete handling:
 - If source supports deletes and CDC is not available: run a full key scan periodically (e.g. daily) and soft-delete rows absent from source
 - Add deleted_at and is_current columns to target table

5. Backfill procedure:
 - To re-process a date range: set watermark back to range start and re-run
 - Ensure the merge logic is idempotent so backfill does not create duplicates

6. Schema change handling:
 - Before each run, compare source schema to last known schema
 - Alert on new, removed, or type-changed columns before proceeding

Return: watermark table DDL, incremental query, merge statement, delete handling, and backfill procedure. Copy prompt View page Show more ↓ Pipeline Design Beginner Prompt 05 
### Ingestion Pattern Selector 
Recommend the right data ingestion pattern for this source system.

Source system: {{source_system}}
Data characteristics: {{data_characteristics}}
Latency requirement: {{latency_requirement}}
Volume: {{volume}}

Evaluate and recommend from these patterns:

1. Full load:
 - Re-ingest the entire source table on every run
 - When to use: small tables (<1M rows), no reliable change tracking, sources that cannot support incremental queries
 - Drawbacks: expensive, slow, high source system load

2. Incremental load (timestamp-based):
 - Query rows where updated_at > last_watermark
 - When to use: source has a reliable updated_at column, append-and-update workloads
 - Drawbacks: misses hard deletes, requires reliable timestamp column

3. Change Data Capture (CDC):
 - Read from database transaction log (Debezium, AWS DMS, Fivetran)
 - When to use: need to capture deletes, near-real-time latency, high-volume OLTP source
 - Drawbacks: requires log access, more complex infrastructure

4. Event streaming:
 - Source publishes events to Kafka/Kinesis, pipeline consumes
 - When to use: event-driven architecture already exists, sub-minute latency needed
 - Drawbacks: requires event producer instrumentation

5. API polling:
 - Call REST/GraphQL API on schedule
 - When to use: no database access, SaaS sources (Salesforce, HubSpot)
 - Drawbacks: rate limits, pagination, no deletes

Return: recommended pattern with rationale, drawbacks to be aware of, and implementation checklist. Copy prompt View page Show more ↓ Pipeline Design Advanced Prompt 06 
### Lambda vs Kappa Architecture 
Evaluate whether this use case calls for a Lambda architecture or a Kappa architecture.

Use case: {{use_case_description}}
Latency requirements: {{latency}}
Historical reprocessing need: {{reprocessing_need}}
Team size and complexity tolerance: {{team_constraints}}

1. Lambda architecture:
 - Two separate pipelines: batch (accurate, slow) and speed (fast, approximate)
 - Serving layer merges batch and speed views
 - Pros: handles historical reprocessing naturally, speed layer can be simpler
 - Cons: two codebases for the same logic (duplication and drift risk), higher operational complexity
 - When to choose: if batch and streaming have genuinely different business logic, or if batch accuracy is non-negotiable and streaming is additive

2. Kappa architecture:
 - Single streaming pipeline for everything
 - Reprocessing = replay from beginning of the message log with a new consumer group
 - Pros: single codebase, simpler operations, no view merging
 - Cons: requires a long-retention message log, streaming system must handle batch-scale replay, stateful processing is more complex
 - When to choose: when batch and streaming logic are identical, team wants to minimize operational surface area

3. Decision framework:
 - Is the processing logic identical for batch and streaming? → Kappa
 - Do you need to reprocess years of history frequently? → Check if Kappa replay is cost-effective
 - Is your team small? → Kappa (less to maintain)
 - Do you have complex, different historical vs real-time logic? → Lambda
 - Is latency requirement < 1 minute AND accuracy is critical? → Lambda with micro-batch

4. Recommended architecture for this use case:
 - State the recommendation clearly with rationale
 - Identify the top 2 risks of the chosen approach and mitigations

Return: architecture comparison, decision framework applied to this use case, recommendation, and risk register. Copy prompt View page Show more ↓ Pipeline Design Beginner Prompt 07 
### Pipeline Architecture Review 
Review this data pipeline architecture and identify weaknesses.

Pipeline description: {{pipeline_description}}

Evaluate across these dimensions and flag each as Critical / Warning / Info:

1. Reliability:
 - Is there a single point of failure? What happens if any one component goes down?
 - Are retries implemented with exponential backoff and jitter?
 - Is there a dead-letter queue or error sink for failed records?
 - Are downstream consumers protected from upstream failures (circuit breaker)?

2. Idempotency:
 - Can the pipeline be safely re-run without producing duplicate data?
 - Is the write operation upsert/merge rather than append-only?
 - If append-only, is there a deduplication step downstream?

3. Observability:
 - Are row counts logged at every stage (source, after transformation, at sink)?
 - Is there alerting on pipeline failure, SLA breach, and anomalous record counts?
 - Can you trace a single record from source to destination?

4. Scalability:
 - Will the design hold at 10× current data volume?
 - Are there any sequential bottlenecks that cannot be parallelized?

5. Maintainability:
 - Is business logic separated from infrastructure concerns?
 - Are transformations testable in isolation?

Return: issue list with severity, impact, and specific remediation for each finding. Copy prompt View page Show more ↓ Pipeline Design Advanced Chain 08 
### Pipeline Design Chain 
Step 1: Requirements gathering — define: source systems and their characteristics (volume, velocity, format, update pattern), latency SLA (batch/micro-batch/real-time), downstream consumers and their needs, and any compliance or data residency constraints.
Step 2: Ingestion pattern selection — for each source, select the appropriate ingestion pattern (full load, incremental, CDC, streaming, API polling) with rationale. Identify which sources need CDC and what infrastructure that requires.
Step 3: Processing layer design — choose the processing technology (dbt, Spark, Flink, SQL) for each transformation layer. Define the medallion layers (Bronze/Silver/Gold or equivalent) and what transformations happen at each layer.
Step 4: Storage and partitioning — design the storage layout for each layer. Define partitioning strategy, file format (Parquet/Delta/Iceberg), and retention policy. Estimate storage cost.
Step 5: Orchestration design — design the DAG structure. Define dependencies between pipelines, scheduling strategy, SLA per pipeline, retry policy, and alerting.
Step 6: Reliability and observability — define: row count reconciliation checks, data freshness monitoring, lineage tracking, alerting thresholds, and incident response procedure.
Step 7: Write the pipeline design document: architecture diagram (text), technology choices with rationale, data flow description, SLA commitments, known risks, and estimated build timeline. Copy prompt View page Show more ↓ Pipeline Design Intermediate Prompt 09 
### Spark Job Optimization 
Optimize this Spark job for performance, cost, and reliability.

Current job: {{job_description}}
Current runtime: {{current_runtime}}
Current cost: {{current_cost}}

1. Diagnose first with Spark UI:
 - Identify stages with the longest duration
 - Check for data skew: are some partitions processing 10× more data than others?
 - Check for shuffle volume: large shuffles are the most common performance killer
 - Check for spill: memory spill to disk indicates insufficient executor memory

2. Partitioning optimization:
 - Repartition before a join or aggregation to the right number of partitions: num_partitions = total_data_size_GB × 128 (for 128MB partitions)
 - Use repartition(n, key_column) to co-locate related records and reduce shuffle
 - Use coalesce() to reduce partition count before writing (avoids full shuffle)

3. Join optimization:
 - Broadcast join: use for any table < {{broadcast_threshold_mb}}MB — eliminates shuffle entirely
 - Sort-merge join (default): ensure both sides are partitioned and sorted on the join key
 - Skew join: handle skewed keys by salting (append a random prefix to the key)

4. Data skew handling:
 - Identify skewed keys: GROUP BY join_key ORDER BY COUNT DESC LIMIT 20
 - Salt skewed keys: join_key_salted = concat(join_key, '_', floor(rand() * N))
 - Process skewed keys separately and union with normal results

5. Caching strategy:
 - cache() / persist() DataFrames used more than once in the same job
 - Use MEMORY_AND_DISK_SER for large DataFrames that don't fit in memory
 - Unpersist cached DataFrames when no longer needed

6. Configuration tuning:
 - spark.sql.adaptive.enabled=true (AQE): enables runtime partition coalescing and join strategy switching
 - spark.sql.adaptive.skewJoin.enabled=true: automatically handles skewed joins
 - Executor memory = (node_memory - overhead) / executors_per_node

Return: diagnosis procedure, optimization implementations with estimated impact, and configuration recommendations. Copy prompt View page Show more ↓ Pipeline Design Intermediate Prompt 10 
### Streaming Pipeline Design 
Design a streaming data pipeline for processing {{event_type}} events from {{source}} to {{destination}}.

Throughput requirement: {{throughput}} events/sec
Latency requirement: end-to-end < {{latency_target}}

1. Message broker configuration (Kafka / Kinesis):
 - Topic partitioning: number of partitions = max_throughput / throughput_per_partition
 - Partition key: choose a key that distributes load evenly AND ensures ordering where required
 - Retention: set to at least 7 days to allow replay from any point in the last week
 - Replication factor: 3 for production (tolerates 2 broker failures)

2. Consumer design:
 - Consumer group: one per logical pipeline to enable independent replay
 - Offset commit strategy: commit after successful write to destination (at-least-once delivery)
 - Idempotent consumer: handle duplicate messages at the destination with deduplication on event_id
 - Backpressure: limit consumer fetch size and processing batch to control memory usage

3. Stream processing (Flink / Spark Structured Streaming / Kafka Streams):
 - Windowing: tumbling window of {{window_size}} for aggregations
 - Watermark: allow late events up to {{late_arrival_tolerance}} before closing window
 - State management: use checkpointing every 60 seconds for fault tolerance

4. Exactly-once semantics:
 - Kafka transactions + idempotent producers for source-to-broker
 - Transactional writes to destination (or idempotent upserts)
 - Checkpoint-based recovery to avoid reprocessing

5. Dead letter queue:
 - Route unparseable or schema-invalid messages to a DLQ topic
 - Alert on DLQ growth rate > {{dlq_threshold}} messages/min

6. Monitoring:
 - Consumer lag per partition (alert if lag > {{lag_threshold}})
 - Processing latency (time from event timestamp to destination write)
 - Throughput (events/sec in and out)

Return: architecture diagram (text), configuration recommendations, processing code skeleton, and monitoring setup. Copy prompt View page Show more ↓ 
## Data Quality 
8 prompt s Data Quality Intermediate Prompt 01 
### Data Lineage Tracking 
Implement column-level data lineage tracking for this data platform.

1. Lineage metadata model:
 - Node types: source_system, table, column, transformation, pipeline_run
 - Edge types: table_derives_from, column_derives_from, transformation_reads, transformation_writes
 - Lineage table DDL:
 ```sql
 CREATE TABLE column_lineage (
 target_table VARCHAR,
 target_column VARCHAR,
 source_table VARCHAR,
 source_column VARCHAR,
 transformation_description VARCHAR,
 pipeline_name VARCHAR,
 recorded_at TIMESTAMP
 )
 ```

2. Automated lineage extraction:
 - For dbt: parse dbt's manifest.json — it contains full column-level lineage from ref() and source() calls
 - For Spark SQL: parse the SQL AST to extract table and column references
 - For Airflow DAGs: extract lineage from task input/output datasets (OpenLineage / Marquez)

3. Lineage use cases:
 - Impact analysis: 'if I change this source column, which downstream tables and reports are affected?'
 - Root cause analysis: 'this report column has wrong values — trace back to the source'
 - Compliance: 'which tables contain data derived from PII column X?'

4. Lineage UI (if building custom):
 - Graph visualization: nodes are tables/columns, edges are derivation relationships
 - Search: find all downstream consumers of a given column
 - Highlight path from a source column to a final report metric

5. OpenLineage integration:
 - Emit OpenLineage events from Airflow and Spark jobs
 - Store in Marquez or forward to data catalog (DataHub, Atlan, Alation)

Return: lineage metadata DDL, automated extraction script for dbt, impact analysis query, and PII propagation query. Copy prompt View page Show more ↓ Data Quality Advanced Chain 02 
### Data Quality Framework Chain 
Step 1: DQ requirements — identify the top 10 most critical tables in the platform. For each, define: the business impact of bad data, the acceptable error rate, and the SLA for detecting and resolving issues.
Step 2: Test implementation — for each critical table, implement the full test suite: schema, freshness, row count reconciliation, business rule validation, and statistical anomaly detection.
Step 3: Severity and routing — classify each test by severity (blocking vs warning) and define the alert routing: who gets notified, by which channel, and within what time window.
Step 4: DQ scorecard — build a daily DQ scorecard: overall pass rate, test pass rate per table, trend over time, and highlight tables with declining quality.
Step 5: Incident workflow — define the incident workflow for DQ failures: detection → acknowledgment → investigation → root cause → fix → post-mortem. Define SLAs per severity.
Step 6: Feedback loop — create a mechanism for analysts to report suspected data quality issues. Triage reported issues, trace to root cause, and update tests to prevent recurrence.
Step 7: Write the DQ framework document: test inventory, severity matrix, alert routing, SLAs, incident workflow, and the governance process for adding new tests. Copy prompt View page Show more ↓ Data Quality Beginner Prompt 03 
### Data Quality Test Suite 
Write a comprehensive data quality test suite for the table {{table_name}}.

Use dbt tests, Great Expectations, or SQL assertions (specify preference: {{testing_tool}}).

1. Schema tests (run on every load):
 - All NOT NULL columns contain no nulls
 - Primary key is unique and not null
 - Foreign keys reference valid records in parent tables
 - Categorical columns contain only accepted values
 - Numeric columns are within expected ranges (no negative IDs, no future dates)

2. Freshness tests (run on every load):
 - Max(updated_at) is within {{freshness_threshold}} hours of current time
 - Row count is within [mean ± 3σ] of the historical daily row count
 - No date partition has zero rows (empty partitions indicate pipeline failure)

3. Consistency tests (run daily):
 - Row count in this table matches row count in the source system (reconciliation)
 - SUM of key measures matches source system totals (financial reconciliation)
 - No duplicate rows on the natural key

4. Business rule tests (run daily):
 - Specific rules from the domain: {{business_rules}}
 - Example: order_total = SUM(line_items) for all orders
 - Example: all active customers have at least one contact record

5. Test severity levels:
 - ERROR: test failure blocks downstream tables from running
 - WARN: test failure logs a warning but does not block
 - Assign each test to the appropriate severity level

Return: complete test suite code, severity assignments, and a test execution schedule. Copy prompt View page Show more ↓ Data Quality Intermediate Prompt 04 
### Duplicate Detection at Scale 
Implement scalable duplicate detection for a large table ({{table_size}} rows) with a compound natural key.

Natural key: {{natural_key_columns}}
Table: {{table_name}}

1. Exact duplicate detection (fast):
 ```sql
 SELECT {{natural_key_columns}}, COUNT(*) AS cnt
 FROM {{table_name}}
 GROUP BY {{natural_key_columns}}
 HAVING COUNT(*) > 1
 ORDER BY cnt DESC
 LIMIT 100
 ```
 - Run this query and report: total duplicate groups, total excess rows, and sample examples

2. Near-duplicate detection for string keys:
 - Phonetic matching: Soundex or Metaphone for name fields
 - MinHash LSH for large-scale fuzzy deduplication (scales to billions of rows)
 - Blocking: reduce comparison space by only comparing within the same first-letter group or zip code

3. Deduplication strategy:
 - Deterministic: define a priority rule for which record to keep (most recent, most complete, specific source)
 - Write a SELECT DISTINCT-equivalent using ROW_NUMBER() to select the canonical record:
 ```sql
 WITH ranked AS (
 SELECT *,
 ROW_NUMBER() OVER (
 PARTITION BY {{natural_key_columns}}
 ORDER BY {{priority_column}} DESC
 ) AS rn
 FROM {{table_name}}
 )
 SELECT * FROM ranked WHERE rn = 1
 ```

4. Prevention (upstream fix):
 - Add a UNIQUE constraint if the warehouse supports it
 - Add a pre-load duplicate check that blocks the load if duplicates are detected in the incoming batch
 - Instrument the source system write path to prevent duplicates at origin

5. Monitoring:
 - Add a daily duplicate count metric to the DQ dashboard
 - Alert if duplicate count increases day-over-day

Return: exact duplicate query, ROW_NUMBER deduplication query, near-duplicate detection approach, and prevention implementation. Copy prompt View page Show more ↓ Data Quality Intermediate Prompt 05 
### Pipeline Anomaly Detection 
Build statistical anomaly detection for this data pipeline's operational metrics.

Metrics to monitor: row counts, processing time, error rate, and key business measure totals.

1. Baseline computation (run weekly):
 - For each metric and each day-of-week, compute: mean, standard deviation, and 5th/95th percentiles from the last 90 days
 - Store baselines in a metadata table: metric_name, day_of_week, mean, std, p5, p95, computed_at

2. Anomaly detection rules (run after each pipeline execution):
 - Statistical: flag if today's value is outside mean ± {{sigma}}σ (e.g. 3σ)
 - Percentage change: flag if WoW change > {{pct_threshold}}% for the same day of week
 - Absolute minimum: flag if row count = 0 (hard rule, always an error)
 - Absolute maximum: flag if row count > {{hard_cap}} (possible runaway job or data duplication)

3. Seasonal adjustment:
 - Normalize metrics by day-of-week (Monday typically has different volumes than Friday)
 - For businesses with monthly seasonality: also normalize by week-of-month

4. Metric-level thresholds:
 - Different thresholds per metric: row counts may tolerate ±20%, revenue totals should only tolerate ±1%
 - Store thresholds in a configuration table for easy adjustment without code changes

5. Alert routing:
 - Route anomalies to the appropriate team based on metric type (data team vs business team)
 - Include context in the alert: current value, expected range, historical chart link
 - Suppress duplicate alerts: do not re-alert the same anomaly within 4 hours

Return: baseline computation SQL, anomaly detection queries, threshold configuration table, and alert routing logic. Copy prompt View page Show more ↓ Data Quality Beginner Prompt 06 
### Row Count Reconciliation 
Build a row count reconciliation framework to verify data completeness across pipeline stages.

1. Count capture at each stage:
 - Extract: rows read from source
 - After filter: rows meeting extraction criteria
 - After transformation: rows output from each major transformation step
 - Load: rows written to target
 - Store all counts in a reconciliation metadata table: pipeline_run_id, stage, table_name, row_count, timestamp

2. Reconciliation checks:
 - Source to target: abs(source_count - target_count) / source_count < {{tolerance}} (e.g. 0.001 = 0.1% tolerance)
 - Explain expected differences: deduplication, filtering, and type-specific exclusions
 - For CDC pipelines: verify inserts + updates + deletes = total source changes

3. Historical comparison:
 - Compare today's count to the same day last week (day-of-week adjusted)
 - Alert if count differs by more than 2σ from the rolling 30-day average for that day
 - Hard alert if count is 0 (empty load — almost always a pipeline error)

4. Metadata table DDL:
 ```sql
 CREATE TABLE pipeline_reconciliation (
 run_id VARCHAR,
 pipeline_name VARCHAR,
 stage VARCHAR,
 table_name VARCHAR,
 expected_count BIGINT,
 actual_count BIGINT,
 variance_pct DECIMAL(10,4),
 status VARCHAR, -- PASS / WARN / FAIL
 run_timestamp TIMESTAMP
 )
 ```

5. Alerting:
 - FAIL: variance > {{fail_threshold}}% → block downstream, page on-call
 - WARN: variance > {{warn_threshold}}% → log warning, notify data team
 - PASS: variance within tolerance → log and continue

Return: reconciliation metadata table DDL, count capture code, comparison queries, and alerting logic. Copy prompt View page Show more ↓ Data Quality Intermediate Prompt 07 
### Schema Drift Detection 
Implement automated schema drift detection to catch upstream schema changes before they break the pipeline.

1. Schema snapshot:
 - After each successful run, save the source schema to a metadata table: column_name, data_type, is_nullable, ordinal_position, table_name, snapshot_date
 - Schema fingerprint: compute a hash of the sorted column list and types — quick change detection

2. Drift detection (run before each pipeline execution):
 Compare current source schema against the last known good schema:
 - NEW columns: column exists in current schema but not in snapshot
 - REMOVED columns: column exists in snapshot but not in current schema
 - TYPE CHANGES: column exists in both but data type has changed
 - RENAME: column removed and new column added with similar name — flag as possible rename
 - REORDERING: column ordinal positions changed (matters for positional file formats like CSV)

3. Severity classification:
 - BREAKING changes (block pipeline):
 - Removed column that is used downstream
 - Type change that is not backwards compatible (VARCHAR to INT)
 - WARNING changes (log and continue):
 - New column added (schema evolution — may need to add to downstream tables)
 - Type widening (INT to BIGINT, VARCHAR(50) to VARCHAR(255))
 - INFO:
 - Ordinal position change only
 - New column not used downstream

4. Automated response:
 - BREAKING: halt the pipeline, alert on-call, create a ticket
 - WARNING: continue pipeline, send a non-urgent notification to data team
 - Update the schema snapshot only after a successful run

Return: schema snapshot table DDL, drift detection query, severity classification logic, and alert templates. Copy prompt View page Show more ↓ Data Quality Advanced Prompt 08 
### SLA Monitoring for Pipelines 
Build an SLA monitoring system for data pipeline delivery commitments.

Pipelines to monitor: {{pipeline_list}}
SLA targets: {{sla_targets}} (e.g. 'orders table available by 06:00 UTC daily')

1. SLA definition table:
 ```sql
 CREATE TABLE pipeline_slas (
 pipeline_name VARCHAR,
 table_name VARCHAR,
 sla_type VARCHAR, -- 'availability' or 'freshness'
 sla_deadline TIME, -- time by which data must be available
 sla_timezone VARCHAR,
 warn_minutes_before INT, -- warn this many minutes before breach
 owner_team VARCHAR,
 slack_channel VARCHAR
 )
 ```

2. SLA tracking (run every 5 minutes):
 - For availability SLAs: has the pipeline completed successfully since the last scheduled run?
 - For freshness SLAs: is MAX(updated_at) in the target table within the SLA window?
 - Record each check: pipeline_name, check_time, status (ON_TIME / AT_RISK / BREACHED)

3. Early warning system:
 - AT_RISK: pipeline is running but has not completed with {{warn_minutes}} minutes remaining before SLA
 - Estimate: based on current progress, will it complete in time?
 - Alert the pipeline owner with estimated completion time

4. SLA breach handling:
 - BREACHED: SLA deadline has passed and data is not available
 - Page the on-call data engineer
 - Notify downstream consumers automatically
 - Log breach duration for SLA reporting

5. SLA reporting (weekly):
 - SLA compliance rate per pipeline (target: ≥ 99.5%)
 - Average delay for late pipelines
 - Top 3 pipelines by breach frequency
 - MTTD and MTTR per pipeline

Return: SLA definition table DDL, monitoring query, early warning logic, breach alert template, and weekly SLA report query. Copy prompt View page Show more ↓ 
## Data Warehouse Patterns 
8 prompt s Data Warehouse Patterns Advanced Prompt 01 
### Data Vault Design 
Design a Data Vault 2.0 model for integrating {{num_sources}} source systems on the entity: {{core_entity}}.

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

Return: Hub, Satellite, and Link DDLs, loading SQL for each component, and PIT table design. Copy prompt View page Show more ↓ Data Warehouse Patterns Intermediate Prompt 02 
### Fact Table Loading Pattern 
Implement a robust fact table loading pattern for {{fact_table}} using a {{loading_strategy}} approach.

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

Return: pre-load validation queries, surrogate key lookup logic, incremental load SQL, and post-load reconciliation queries. Copy prompt View page Show more ↓ Data Warehouse Patterns Intermediate Prompt 03 
### Medallion Architecture Design 
Design a medallion (Bronze / Silver / Gold) architecture for this data platform.

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

Return: layer definitions, DDL templates for each layer, lineage tracking approach, and SLA commitments. Copy prompt View page Show more ↓ Data Warehouse Patterns Intermediate Prompt 04 
### Partitioning Strategy 
Design the optimal partitioning and clustering strategy for this data warehouse table.

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

Return: partitioning and clustering DDL, partition pruning test query, and maintenance schedule. Copy prompt View page Show more ↓ Data Warehouse Patterns Advanced Prompt 05 
### Query Performance Tuning 
Tune this slow data warehouse query for performance.

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

Return: annotated execution plan, specific rewrites for each optimization applied, and before/after runtime comparison. Copy prompt View page Show more ↓ Data Warehouse Patterns Beginner Template 06 
### Slowly Changing Dimension 
Implement a Type 2 Slowly Changing Dimension (SCD2) for the table {{dim_table}} in {{database_type}}.

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

Return: CREATE TABLE DDL, MERGE statement, point-in-time query, and current records query. Copy prompt View page Show more ↓ Data Warehouse Patterns Beginner Prompt 07 
### Star Schema Design 
Design a star schema for this business process: {{business_process}}

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

Return: fact table DDL, dimension table DDLs, date dimension generation SQL, and ER diagram (text). Copy prompt View page Show more ↓ Data Warehouse Patterns Advanced Chain 08 
### Warehouse Design Chain 
Step 1: Requirements — identify the business processes to model, the grain of each fact table, the key business questions to answer, and the consumers (BI tools, DS teams, apps).
Step 2: Source analysis — profile each source table: row counts, key columns, update patterns, data quality issues, and join relationships. Identify integration challenges (different customer IDs across systems).
Step 3: Dimensional model design — design the star schema(s): fact tables with grain and measures, dimension tables with attributes and SCD type per column. Draw the ER diagram.
Step 4: Physical design — choose partitioning, clustering, file format, and materialization strategy for each table. Estimate storage size and query cost at expected query volume.
Step 5: Loading design — design the loading pattern for each table: full load vs incremental vs SCD2 merge. Write the key SQL statements.
Step 6: Testing plan — define data quality tests for each table: row count checks, uniqueness, not-null, referential integrity, and business rule validation.
Step 7: Document the warehouse design: data model diagram, table catalog (name, description, grain, owner), loading schedule, SLA, and known limitations. Copy prompt View page Show more ↓ 
## Data Contracts 
5 prompt s Data Contracts Advanced Prompt 01 
### Breaking Change Migration 
Design a safe migration process for this breaking schema change.

Breaking change: {{change_description}} (e.g. renaming column customer_id to account_id, or changing the grain from order to order_line)
Affected table: {{table_name}}
Known consumers: {{consumer_list}}

1. Impact assessment:
 - Query the data lineage graph to find ALL consumers of the affected table and column
 - For each consumer: team, table/report name, how the breaking column is used, migration effort (Low/Medium/High)
 - Identify any external consumers (APIs, applications) that cannot be migrated centrally

2. Migration strategy: Expand and Contract (strangler fig pattern):
 Phase 1 — Expand (add, don't remove):
 - Add the new column/structure alongside the existing one
 - Populate both: old column = old value, new column = new value
 - Publish schema with both old and new columns
 - Notify all consumers: 'New column available, please migrate. Old column will be removed on {{sunset_date}}'

 Phase 2 — Migrate:
 - Support consumer teams in migrating their pipelines/reports to the new column
 - Track migration progress per consumer team
 - Provide a migration deadline: {{deadline}}

 Phase 3 — Contract (remove the old):
 - Verify all consumers have migrated (query lineage + direct confirmation)
 - Remove the old column
 - Publish final schema version

3. Rollback plan:
 - At each phase: what is the rollback procedure if a critical consumer cannot migrate in time?
 - Rollback requires reverting only Phase 1 changes — no data is lost

4. Communication plan:
 - Initial announcement: {{notice_period}} before Phase 1
 - Weekly migration status updates to all consumers
 - Final warning: 1 week before Phase 3

Return: impact assessment table, phase-by-phase implementation plan, consumer communication templates, and rollback procedure. Copy prompt View page Show more ↓ Data Contracts Intermediate Prompt 02 
### Contract Validation Pipeline 
Build an automated contract validation pipeline that verifies produced data meets all contract commitments before it is made available to consumers.

Data contract: {{contract_name}}

1. Validation gate architecture:
 - Produce data to a staging location (not the production table)
 - Run all contract validations against the staging data
 - Only promote to production if ALL blocking validations pass
 - If any blocking validation fails: halt, alert producer, do not expose data to consumers

2. Schema validation:
 - All required columns are present
 - All column data types match the contract definition
 - No unexpected new columns (flag as warning — possible unplanned schema evolution)

3. Semantic validation:
 - Primary key is unique and non-null
 - All NOT NULL columns have no nulls
 - All categorical columns contain only contract-defined values
 - Business rule assertions: {{business_rules}}

4. Freshness validation:
 - MAX(event_timestamp) is within the contract-defined freshness window
 - Row count is within ±{{tolerance}}% of the expected count for this time period

5. Promotion to production:
 - Atomic swap: rename staging table to production (or INSERT OVERWRITE the partition)
 - Log promotion: contract_name, run_id, validation_results, promotion_timestamp
 - Notify downstream consumers that fresh data is available (via event or polling endpoint)

6. Consumer-facing freshness endpoint:
 - GET /contracts/{{contract_name}}/freshness → returns: last_updated, row_count, validation_status
 - Consumers can poll this endpoint to know when new data is ready

Return: validation pipeline code, promotion logic, freshness endpoint spec, and consumer notification design. Copy prompt View page Show more ↓ Data Contracts Beginner Prompt 03 
### Data Contract Definition 
Write a data contract for the dataset: {{dataset_name}} produced by the {{producer_team}} team and consumed by {{consumer_teams}}.

A data contract is a formal agreement between data producers and consumers specifying what data will be delivered, in what format, with what quality guarantees, and on what schedule.

1. Dataset identity:
 - Dataset name and version
 - Producer: team, contact, and escalation path
 - Consumers: teams currently depending on this dataset

2. Schema definition:
 - Table or topic name
 - For each column/field: name, data type, nullable (Y/N), description, example value, PII classification (Y/N)
 - Primary key or unique identifier
 - Partitioning columns

3. Semantics and business rules:
 - Grain: what does one row represent?
 - Business rules: constraints and derived logic (e.g. 'order_total is always the sum of line items')
 - Key relationships to other datasets

4. Quality commitments:
 - Completeness: which columns are guaranteed non-null?
 - Uniqueness: which column combinations are guaranteed unique?
 - Freshness: data will be available by {{sla_time}} on each {{frequency}}
 - Accuracy: key measures are reconciled to source within {{tolerance}}

5. Change management:
 - Breaking change definition: removed column, type change, semantic change
 - Notice period: {{notice_period}} days notice required before a breaking change
 - Deprecation process: how will consumers be notified and given time to migrate?

6. SLA and support:
 - Incident response time: {{response_time}}
 - Scheduled maintenance window: {{maintenance_window}}
 - Where to report issues: {{issue_channel}}

Return: complete data contract document in YAML format. Copy prompt View page Show more ↓ Data Contracts Advanced Prompt 04 
### Data Mesh Contract Governance 
Design a data contract governance model for a data mesh architecture with {{num_domains}} domain teams.

In a data mesh, domain teams own and publish their own data products. Contracts are the mechanism that makes data products reliable and trustworthy.

1. Contract ownership model:
 - Producer team: responsible for defining the contract, meeting the commitments, and handling breaking changes
 - Consumer teams: responsible for registering as consumers and migrating when notified
 - Data platform team: responsible for tooling, enforcement, and governance process
 - No central team should approve every contract — this creates bottlenecks

2. Contract registry:
 - Centralized catalog of all published contracts (not a bottleneck — just a registry)
 - Each contract: schema, SLA, consumers, version history, compliance status
 - Automatic registration when a producer publishes a new dataset

3. Automated enforcement:
 - CI/CD check: new data publication must include a valid contract
 - Automated compatibility check: new schema version must be compatible with current contract
 - Consumer registration: consumers must register in the contract registry to receive change notifications
 - SLA monitoring: automated checks run against every published contract

4. Cross-domain standards (things that must be consistent across all domains):
 - Common entity IDs (customer_id must mean the same thing everywhere)
 - Standard date/time formats and timezone
 - PII classification and handling
 - Minimum required fields in every contract

5. Dispute resolution:
 - Process for when a producer cannot meet a consumer's requirements
 - Escalation path for unresolved contract disputes
 - SLA breach accountability and remediation

6. Discoverability:
 - Data product catalog: searchable, showing all published contracts, quality scores, and consumer counts
 - Quality score per data product: based on SLA compliance, test pass rate, consumer satisfaction

Return: governance model document, contract registry schema, enforcement automation design, and cross-domain standards. Copy prompt View page Show more ↓ Data Contracts Intermediate Prompt 05 
### Schema Evolution Strategy 
Design a schema evolution strategy that allows the {{producer_team}} to evolve data schemas without breaking downstream consumers.

1. Compatible change classification:
 BACKWARD COMPATIBLE (consumers with old schema can read new data):
 - Adding a new optional column with a default value
 - Widening a type (INT → BIGINT, VARCHAR(50) → VARCHAR(255))
 - Adding a new enum value to a categorical column

 FORWARD COMPATIBLE (consumers with new schema can read old data):
 - Removing a column (old data will have the column, new data won't)
 - Narrowing a type (consumers must handle both)

 BREAKING (requires coordinated migration):
 - Removing a required column
 - Renaming a column
 - Changing a type in a non-widening way (VARCHAR → INT)
 - Changing the meaning of an existing column
 - Changing the grain of the table

2. Schema registry:
 - Register every schema version with its compatibility mode in Confluent Schema Registry or AWS Glue
 - Default compatibility mode: BACKWARD (new schema must be able to read old data)
 - Enforce compatibility checks on every schema change before deployment

3. Additive-first approach:
 - Prefer adding new columns over renaming or replacing existing ones
 - Deprecate columns by marking them in the schema comment before removing
 - Retain deprecated columns for {{deprecation_period}} before removing

4. Versioned tables:
 - For breaking changes that cannot be avoided: publish a new versioned table (orders_v2)
 - Run v1 and v2 in parallel for {{parallel_period}} to allow consumers to migrate
 - Provide a migration guide and migration deadline

5. Consumer notification workflow:
 - Automated notification to all registered consumers when schema changes are registered
 - For breaking changes: personal outreach to each consumer team, migration support offered

Return: change classification guide, schema registry setup, deprecation process, and versioned table migration procedure. Copy prompt View page Show more ↓ 
## Infrastructure and Platform 
4 prompt s Infrastructure and Platform Intermediate Prompt 01 
### Compute Sizing Guide 
Determine the right compute configuration for this data engineering workload.

Workload: {{workload_description}}
Data volume: {{data_volume}}
Runtime requirement: {{runtime_sla}}
Budget constraint: {{budget}}

1. Spark cluster sizing:
 - Driver: 1 node with 4–8 cores and 16–32GB RAM (driver is a coordinator, not a worker)
 - Executor memory rule: executor_memory = (node_memory × 0.75) / executors_per_node
 - Executor cores: 4–5 per executor (sweet spot — too many causes context switching, too few underutilizes memory parallelism)
 - Number of executors: total_data_size_GB / (executor_memory × compression_ratio) as a starting point
 - For shuffle-heavy jobs: more executors with less memory each (shuffle writes to local disk)
 - For memory-heavy joins: fewer executors with more memory each

2. Scaling strategy:
 - Start with a cluster that fits the data comfortably in memory
 - Profile first: identify if job is CPU-bound, memory-bound, or I/O-bound before scaling
 - CPU-bound: add more cores (more executors)
 - Memory-bound: add more RAM per executor (increase executor memory)
 - I/O-bound: add more storage bandwidth (use instance storage types like i3 on AWS)

3. Spot/preemptible instances:
 - Use spot for worker nodes (can tolerate eviction + checkpoint recovery)
 - Use on-demand for driver (eviction kills the entire job)
 - Savings: 60–80% cost reduction vs on-demand

4. Autoscaling:
 - Enable autoscaling for interactive and variable workloads
 - Disable for scheduled batch jobs with predictable volume (autoscaling overhead not worth it)

5. Benchmark procedure:
 - Run the job at 1×, 2×, 4× the baseline cluster size
 - Plot runtime vs cost: find the point of diminishing returns

Return: sizing recommendation, benchmark procedure, spot instance configuration, and cost estimate. Copy prompt View page Show more ↓ Infrastructure and Platform Intermediate Prompt 02 
### Data Lake File Format Selection 
Select the right file format and table format for each layer of this data lake.

Workloads: {{workloads}} (batch analytics, streaming, ML feature engineering, etc.)
Platform: {{compute_engines}} (Spark, Trino, Dremio, BigQuery, etc.)

1. File format comparison:

 Parquet:
 - Columnar, splittable, highly compressed
 - Best for: analytical reads, column-selective queries, broad engine support
 - Limitations: no ACID transactions, no efficient row-level updates, schema evolution is limited
 - Choose when: read-heavy analytics, stable schemas, no need for row-level changes

 ORC:
 - Similar to Parquet, marginally better for Hive workloads
 - Choose when: primary engine is Hive or Hive-compatible

 Avro:
 - Row-based, schema embedded in file, excellent schema evolution support
 - Best for: streaming ingestion, schema-registry integration, write-heavy workloads
 - Choose when: Kafka → data lake ingestion, schema evolution is frequent

 Delta Lake / Apache Iceberg / Apache Hudi (table formats):
 - ACID transactions, time travel, schema evolution, row-level deletes
 - Delta: tightest Spark integration, best for Databricks
 - Iceberg: broadest engine support (Spark, Trino, Flink, Dremio, BigQuery), best for multi-engine lakes
 - Hudi: streaming-optimized, best for CDC and near-real-time use cases

2. Recommendation by layer:
 - Bronze (raw ingest): Parquet or Avro depending on source
 - Silver (cleansed): Delta or Iceberg (need row-level updates for SCD)
 - Gold (marts): Delta or Iceberg (need ACID for concurrent writes)

3. Compression codec recommendation:
 - Snappy: fast compression/decompression, moderate compression ratio (default)
 - Zstd: better compression ratio than Snappy at similar speed (preferred for cold storage)
 - Gzip: maximum compression, slow decompression (use only for archival)

Return: format selection matrix, recommendation per layer, and compression codec guide. Copy prompt View page Show more ↓ Infrastructure and Platform Advanced Chain 03 
### Platform Evaluation Chain 
Step 1: Requirements gathering — document the platform requirements: data volume (current and 3-year projection), workload types (batch ETL, streaming, ad-hoc SQL, ML), latency SLAs, team size and SQL vs code preference, compliance requirements (data residency, SOC2, HIPAA), and budget range.
Step 2: Candidate selection — identify 3 candidate platforms based on the requirements. Typical candidates: Snowflake vs Databricks vs BigQuery, or Airflow vs Prefect vs Dagster. Eliminate options that fail hard requirements immediately.
Step 3: Evaluation criteria scoring — score each candidate on: performance (benchmark on representative workloads), total cost of ownership (compute + storage + egress + seats), developer experience (ease of use for the team), ecosystem (integrations with existing tools), operational burden (managed vs self-hosted), and vendor risk.
Step 4: Proof of concept — run a 2-week PoC for the top 2 candidates. Use a representative subset of actual workloads. Measure: query performance, pipeline development speed, operational effort, and cost.
Step 5: TCO modeling — build a 3-year TCO model for each finalist: compute, storage, licensing, personnel, migration, and training costs. Include the cost of not choosing this platform (opportunity cost).
Step 6: Risk assessment — for each finalist: vendor lock-in risk, migration complexity, scaling limits, support quality, and financial stability of the vendor.
Step 7: Write the platform recommendation document: requirements summary, evaluation matrix, PoC results, TCO comparison, risk assessment, final recommendation with rationale, migration plan, and success metrics. Copy prompt View page Show more ↓ Infrastructure and Platform Beginner Prompt 04 
### Warehouse Cost Optimization 
Analyze and optimize the cost of this cloud data warehouse.

Platform: {{platform}} (Snowflake / BigQuery / Redshift / Databricks)
Current monthly cost: {{current_cost}}
Target reduction: {{target_reduction}}

1. Cost breakdown analysis:
 - Identify the top 10 most expensive queries by compute cost
 - Identify the top 10 most expensive users/teams by spend
 - Break down storage cost: active storage vs time-travel vs fail-safe
 - Identify tables that have not been queried in the last 90 days (zombie tables)

2. Compute optimizations:
 - Auto-suspend: set warehouse auto-suspend to 1–2 minutes (not the default 10)
 - Auto-scale: use multi-cluster warehouses only for concurrent workloads, not sequential ones
 - Query optimization: the top 3 most expensive queries — can they be rewritten to scan less data?
 - Result caching: are users re-running identical queries? Enable result cache.
 - Materialization: for frequently run expensive aggregations, create a pre-aggregated table

3. Storage optimizations:
 - Reduce time-travel retention from 90 days to 7 days for non-critical tables (Snowflake)
 - Set partition expiration for old data that is no longer needed (BigQuery)
 - Compress and archive historical data to cheaper storage tiers
 - Delete zombie tables after confirming with owners

4. Governance:
 - Set per-user and per-team cost budgets with alerts at 80% and 100% of budget
 - Require query cost estimates before running full-table scans over {{threshold_gb}}GB
 - Tag queries with cost center for chargeback reporting

Return: cost breakdown analysis queries, top optimizations with estimated savings each, and governance policy. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
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
