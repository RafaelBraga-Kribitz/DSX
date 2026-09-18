# DataOps Engineer *AI Prompts *

DataOps Engineer AI prompt library with 16 prompts in 4 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 4 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse DataOps Engineer prompt categories 
4 categories 
### Pipeline Reliability 

AI prompts for pipeline reliability engineering including retry policy, idempotency, failure isolation, and operational resilience practices. 
5 prompts Data Pipeline Testing Strategy DataOps Principles and Practices → 
### CI/CD for Data 

AI prompts for CI/CD in data workflows, including automated tests, deployment gates, rollback strategy, and safe data pipeline releases. 
4 prompts Data Pipeline CI/CD DataOps Maturity Assessment → 
### Monitoring and Observability 

AI prompts for monitoring and observability, including metric design, alerting thresholds, incident detection, and root-cause diagnostics. 
4 prompts Cost Optimization for Data Pipelines Data Pipeline Monitoring → 
### Data Quality Operations 

AI prompts for operational data quality practices including SLA checks, anomaly alerts, incident triage, and remediation workflows. 
3 prompts Anomaly Detection for Data Pipelines Automated Data Quality Framework → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 16 Pipeline Reliability 5 CI/CD for Data 4 Monitoring and Observability 4 Data Quality Operations 3 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **16 **of 16 prompts 
## Pipeline Reliability 
5 prompt s Pipeline Reliability Intermediate Prompt 01 
### Data Pipeline Testing Strategy 
Design a comprehensive testing strategy for this data pipeline.

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

Return: test pyramid implementation for the stack, synthetic data strategy, regression testing approach, and contract test configuration. Copy prompt View page Show more ↓ Pipeline Reliability Beginner Prompt 02 
### DataOps Principles and Practices 
Apply DataOps principles to improve the reliability and speed of this data pipeline.

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

Return: maturity assessment, quick win roadmap, pipeline contract template, and feedback loop design. Copy prompt View page Show more ↓ Pipeline Reliability Intermediate Prompt 03 
### Idempotent Pipeline Design 
Design idempotent data pipelines that can be safely re-run without producing duplicate or incorrect data.

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

Return: idempotency technique for each storage target, backfill pattern, partition-based processing, and idempotency test design. Copy prompt View page Show more ↓ Pipeline Reliability Advanced Prompt 04 
### Pipeline Dependency Management 
Design a robust dependency management system for interconnected data pipelines.

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

Return: dependency wiring code, sensor configuration, data-aware scheduling setup, SLA handling policy, and dependency registry format. Copy prompt View page Show more ↓ Pipeline Reliability Advanced Prompt 05 
### Self-Healing Pipeline Patterns 
Design self-healing mechanisms for this data pipeline that automatically detect and recover from common failures.

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

Return: retry and backoff configuration, quality remediation rules, gap detection and backfill automation, stale data prevention, and fallback data strategy. Copy prompt View page Show more ↓ 
## CI/CD for Data 
4 prompt s CI/CD for Data Intermediate Prompt 01 
### Data Pipeline CI/CD 
Design a CI/CD pipeline for this data pipeline project.

Stack: {{stack}} (dbt, Airflow, Spark, Python)
Repository: {{repo}}
Environments: {{environments}} (dev, staging, prod)
Deployment frequency target: {{target}}

1. CI pipeline (every pull request):
 - Lint: flake8, black, sqlfluff (SQL style checker)
 - Unit tests: pytest → fail if any test fails
 - Schema validation: verify SQL models compile and the output schema is as expected
 - Data quality checks: run against a small synthetic dataset
 - Security scan: detect hardcoded credentials, sensitive data in code (Trufflehog, detect-secrets)
 - Documentation check: ensure every changed model has a description

2. Staging deployment (merge to main):
 - Deploy pipeline changes to the staging environment
 - Run integration tests against staging data (representative subset of production)
 - Comparison tests: compare output of new version vs current production version
 - Notify: Slack message to #data-deployments channel

3. Production deployment (manual approval or automatic):
 - High-criticality pipelines: require manual approval from a senior engineer
 - Low-criticality pipelines: auto-deploy after staging tests pass
 - Canary: route 5% of data through new pipeline version first (if architecture supports it)
 - Zero-downtime deployment: for Airflow, version DAG filenames; old version finishes, new version starts

