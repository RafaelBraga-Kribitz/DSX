# Pipeline Reliability *AI Prompts *

5 DataOps Engineer prompts in Pipeline Reliability. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 5 single prompts. 

## AI prompts in Pipeline Reliability 
5 prompts Intermediate Single prompt 01 
### Data Pipeline Testing Strategy 

Design a comprehensive testing strategy for this data pipeline. Pipeline: {{pipeline_description}} Technology stack: {{stack}} Data volume: {{volume}} 1. Test pyramid for data p... 
Prompt text Design a comprehensive testing strategy for this data pipeline.

Pipeline: {{pipeline_description}}
Technology stack: {{stack}}
Data volume: {{volume}}

1. Test pyramid for data pipelines:

 Unit tests (many, fast):
 - Test individual transformation functions, SQL logic, and business rules
 - Use: pytest for Python, dbt tests for SQL models
 - Sample data: create small, synthetic datasets covering edge cases
 - Run in: local development and CI (< 2 minutes)

 Integration tests (some, medium speed):
 - Test the full pipeline end-to-end on a representative data sample
 - Verify: input → transform → output produces expected results
 - Use: a dedicated test environment with a small copy of production data
 - Run in: CI on PR (< 10 minutes)

 Data quality tests (automated, production):
 - Run continuously on production data
 - Test: row counts, null rates, uniqueness, referential integrity, distribution ranges
 - Alert on failure; do not block deployment but create an incident

2. Test data management:
 - Golden dataset: a curated set of inputs with verified expected outputs
 - Synthetic data generation: use Faker or Mimesis to generate realistic test data
 - Production data snapshot: an anonymized subset of production data for integration tests
 - Data versioning: version the test datasets alongside the pipeline code

3. Regression testing:
 - After any change: compare output of new version vs old version on the same input
 - Row count comparison: new_count / old_count should be between 0.95 and 1.05
 - Key metric comparison: sum of revenue, count of distinct customers should match ± 1%
 - Schema comparison: no columns added, removed, or type-changed without a version bump

4. Contract testing:
 - Verify: the pipeline's output matches the consumer's expected schema and quality requirements
 - Run at deployment time: if the contract is violated, block the deployment

Return: test pyramid implementation for the stack, synthetic data strategy, regression testing approach, and contract test configuration. Copy prompt Open prompt details Beginner Single prompt 02 
### DataOps Principles and Practices 

Apply DataOps principles to improve the reliability and speed of this data pipeline. Current pipeline: {{pipeline_description}} Pain points: {{pain_points}} (long release cycles... 
Prompt text Apply DataOps principles to improve the reliability and speed of this data pipeline.

Current pipeline: {{pipeline_description}}
Pain points: {{pain_points}} (long release cycles, data quality issues, slow debugging, etc.)
Team: {{team}}

1. DataOps core principles:
 - Automated testing: every data transformation is tested before it reaches production
 - Continuous delivery: pipeline changes deploy frequently with automated validation
 - Monitoring: every pipeline has health metrics and alerts
 - Version control: all pipeline code, configurations, and SQL are in git
 - Collaboration: data engineers and data consumers work together in the feedback loop

2. DataOps maturity model:
 Level 1 (manual): ad-hoc pipelines, no tests, deployments are manual and infrequent
 Level 2 (repeatable): pipelines in version control, some tests, scheduled deployments
 Level 3 (defined): automated CI/CD, comprehensive tests, monitoring with alerting
 Level 4 (managed): data contracts, SLA tracking, automated anomaly detection
 Level 5 (optimizing): self-healing pipelines, automated root cause analysis

3. Quick wins (Level 1 → Level 3 in 4 weeks):
 Week 1: Move all pipeline code to git; add README.md for each pipeline
 Week 2: Add smoke tests and schema validation to CI
 Week 3: Set up monitoring (freshness alerts, row count tracking)
 Week 4: Automate deployment; require PR reviews before merging

4. Pipeline contract:
 Every pipeline should define and publish:
 - Input schema and freshness SLA
 - Output schema and freshness SLA
 - Owner and on-call rotation
 - Known failure modes and recovery procedure

5. Feedback loops:
 - Development feedback: tests run in < 10 minutes in CI
 - Production feedback: monitoring alerts within 15 minutes of a failure
 - Consumer feedback: data quality issues reported via a defined channel

Return: maturity assessment, quick win roadmap, pipeline contract template, and feedback loop design. Copy prompt Open prompt details Intermediate Single prompt 03 
### Idempotent Pipeline Design 

Design idempotent data pipelines that can be safely re-run without producing duplicate or incorrect data. Pipeline type: {{pipeline_type}} (ELT, streaming, batch scoring) Storag... 
Prompt text Design idempotent data pipelines that can be safely re-run without producing duplicate or incorrect data.

Pipeline type: {{pipeline_type}} (ELT, streaming, batch scoring)
Storage target: {{target}} (database table, S3, data warehouse)
Re-run scenarios: {{scenarios}} (duplicate events, partial failure, backfill)

1. Idempotency definition:
 A pipeline is idempotent if running it multiple times with the same input produces the same output as running it once.
 All production pipelines should be idempotent to allow safe retries and backfills.

2. Techniques for idempotency:

 UPSERT (INSERT OR UPDATE):
 - Use MERGE or ON CONFLICT for database targets
 - Requires a unique key per record
 - Safe to run multiple times: existing rows are updated, new rows are inserted

 Delete + reinsert for partitioned tables:
 - Delete all rows for the partition being processed, then re-insert
 - DELETE FROM orders WHERE date = '2024-01-15'; followed by INSERT
 - Atomic if done in a single transaction

 Deduplication after load:
 - Load all records including duplicates into a staging table
 - Final table: SELECT DISTINCT ON (primary_key) ... ORDER BY updated_at DESC

 S3 key naming for idempotency:
 - Use deterministic paths: s3://bucket/year=2024/month=01/day=15/run_id=20240115T120000Z/
 - Overwriting the same S3 key produces a deterministic result
 - Avoid: appending to existing files (non-idempotent)

3. Partitioned backfill:
 - Process one time partition per pipeline run
 - Parameter: execution_date → determines which partition to process
 - Backfill: run the pipeline for each historical date partition
 - Airflow: dbt run --vars '{"execution_date": "2024-01-15"}'

4. Testing idempotency:
 - Run the pipeline twice for the same input date
 - Verify: row count is the same after the second run
 - Verify: no duplicate rows in the output (run unique test on primary key)

Return: idempotency technique for each storage target, backfill pattern, partition-based processing, and idempotency test design. Copy prompt Open prompt details Advanced Single prompt 04 
### Pipeline Dependency Management 

Design a robust dependency management system for interconnected data pipelines. Pipelines: {{pipeline_list}} Dependency graph: {{dependencies}} (which pipelines consume outputs... 
Prompt text Design a robust dependency management system for interconnected data pipelines.

Pipelines: {{pipeline_list}}
Dependency graph: {{dependencies}} (which pipelines consume outputs of others)
Orchestrator: {{orchestrator}}

1. Dependency types:
 - Direct data dependency: pipeline B reads from a table written by pipeline A → A must complete before B
 - Time dependency: pipeline B runs after pipeline A completes on the same execution date
 - External dependency: pipeline B requires a file to arrive in S3 from an external system

2. Airflow dependency patterns:

 Within a DAG:
 extract_task >> transform_task >> load_task

 Across DAGs (ExternalTaskSensor):
 ExternalTaskSensor(
 task_id='wait_for_upstream',
 external_dag_id='upstream_pipeline',
 external_task_id='final_task',
 timeout=7200, # 2 hours max wait
 poke_interval=60
 )

 Data-aware scheduling (Airflow 2.4+):
 @dag(schedule=[Dataset('s3://bucket/orders/latest')])
 def downstream_pipeline():
 ...
 # Triggers when the upstream pipeline updates the dataset

3. External file arrival:
 S3KeySensor(
 task_id='wait_for_file',
 bucket_name='uploads',
 bucket_key='daily_report_{{ ds }}.csv',
 timeout=3600
 )

4. SLA-aware dependencies:
 - If upstream is late: should downstream wait or run with available data?
 - Decision: for time-critical downstream (exec dashboard): wait up to 2 hours then alert
 - Decision: for non-critical downstream: run with available data; log a warning

5. Dependency documentation:
 - Maintain a dependency registry: each pipeline lists its upstream and downstream dependencies
 - Visualize with Airflow's DAG graph view or a data lineage tool (DataHub, Atlan)
 - Impact analysis: before changing any pipeline, check: 'which downstream pipelines depend on this output?'

Return: dependency wiring code, sensor configuration, data-aware scheduling setup, SLA handling policy, and dependency registry format. Copy prompt Open prompt details Advanced Single prompt 05 
### Self-Healing Pipeline Patterns 

Design self-healing mechanisms for this data pipeline that automatically detect and recover from common failures. Pipeline: {{pipeline}} Common failure modes: {{failure_modes}}... 
Prompt text Design self-healing mechanisms for this data pipeline that automatically detect and recover from common failures.

Pipeline: {{pipeline}}
Common failure modes: {{failure_modes}}
Recovery SLA: {{recovery_sla}}

1. Automatic retry with backoff:
 - Retry transient failures: network timeouts, API rate limits, temporary resource unavailability
 - Exponential backoff: 1s → 2s → 4s → 8s (max 3 retries)
 - Circuit breaker: after 3 consecutive failures, stop retrying and alert humans
 - Idempotent design: retries require idempotent operations (UPSERT, not INSERT)

2. Automatic data quality remediation:
 - If a source file has schema drift: route to a quarantine path; send an alert; process the rest
 - If row count is 0 (source empty): skip the run; do not overwrite the target with empty data
 - If a critical DQ test fails: pause downstream pipelines; alert; wait for human sign-off

3. Backfill automation:
 - Detect gaps: query the output table for missing date partitions
 - Auto-trigger backfill: if a gap is detected, automatically trigger a backfill run for the missing partition
 - Airflow implementation: a 'gap detection' DAG runs daily; if gaps found, it triggers the backfill DAG

4. Stale data prevention:
 - Before overwriting a table with a new run, compare: does the new data have >= the expected row count?
 - If new data is suspiciously small (< 50% of yesterday): abort the write; alert

5. Fallback data:
 - For non-critical data: if the fresh run fails, serve the last known good data with a staleness warning
 - Maintain a 'last_successful_run' timestamp per table for staleness calculations
 - Never serve data older than {{max_staleness}} without an explicit staleness flag for consumers

Return: retry and backoff configuration, quality remediation rules, gap detection and backfill automation, stale data prevention, and fallback data strategy. Copy prompt Open prompt details 
## Recommended Pipeline Reliability workflow 
1 
### Data Pipeline Testing Strategy 

Start with a focused prompt in Pipeline Reliability so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### DataOps Principles and Practices 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Idempotent Pipeline Design 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Pipeline Dependency Management 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
