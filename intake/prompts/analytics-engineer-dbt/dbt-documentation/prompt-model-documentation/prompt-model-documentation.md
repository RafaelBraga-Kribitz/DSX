# dbt Model Documentation *AI Prompt *

Write comprehensive dbt documentation for this model. Model name: {{model_name}} Layer: {{layer}} (staging, intermediate, mart) Grain: {{grain}} Key columns: {{columns}} Upstrea... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: complete schema.yml entry for the model, column documentation, meta fields, and documentation hosting recommendation. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin dbt documentation work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in dbt Documentation or the wider Analytics Engineer (dbt) library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Model-level description:, name: fct_orders, Column-level documentation:. The final answer should stay clear, actionable, and easy to review inside a dbt documentation workflow for analytics engineer (dbt) work. 

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

Once you have the first result, continue deeper with related prompts in dbt Documentation.