4. Rollback strategy:
 - Tag every production deployment with a git tag
 - Rollback: deploy the previous tagged version
 - Data rollback: if the pipeline has already written bad data, run a compensation job to restore from the last known good state
 - Time to rollback SLA: < 15 minutes for Tier 1 pipelines

5. Environment configuration management:
 - Use environment variables or secrets managers (AWS Secrets Manager, GCP Secret Manager) for credentials
 - Never commit credentials to git
 - Configuration file per environment: config/dev.yml, config/prod.yml

Return: CI workflow YAML, staging and production deployment steps, rollback procedure, and credential management pattern. Copy prompt View page Show more ↓ CI/CD for Data Advanced Prompt 02 
### DataOps Maturity Assessment 
Conduct a DataOps maturity assessment for this data team and create an improvement roadmap.

Team: {{team_description}}
Current practices: {{current_practices}}
Pain points: {{pain_points}}
Goals: {{goals}}

1. Maturity dimensions to assess (score 1-5 each):

 Version control:
 1: No version control; SQL in spreadsheets / ad-hoc scripts
 3: All code in git; PRs required for changes
 5: All code, config, and DDL in git; automated linting and formatting

 Automated testing:
 1: No automated tests; manual QA before deployment
 3: Unit tests for transformations; basic schema tests
 5: Full test pyramid; contract tests; automated regression testing

 CI/CD:
 1: Manual deployments; no CI
 3: CI runs on PR; deployment is semi-automated with a manual step
 5: Fully automated CI/CD; canary deployments; automated rollback

 Monitoring and alerting:
 1: Consumers notice data issues before the data team
 3: Pipeline success/failure alerts; basic freshness monitoring
 5: Comprehensive quality monitoring; anomaly detection; SLA tracking per table

 Documentation:
 1: No documentation; knowledge in people's heads
 3: Key models documented in the catalog; ownership assigned
 5: All assets documented; auto-updated catalog; data contracts for all public data products

 Incident management:
 1: Ad-hoc response; no runbooks
 3: Runbooks for common failures; post-mortems for major incidents
 5: Automated incident detection; auto-remediation for known failure patterns; blameless post-mortems

2. Current state scoring:
 Score each dimension for the current team.
 Identify: the two lowest-scoring dimensions (highest improvement opportunity).

3. 90-day improvement roadmap:
 Based on the lowest scores, propose 3 high-impact initiatives for the next 90 days.
 Each initiative: title, current state, target state, actions, owner, success metric.

4. Quick wins (< 2 weeks each):
 Identify 3 changes that can be made immediately with high visibility impact.

Return: maturity scorecard for each dimension, gap analysis, 90-day roadmap, and quick wins. Copy prompt View page Show more ↓ CI/CD for Data Advanced Prompt 03 
### Environment Parity and Promotion 
Design a data environment strategy that ensures dev/staging/prod parity and safe change promotion.

Stack: {{stack}}
Environments needed: {{environments}}
Data sensitivity: {{sensitivity}}

1. Environment definitions:

 Development (dev):
 - Each engineer has their own isolated dev environment
 - Small subset of data (last 7 days, or synthetic)
 - Cheap: use small warehouse sizes, turn off when not in use
 - Schema prefix: dbt_{{user}}_ (e.g., dbt_john_orders)

 Staging / QA:
 - Shared environment for integration testing before production
 - A representative subset of production data (30-day snapshot, anonymized)
 - Must have the same schema as production — never drift
 - Updated weekly from a production snapshot

 Production:
 - Full data, full warehouse size
 - Changes only via the automated CD pipeline; no manual changes

2. Data anonymization for non-prod environments:
 - PII replacement: replace names with Faker-generated names, emails with test@example.com format
 - Consistent anonymization: use deterministic hashing so foreign key relationships are preserved
 - Automated: run an anonymization pipeline on the production snapshot before loading to staging

3. Promotion gates:
 Dev → Staging: PR approved, CI passes, documentation added
 Staging → Production: integration tests pass, regression comparison approved, no open critical incidents

