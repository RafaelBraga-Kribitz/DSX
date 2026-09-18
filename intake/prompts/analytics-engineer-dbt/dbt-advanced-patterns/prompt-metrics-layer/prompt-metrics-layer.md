# dbt Metrics Layer *AI Prompt *

Define and govern business metrics using dbt's semantic layer. Metrics to define: {{metrics}} (e.g. monthly_recurring_revenue, customer_acquisition_cost, churn_rate) Metric owne... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: semantic model YAML, metric definitions, MetricFlow query examples, and governance process. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin dbt advanced patterns work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in dbt Advanced Patterns or the wider Analytics Engineer (dbt) library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as dbt Semantic Layer overview:, Defines metrics in YAML with consistent business logic, Metrics are computed at query time, not stored. The final answer should stay clear, actionable, and easy to review inside a dbt advanced patterns workflow for analytics engineer (dbt) work. 

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

Once you have the first result, continue deeper with related prompts in dbt Advanced Patterns.
