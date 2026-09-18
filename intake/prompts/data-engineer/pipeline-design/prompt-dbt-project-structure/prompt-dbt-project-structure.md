# dbt Project Structure *AI Prompt *

This prompt defines how to structure a dbt project so that models remain understandable, testable, and maintainable as the warehouse grows. It is useful for teams that want consistent naming, layer separation, materialization choices, testing, and CI rules from the start. It encourages a scalable project layout rather than ad hoc model sprawl. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design the dbt project structure for a data warehouse with {{num_source_systems}} source systems.

1. Directory structure:
```
models/
 staging/ # 1:1 with source tables, light cleaning only
 source_a/
 source_b/
 intermediate/ # Business logic, joining staging models
 marts/
 core/ # Shared dimension and fact tables
 finance/ # Domain-specific marts
 marketing/
tests/
 generic/ # Custom generic tests
 singular/ # One-off data quality tests
macros/
seeds/
snapshots/
```

2. Model naming conventions:
 - Staging: stg_{source}__{entity} (e.g. stg_salesforce__accounts)
 - Intermediate: int_{entity}_{verb} (e.g. int_orders_pivoted)
 - Marts: {entity} or dim_{entity} / fct_{entity}

3. Materialization strategy:
 - Staging: view (always fresh, no storage cost)
 - Intermediate: ephemeral or table depending on complexity
 - Marts: table or incremental depending on size and freshness requirements

4. Sources configuration (sources.yml):
 - Define all source tables with freshness checks
 - freshness: warn_after: {count: 12, period: hour}, error_after: {count: 24, period: hour}

5. Model configuration (schema.yml):
 - Document every model and column
 - Apply generic tests: unique, not_null, accepted_values, relationships

6. Incremental models:
 - Use unique_key for merge strategy
 - Filter with is_incremental() macro: WHERE updated_at > (SELECT MAX(updated_at) FROM {{ this }})
 - Handle late-arriving data with a lookback window

7. CI/CD integration:
 - dbt build --select state:modified+ on PRs (only changed models and their downstream)
 - dbt test --select source:* for source freshness checks

Return: directory structure, naming convention guide, materialization decision matrix, and CI/CD integration config. 
```

## When to use this prompt 
Use case 01 
When starting a new dbt project or reorganizing an existing one. 
Use case 02 
When multiple source systems must be modeled in a clean, repeatable way. 
Use case 03 
When standardizing dbt practices across a team. 
Use case 04 
When you need a blueprint for documentation, testing, and CI/CD. 

## What the AI should return 

Return a recommended dbt folder structure, naming rules, materialization decision matrix, and example configuration files. Include guidance for sources, schema.yml documentation, incremental models, and CI/CD commands. The response should read like a project setup guide that a team can adopt directly. 

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

Once you have the first result, continue deeper with related prompts in Pipeline Design.
