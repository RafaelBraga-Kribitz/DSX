# dbt Query Performance Optimization *AI Prompt *

Optimize slow dbt models for this warehouse. Slow model: {{model_name}} Current runtime: {{runtime}} seconds Warehouse: {{warehouse}} Model type: {{model_type}} (incremental, fu... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Optimize slow dbt models for this warehouse.

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

Return: diagnosis approach, partitioning / clustering config for the warehouse, incremental filter optimization, and CTE vs table strategy. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin dbt performance work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in dbt Performance or the wider Analytics Engineer (dbt) library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Diagnose the bottleneck:, Run: dbt build --select {{model_name}} and check the query profile in the warehouse console, Identify: full table scans, missing clustering/partitioning, large cross-joins, excessive CTEs. The final answer should stay clear, actionable, and easy to review inside a dbt performance workflow for analytics engineer (dbt) work. 

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

Once you have the first result, continue deeper with related prompts in dbt Performance.