4. Schema drift detection:
 - Run a schema comparison job daily: staging schema vs production schema
 - Alert if staging has columns or tables not in production (or vice versa)
 - Prevents surprises where staging tests pass but production breaks due to schema differences

5. Feature flags for data:
 - Allow a new pipeline feature to be deployed to production but not activated
 - Activation: update the feature flag (a database table or config) without redeploying code
 - Useful for: gradual rollouts, A/B testing pipeline versions

Return: environment configuration, anonymization pipeline, promotion gate checklist, drift detection, and feature flag implementation. Copy prompt View page Show more ↓ CI/CD for Data Intermediate Prompt 04 
### Schema Version Control 
Implement schema version control and migration management for this database.

Database: {{database}}
Migration tool: {{tool}} (Flyway, Liquibase, Alembic, sqitch, dbt contracts)
Change types: {{change_types}} (additive, destructive, data migrations)

1. Schema migration principles:
 - Every schema change is versioned and applied consistently across all environments
 - Changes are irreversible once applied to production; never modify a migration after it runs
 - All changes applied by an automated migration tool, never manually
 - Every migration has a corresponding rollback (or a documented reason why rollback is not possible)

2. Migration file structure (Flyway/Liquibase):
 V001__create_orders_table.sql
 V002__add_status_column.sql
 V003__add_customer_index.sql
 V004__backfill_status_values.sql

 Naming convention: V{version}__{description}.sql
 Version: timestamp or sequential integer

3. Safe migration patterns:
 Additive changes (safe, no downtime):
 - Add a new column (nullable or with a default)
 - Add an index CONCURRENTLY
 - Add a new table

 Destructive changes (require careful handling):
 - Remove a column: use the expand-contract pattern (2 deployments)
 - Rename a column: add new, migrate data, remove old (3 deployments)
 - Change a column type: depends on the type change; most require a rewrite

4. Data migration within schema migrations:
 - Keep DDL migrations separate from data migrations
 - Data migrations can be slow on large tables and may need to be run as separate batch jobs
 - Idempotent data migrations: check if the migration has already been applied before running

5. CI/CD integration:
 - Run migrations in CI against a test database: verify the migration applies cleanly
 - Staging: migrations run automatically on merge
 - Production: migrations run as part of the deployment pipeline; applied before new code is deployed

Return: migration file structure, naming conventions, safe vs destructive migration patterns, and CI/CD integration steps. Copy prompt View page Show more ↓ 
## Monitoring and Observability 
4 prompt s Monitoring and Observability Advanced Prompt 01 
### Cost Optimization for Data Pipelines 
Optimize the cost of running these data pipelines.

Pipelines: {{pipeline_list}}
Current monthly cost: {{cost}}
Primary cost drivers: {{drivers}} (compute, query scanning, storage, data transfer)

1. Identify cost drivers:
 - Compute: warehouse/cluster runtime (cloud DW idle time, Spark cluster cost)
 - Query scanning: BigQuery/Athena per-byte pricing
 - Storage: raw data accumulation, no lifecycle policies
 - Data transfer: cross-region or cross-cloud movements

2. Compute optimization:
 - Right-size clusters: monitor CPU and memory utilization; if < 40%, downsize
 - Auto-terminate idle clusters: Databricks clusters auto-terminate after 10 minutes of inactivity
 - Spot/preemptible instances: 70-90% cheaper for fault-tolerant batch jobs
 - Consolidate pipelines: running 10 pipelines per hour is more expensive than 1 pipeline that processes 10 jobs per run

3. Query scanning optimization:
 - Partition pruning: ensure queries include the partition key in WHERE clauses
 - Column pruning: avoid SELECT *; query only required columns
 - Cache: use result caching for repeated identical queries
 - Materialized views: pre-compute expensive aggregations that are queried frequently

4. Storage optimization:
 - Enforce lifecycle policies: delete staging and temp files after 7 days
 - Compress and convert: convert CSV raw files to Parquet (5-10x smaller)
 - Deduplicate: remove exact duplicate files in the landing zone
 - Tiered storage: move cold data to cheaper storage tiers after 90 days

5. Pipeline scheduling optimization:
 - Batch small jobs together: instead of running 20 single-table pipelines, run one multi-table job
 - Shift heavy jobs to off-peak hours (lower spot prices; avoids peak warehouse pricing)
 - Skip runs when source data has not changed (source freshness check before running)

