# Analytics Engineer (dbt) *AI Prompts *

Analytics Engineer (dbt) AI prompt library with 20 prompts in 5 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 5 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Analytics Engineer (dbt) prompt categories 
5 categories 
### dbt Advanced Patterns 

AI prompts for advanced dbt patterns including macros, reusable modeling architecture, package strategy, and maintainable project structure. 
6 prompts dbt CI/CD Pipeline dbt for Machine Learning Features → 
### dbt Modeling 

AI prompts for dbt modeling best practices including staging/intermediate/mart layers, naming conventions, and metric-ready data models. 
6 prompts dbt Model Structure Event Data Modeling → 
### dbt Documentation 

AI prompts for dbt documentation workflows including model descriptions, lineage communication, ownership clarity, and analytics discoverability. 
3 prompts dbt Governance and Standards dbt Lineage and Impact Analysis → 
### dbt Testing 

AI prompts for dbt testing strategy including schema tests, data tests, custom assertions, and quality guardrails in analytics engineering. 
3 prompts dbt Data Freshness and Monitoring dbt Test Coverage Plan → 
### dbt Performance 

AI prompts for dbt performance optimization including incremental strategy, materialization choices, dependency pruning, and warehouse-efficient builds. 
2 prompts dbt Project Scalability dbt Query Performance Optimization → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 20 dbt Advanced Patterns 6 dbt Modeling 6 dbt Documentation 3 dbt Testing 3 dbt Performance 2 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **20 **of 20 prompts 
## dbt Advanced Patterns 
6 prompt s dbt Advanced Patterns Advanced Prompt 01 
### dbt CI/CD Pipeline 
Design a CI/CD pipeline for this dbt project.

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

Return: branch strategy, CI workflow YAML, production deployment steps, and dbt Cloud job configuration. Copy prompt View page Show more ↓ dbt Advanced Patterns Advanced Prompt 02 
### dbt for Machine Learning Features 
Use dbt to build and manage ML feature tables for training and serving.

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

Return: feature table schema, point-in-time join pattern, ML-specific tests, and export strategy. Copy prompt View page Show more ↓ dbt Advanced Patterns Intermediate Prompt 03 
### dbt Macros and Reusability 
Write reusable dbt macros for common transformation patterns in this project.

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

Return: macro implementations for the identified patterns, usage examples, and testing approach. Copy prompt View page Show more ↓ dbt Advanced Patterns Advanced Prompt 04 
### dbt Metrics Layer 
Define and govern business metrics using dbt's semantic layer.

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

Return: semantic model YAML, metric definitions, MetricFlow query examples, and governance process. Copy prompt View page Show more ↓ dbt Advanced Patterns Intermediate Prompt 05 
### dbt Packages and Ecosystem 
Select and configure the right dbt packages for this project's needs.

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

Return: recommended package set for the project requirements, packages.yml configuration, and upgrade governance policy. Copy prompt View page Show more ↓ dbt Advanced Patterns Advanced Chain 06 
### Full dbt Project Build Chain 
Step 1: Source assessment - catalog all source tables from the raw schema. For each source: document the schema, identify the primary key, assess data quality issues, and configure source freshness checks in sources.yml.
Step 2: Staging layer - build one staging model per source table. Apply: rename columns to snake_case, explicit type casts, null handling for empty strings, and source metadata columns. Add not_null and unique tests on primary keys.
Step 3: Intermediate layer - identify shared transformation logic needed by multiple marts. Build intermediate models for: entity resolution, sessionization, or complex joins. Document each intermediate model's grain and purpose.
Step 4: Mart layer - design the dimensional schema for the target analytics use case. Define the grain. Build fct_* and dim_* models with appropriate materializations. Add relationships tests for all foreign keys and business rule tests for critical logic.
Step 5: Metrics layer - define dbt semantic layer metrics for key business KPIs. Ensure each metric has a description, owner, and test. Validate MetricFlow queries return expected results.
Step 6: Documentation and governance - ensure all models have descriptions, all columns are documented, and all models have an owner in meta. Compute documentation coverage. Set up model access levels and contracts for public models.
Step 7: CI/CD pipeline - configure GitHub Actions CI with slim state-based builds. Set up production job with failure alerting. Store manifest.json artifacts. Define the deployment and rollback process. Copy prompt View page Show more ↓ 
## dbt Modeling 
6 prompt s dbt Modeling Beginner Prompt 01 
### dbt Model Structure 
Design the folder structure and model layering for a dbt project for this data stack.

