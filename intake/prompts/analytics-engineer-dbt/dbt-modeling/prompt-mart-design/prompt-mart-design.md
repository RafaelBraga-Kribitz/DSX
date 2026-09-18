# Mart Design for Analytics *AI Prompt *

Design a dimensional mart for this analytics use case. Business domain: {{domain}} (e.g. finance, product, marketing) Key questions to answer: {{questions}} Source models: {{sou... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: fact table schema, dimension table schemas, date dimension spec, grain definition, and materialization recommendation. 
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

The AI should return a structured result that covers the main requested outputs, such as Identify the grain:, Fact table design (fct_*):, Include: surrogate key, all foreign keys to dimensions, date keys, degenerate dimensions (order_number), and measures. The final answer should stay clear, actionable, and easy to review inside a dbt modeling workflow for analytics engineer (dbt) work. 

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
