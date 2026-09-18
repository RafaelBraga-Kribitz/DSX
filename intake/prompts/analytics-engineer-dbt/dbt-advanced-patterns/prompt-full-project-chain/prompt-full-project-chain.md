# Full dbt Project Build Chain *AI Prompt *

Step 1: Source assessment - catalog all source tables from the raw schema. For each source: document the schema, identify the primary key, assess data quality issues, and config... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Source assessment - catalog all source tables from the raw schema. For each source: document the schema, identify the primary key, assess data quality issues, and configure source freshness checks in sources.yml.
Step 2: Staging layer - build one staging model per source table. Apply: rename columns to snake_case, explicit type casts, null handling for empty strings, and source metadata columns. Add not_null and unique tests on primary keys.
Step 3: Intermediate layer - identify shared transformation logic needed by multiple marts. Build intermediate models for: entity resolution, sessionization, or complex joins. Document each intermediate model's grain and purpose.
Step 4: Mart layer - design the dimensional schema for the target analytics use case. Define the grain. Build fct_* and dim_* models with appropriate materializations. Add relationships tests for all foreign keys and business rule tests for critical logic.
Step 5: Metrics layer - define dbt semantic layer metrics for key business KPIs. Ensure each metric has a description, owner, and test. Validate MetricFlow queries return expected results.
Step 6: Documentation and governance - ensure all models have descriptions, all columns are documented, and all models have an owner in meta. Compute documentation coverage. Set up model access levels and contracts for public models.
Step 7: CI/CD pipeline - configure GitHub Actions CI with slim state-based builds. Set up production job with failure alerting. Store manifest.json artifacts. Define the deployment and rollback process. 
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

The AI should return a structured result that is directly usable in a dbt advanced patterns workflow, with explicit outputs, readable formatting, and enough clarity to support the next step in analytics engineer (dbt) work. 

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