Data sources: {{sources}} (e.g. Postgres transactional DB, Stripe, Salesforce)
Warehouse: {{warehouse}} (Snowflake, BigQuery, Redshift, DuckDB)
Team size: {{team_size}}

1. Recommended layer architecture:

 staging/ (stg_*):
 - One model per source table
 - 1:1 with the source; no joins, no business logic
 - Rename columns to consistent snake_case
 - Cast data types explicitly
 - Add _loaded_at or source metadata columns
 - Materialized as: view (cheap, always fresh)

 intermediate/ (int_*):
 - Optional layer for complex transformations shared across marts
 - Fan-out from staging: join, unnest, pivot
 - Not exposed to BI tools
 - Materialized as: view or ephemeral

 marts/ (fct_* and dim_*):
 - Business-oriented models organized by domain (mart/finance/, mart/marketing/)
 - fct_*: facts (grain = one row per event/transaction)
 - dim_*: dimensions (grain = one row per entity)
 - ref() all upstream models — never direct source references
 - Materialized as: table or incremental

2. Naming conventions:
 - stg_{source}__{object}: stg_salesforce__accounts
 - int_{verb}_{object}: int_orders_joined
 - fct_{verb/noun}: fct_orders, fct_revenue
 - dim_{noun}: dim_customers, dim_products

3. sources.yml:
 - Define all raw sources with database, schema, and table
 - Add source freshness checks: loaded_at_field + warn_after / error_after

4. Materialization strategy:
 - Staging: view
 - Intermediate: view or ephemeral
 - Marts (large): incremental with unique_key and updated_at
 - Marts (small/lookup): table

Return: folder structure, naming conventions, sources.yml template, and materialization strategy per layer. Copy prompt View page Show more ↓ dbt Modeling Advanced Prompt 02 
### Event Data Modeling 
Model raw event data (clickstream, product events) into analytics-ready tables using dbt.

Event source: {{event_source}} (Segment, Amplitude, custom event log)
Key events: {{events}} (page_viewed, button_clicked, signed_up, purchased)
Destination: {{warehouse}}

1. Raw event structure:
 Typical raw event schema:
 - event_id: unique identifier for each event
 - event_name: the event type
 - user_id: actor (may be anonymous pre-login)
 - anonymous_id: cookie or device identifier for pre-login events
 - properties: JSON blob of event-specific attributes
 - received_at, sent_at, original_timestamp: event timing

2. Staging layer — event-type-specific models:
 Create one staging model per event type to extract the relevant properties:

 stg_events__page_viewed:
 SELECT
 event_id,
 user_id,
 anonymous_id,
 received_at AS viewed_at,
 properties:page_url::varchar AS page_url,
 properties:referrer::varchar AS referrer
 FROM {{ source('segment', 'tracks') }}
 WHERE event_name = 'page_viewed'

3. Identity stitching (anonymous_id → user_id):
 Build an identity map:
 SELECT
 anonymous_id,
 FIRST_VALUE(user_id) OVER (
 PARTITION BY anonymous_id
 ORDER BY received_at
 ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
 ) AS resolved_user_id
 FROM {{ ref('stg_events__all') }}
 WHERE user_id IS NOT NULL

4. Session modeling:
 Define a session as: a group of events from the same user with < 30-minute gaps.
 USE LAG to find time since last event; a gap > 30 minutes = new session.

