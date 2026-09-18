# Staging Model Patterns *AI Prompt *

Write best-practice staging models for these source systems. Source systems: {{sources}} (e.g. Postgres, Stripe, Salesforce, Hubspot) Warehouse: {{warehouse}} Raw schema: {{raw_... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: staging model templates for each source, type casting patterns, source.yml configuration, and anti-pattern list. 
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

The AI should return a structured result that covers the main requested outputs, such as Staging model purpose and rules:, One model per source table (1:1 relationship), No joins between source tables in staging. The final answer should stay clear, actionable, and easy to review inside a dbt modeling workflow for analytics engineer (dbt) work. 

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
