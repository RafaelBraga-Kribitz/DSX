# Automated Data Quality Framework *AI Prompt *

Build an automated data quality monitoring framework for this data platform. Technology stack: {{stack}} Data criticality tiers: {{tiers}} Alert channel: {{channel}} 1. DQ frame... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build an automated data quality monitoring framework for this data platform.

Technology stack: {{stack}}
Data criticality tiers: {{tiers}}
Alert channel: {{channel}}

1. DQ framework layers:

 Schema validation (at ingestion):
 - Verify column names, data types, and required columns match the expected schema
 - Fail-fast: reject malformed files before they corrupt downstream tables
 - Tool: Pydantic for Python pipelines, INFORMATION_SCHEMA checks, dbt source tests

 Completeness checks:
 - Row count: is the expected number of rows present?
 - Non-null rate: critical columns must be non-null
 - Coverage: all expected partitions present (no missing dates)

 Validity checks:
 - Range checks: values within expected bounds
 - Format checks: date formats, email regex, ID patterns
 - Referential integrity: foreign keys have matching primary keys

 Consistency checks:
 - Cross-table: revenue in the fact table matches sum of line items
 - Cross-period: today's metric is consistent with yesterday's (no >50% jump without explanation)
 - Aggregate invariants: sum(refunds) <= sum(gross_revenue) for any period

2. Tooling:
 - dbt tests: schema.yml tests (generic) + custom singular tests (business rules)
 - Great Expectations: Python-based; define expectations as code; integrates with Airflow
 - Soda Core: YAML-based quality checks; cloud platform for centralized results
 - Elementary: dbt-native anomaly detection; sends Slack alerts with dbt lineage context

3. DQ scoring:
 Compute a DQ score per table: (tests passing / total tests) × 100%
 Publish scores in the data catalog and on a DQ dashboard
 Alert: if any Tier 1 table drops below 95% DQ score

4. DQ SLA by tier:
 Tier 1 (executive-facing): 100% DQ tests must pass; alert immediately on failure
 Tier 2 (operational): 95% tests must pass; daily review of failures
 Tier 3 (exploratory): best effort; weekly DQ report

Return: DQ framework architecture, tooling selection, DQ scoring implementation, and SLA by tier. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin data quality operations work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Data Quality Operations or the wider DataOps Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as DQ framework layers:, Verify column names, data types, and required columns match the expected schema, Fail-fast: reject malformed files before they corrupt downstream tables. The final answer should stay clear, actionable, and easy to review inside a data quality operations workflow for dataops engineer work. 

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

Once you have the first result, continue deeper with related prompts in Data Quality Operations.