5. Funnel models:
 Build per-user, per-session event sequences:
 SELECT
 user_id,
 session_id,
 MIN(CASE WHEN event_name = 'viewed_product' THEN event_time END) AS viewed_product_at,
 MIN(CASE WHEN event_name = 'added_to_cart' THEN event_time END) AS added_cart_at,
 MIN(CASE WHEN event_name = 'purchased' THEN event_time END) AS purchased_at
 FROM {{ ref('int_events__sessionized') }}
 GROUP BY 1, 2

Return: staging model patterns for event data, identity stitching logic, session modeling SQL, and funnel model design. Copy prompt View page Show more ↓ dbt Modeling Intermediate Prompt 03 
### Incremental Model Design 
Design a production-grade dbt incremental model for this large table.

Source table: {{source_table}}
Update pattern: {{update_pattern}} (append-only, late-arriving records, mutable rows)
Warehouse: {{warehouse}}
Expected daily volume: {{daily_rows}} rows

1. Incremental model template:
 {{'{{'}}config(
 materialized='incremental',
 unique_key='order_id',
 incremental_strategy='merge',
 on_schema_change='sync_all_columns'
 ){{'}}'}}

 SELECT ...
 FROM {{ source('stripe', 'charges') }}
 {% if is_incremental() %}
 WHERE updated_at > (
 SELECT MAX(updated_at) FROM {{ this }}
 )
 {% endif %}

2. Incremental strategy selection:

 append (append-only, immutable events):
 - Only adds new rows; never updates existing ones
 - Fastest; use for event logs, impressions, clicks
 - Risk: duplicate rows if the job re-runs

 merge (mutable rows with a unique key):
 - Upserts: insert new rows, update changed rows
 - Requires unique_key
 - Most versatile; recommended default for most tables

 delete+insert (Redshift, BigQuery partition-based):
 - Deletes all rows in the affected partitions, re-inserts
 - Efficient for partitioned tables on Redshift or BQ

 insert_overwrite (Spark / BigQuery):
 - Replaces entire partitions atomically
 - Use with partition_by config

3. Late-arriving data:
 - Use a lookback window: WHERE updated_at >= (MAX(updated_at) - INTERVAL '3 days')
 - Protects against late-arriving events without full refresh
 - Document the lookback assumption in model description

4. Full refresh safety:
 - Always test: dbt run --full-refresh on a dev schema before promoting changes
 - Add a comment: -- full refresh required if schema changes

5. Testing incremental logic:
 - Compare row counts: incremental run vs full refresh on a 7-day window
 - Verify: no duplicates on unique_key after multiple incremental runs

Return: incremental model config, strategy recommendation, late-arriving data handling, and testing approach. Copy prompt View page Show more ↓ dbt Modeling Intermediate Prompt 04 
### Mart Design for Analytics 
Design a dimensional mart for this analytics use case.

Business domain: {{domain}} (e.g. finance, product, marketing)
Key questions to answer: {{questions}}
Source models: {{source_models}}

1. Identify the grain:
 The grain is the most precise definition of what one row in the fact table represents.
 'One row per order' → fct_orders
 'One row per user per day' → fct_user_daily_activity
 'One row per ad impression' → fct_impressions
 State the grain explicitly in the model description and enforce it with a unique + not_null test.

2. Fact table design (fct_*):
 - Include: surrogate key, all foreign keys to dimensions, date keys, degenerate dimensions (order_number), and measures
 - Measures: raw numeric facts only (amount, quantity, duration) — no calculated metrics in the fact table
 - Avoid: text descriptions in fact tables (use dimension keys instead)
 - Include: _loaded_at, _updated_at metadata columns

3. Dimension table design (dim_*):
 - Include: surrogate key, natural key, all descriptive attributes, and SCD tracking columns if applicable
 - Slowly changing: use dbt snapshots for Type 2 history
 - Conformed dimensions: dim_customers, dim_dates used across multiple fact tables

