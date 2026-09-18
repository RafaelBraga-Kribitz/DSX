# Warehouse Cost Optimization *AI Prompt *

This prompt examines warehouse spend and turns cost into concrete optimization opportunities across compute, storage, governance, and user behavior. It is useful when teams need to reduce cloud warehouse cost without blindly cutting performance or access. The answer should connect savings ideas to measurable spend drivers. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze and optimize the cost of this cloud data warehouse.

Platform: {{platform}} (Snowflake / BigQuery / Redshift / Databricks)
Current monthly cost: {{current_cost}}
Target reduction: {{target_reduction}}

1. Cost breakdown analysis:
 - Identify the top 10 most expensive queries by compute cost
 - Identify the top 10 most expensive users/teams by spend
 - Break down storage cost: active storage vs time-travel vs fail-safe
 - Identify tables that have not been queried in the last 90 days (zombie tables)

2. Compute optimizations:
 - Auto-suspend: set warehouse auto-suspend to 1–2 minutes (not the default 10)
 - Auto-scale: use multi-cluster warehouses only for concurrent workloads, not sequential ones
 - Query optimization: the top 3 most expensive queries — can they be rewritten to scan less data?
 - Result caching: are users re-running identical queries? Enable result cache.
 - Materialization: for frequently run expensive aggregations, create a pre-aggregated table

3. Storage optimizations:
 - Reduce time-travel retention from 90 days to 7 days for non-critical tables (Snowflake)
 - Set partition expiration for old data that is no longer needed (BigQuery)
 - Compress and archive historical data to cheaper storage tiers
 - Delete zombie tables after confirming with owners

4. Governance:
 - Set per-user and per-team cost budgets with alerts at 80% and 100% of budget
 - Require query cost estimates before running full-table scans over {{threshold_gb}}GB
 - Tag queries with cost center for chargeback reporting

Return: cost breakdown analysis queries, top optimizations with estimated savings each, and governance policy. 
```

## When to use this prompt 
Use case 01 
When warehouse costs are growing faster than expected. 
Use case 02 
When leadership asks for a cost-reduction plan with evidence. 
Use case 03 
When teams need to identify expensive queries, users, or idle assets. 
Use case 04 
When governance controls like budgets and query scan limits are missing. 

## What the AI should return 

Return cost-breakdown analysis queries, a prioritized savings plan with estimated impact, and governance recommendations. Distinguish compute savings from storage savings and call out zombie assets or inefficient workloads. The result should make it clear where the biggest savings are and how to realize them. 

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

Once you have the first result, continue deeper with related prompts in Infrastructure and Platform.
