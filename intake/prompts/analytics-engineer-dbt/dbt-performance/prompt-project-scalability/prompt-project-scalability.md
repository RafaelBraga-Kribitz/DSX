# dbt Project Scalability *AI Prompt *

Scale this dbt project to support a growing team and larger data volumes. Current project size: {{model_count}} models, {{team_size}} engineers Pain points: {{pain_points}} (slo... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Scale this dbt project to support a growing team and larger data volumes.

Current project size: {{model_count}} models, {{team_size}} engineers
Pain points: {{pain_points}} (slow CI, difficult navigation, merge conflicts, inconsistent standards)
Warehouse: {{warehouse}}

1. Multi-project architecture (dbt mesh):
 Split the monorepo into multiple smaller dbt projects connected via cross-project refs:
 - Platform project: shared staging and dimension models consumed by all
 - Domain projects: finance, marketing, product — each with their own team and release cycle
 - Cross-project ref: {{ ref('platform', 'dim_customers') }}
 Benefits: independent deployments, clear ownership, faster CI (smaller projects)

2. Model governance with groups and contracts:

 Groups (assign ownership):
 groups:
 - name: finance
 owner:
 name: Finance Analytics Team
 email: finance-analytics@company.com

 Model contract (enforce public model schema):
 models:
 - name: fct_revenue
 group: finance
 access: public # can be referenced from other projects
 config:
 contract:
 enforced: true # CI fails if schema drifts
 columns:
 - name: revenue_usd
 data_type: numeric

3. Slim CI for large projects:
 - Use dbt state artifacts to run only modified models and their dependents
 - Target: CI time < 10 minutes regardless of project size
 - Store production manifest.json in S3; download in CI as the comparison state

4. Model access levels:
 - private: only accessible within the same group/project
 - protected: accessible from the same project
 - public: can be referenced cross-project
 Enforce: downstream teams can only depend on public models

5. Style guide enforcement:
 - sqlfluff: SQL linter with dbt dialect support
 sqlfluff lint models/ --dialect snowflake
 - pre-commit hooks: run sqlfmt, sqlfluff, and yamllint before every commit
 - Standardized model config template in .dbt/config.yml

Return: dbt mesh architecture design, contract enforcement setup, slim CI configuration, access level policy, and style guide tooling. 
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

The AI should return a structured result that covers the main requested outputs, such as Multi-project architecture (dbt mesh):, Platform project: shared staging and dimension models consumed by all, Domain projects: finance, marketing, product — each with their own team and release cycle. The final answer should stay clear, actionable, and easy to review inside a dbt performance workflow for analytics engineer (dbt) work. 

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