4. Date dimension (dim_dates):
 Generate using dbt_utils.date_spine covering your full date range:
 - date_day, week_start_date, month_start_date, year
 - Fiscal calendar fields if needed
 - is_weekend, is_holiday, is_business_day
 - Materialized as: table (pre-generated, never changes)

5. Wide vs normalized:
 Wide (one big denormalized table):
 - Joins pre-done; easier for BI users
 - Larger storage; slower incremental updates
 Use for: smaller domains, BI tools with limited join support

 Star schema (normalized):
 - Smaller fact table; flexible slicing by any dimension
 - BI users must join fact to dimensions
 Use for: large fact tables, complex domains

Return: fact table schema, dimension table schemas, date dimension spec, grain definition, and materialization recommendation. Copy prompt View page Show more ↓ dbt Modeling Intermediate Prompt 05 
### Slowly Changing Dimensions 
Implement slowly changing dimensions (SCD) in dbt for this entity.

Entity: {{entity}} (customer, product, employee, account)
Attributes that change over time: {{changing_attributes}}
SCD type needed: {{scd_type}} (Type 1, Type 2, or Type 3)
Warehouse: {{warehouse}}

1. SCD Type 1 — Overwrite:
 - Simply update the current value; no history preserved
 - Implementation: dbt incremental model with merge strategy and the changing columns
 - Use when: history of the attribute is not needed

2. SCD Type 2 — Full history with effective dates:
 Each change creates a new row with:
 - dbt_scd_id: surrogate key (hash of natural key + updated_at)
 - dbt_valid_from: timestamp when this version became active
 - dbt_valid_to: timestamp when this version was superseded (NULL = current row)
 - dbt_is_current: boolean flag for the current version

 dbt snapshot implementation:
 {% snapshot customers_snapshot %}
 {{
 config(
 target_schema='snapshots',
 unique_key='customer_id',
 strategy='timestamp',
 updated_at='updated_at'
 )
 }}
 SELECT * FROM {{ source('app', 'customers') }}
 {% endsnapshot %}

 Snapshot strategies:
 - timestamp: detects changes via updated_at column
 - check: compares specified columns for changes (use when no updated_at exists)
 check_cols=['email', 'plan_tier', 'country']

3. SCD Type 2 from the snapshot:
 Build a mart model on top of the snapshot:
 SELECT
 customer_id,
 email,
 plan_tier,
 dbt_valid_from AS valid_from,
 COALESCE(dbt_valid_to, '9999-12-31') AS valid_to,
 dbt_is_current AS is_current
 FROM {{ ref('customers_snapshot') }}

4. Point-in-time joins:
 To join fact events to the customer's attributes at the time of the event:
 SELECT
 o.order_id,
 o.order_date,
 c.plan_tier AS customer_plan_at_order_time
 FROM {{ ref('fct_orders') }} o
 LEFT JOIN {{ ref('dim_customers_scd') }} c
 ON o.customer_id = c.customer_id
 AND o.order_date BETWEEN c.valid_from AND c.valid_to

Return: SCD type recommendation, snapshot config, mart model on top of snapshot, and point-in-time join pattern. Copy prompt View page Show more ↓ dbt Modeling Beginner Prompt 06 
### Staging Model Patterns 
Write best-practice staging models for these source systems.

Source systems: {{sources}} (e.g. Postgres, Stripe, Salesforce, Hubspot)
Warehouse: {{warehouse}}
Raw schema: {{raw_schema}}

1. Staging model purpose and rules:
 - One model per source table (1:1 relationship)
 - No joins between source tables in staging
 - No business logic — only technical cleaning
 - Always reference via source() not raw SQL

2. Standard transformations to apply in every staging model:

 Rename to snake_case:
 customerID → customer_id
 CreatedAt → created_at

 Explicit type casting:
 CAST(amount AS NUMERIC) AS amount,
 CAST(created_at AS TIMESTAMP) AS created_at,

 Null handling:
 NULLIF(status, '') AS status, -- empty string → NULL

 Trim whitespace:
 TRIM(LOWER(email)) AS email,

 Add source metadata:
 _fivetran_synced AS _loaded_at,
 '{{ source_name }}' AS _source,

