# dbt Modeling *AI Prompts *

6 Analytics Engineer (dbt) prompts in dbt Modeling. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 6 single prompts. 

## AI prompts in dbt Modeling 
6 prompts Beginner Single prompt 01 
### dbt Model Structure 

Design the folder structure and model layering for a dbt project for this data stack. Data sources: {{sources}} (e.g. Postgres transactional DB, Stripe, Salesforce) Warehouse: {... 
Prompt text Design the folder structure and model layering for a dbt project for this data stack.

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

Return: folder structure, naming conventions, sources.yml template, and materialization strategy per layer. Copy prompt Open prompt details Advanced Single prompt 02 
### Event Data Modeling 

Model raw event data (clickstream, product events) into analytics-ready tables using dbt. Event source: {{event_source}} (Segment, Amplitude, custom event log) Key events: {{eve... 
Prompt text Model raw event data (clickstream, product events) into analytics-ready tables using dbt.

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

Return: staging model patterns for event data, identity stitching logic, session modeling SQL, and funnel model design. Copy prompt Open prompt details Intermediate Single prompt 03 
### Incremental Model Design 

Design a production-grade dbt incremental model for this large table. Source table: {{source_table}} Update pattern: {{update_pattern}} (append-only, late-arriving records, muta... 
Prompt text Design a production-grade dbt incremental model for this large table.

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

Return: incremental model config, strategy recommendation, late-arriving data handling, and testing approach. Copy prompt Open prompt details Intermediate Single prompt 04 
### Mart Design for Analytics 

Design a dimensional mart for this analytics use case. Business domain: {{domain}} (e.g. finance, product, marketing) Key questions to answer: {{questions}} Source models: {{sou... 
Prompt text Design a dimensional mart for this analytics use case.

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

Return: fact table schema, dimension table schemas, date dimension spec, grain definition, and materialization recommendation. Copy prompt Open prompt details Intermediate Single prompt 05 
### Slowly Changing Dimensions 

Implement slowly changing dimensions (SCD) in dbt for this entity. Entity: {{entity}} (customer, product, employee, account) Attributes that change over time: {{changing_attribu... 
Prompt text Implement slowly changing dimensions (SCD) in dbt for this entity.

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

Return: SCD type recommendation, snapshot config, mart model on top of snapshot, and point-in-time join pattern. Copy prompt Open prompt details Beginner Single prompt 06 
### Staging Model Patterns 

Write best-practice staging models for these source systems. Source systems: {{sources}} (e.g. Postgres, Stripe, Salesforce, Hubspot) Warehouse: {{warehouse}} Raw schema: {{raw_... 
Prompt text Write best-practice staging models for these source systems.

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

Return: staging model templates for each source, type casting patterns, source.yml configuration, and anti-pattern list. Copy prompt Open prompt details 
## Recommended dbt Modeling workflow 
1 
### dbt Model Structure 

Start with a focused prompt in dbt Modeling so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Event Data Modeling 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Incremental Model Design 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Mart Design for Analytics 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
