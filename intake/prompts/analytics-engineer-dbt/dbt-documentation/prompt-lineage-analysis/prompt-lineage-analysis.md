# dbt Lineage and Impact Analysis *AI Prompt *

Analyze data lineage and assess the impact of a proposed change in this dbt project. Proposed change: {{change_description}} (e.g. rename column, change grain, drop a staging mo... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze data lineage and assess the impact of a proposed change in this dbt project.

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

Return: downstream impact list, safe change process, breaking change checklist, and state-based CI configuration. 
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

The AI should return a structured result that covers the main requested outputs, such as Understanding dbt lineage:, Impact analysis commands:, Safe column rename process:. The final answer should stay clear, actionable, and easy to review inside a dbt documentation workflow for analytics engineer (dbt) work. 

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