3. Staging model template:
 WITH source AS (
 SELECT * FROM {{ source('app_db', 'orders') }}
 ),
 renamed AS (
 SELECT
 id AS order_id,
 customer_id,
 CAST(total_amount AS NUMERIC) AS total_amount,
 CAST(created_at AS TIMESTAMP) AS created_at,
 NULLIF(status, '') AS status,
 _fivetran_synced AS _loaded_at
 FROM source
 )
 SELECT * FROM renamed

4. What NOT to do in staging:
 - Do not join to other models
 - Do not filter rows (preserve all source data; filter in marts)
 - Do not apply business logic (e.g. calculating total_with_tax)
 - Do not rename using business terminology (use source system names at this layer)

Return: staging model templates for each source, type casting patterns, source.yml configuration, and anti-pattern list. Copy prompt View page Show more ↓ 
## dbt Documentation 
3 prompt s dbt Documentation Advanced Prompt 01 
### dbt Governance and Standards 
Establish governance standards and engineering practices for a dbt project used by multiple teams.

Team: {{team_description}}
Project maturity: {{maturity}} (early/growing/mature)
Stakeholders: {{stakeholders}}

1. Model ownership policy:
 - Every model must have an owner defined in the meta field
 - Owner is responsible for: test coverage, documentation, SLA compliance, and responding to data quality alerts
 - Review ownership quarterly; transfer ownership when team membership changes

2. PR review checklist:
 Before approving any PR that adds or modifies a model:
 ☐ Model has a description in schema.yml
 ☐ All columns documented
 ☐ Primary key has unique + not_null tests
 ☐ Foreign keys have relationships tests
 ☐ Business rule tests present for critical logic
 ☐ Model uses ref() not raw SQL table references
 ☐ Naming conventions followed (stg_/int_/fct_/dim_)
 ☐ Materialization appropriate for the model size and usage pattern

3. Breaking change policy:
 Public models (consumed by other teams or BI tools) require:
 - 2-week deprecation notice before removing a column
 - Use of the deprecated config flag + a migration guide in the description
 - Announcement in the #data-announcements channel

4. Data SLA tiers:
 Tier 1 (critical, exec-facing): freshness SLA = 4 hours; test failures → immediate alert
 Tier 2 (operational): freshness SLA = 24 hours; test failures → next-business-day response
 Tier 3 (exploratory): best effort; test failures → weekly triage

5. Documentation completeness score:
 Compute: models with descriptions / total models
 Target: > 90% for Tier 1 models, > 70% overall
 Track in a dbt model: query the dbt catalog artifact to measure coverage

Return: ownership policy, PR checklist, breaking change SLA, tier definitions, and documentation coverage tracking approach. Copy prompt View page Show more ↓ dbt Documentation Intermediate Prompt 02 
### dbt Lineage and Impact Analysis 
Analyze data lineage and assess the impact of a proposed change in this dbt project.

Proposed change: {{change_description}} (e.g. rename column, change grain, drop a staging model)
Affected model: {{affected_model}}
Warehouse: {{warehouse}}

1. Understanding dbt lineage:
 dbt automatically builds a DAG (Directed Acyclic Graph) from all ref() and source() calls.
 Every model knows its parents (models it depends on) and children (models that depend on it).

2. Impact analysis commands:

 Find all downstream dependents:
 dbt ls --select fct_orders+ # all models downstream of fct_orders
 dbt ls --select +fct_orders # all models upstream of fct_orders
 dbt ls --select +fct_orders+ # full lineage in both directions

 Identify exposed models (BI-facing):
 dbt ls --select fct_orders+ --resource-type exposure

 Check which metrics depend on a column:
 dbt ls --select metric:* # list all defined metrics

3. Safe column rename process:
 Step 1: Add the new column with the new name alongside the old one
 Step 2: Deploy; validate downstream models use the new name
 Step 3: Remove the old column in the next deployment
 Never: rename a column and deploy in a single step without checking downstream

