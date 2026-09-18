# Data Quality Operations *AI Prompts *

3 DataOps Engineer prompts in Data Quality Operations. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts. 

## AI prompts in Data Quality Operations 
3 prompts Intermediate Single prompt 01 
### Anomaly Detection for Data Pipelines 

Implement automated anomaly detection for data metrics in this pipeline. Metrics to monitor: {{metrics}} (row counts, revenue, event counts, null rates) Historical data availabl... 
Prompt text Implement automated anomaly detection for data metrics in this pipeline.

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

Return: anomaly detection SQL, threshold calibration, seasonality handling, and alert routing rules. Copy prompt Open prompt details Intermediate Single prompt 02 
### Automated Data Quality Framework 

Build an automated data quality monitoring framework for this data platform. Technology stack: {{stack}} Data criticality tiers: {{tiers}} Alert channel: {{channel}} 1. DQ frame... 
Prompt text Build an automated data quality monitoring framework for this data platform.

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

Return: DQ framework architecture, tooling selection, DQ scoring implementation, and SLA by tier. Copy prompt Open prompt details Advanced Single prompt 03 
### Data Lineage Implementation 

Implement data lineage tracking for this data platform. Stack: {{stack}} Lineage granularity needed: {{granularity}} (table-level, column-level) Compliance driver: {{compliance}... 
Prompt text Implement data lineage tracking for this data platform.

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

Return: lineage collection architecture, OpenLineage configuration, dbt column lineage setup, and lineage use case examples. Copy prompt Open prompt details 
## Recommended Data Quality Operations workflow 
1 
### Anomaly Detection for Data Pipelines 

Start with a focused prompt in Data Quality Operations so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Automated Data Quality Framework 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Data Lineage Implementation 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
