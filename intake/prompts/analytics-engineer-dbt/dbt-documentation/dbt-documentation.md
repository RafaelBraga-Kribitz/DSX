# dbt Documentation *AI Prompts *

3 Analytics Engineer (dbt) prompts in dbt Documentation. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 3 single prompts. 

## AI prompts in dbt Documentation 
3 prompts Advanced Single prompt 01 
### dbt Governance and Standards 

Establish governance standards and engineering practices for a dbt project used by multiple teams. Team: {{team_description}} Project maturity: {{maturity}} (early/growing/matur... 
Prompt text Establish governance standards and engineering practices for a dbt project used by multiple teams.

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

Return: ownership policy, PR checklist, breaking change SLA, tier definitions, and documentation coverage tracking approach. Copy prompt Open prompt details Intermediate Single prompt 02 
### dbt Lineage and Impact Analysis 

Analyze data lineage and assess the impact of a proposed change in this dbt project. Proposed change: {{change_description}} (e.g. rename column, change grain, drop a staging mo... 
Prompt text Analyze data lineage and assess the impact of a proposed change in this dbt project.

Proposed change: {{change_description}} (e.g. rename column, change grain, drop a staging model)
Affected model: {{affected_model}}
Warehouse: {{warehouse}}

1. Understanding dbt lineage:
 dbt automatically builds a DAG (Directed Acyclic Graph) from all ref() and source() calls.
 Every model knows its parents (models it depends on) and children (models that depend on it).

2. Impact analysis commands:

 Find all downstream dependents:
 dbt ls --select fct_orders+ # all models downstream of fct_orders
 dbt ls --select +fct_orders # all models upstream of fct_orders
 dbt ls --select +fct_orders+ # full lineage in both directions

 Identify exposed models (BI-facing):
 dbt ls --select fct_orders+ --resource-type exposure

 Check which metrics depend on a column:
 dbt ls --select metric:* # list all defined metrics

3. Safe column rename process:
 Step 1: Add the new column with the new name alongside the old one
 Step 2: Deploy; validate downstream models use the new name
 Step 3: Remove the old column in the next deployment
 Never: rename a column and deploy in a single step without checking downstream

4. Breaking change checklist:
 Before merging any change to a widely-used mart model:
 ☐ Run: dbt ls --select {model}+ to list all downstream models
 ☐ Check: are any downstream models used in BI dashboards or exported to external systems?
 ☐ Notify: owners of affected downstream models
 ☐ Test: run full dbt build --select {model}+ in a dev schema
 ☐ Document: add a changelog entry to the model description

5. State-based CI (dbt Cloud / dbt Core):
 dbt build --select state:modified+
 - Only builds models that changed AND their downstream dependents
 - Dramatically faster CI than running the full project
 - Requires: dbt state artifacts from the last production run

Return: downstream impact list, safe change process, breaking change checklist, and state-based CI configuration. Copy prompt Open prompt details Beginner Single prompt 03 
### dbt Model Documentation 

Write comprehensive dbt documentation for this model. Model name: {{model_name}} Layer: {{layer}} (staging, intermediate, mart) Grain: {{grain}} Key columns: {{columns}} Upstrea... 
Prompt text Write comprehensive dbt documentation for this model.

Model name: {{model_name}}
Layer: {{layer}} (staging, intermediate, mart)
Grain: {{grain}}
Key columns: {{columns}}
Upstream models: {{upstream}}

1. Model-level description:
 models:
 - name: fct_orders
 description: |
 Fact table capturing all customer orders at the order grain.
 One row per unique order. Includes financial metrics, fulfillment
 status, and customer and product dimension keys for joining.
 Source: {{ source('app', 'orders') }} joined with shipping data.
 Grain: one row per order_id.
 Refresh: incremental, daily at 06:00 UTC.
 Owner: Data team (analytics-eng@company.com)

2. Column-level documentation:
 columns:
 - name: order_id
 description: Unique identifier for each order. Primary key.
 tests: [unique, not_null]
 - name: customer_id
 description: Foreign key to dim_customers. The customer who placed the order.
 tests:
 - relationships:
 to: ref('dim_customers')
 field: customer_id
 - name: order_amount_usd
 description: |
 Total order value in USD at time of order, inclusive of all line items
 and exclusive of shipping fees and taxes. Negative values indicate refunds.

3. Meta fields for data catalog integration:
 meta:
 owner: 'analytics-engineering'
 domain: 'finance'
 tier: 'gold'
 pii: false
 sla_hours: 4

4. Tags for organization:
 config:
 tags: ['finance', 'daily', 'mart']

5. Generating and hosting docs:
 dbt docs generate → builds the catalog.json artifact
 dbt docs serve → local documentation site
 For production: host the generated docs/ folder on:
 - dbt Cloud: built-in docs hosting
 - GitHub Pages or Netlify (static site deployment)
 - Internal data catalog (DataHub, Atlan, Alation) via dbt artifact import

Return: complete schema.yml entry for the model, column documentation, meta fields, and documentation hosting recommendation. Copy prompt Open prompt details 
## Recommended dbt Documentation workflow 
1 
### dbt Governance and Standards 

Start with a focused prompt in dbt Documentation so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### dbt Lineage and Impact Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### dbt Model Documentation 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