Return: cost breakdown analysis, compute optimization plan, query scanning reduction, storage lifecycle configuration, and scheduling optimization. Copy prompt View page Show more ↓ Monitoring and Observability Intermediate Prompt 02 
### Data Pipeline Monitoring 
Set up comprehensive monitoring and alerting for this data pipeline.

Pipeline: {{pipeline}}
Orchestrator: {{orchestrator}}
Stakeholder SLA: {{sla}}
Alert channel: {{channel}} (Slack, PagerDuty, email)

1. Pipeline health metrics:
 - Success rate: % of pipeline runs that completed without errors (target > 99% for Tier 1)
 - Duration trend: track p50/p95 runtime per pipeline; alert on significant increase (>30% WoW)
 - Retry rate: high retries indicate a flaky upstream dependency
 - Queue wait time: for orchestrators with queuing, time before a task starts executing

2. Data freshness monitoring:
 - For each critical output table: monitor MAX(updated_at)
 - Alert: if MAX(updated_at) has not moved within 1.5× the expected refresh interval
 - Freshness check query:
 SELECT table_name,
 MAX(updated_at) AS last_update,
 CURRENT_TIMESTAMP - MAX(updated_at) AS lag
 FROM critical_tables
 GROUP BY 1
 HAVING lag > INTERVAL '4 hours';

3. Data quality monitoring:
 - Row count trend: compare today's row count to the 7-day rolling average
 Flag: > 20% deviation
 - Null rate: track % null per critical column over time
 Flag: null rate increases by > 5 percentage points
 - Duplicate rate: unique count / total count per primary key column
 Flag: duplicate rate > 0.01%

4. Alerting runbook per alert type:
 Pipeline failure alert:
 1. Check Airflow/orchestrator logs for the error
 2. Check upstream data source for freshness
 3. Retry the pipeline; if it fails again, escalate
 4. If blocked for > 30 minutes, post in #data-incidents and tag the on-call engineer

5. Alert suppression during maintenance:
 - Suppress alerts during planned maintenance windows
 - Declare maintenance in a shared runbook before starting
 - Auto-suppress: if the pipeline is manually paused, suppress freshness alerts

Return: metrics definition, freshness monitoring queries, quality monitoring setup, alerting rules, and runbook templates. Copy prompt View page Show more ↓ Monitoring and Observability Advanced Chain 03 
### Full DataOps Chain 
Step 1: Maturity assessment - score the current team on: version control, automated testing, CI/CD, monitoring, documentation, and incident management. Identify the two lowest-scoring dimensions and set 90-day improvement targets.
Step 2: Pipeline testing strategy - design the test pyramid for the stack. Implement unit tests for transformation logic. Configure dbt or Great Expectations for data quality tests. Create synthetic test data for integration tests.
Step 3: CI/CD pipeline - configure CI with linting, unit tests, smoke tests, and schema validation. Configure CD with environment promotion gates, staging integration tests, and automated production deployment with rollback capability.
Step 4: Monitoring and alerting - set up pipeline health metrics (success rate, duration trend, retry rate). Configure freshness monitoring per critical table. Implement row count anomaly detection with seasonality adjustment.
Step 5: Incident management - write a runbook for the top 5 most common failure modes. Set up Slack/PagerDuty alerting with escalation policies. Run the first blameless post-mortem simulation to build the muscle.
Step 6: Data quality framework - implement schema validation at ingestion, completeness/validity/consistency checks at each pipeline stage, and a DQ score dashboard by tier.
Step 7: Documentation and governance - register all production pipelines in the data catalog with owner, SLA, and lineage. Set up schema version control with Flyway or Liquibase. Establish the data contract registration process for all new data products. Copy prompt View page Show more ↓ Monitoring and Observability Advanced Prompt 04 
### Root Cause Analysis for Data Incidents 
Build a root cause analysis process for data incidents in this pipeline.

Incident: {{incident_description}}
Affected pipelines: {{affected}}
Business impact: {{impact}}

