# Data Lineage Implementation *AI Prompt *

Implement data lineage tracking for this data platform. Stack: {{stack}} Lineage granularity needed: {{granularity}} (table-level, column-level) Compliance driver: {{compliance}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement data lineage tracking for this data platform.

Stack: {{stack}}
Lineage granularity needed: {{granularity}} (table-level, column-level)
Compliance driver: {{compliance}} (GDPR data subject access, SOX auditability, debugging)

1. Why data lineage:
 - Debugging: trace a data quality issue from symptom to root cause
 - Impact analysis: understand which downstream tables are affected before making a change
 - Compliance: demonstrate to auditors where sensitive data originates and how it flows
 - Trust: data consumers know where the data came from and can assess its reliability

2. Lineage collection methods:

 SQL parsing (static):
 - Parse SQL transformations to extract table-level dependencies
 - dbt: automatically builds column-level lineage from SQL ref() and source() calls
 - Limitation: cannot capture runtime/dynamic SQL lineage

 Runtime instrumentation (dynamic):
 - Instrument Spark jobs to emit OpenLineage events
 - OpenLineage: open standard for lineage events; Spark integration via openlineage-spark
 - Collect events in Marquez (open-source) or DataHub

3. OpenLineage with Airflow:
 Install: pip install openlineage-airflow
 Configure: AIRFLOW__OPENLINEAGE__TRANSPORT = '{"type": "http", "url": "http://marquez:5000"}'
 Automatically emits: job start/end, input datasets, output datasets, run metadata

4. Column-level lineage (via dbt):
 - dbt automatically traces column references through SQL
 - Elementary: exposes column-level lineage via dbt artifacts
 - Enable: generate_column_lineage: true in dbt_project.yml (dbt 1.6+)

5. Lineage graph use cases:
 - 'What does this PII column feed into?' → identify all tables containing derived PII
 - 'If I drop this column from orders, what breaks?' → find all downstream references
 - 'Where did this null value come from?' → walk the lineage backwards from the symptom

Return: lineage collection architecture, OpenLineage configuration, dbt column lineage setup, and lineage use case examples. 
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

The AI should return a structured result that covers the main requested outputs, such as Why data lineage:, Debugging: trace a data quality issue from symptom to root cause, Impact analysis: understand which downstream tables are affected before making a change. The final answer should stay clear, actionable, and easy to review inside a data quality operations workflow for dataops engineer work. 

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
