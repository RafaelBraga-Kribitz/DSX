# Data Quality *AI Prompts *

8 Data Engineer prompts in Data Quality. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 7 single prompts · 1 chain. 

## AI prompts in Data Quality 
8 prompts Intermediate Single prompt 01 
### Data Lineage Tracking 

This prompt designs lineage tracking so teams can understand how data moves from source columns through transformations into analytical outputs. It supports impact analysis, root-cause investigation, and compliance questions, especially in platforms with dbt, Spark, and orchestration tools. The answer should treat lineage as an operational capability, not just documentation. 
Prompt text Implement column-level data lineage tracking for this data platform.

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

Return: lineage metadata DDL, automated extraction script for dbt, impact analysis query, and PII propagation query. Copy prompt Open prompt details Advanced Chain 02 
### Data Quality Framework Chain 

This prompt assembles a full data quality operating model, not just individual checks. It covers critical-table selection, testing, severity, routing, scorecards, incidents, and continuous feedback. It is best used when an organization wants a formal DQ framework with ownership and response expectations. 
Prompt text Step 1: DQ requirements — identify the top 10 most critical tables in the platform. For each, define: the business impact of bad data, the acceptable error rate, and the SLA for detecting and resolving issues.
Step 2: Test implementation — for each critical table, implement the full test suite: schema, freshness, row count reconciliation, business rule validation, and statistical anomaly detection.
Step 3: Severity and routing — classify each test by severity (blocking vs warning) and define the alert routing: who gets notified, by which channel, and within what time window.
Step 4: DQ scorecard — build a daily DQ scorecard: overall pass rate, test pass rate per table, trend over time, and highlight tables with declining quality.
Step 5: Incident workflow — define the incident workflow for DQ failures: detection → acknowledgment → investigation → root cause → fix → post-mortem. Define SLAs per severity.
Step 6: Feedback loop — create a mechanism for analysts to report suspected data quality issues. Triage reported issues, trace to root cause, and update tests to prevent recurrence.
Step 7: Write the DQ framework document: test inventory, severity matrix, alert routing, SLAs, incident workflow, and the governance process for adding new tests. Copy prompt Open prompt details Beginner Single prompt 03 
### Data Quality Test Suite 

This prompt creates a complete data quality testing package for a table, combining structural, freshness, consistency, and business-rule checks. It helps standardize what ‘good data’ means and how failures should be treated operationally. It is most useful when a team wants repeatable automated checks rather than manual spot checks. 
Prompt text Write a comprehensive data quality test suite for the table {{table_name}}.

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

Return: complete test suite code, severity assignments, and a test execution schedule. Copy prompt Open prompt details Intermediate Single prompt 04 
### Duplicate Detection at Scale 

This prompt tackles duplicate detection in large tables where simple manual inspection is not enough. It combines exact duplicate checks, near-duplicate strategies, canonical record selection, and upstream prevention. It is particularly useful for high-volume datasets with compound keys and recurring deduplication problems. 
Prompt text Implement scalable duplicate detection for a large table ({{table_size}} rows) with a compound natural key.

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

Return: exact duplicate query, ROW_NUMBER deduplication query, near-duplicate detection approach, and prevention implementation. Copy prompt Open prompt details Intermediate Single prompt 05 
### Pipeline Anomaly Detection 

This prompt applies statistical anomaly detection to operational pipeline metrics so teams can catch unusual behavior even when a job technically succeeds. It is valuable for spotting silent failures such as row-count drops, unusual runtimes, or business-total shifts. The output should combine statistical baselines with configurable thresholds and practical alert routing. 
Prompt text Build statistical anomaly detection for this data pipeline's operational metrics.

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

Return: baseline computation SQL, anomaly detection queries, threshold configuration table, and alert routing logic. Copy prompt Open prompt details Beginner Single prompt 06 
### Row Count Reconciliation 

This prompt builds a reconciliation framework around row counts across extraction, transformation, and load stages. It is intended to make completeness issues visible quickly and consistently, especially in ETL and CDC pipelines. The focus is on metadata capture, tolerance-based comparisons, and operational alerting. 
Prompt text Build a row count reconciliation framework to verify data completeness across pipeline stages.

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

Return: reconciliation metadata table DDL, count capture code, comparison queries, and alerting logic. Copy prompt Open prompt details Intermediate Single prompt 07 
### Schema Drift Detection 

This prompt catches upstream schema changes before they cause silent data corruption or pipeline failures. It is useful for pipelines that depend on external systems, files, or APIs where fields can appear, disappear, or change type unexpectedly. The answer should distinguish between informative drift and truly breaking changes. 
Prompt text Implement automated schema drift detection to catch upstream schema changes before they break the pipeline.

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

Return: schema snapshot table DDL, drift detection query, severity classification logic, and alert templates. Copy prompt Open prompt details Advanced Single prompt 08 
### SLA Monitoring for Pipelines 

This prompt builds an SLA monitoring system around pipeline delivery commitments such as table availability and freshness deadlines. It is useful when business users depend on data arriving by specific times and late delivery must be detected early. The output should include both real-time checks and recurring compliance reporting. 
Prompt text Build an SLA monitoring system for data pipeline delivery commitments.

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

Return: SLA definition table DDL, monitoring query, early warning logic, breach alert template, and weekly SLA report query. Copy prompt Open prompt details 
## Recommended Data Quality workflow 
1 
### Data Lineage Tracking 

Start with a focused prompt in Data Quality so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Data Quality Framework Chain 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Data Quality Test Suite 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Duplicate Detection at Scale 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
