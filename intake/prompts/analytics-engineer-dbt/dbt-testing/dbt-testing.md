# dbt Testing *AI Prompts *

3 Analytics Engineer (dbt) prompts in dbt Testing. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 3 single prompts. 

## AI prompts in dbt Testing 
3 prompts Intermediate Single prompt 01 
### dbt Data Freshness and Monitoring 

Configure source freshness monitoring and anomaly detection for this dbt project. Sources: {{sources}} SLA requirements: {{sla}} (e.g. dashboard data must be < 4 hours old) Aler... 
Prompt text Configure source freshness monitoring and anomaly detection for this dbt project.

Sources: {{sources}}
SLA requirements: {{sla}} (e.g. dashboard data must be < 4 hours old)
Alert channel: {{alerts}} (Slack, PagerDuty, email)

1. Source freshness config in sources.yml:
 sources:
 - name: stripe
 database: raw
 schema: stripe
 loaded_at_field: _fivetran_synced
 freshness:
 warn_after: {count: 6, period: hour}
 error_after: {count: 24, period: hour}
 tables:
 - name: charges
 freshness:
 warn_after: {count: 2, period: hour}
 error_after: {count: 6, period: hour}

2. Run freshness checks:
 dbt source freshness
 - Queries each source table for the MAX of the loaded_at_field
 - Reports: pass / warn / error per source table
 - Integrate into CI: fail the pipeline if any source is in error state

3. Model-level recency test (dbt-utils):
 - name: recency
 config:
 severity: warn
 meta:
 description: 'Orders table should have records from today'
 tests:
 - dbt_utils.recency:
 datepart: hour
 field: created_at
 interval: 6

4. Row count anomaly detection:
 - dbt-expectations: expect_table_row_count_to_be_between
 min_value: 1000
 max_value: 500000
 - Or: custom singular test comparing today's row count to 7-day rolling average
 SELECT ABS(today_count - avg_7d) / avg_7d AS pct_deviation
 FROM daily_counts
 WHERE pct_deviation > 0.3

5. Elementary (open-source dbt monitoring):
 - Installs as a dbt package
 - Monitors: row count anomalies, null rate, uniqueness, distribution shifts
 - Sends Slack alerts with anomaly details and a link to the affected model
 - config: elementary_timeframe_days: 30, anomaly_sensitivity: 3

6. Alerting integration:
 - On dbt Cloud: set up job notifications to Slack on failure
 - Custom: parse dbt run results JSON and post to Slack webhook
 artifacts/run_results.json → filter status == 'error' → Slack message

Return: sources.yml freshness config, recency test configuration, row count anomaly detection SQL, Elementary setup, and alerting integration. Copy prompt Open prompt details Beginner Single prompt 02 
### dbt Test Coverage Plan 

Design a comprehensive dbt test suite for this model or project. Model: {{model_name}} Grain: {{grain}} (one row per order, one row per customer per day, etc.) Key columns: {{ke... 
Prompt text Design a comprehensive dbt test suite for this model or project.

Model: {{model_name}}
Grain: {{grain}} (one row per order, one row per customer per day, etc.)
Key columns: {{key_columns}}
Business rules: {{business_rules}}

1. Generic tests (schema.yml):

 Every model must have at minimum:
 - unique: on the primary key or unique identifier
 - not_null: on all columns that must never be null (primary keys, critical FKs, metric numerators)

 Additional recommended generics:
 - accepted_values: on status, type, or enum columns
 values: ['pending', 'completed', 'refunded']
 - relationships: foreign key integrity check
 to: ref('dim_customers'), field: customer_id

2. Singular tests (tests/ folder):
 Write SQL assertions that return 0 rows when the test passes.

 Row count validation:
 -- Test: fct_orders should never have more rows than the source
 SELECT COUNT(*) > (SELECT COUNT(*) FROM {{ source('app', 'orders') }}) AS has_more_rows_than_source
 WHERE has_more_rows_than_source

 Metric range check:
 -- Test: order_amount should be positive
 SELECT * FROM {{ ref('fct_orders') }}
 WHERE order_amount <= 0

 Referential integrity:
 SELECT o.customer_id
 FROM {{ ref('fct_orders') }} o
 LEFT JOIN {{ ref('dim_customers') }} c ON o.customer_id = c.customer_id
 WHERE c.customer_id IS NULL

3. dbt-utils tests:
 - expression_is_true: assert a SQL expression is true for all rows
 - recency: warn if the most recent record is older than N hours
 - equal_rowcount: two models have the same row count
 - mutually_exclusive_ranges: non-overlapping date ranges (for SCDs)

4. Severity and alert routing:
 - warn: flag anomalies without blocking CI (non-critical quality issues)
 - error: block CI and deployment (data integrity failures)
 - config error_if: '>0', warn_if: '>100'

5. Test organization by layer:
 - Staging: focus on not_null, unique, accepted_values on raw source columns
 - Marts: focus on business rule tests, metric range checks, referential integrity

Return: schema.yml test block for the model, singular test SQLs for critical business rules, dbt-utils test recommendations, and severity assignments. Copy prompt Open prompt details Advanced Single prompt 03 
### dbt-expectations Test Suite 

Implement advanced data quality tests using the dbt-expectations package. Model: {{model_name}} Quality requirements: {{requirements}} (SLA, business rules, statistical threshol... 
Prompt text Implement advanced data quality tests using the dbt-expectations package.

Model: {{model_name}}
Quality requirements: {{requirements}} (SLA, business rules, statistical thresholds)

1. Install dbt-expectations:
 packages.yml:
 packages:
 - package: calogica/dbt_expectations
 version: [">=0.10.0", "<0.11.0"]

2. Column value tests:

 Numeric range:
 - dbt_expectations.expect_column_values_to_be_between:
 min_value: 0
 max_value: 1000000
 strictly: false

 Non-negative:
 - dbt_expectations.expect_column_values_to_be_positive:
 severity: error

 String pattern (regex):
 - dbt_expectations.expect_column_values_to_match_regex:
 regex: '^[A-Z]{2}-[0-9]{6}$'

 Date range:
 - dbt_expectations.expect_column_values_to_be_of_type:
 column_type: date

3. Table-level tests:

 Row count bounds:
 - dbt_expectations.expect_table_row_count_to_be_between:
 min_value: 1000
 max_value: 10000000

 Column count:
 - dbt_expectations.expect_table_column_count_to_equal:
 value: 15

 Schema completeness:
 - dbt_expectations.expect_table_columns_to_contain_set:
 column_list: ['order_id', 'customer_id', 'order_amount_usd', 'order_date']

4. Distribution tests:

 Proportion of null values:
 - dbt_expectations.expect_column_proportion_of_unique_values_to_be_between:
 min_value: 0.95
 max_value: 1.0

 Mean value range (catches data quality regressions):
 - dbt_expectations.expect_column_mean_to_be_between:
 min_value: 50
 max_value: 500

5. Cross-column tests:
 - dbt_expectations.expect_column_pair_values_A_to_be_greater_than_B:
 column_A: total_amount
 column_B: discount_amount
 or_equal: true

Return: complete schema.yml with dbt-expectations tests, severity assignments, and interpretation of each test's business meaning. Copy prompt Open prompt details 
## Recommended dbt Testing workflow 
1 
### dbt Data Freshness and Monitoring 

Start with a focused prompt in dbt Testing so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### dbt Test Coverage Plan 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### dbt-expectations Test Suite 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
