# Incremental Model Design *AI Prompt *

Design a production-grade dbt incremental model for this large table. Source table: {{source_table}} Update pattern: {{update_pattern}} (append-only, late-arriving records, muta... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a production-grade dbt incremental model for this large table.

Source table: {{source_table}}
Update pattern: {{update_pattern}} (append-only, late-arriving records, mutable rows)
Warehouse: {{warehouse}}
Expected daily volume: {{daily_rows}} rows

1. Incremental model template:
 {{'{{'}}config(
 materialized='incremental',
 unique_key='order_id',
 incremental_strategy='merge',
 on_schema_change='sync_all_columns'
 ){{'}}'}}

 SELECT ...
 FROM {{ source('stripe', 'charges') }}
 {% if is_incremental() %}
 WHERE updated_at > (
 SELECT MAX(updated_at) FROM {{ this }}
 )
 {% endif %}

2. Incremental strategy selection:

 append (append-only, immutable events):
 - Only adds new rows; never updates existing ones
 - Fastest; use for event logs, impressions, clicks
 - Risk: duplicate rows if the job re-runs

 merge (mutable rows with a unique key):
 - Upserts: insert new rows, update changed rows
 - Requires unique_key
 - Most versatile; recommended default for most tables

 delete+insert (Redshift, BigQuery partition-based):
 - Deletes all rows in the affected partitions, re-inserts
 - Efficient for partitioned tables on Redshift or BQ

 insert_overwrite (Spark / BigQuery):
 - Replaces entire partitions atomically
 - Use with partition_by config

3. Late-arriving data:
 - Use a lookback window: WHERE updated_at >= (MAX(updated_at) - INTERVAL '3 days')
 - Protects against late-arriving events without full refresh
 - Document the lookback assumption in model description

4. Full refresh safety:
 - Always test: dbt run --full-refresh on a dev schema before promoting changes
 - Add a comment: -- full refresh required if schema changes

5. Testing incremental logic:
 - Compare row counts: incremental run vs full refresh on a 7-day window
 - Verify: no duplicates on unique_key after multiple incremental runs

Return: incremental model config, strategy recommendation, late-arriving data handling, and testing approach. 
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

The AI should return a structured result that covers the main requested outputs, such as Incremental model template:, Incremental strategy selection:, Only adds new rows; never updates existing ones. The final answer should stay clear, actionable, and easy to review inside a dbt modeling workflow for analytics engineer (dbt) work. 

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