1. Incident response phases:

 Detection (0-5 minutes):
 - Automated alert fires → on-call engineer acknowledges
 - Declare incident in #data-incidents: title, affected systems, business impact
 - Start an incident timeline document

 Triage (5-30 minutes):
 - Is this affecting consumers right now? If yes: communicate status to stakeholders
 - What is the blast radius? List affected tables, dashboards, and downstream pipelines
 - Can we roll back to a known good state? If yes: initiate rollback while investigating

 Investigation (30 minutes - 2 hours):
 - Walk the pipeline backwards from the symptom to the root cause
 - Check: upstream data freshness, row counts at each stage, error logs at each step
 - Questions to answer:
 When did it start? (check pipeline history)
 What changed recently? (git log, deployment history)
 Is the source data valid? (check at the raw/bronze layer)

 Resolution:
 - Fix the root cause OR apply a workaround (data patch, pipeline re-run)
 - Verify: affected tables are fresh and quality checks pass
 - Close the incident; communicate resolution to stakeholders

2. Blameless post-mortem template:
 Incident summary:
 Timeline: (bullet points with timestamps)
 Root cause: (technical and process causes)
 Impact: (duration, affected users, business cost)
 What went well:
 What went poorly:
 Action items: (specific, assigned, time-bound)

3. Five whys for data incidents:
 Why were the dashboards stale? → The pipeline failed
 Why did the pipeline fail? → A source table had no new rows
 Why was the source table empty? → The upstream ETL job failed silently
 Why was the failure silent? → No alert was configured for that ETL job
 Why was no alert configured? → The pipeline was added without following the onboarding checklist
 Root cause: missing monitoring onboarding checklist item

4. Action item types:
 Detection: add monitoring to catch this class of failure earlier
 Prevention: add a test or validation that would have prevented this
 Response: update the runbook with the steps that resolved this incident

Return: incident response runbook, post-mortem template, five whys analysis, and action item tracking process. Copy prompt View page Show more ↓ 
## Data Quality Operations 
3 prompt s Data Quality Operations Intermediate Prompt 01 
### Anomaly Detection for Data Pipelines 
Implement automated anomaly detection for data metrics in this pipeline.

Metrics to monitor: {{metrics}} (row counts, revenue, event counts, null rates)
Historical data available: {{history}} (weeks of data)
False positive tolerance: {{tolerance}} (strict vs lenient)

1. Statistical anomaly detection approaches:

 Z-score (simple, works for normally distributed metrics):
 anomaly if |value - rolling_mean| / rolling_std > threshold
 threshold = 3 for strict (0.3% false positive), 2 for lenient (5% false positive)

 IQR-based (robust to outliers):
 Q1 = 25th percentile, Q3 = 75th percentile, IQR = Q3 - Q1
 anomaly if value < Q1 - 1.5 × IQR OR value > Q3 + 1.5 × IQR

 Percentage deviation from rolling average:
 anomaly if |value - rolling_avg_7d| / rolling_avg_7d > 0.3
 -- 30% deviation from the 7-day average
 Works well for business metrics with weekly seasonality

2. SQL implementation (row count anomaly detection):
 WITH daily_counts AS (
 SELECT DATE(created_at) AS d, COUNT(*) AS row_count
 FROM orders
 WHERE DATE(created_at) >= CURRENT_DATE - 30
 GROUP BY 1
 ),
 stats AS (
 SELECT d, row_count,
 AVG(row_count) OVER (ORDER BY d ROWS BETWEEN 6 PRECEDING AND 1 PRECEDING) AS avg_7d,
 STDDEV(row_count) OVER (ORDER BY d ROWS BETWEEN 6 PRECEDING AND 1 PRECEDING) AS std_7d
 FROM daily_counts
 )
 SELECT d, row_count, avg_7d,
 ABS(row_count - avg_7d) / NULLIF(std_7d, 0) AS z_score
 FROM stats
 WHERE ABS(row_count - avg_7d) / NULLIF(std_7d, 0) > 3;

3. Seasonality adjustment:
 - Day-of-week seasonality: compare to the same day of week in prior weeks
 - Holiday effects: create a holiday flag and exclude from the baseline
 - Elementary handles seasonality automatically using STL decomposition

4. Alert routing:
 - Z-score 2-3: warn in Slack; no action required unless confirmed by an analyst
 - Z-score > 3: alert to on-call; requires acknowledgment within 15 minutes
 - Consecutive anomalies (2+ days): escalate to a data incident

