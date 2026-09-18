# Query Performance Tuning *AI Prompt *

This prompt tunes a slow warehouse query methodically by analyzing the execution plan and then rewriting the most expensive parts. It is helpful when teams need to bring query latency down while also reducing scanned data and compute cost. The answer should prioritize changes with the biggest likely payoff first. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Tune this slow data warehouse query for performance.

Query: {{slow_query}}
Current runtime: {{current_runtime}}
Target runtime: {{target_runtime}}
Platform: {{platform}}

Work through these optimizations in order:

1. Execution plan analysis:
 - Run EXPLAIN ANALYZE (or platform equivalent)
 - Identify the most expensive operations: full table scans, hash joins on large tables, sorts on large datasets
 - Check estimated vs actual row counts — large divergence indicates stale statistics

2. Filter pushdown:
 - Ensure WHERE clause filters on partitioned/clustered columns appear as early as possible
 - Check if filters are being applied before or after a JOIN — move them before the JOIN
 - Replace HAVING with WHERE where possible (filter before aggregation)

3. Join optimization:
 - Order JOINs from smallest to largest result set
 - Use broadcast/replicate hint for small dimension tables
 - Check for accidental cartesian products (missing JOIN conditions)
 - Replace correlated subqueries with JOINs or window functions

4. Aggregation optimization:
 - Pre-aggregate before joining to reduce row count going into the join
 - Use approximate aggregations (APPROX_COUNT_DISTINCT) where exact precision is not required
 - Push GROUP BY to a subquery before the outer SELECT

5. Materialization:
 - If this query runs frequently: materialize it as a table and schedule refresh
 - Create a summary table at the right grain to avoid full re-aggregation each time

6. Statistics:
 - Run ANALYZE TABLE to refresh statistics if the query plan looks wrong
 - Check column statistics: histograms for skewed columns, NDV for join columns

Return: annotated execution plan, specific rewrites for each optimization applied, and before/after runtime comparison. 
```

## When to use this prompt 
Use case 01 
When a query is too slow for dashboards, pipelines, or ad hoc analysis. 
Use case 02 
When EXPLAIN output is available or can be generated. 
Use case 03 
When you need specific rewrites, not general SQL advice. 
Use case 04 
When deciding whether to optimize the query itself or materialize the result. 

## What the AI should return 

Return an annotated optimization plan based on execution-plan findings. Include query rewrites, join or aggregation improvements, statistics recommendations, and any materialization options. Show what each change is expected to improve and summarize the likely before/after runtime picture. 

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

Once you have the first result, continue deeper with related prompts in Data Warehouse Patterns.
