# dbt Advanced Patterns *AI Prompts *

6 Analytics Engineer (dbt) prompts in dbt Advanced Patterns. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 5 single prompts · 1 chain. 

## AI prompts in dbt Advanced Patterns 
6 prompts Advanced Single prompt 01 
### dbt CI/CD Pipeline 

Design a CI/CD pipeline for this dbt project. Repository: {{repo}} (GitHub, GitLab, Bitbucket) Warehouse: {{warehouse}} Platform: {{platform}} (dbt Cloud, dbt Core + Airflow, Pr... 
Prompt text Design a CI/CD pipeline for this dbt project.

Repository: {{repo}} (GitHub, GitLab, Bitbucket)
Warehouse: {{warehouse}}
Platform: {{platform}} (dbt Cloud, dbt Core + Airflow, Prefect, etc.)
Team size: {{team_size}}

1. Branch strategy:
 - main / production: deploys to production schema
 - dev branches: each engineer works in a personal dev schema (schema: dbt_{{ env_var('DBT_USER') }})
 - PR → staging → main merge

2. CI checks on every PR:

 Step 1: dbt compile
 - Verifies all SQL is syntactically valid and all ref() / source() targets exist
 - Catches: typos, broken references, missing macros

 Step 2: dbt build --select state:modified+
 - Runs only modified models and their downstream dependents
 - Compares against the last production manifest (state artifacts)
 - Much faster than running the full project

 Step 3: dbt test --select state:modified+
 - Runs all tests on the affected models
 - Fail CI if any test with severity: error fails

 Step 4: dbt source freshness
 - Verify all source tables are fresh before running

3. GitHub Actions workflow:
 name: dbt CI
 on: [pull_request]
 jobs:
 dbt-ci:
 runs-on: ubuntu-latest
 steps:
 - uses: actions/checkout@v4
 - name: Install dbt
 run: pip install dbt-snowflake
 - name: dbt compile
 run: dbt compile --profiles-dir .
 - name: dbt build (modified)
 run: dbt build --select state:modified+ --defer --state ./prod-artifacts

4. Production deployment:
 - Trigger: merge to main
 - Run: dbt build (full project or slim CI against state)
 - On failure: alert Slack, block further deployments until resolved
 - Artifact storage: upload manifest.json to S3 or dbt Cloud after each successful run

5. dbt Cloud setup:
 - Dev environment: each user gets their own target schema
 - CI job: triggered on PR, runs slim CI
 - Production job: scheduled daily, full run with freshness checks
 - Notifications: Slack on job failure

Return: branch strategy, CI workflow YAML, production deployment steps, and dbt Cloud job configuration. Copy prompt Open prompt details Advanced Single prompt 02 
### dbt for Machine Learning Features 

Use dbt to build and manage ML feature tables for training and serving. ML use case: {{use_case}} (e.g. churn prediction, recommendation, fraud detection) Features needed: {{fea... 
Prompt text Use dbt to build and manage ML feature tables for training and serving.

ML use case: {{use_case}} (e.g. churn prediction, recommendation, fraud detection)
Features needed: {{features}}
Downstream ML platform: {{platform}} (SageMaker, Vertex AI, Feature Store, custom)

1. Why dbt for ML features:
 - Features computed in the warehouse are reproducible, testable, and versioned
 - dbt tests catch feature drift before it reaches the model
 - Same feature definitions for training AND serving (no training-serving skew)
 - Feature history available via incremental models or snapshots

2. Feature table design:
 Each feature table has:
 - entity_id: the prediction target (customer_id, user_id, etc.)
 - feature_date: the date the feature was computed (for point-in-time correctness)
 - One column per feature

 Example: fct_customer_features_daily
 customer_id | feature_date | days_since_last_purchase | order_count_30d | avg_order_value_90d

3. Point-in-time correct features:
 For training: join features to labels using the feature_date <= label_date condition
 SELECT
 l.customer_id,
 l.churned_flag,
 f.days_since_last_purchase,
 f.order_count_30d
 FROM {{ ref('training_labels') }} l
 LEFT JOIN {{ ref('fct_customer_features_daily') }} f
 ON l.customer_id = f.customer_id
 AND f.feature_date = l.label_date

4. Feature tests for ML:
 - No future leakage: verify feature_date is always <= the observation date
 - No nulls in required features: all input features must be non-null
 - Reasonable ranges: order_count_30d between 0 and 1000
 - Stability: feature distribution should not shift dramatically week-over-week

5. Export to ML platform:
 Option A: Export from warehouse to S3/GCS as Parquet for batch training
 Option B: Connect dbt-generated tables directly to a feature store (Feast, Tecton)
 Option C: Use dbt Cloud job to trigger a downstream Python training pipeline on completion

Return: feature table schema, point-in-time join pattern, ML-specific tests, and export strategy. Copy prompt Open prompt details Intermediate Single prompt 03 
### dbt Macros and Reusability 

Write reusable dbt macros for common transformation patterns in this project. Repetitive patterns identified: {{patterns}} (e.g. currency conversion, fiscal calendar, event dedu... 
Prompt text Write reusable dbt macros for common transformation patterns in this project.

Repetitive patterns identified: {{patterns}} (e.g. currency conversion, fiscal calendar, event deduplication)
Warehouse: {{warehouse}}

1. Basic macro structure:
 {% macro cents_to_dollars(column_name, precision=2) %}
 ROUND({{ column_name }} / 100.0, {{ precision }})
 {% endmacro %}

 Usage in a model:
 SELECT {{ cents_to_dollars('amount_cents') }} AS amount_dollars

2. Deduplication macro (common pattern):
 {% macro deduplicate(relation, partition_by, order_by) %}
 SELECT *
 FROM (
 SELECT
 *,
 ROW_NUMBER() OVER (
 PARTITION BY {{ partition_by }}
 ORDER BY {{ order_by }} DESC
 ) AS _row_number
 FROM {{ relation }}
 )
 WHERE _row_number = 1
 {% endmacro %}

 Usage:
 {{ deduplicate(ref('stg_orders'), 'order_id', 'updated_at') }}

3. Date spine macro (dbt-utils built-in):
 {{ dbt_utils.date_spine(
 datepart='day',
 start_date=cast('2020-01-01' as date),
 end_date=cast(now() as date)
 ) }}

4. Generate surrogate key:
 {{ dbt_utils.generate_surrogate_key(['order_id', 'line_item_id']) }}
 - MD5 hash of concatenated key columns
 - Use as primary key for fact tables without a natural unique key

5. Star schema helper macros:
 - Union multiple tables of the same schema:
 {{ dbt_utils.union_relations(relations=[ref('orders_us'), ref('orders_eu')]) }}

 - Pivot rows to columns:
 {{ dbt_utils.pivot('metric_name', ['revenue', 'cost', 'profit'], agg='SUM', then_value='metric_value') }}

6. Macro testing:
 - Write a simple model that uses the macro and add generic tests on its output
 - Add a CI step: dbt compile → verify compiled SQL for macros is correct

Return: macro implementations for the identified patterns, usage examples, and testing approach. Copy prompt Open prompt details Advanced Single prompt 04 
### dbt Metrics Layer 

Define and govern business metrics using dbt's semantic layer. Metrics to define: {{metrics}} (e.g. monthly_recurring_revenue, customer_acquisition_cost, churn_rate) Metric owne... 
Prompt text Define and govern business metrics using dbt's semantic layer.

Metrics to define: {{metrics}} (e.g. monthly_recurring_revenue, customer_acquisition_cost, churn_rate)
Metric owners: {{owners}}
BI tool: {{bi_tool}} (Tableau, Looker, Metabase, etc.)

1. dbt Semantic Layer overview:
 - Defines metrics in YAML with consistent business logic
 - Metrics are computed at query time, not stored
 - Downstream BI tools query metrics via the semantic layer API → same definition everywhere
 - Eliminates the 'metric disagreement' problem between teams

2. Semantic model definition:
 semantic_models:
 - name: orders
 description: Orders fact table at order grain
 model: ref('fct_orders')
 entities:
 - name: order
 type: primary
 expr: order_id
 - name: customer
 type: foreign
 expr: customer_id
 dimensions:
 - name: order_date
 type: time
 type_params:
 time_granularity: day
 - name: order_status
 type: categorical
 measures:
 - name: order_amount
 agg: sum
 expr: order_amount_usd
 - name: order_count
 agg: count_distinct
 expr: order_id

3. Metric definition:
 metrics:
 - name: revenue
 label: 'Total Revenue'
 description: Sum of all completed order amounts in USD
 type: simple
 type_params:
 measure: order_amount
 filter: "{{ Dimension('order__order_status') }} = 'completed'"

 - name: revenue_growth_mom
 label: 'Revenue MoM Growth'
 type: derived
 type_params:
 expr: (revenue - lag_revenue) / lag_revenue
 metrics:
 - name: revenue
 - name: revenue
 offset_window: 1 month
 alias: lag_revenue

4. Querying via MetricFlow:
 mf query --metrics revenue --group-by order__order_date__month
 mf query --metrics revenue,order_count --group-by order__order_status

5. Governance:
 - Every metric must have: description, label, owner (in meta), and at least one test
 - Review process: metric changes require PR approval from the data team lead
 - Changelog: document when a metric definition changes and notify BI tool owners

Return: semantic model YAML, metric definitions, MetricFlow query examples, and governance process. Copy prompt Open prompt details Intermediate Single prompt 05 
### dbt Packages and Ecosystem 

Select and configure the right dbt packages for this project's needs. Project requirements: {{requirements}} Warehouse: {{warehouse}} 1. Essential packages for every project: db... 
Prompt text Select and configure the right dbt packages for this project's needs.

Project requirements: {{requirements}}
Warehouse: {{warehouse}}

1. Essential packages for every project:

 dbt-utils:
 - Macros: generate_surrogate_key, union_relations, date_spine, pivot, unpivot
 - Tests: expression_is_true, recency, equal_rowcount
 - Install: calogica/dbt_utils >= 1.0.0

 dbt-expectations:
 - Port of Great Expectations for dbt
 - Tests: row count bounds, column value ranges, regex patterns, distribution checks

 Elementary:
 - Data observability and anomaly detection
 - Monitors: row count, null rates, freshness, distribution shifts
 - Sends Slack alerts; generates a data observability dashboard

2. Warehouse-specific packages:

 dbt-date (date utilities):
 - Fiscal calendars, date spine helpers, timezone conversions
 - Works across all warehouses

 dbt-audit-helper:
 - Compare two versions of a model to validate changes
 - compare_queries macro: finds rows in A not in B and vice versa
 - compare_column_values: per-column comparison statistics

3. Domain-specific packages:

 dbt-mrr (subscription metrics):
 - MRR, churn, expansion, contraction calculations from subscription data

 dbt-feature-store:
 - Generates ML feature tables from dbt models

4. Package configuration (packages.yml):
 packages:
 - package: dbt-labs/dbt_utils
 version: [">=1.1.0", "<2.0.0"]
 - package: calogica/dbt_expectations
 version: [">=0.10.0", "<0.11.0"]
 - package: elementary-data/elementary
 version: [">=0.13.0", "<0.14.0"]

5. Package governance:
 - Pin minor version ranges (not just major) to avoid unexpected breaking changes
 - Review changelog before upgrading any package
 - Run dbt build after package upgrades to verify no regressions

Return: recommended package set for the project requirements, packages.yml configuration, and upgrade governance policy. Copy prompt Open prompt details Advanced Chain 06 
### Full dbt Project Build Chain 

Step 1: Source assessment - catalog all source tables from the raw schema. For each source: document the schema, identify the primary key, assess data quality issues, and config... 
Prompt text Step 1: Source assessment - catalog all source tables from the raw schema. For each source: document the schema, identify the primary key, assess data quality issues, and configure source freshness checks in sources.yml.
Step 2: Staging layer - build one staging model per source table. Apply: rename columns to snake_case, explicit type casts, null handling for empty strings, and source metadata columns. Add not_null and unique tests on primary keys.
Step 3: Intermediate layer - identify shared transformation logic needed by multiple marts. Build intermediate models for: entity resolution, sessionization, or complex joins. Document each intermediate model's grain and purpose.
Step 4: Mart layer - design the dimensional schema for the target analytics use case. Define the grain. Build fct_* and dim_* models with appropriate materializations. Add relationships tests for all foreign keys and business rule tests for critical logic.
Step 5: Metrics layer - define dbt semantic layer metrics for key business KPIs. Ensure each metric has a description, owner, and test. Validate MetricFlow queries return expected results.
Step 6: Documentation and governance - ensure all models have descriptions, all columns are documented, and all models have an owner in meta. Compute documentation coverage. Set up model access levels and contracts for public models.
Step 7: CI/CD pipeline - configure GitHub Actions CI with slim state-based builds. Set up production job with failure alerting. Store manifest.json artifacts. Define the deployment and rollback process. Copy prompt Open prompt details 
## Recommended dbt Advanced Patterns workflow 
1 
### dbt CI/CD Pipeline 

Start with a focused prompt in dbt Advanced Patterns so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### dbt for Machine Learning Features 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### dbt Macros and Reusability 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### dbt Metrics Layer 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
