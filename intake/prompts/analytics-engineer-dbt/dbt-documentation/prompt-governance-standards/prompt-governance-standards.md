# dbt Governance and Standards *AI Prompt *

Establish governance standards and engineering practices for a dbt project used by multiple teams. Team: {{team_description}} Project maturity: {{maturity}} (early/growing/matur... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Establish governance standards and engineering practices for a dbt project used by multiple teams.

Team: {{team_description}}
Project maturity: {{maturity}} (early/growing/mature)
Stakeholders: {{stakeholders}}

1. Model ownership policy:
 - Every model must have an owner defined in the meta field
 - Owner is responsible for: test coverage, documentation, SLA compliance, and responding to data quality alerts
 - Review ownership quarterly; transfer ownership when team membership changes

2. PR review checklist:
 Before approving any PR that adds or modifies a model:
 ☐ Model has a description in schema.yml
 ☐ All columns documented
 ☐ Primary key has unique + not_null tests
 ☐ Foreign keys have relationships tests
 ☐ Business rule tests present for critical logic
 ☐ Model uses ref() not raw SQL table references
 ☐ Naming conventions followed (stg_/int_/fct_/dim_)
 ☐ Materialization appropriate for the model size and usage pattern

3. Breaking change policy:
 Public models (consumed by other teams or BI tools) require:
 - 2-week deprecation notice before removing a column
 - Use of the deprecated config flag + a migration guide in the description
 - Announcement in the #data-announcements channel

4. Data SLA tiers:
 Tier 1 (critical, exec-facing): freshness SLA = 4 hours; test failures → immediate alert
 Tier 2 (operational): freshness SLA = 24 hours; test failures → next-business-day response
 Tier 3 (exploratory): best effort; test failures → weekly triage

5. Documentation completeness score:
 Compute: models with descriptions / total models
 Target: > 90% for Tier 1 models, > 70% overall
 Track in a dbt model: query the dbt catalog artifact to measure coverage

Return: ownership policy, PR checklist, breaking change SLA, tier definitions, and documentation coverage tracking approach. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin dbt documentation work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in dbt Documentation or the wider Analytics Engineer (dbt) library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Model ownership policy:, Every model must have an owner defined in the meta field, Owner is responsible for: test coverage, documentation, SLA compliance, and responding to data quality alerts. The final answer should stay clear, actionable, and easy to review inside a dbt documentation workflow for analytics engineer (dbt) work. 

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

Once you have the first result, continue deeper with related prompts in dbt Documentation.