4. Breaking change checklist:
 Before merging any change to a widely-used mart model:
 ☐ Run: dbt ls --select {model}+ to list all downstream models
 ☐ Check: are any downstream models used in BI dashboards or exported to external systems?
 ☐ Notify: owners of affected downstream models
 ☐ Test: run full dbt build --select {model}+ in a dev schema
 ☐ Document: add a changelog entry to the model description

5. State-based CI (dbt Cloud / dbt Core):
 dbt build --select state:modified+
 - Only builds models that changed AND their downstream dependents
 - Dramatically faster CI than running the full project
 - Requires: dbt state artifacts from the last production run

Return: downstream impact list, safe change process, breaking change checklist, and state-based CI configuration. Copy prompt View page Show more ↓ dbt Documentation Beginner Prompt 03 
### dbt Model Documentation 
Write comprehensive dbt documentation for this model.

Model name: {{model_name}}
Layer: {{layer}} (staging, intermediate, mart)
Grain: {{grain}}
Key columns: {{columns}}
Upstream models: {{upstream}}

1. Model-level description:
 models:
 - name: fct_orders
 description: |
 Fact table capturing all customer orders at the order grain.
 One row per unique order. Includes financial metrics, fulfillment
 status, and customer and product dimension keys for joining.
 Source: {{ source('app', 'orders') }} joined with shipping data.
 Grain: one row per order_id.
 Refresh: incremental, daily at 06:00 UTC.
 Owner: Data team (analytics-eng@company.com)

2. Column-level documentation:
 columns:
 - name: order_id
 description: Unique identifier for each order. Primary key.
 tests: [unique, not_null]
 - name: customer_id
 description: Foreign key to dim_customers. The customer who placed the order.
 tests:
 - relationships:
 to: ref('dim_customers')
 field: customer_id
 - name: order_amount_usd
 description: |
 Total order value in USD at time of order, inclusive of all line items
 and exclusive of shipping fees and taxes. Negative values indicate refunds.

3. Meta fields for data catalog integration:
 meta:
 owner: 'analytics-engineering'
 domain: 'finance'
 tier: 'gold'
 pii: false
 sla_hours: 4

4. Tags for organization:
 config:
 tags: ['finance', 'daily', 'mart']

5. Generating and hosting docs:
 dbt docs generate → builds the catalog.json artifact
 dbt docs serve → local documentation site
 For production: host the generated docs/ folder on:
 - dbt Cloud: built-in docs hosting
 - GitHub Pages or Netlify (static site deployment)
 - Internal data catalog (DataHub, Atlan, Alation) via dbt artifact import

Return: complete schema.yml entry for the model, column documentation, meta fields, and documentation hosting recommendation. Copy prompt View page Show more ↓ 
## dbt Testing 
3 prompt s dbt Testing Intermediate Prompt 01 
### dbt Data Freshness and Monitoring 
Configure source freshness monitoring and anomaly detection for this dbt project.

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

Return: sources.yml freshness config, recency test configuration, row count anomaly detection SQL, Elementary setup, and alerting integration. Copy prompt View page Show more ↓ dbt Testing Beginner Prompt 02 
### dbt Test Coverage Plan 
Design a comprehensive dbt test suite for this model or project.

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

Return: schema.yml test block for the model, singular test SQLs for critical business rules, dbt-utils test recommendations, and severity assignments. Copy prompt View page Show more ↓ dbt Testing Advanced Prompt 03 
### dbt-expectations Test Suite 
Implement advanced data quality tests using the dbt-expectations package.

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

Return: complete schema.yml with dbt-expectations tests, severity assignments, and interpretation of each test's business meaning. Copy prompt View page Show more ↓ 
## dbt Performance 
2 prompt s dbt Performance Advanced Prompt 01 
### dbt Project Scalability 
Scale this dbt project to support a growing team and larger data volumes.

