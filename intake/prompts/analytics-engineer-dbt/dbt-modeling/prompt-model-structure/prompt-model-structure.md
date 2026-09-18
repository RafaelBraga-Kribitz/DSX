# dbt Model Structure *AI Prompt *

Design the folder structure and model layering for a dbt project for this data stack. Data sources: {{sources}} (e.g. Postgres transactional DB, Stripe, Salesforce) Warehouse: {... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: folder structure, naming conventions, sources.yml template, and materialization strategy per layer. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin dbt modeling work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in dbt Modeling or the wider Analytics Engineer (dbt) library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Recommended layer architecture:, One model per source table, 1:1 with the source; no joins, no business logic. The final answer should stay clear, actionable, and easy to review inside a dbt modeling workflow for analytics engineer (dbt) work. 

## How to use this prompt 
1 
### Open your data context 

Load your dataset, notebook, or working environment so the AI can operate on the actual project context. 
2 
### Copy the prompt text 

Use the copy button above and paste the prompt into the AI assistant or prompt input area. 
3 
### Review the output critically 

Check whether the result matches your data, assumptions, and desired format before moving on. 
4 
### Chain into the next prompt 

Once you have the first result, continue deeper with related prompts in dbt Modeling.