Return: anomaly detection SQL, threshold calibration, seasonality handling, and alert routing rules. Copy prompt View page Show more ↓ Data Quality Operations Intermediate Prompt 02 
### Automated Data Quality Framework 
Build an automated data quality monitoring framework for this data platform.

Technology stack: {{stack}}
Data criticality tiers: {{tiers}}
Alert channel: {{channel}}

1. DQ framework layers:

 Schema validation (at ingestion):
 - Verify column names, data types, and required columns match the expected schema
 - Fail-fast: reject malformed files before they corrupt downstream tables
 - Tool: Pydantic for Python pipelines, INFORMATION_SCHEMA checks, dbt source tests

 Completeness checks:
 - Row count: is the expected number of rows present?
 - Non-null rate: critical columns must be non-null
 - Coverage: all expected partitions present (no missing dates)

 Validity checks:
 - Range checks: values within expected bounds
 - Format checks: date formats, email regex, ID patterns
 - Referential integrity: foreign keys have matching primary keys

 Consistency checks:
 - Cross-table: revenue in the fact table matches sum of line items
 - Cross-period: today's metric is consistent with yesterday's (no >50% jump without explanation)
 - Aggregate invariants: sum(refunds) <= sum(gross_revenue) for any period

2. Tooling:
 - dbt tests: schema.yml tests (generic) + custom singular tests (business rules)
 - Great Expectations: Python-based; define expectations as code; integrates with Airflow
 - Soda Core: YAML-based quality checks; cloud platform for centralized results
 - Elementary: dbt-native anomaly detection; sends Slack alerts with dbt lineage context

3. DQ scoring:
 Compute a DQ score per table: (tests passing / total tests) × 100%
 Publish scores in the data catalog and on a DQ dashboard
 Alert: if any Tier 1 table drops below 95% DQ score

4. DQ SLA by tier:
 Tier 1 (executive-facing): 100% DQ tests must pass; alert immediately on failure
 Tier 2 (operational): 95% tests must pass; daily review of failures
 Tier 3 (exploratory): best effort; weekly DQ report

Return: DQ framework architecture, tooling selection, DQ scoring implementation, and SLA by tier. Copy prompt View page Show more ↓ Data Quality Operations Advanced Prompt 03 
### Data Lineage Implementation 
Implement data lineage tracking for this data platform.

Stack: {{stack}}
Lineage granularity needed: {{granularity}} (table-level, column-level)
Compliance driver: {{compliance}} (GDPR data subject access, SOX auditability, debugging)

1. Why data lineage:
 - Debugging: trace a data quality issue from symptom to root cause
 - Impact analysis: understand which downstream tables are affected before making a change
 - Compliance: demonstrate to auditors where sensitive data originates and how it flows
 - Trust: data consumers know where the data came from and can assess its reliability

2. Lineage collection methods:

 SQL parsing (static):
 - Parse SQL transformations to extract table-level dependencies
 - dbt: automatically builds column-level lineage from SQL ref() and source() calls
 - Limitation: cannot capture runtime/dynamic SQL lineage

 Runtime instrumentation (dynamic):
 - Instrument Spark jobs to emit OpenLineage events
 - OpenLineage: open standard for lineage events; Spark integration via openlineage-spark
 - Collect events in Marquez (open-source) or DataHub

3. OpenLineage with Airflow:
 Install: pip install openlineage-airflow
 Configure: AIRFLOW__OPENLINEAGE__TRANSPORT = '{"type": "http", "url": "http://marquez:5000"}'
 Automatically emits: job start/end, input datasets, output datasets, run metadata

4. Column-level lineage (via dbt):
 - dbt automatically traces column references through SQL
 - Elementary: exposes column-level lineage via dbt artifacts
 - Enable: generate_column_lineage: true in dbt_project.yml (dbt 1.6+)

5. Lineage graph use cases:
 - 'What does this PII column feed into?' → identify all tables containing derived PII
 - 'If I drop this column from orders, what breaks?' → find all downstream references
 - 'Where did this null value come from?' → walk the lineage backwards from the symptom

Return: lineage collection architecture, OpenLineage configuration, dbt column lineage setup, and lineage use case examples. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
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
