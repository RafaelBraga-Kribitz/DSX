# dbt Packages and Ecosystem *AI Prompt *

Select and configure the right dbt packages for this project's needs. Project requirements: {{requirements}} Warehouse: {{warehouse}} 1. Essential packages for every project: db... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Select and configure the right dbt packages for this project's needs.

Project requirements: {{requirements}}
Warehouse: {{warehouse}}

1. Essential packages for every project:

 dbt-utils:
 - Macros: generate_surrogate_key, union_relations, date_spine, pivot, unpivot
 - Tests: expression_is_true, recency, equal_rowcount
 - Install: calogica/dbt_utils >= 1.0.0

 dbt-expectations:
 - Port of Great Expectations for dbt
 - Tests: row count bounds, column value ranges, regex patterns, distribution checks

 Elementary:
 - Data observability and anomaly detection
 - Monitors: row count, null rates, freshness, distribution shifts
 - Sends Slack alerts; generates a data observability dashboard

2. Warehouse-specific packages:

 dbt-date (date utilities):
 - Fiscal calendars, date spine helpers, timezone conversions
 - Works across all warehouses

 dbt-audit-helper:
 - Compare two versions of a model to validate changes
 - compare_queries macro: finds rows in A not in B and vice versa
 - compare_column_values: per-column comparison statistics

3. Domain-specific packages:

 dbt-mrr (subscription metrics):
 - MRR, churn, expansion, contraction calculations from subscription data

 dbt-feature-store:
 - Generates ML feature tables from dbt models

4. Package configuration (packages.yml):
 packages:
 - package: dbt-labs/dbt_utils
 version: [">=1.1.0", "<2.0.0"]
 - package: calogica/dbt_expectations
 version: [">=0.10.0", "<0.11.0"]
 - package: elementary-data/elementary
 version: [">=0.13.0", "<0.14.0"]

5. Package governance:
 - Pin minor version ranges (not just major) to avoid unexpected breaking changes
 - Review changelog before upgrading any package
 - Run dbt build after package upgrades to verify no regressions

Return: recommended package set for the project requirements, packages.yml configuration, and upgrade governance policy. 
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

The AI should return a structured result that covers the main requested outputs, such as Essential packages for every project:, Macros: generate_surrogate_key, union_relations, date_spine, pivot, unpivot, Tests: expression_is_true, recency, equal_rowcount. The final answer should stay clear, actionable, and easy to review inside a dbt advanced patterns workflow for analytics engineer (dbt) work. 

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