Current project size: {{model_count}} models, {{team_size}} engineers
Pain points: {{pain_points}} (slow CI, difficult navigation, merge conflicts, inconsistent standards)
Warehouse: {{warehouse}}

1. Multi-project architecture (dbt mesh):
 Split the monorepo into multiple smaller dbt projects connected via cross-project refs:
 - Platform project: shared staging and dimension models consumed by all
 - Domain projects: finance, marketing, product — each with their own team and release cycle
 - Cross-project ref: {{ ref('platform', 'dim_customers') }}
 Benefits: independent deployments, clear ownership, faster CI (smaller projects)

2. Model governance with groups and contracts:

 Groups (assign ownership):
 groups:
 - name: finance
 owner:
 name: Finance Analytics Team
 email: finance-analytics@company.com

 Model contract (enforce public model schema):
 models:
 - name: fct_revenue
 group: finance
 access: public # can be referenced from other projects
 config:
 contract:
 enforced: true # CI fails if schema drifts
 columns:
 - name: revenue_usd
 data_type: numeric

3. Slim CI for large projects:
 - Use dbt state artifacts to run only modified models and their dependents
 - Target: CI time < 10 minutes regardless of project size
 - Store production manifest.json in S3; download in CI as the comparison state

4. Model access levels:
 - private: only accessible within the same group/project
 - protected: accessible from the same project
 - public: can be referenced cross-project
 Enforce: downstream teams can only depend on public models

5. Style guide enforcement:
 - sqlfluff: SQL linter with dbt dialect support
 sqlfluff lint models/ --dialect snowflake
 - pre-commit hooks: run sqlfmt, sqlfluff, and yamllint before every commit
 - Standardized model config template in .dbt/config.yml

Return: dbt mesh architecture design, contract enforcement setup, slim CI configuration, access level policy, and style guide tooling. Copy prompt View page Show more ↓ dbt Performance Intermediate Prompt 02 
### dbt Query Performance Optimization 
Optimize slow dbt models for this warehouse.

Slow model: {{model_name}}
Current runtime: {{runtime}} seconds
Warehouse: {{warehouse}}
Model type: {{model_type}} (incremental, full table, view)

1. Diagnose the bottleneck:
 - Run: dbt build --select {{model_name}} and check the query profile in the warehouse console
 - Identify: full table scans, missing clustering/partitioning, large cross-joins, excessive CTEs

2. Partitioning and clustering:

 BigQuery:
 config(
 partition_by={"field": "order_date", "data_type": "date"},
 cluster_by=["customer_id", "order_status"]
 )

 Snowflake:
 config(
 cluster_by=['TO_DATE(order_date)', 'order_status']
 )

 Redshift:
 config(
 sort=['order_date'],
 dist='customer_id'
 )

3. Incremental optimization:
 - Ensure the WHERE clause in the incremental filter uses the partition column
 - Wrong: WHERE id > (SELECT MAX(id) FROM {{this}}) — full table scan on the source
 - Right: WHERE updated_at >= (SELECT MAX(updated_at) FROM {{this}}) — if updated_at is the partition key

4. CTE vs temp table trade-off:
 - Many nested CTEs can confuse the optimizer on some warehouses
 - Snowflake: CTEs are generally fine
 - BigQuery: deeply nested CTEs with repeated references can be slow — consider intermediate tables
 - Redshift: complex CTEs may benefit from being broken into separate models

5. Reduce data early:
 - Push filters as early as possible in the CTE chain
 - Do not JOIN before filtering: filter first, then join
 - Avoid SELECT * in intermediate CTEs — project only needed columns

6. Warehouse-specific tuning:
 Snowflake: configure warehouse size per model:
 config(snowflake_warehouse='LARGE_WH')

 BigQuery: enable BI Engine for sub-second queries on frequently used tables

 Redshift: ANALYZE after large loads; VACUUM for reclaiming deleted rows space

Return: diagnosis approach, partitioning / clustering config for the warehouse, incremental filter optimization, and CTE vs table strategy. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
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
