# dbt Test Coverage Plan *AI Prompt *

Design a comprehensive dbt test suite for this model or project. Model: {{model_name}} Grain: {{grain}} (one row per order, one row per customer per day, etc.) Key columns: {{ke... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: schema.yml test block for the model, singular test SQLs for critical business rules, dbt-utils test recommendations, and severity assignments. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin dbt testing work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in dbt Testing or the wider Analytics Engineer (dbt) library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Generic tests (schema.yml):, unique: on the primary key or unique identifier, not_null: on all columns that must never be null (primary keys, critical FKs, metric numerators). The final answer should stay clear, actionable, and easy to review inside a dbt testing workflow for analytics engineer (dbt) work. 

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

Once you have the first result, continue deeper with related prompts in dbt Testing.
