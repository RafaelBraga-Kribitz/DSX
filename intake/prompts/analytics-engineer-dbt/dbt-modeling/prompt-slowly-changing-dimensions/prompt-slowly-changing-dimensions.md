# Slowly Changing Dimensions *AI Prompt *

Implement slowly changing dimensions (SCD) in dbt for this entity. Entity: {{entity}} (customer, product, employee, account) Attributes that change over time: {{changing_attribu... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: SCD type recommendation, snapshot config, mart model on top of snapshot, and point-in-time join pattern. 
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

The AI should return a structured result that covers the main requested outputs, such as SCD Type 1 — Overwrite:, Simply update the current value; no history preserved, Implementation: dbt incremental model with merge strategy and the changing columns. The final answer should stay clear, actionable, and easy to review inside a dbt modeling workflow for analytics engineer (dbt) work. 

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
