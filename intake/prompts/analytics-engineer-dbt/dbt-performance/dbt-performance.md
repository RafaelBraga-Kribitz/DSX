# dbt Performance *AI Prompts *

2 Analytics Engineer (dbt) prompts in dbt Performance. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 2 single prompts. 

## AI prompts in dbt Performance 
2 prompts Advanced Single prompt 01 
### dbt Project Scalability 

Scale this dbt project to support a growing team and larger data volumes. Current project size: {{model_count}} models, {{team_size}} engineers Pain points: {{pain_points}} (slo... 
Prompt text Scale this dbt project to support a growing team and larger data volumes.

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

Return: dbt mesh architecture design, contract enforcement setup, slim CI configuration, access level policy, and style guide tooling. Copy prompt Open prompt details Intermediate Single prompt 02 
### dbt Query Performance Optimization 

Optimize slow dbt models for this warehouse. Slow model: {{model_name}} Current runtime: {{runtime}} seconds Warehouse: {{warehouse}} Model type: {{model_type}} (incremental, fu... 
Prompt text Optimize slow dbt models for this warehouse.

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

Return: diagnosis approach, partitioning / clustering config for the warehouse, incremental filter optimization, and CTE vs table strategy. Copy prompt Open prompt details 
## Recommended dbt Performance workflow 
1 
### dbt Project Scalability 

Start with a focused prompt in dbt Performance so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### dbt Query Performance Optimization 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt
