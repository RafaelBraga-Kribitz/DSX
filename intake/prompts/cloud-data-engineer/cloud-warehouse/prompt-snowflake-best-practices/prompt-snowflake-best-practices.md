# Snowflake Architecture and Best Practices *AI Prompt *

Design and optimize a Snowflake deployment for this organization. Workload: {{workload}} (ELT, mixed, analytics, ML feature store) Team: {{team}} (data engineers, analysts, data... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design and optimize a Snowflake deployment for this organization.

Workload: {{workload}} (ELT, mixed, analytics, ML feature store)
Team: {{team}} (data engineers, analysts, data scientists)
Data volume: {{volume}}
Cost target: {{cost_target}}

1. Snowflake architecture concepts:
 - Separation of storage and compute: storage billed per TB, compute per second
 - Virtual warehouses: compute clusters that scale independently
 - Databases → Schemas → Tables: same as traditional databases
 - Zero-copy cloning: instant clone of any table/schema/database for testing or branching

2. Virtual warehouse strategy:
 - One warehouse per workload type (not per team):
 LOADING_WH (X-Large): bulk data loading, ELT
 ANALYTICS_WH (Small-Medium): analyst queries
 TRANSFORM_WH (Medium): dbt runs
 ML_WH (Large): data science ad-hoc
 - Auto-suspend: 60 seconds (analysts), 300 seconds (loading)
 - Auto-resume: always enabled
 - Multi-cluster warehouses: for concurrent analyst workloads

3. Cost optimization:
 - Monitor: QUERY_HISTORY view for expensive queries
 - Use result cache: same query within 24h returns the cached result (free)
 - Use CLUSTERING KEYS on large tables filtered by a column:
 ALTER TABLE orders CLUSTER BY (TO_DATE(order_date));
 - Use SEARCH OPTIMIZATION for high-cardinality point lookups
 - Tag warehouses with resource monitors to cap monthly spend

4. Snowflake roles hierarchy:
 ACCOUNTADMIN → SYSADMIN → custom roles
 - SYSADMIN: creates databases, warehouses
 - Custom roles: ANALYST_ROLE (SELECT), ENGINEER_ROLE (DML + DDL on own schema), LOADER_ROLE (COPY INTO)
 - Follow least-privilege; never use ACCOUNTADMIN for day-to-day operations

5. Data sharing:
 - Share data with other Snowflake accounts without copying (live read access)
 - CREATE SHARE; GRANT SELECT ON TABLE TO SHARE; ADD ACCOUNT TO SHARE
 - Use for: sharing data products with customers, cross-department data sharing

Return: warehouse configuration, role hierarchy DDL, clustering key recommendations, cost monitoring queries, and data sharing setup. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin cloud warehouse work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Cloud Warehouse or the wider Cloud Data Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Snowflake architecture concepts:, Separation of storage and compute: storage billed per TB, compute per second, Virtual warehouses: compute clusters that scale independently. The final answer should stay clear, actionable, and easy to review inside a cloud warehouse workflow for cloud data engineer work. 

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

Once you have the first result, continue deeper with related prompts in Cloud Warehouse.
