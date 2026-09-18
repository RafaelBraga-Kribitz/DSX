# Data Contract Definition *AI Prompt *

This prompt creates a formal data contract that defines what a dataset is, what it means, how fresh and accurate it will be, and how changes are managed. It is useful when producer and consumer teams need explicit expectations instead of informal assumptions. The contract should be precise enough to support governance and automation. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write a data contract for the dataset: {{dataset_name}} produced by the {{producer_team}} team and consumed by {{consumer_teams}}.

A data contract is a formal agreement between data producers and consumers specifying what data will be delivered, in what format, with what quality guarantees, and on what schedule.

1. Dataset identity:
 - Dataset name and version
 - Producer: team, contact, and escalation path
 - Consumers: teams currently depending on this dataset

2. Schema definition:
 - Table or topic name
 - For each column/field: name, data type, nullable (Y/N), description, example value, PII classification (Y/N)
 - Primary key or unique identifier
 - Partitioning columns

3. Semantics and business rules:
 - Grain: what does one row represent?
 - Business rules: constraints and derived logic (e.g. 'order_total is always the sum of line items')
 - Key relationships to other datasets

4. Quality commitments:
 - Completeness: which columns are guaranteed non-null?
 - Uniqueness: which column combinations are guaranteed unique?
 - Freshness: data will be available by {{sla_time}} on each {{frequency}}
 - Accuracy: key measures are reconciled to source within {{tolerance}}

5. Change management:
 - Breaking change definition: removed column, type change, semantic change
 - Notice period: {{notice_period}} days notice required before a breaking change
 - Deprecation process: how will consumers be notified and given time to migrate?

6. SLA and support:
 - Incident response time: {{response_time}}
 - Scheduled maintenance window: {{maintenance_window}}
 - Where to report issues: {{issue_channel}}

Return: complete data contract document in YAML format. 
```

## When to use this prompt 
Use case 01 
When publishing a dataset for multiple downstream consumers. 
Use case 02 
When introducing producer-consumer accountability in a platform. 
Use case 03 
When freshness, quality, and change guarantees must be documented. 
Use case 04 
When you want a machine-readable contract format such as YAML. 

## What the AI should return 

Return a complete YAML data contract covering identity, schema, grain, business rules, quality commitments, change management, and support details. Ensure required fields, SLA language, and breaking-change definitions are explicit. The output should be ready to store in version control or a registry. 

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

Once you have the first result, continue deeper with related prompts in Data Contracts.
