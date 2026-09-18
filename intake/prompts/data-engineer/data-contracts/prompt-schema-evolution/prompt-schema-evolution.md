# Schema Evolution Strategy *AI Prompt *

This prompt defines how schemas can evolve safely over time without breaking downstream consumers unexpectedly. It helps classify changes by compatibility, define registry rules, enforce additive-first practices, and handle unavoidable breaking changes with versioning. The response should feel like a policy plus an implementation pattern. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a schema evolution strategy that allows the {{producer_team}} to evolve data schemas without breaking downstream consumers.

1. Compatible change classification:
 BACKWARD COMPATIBLE (consumers with old schema can read new data):
 - Adding a new optional column with a default value
 - Widening a type (INT → BIGINT, VARCHAR(50) → VARCHAR(255))
 - Adding a new enum value to a categorical column

 FORWARD COMPATIBLE (consumers with new schema can read old data):
 - Removing a column (old data will have the column, new data won't)
 - Narrowing a type (consumers must handle both)

 BREAKING (requires coordinated migration):
 - Removing a required column
 - Renaming a column
 - Changing a type in a non-widening way (VARCHAR → INT)
 - Changing the meaning of an existing column
 - Changing the grain of the table

2. Schema registry:
 - Register every schema version with its compatibility mode in Confluent Schema Registry or AWS Glue
 - Default compatibility mode: BACKWARD (new schema must be able to read old data)
 - Enforce compatibility checks on every schema change before deployment

3. Additive-first approach:
 - Prefer adding new columns over renaming or replacing existing ones
 - Deprecate columns by marking them in the schema comment before removing
 - Retain deprecated columns for {{deprecation_period}} before removing

4. Versioned tables:
 - For breaking changes that cannot be avoided: publish a new versioned table (orders_v2)
 - Run v1 and v2 in parallel for {{parallel_period}} to allow consumers to migrate
 - Provide a migration guide and migration deadline

5. Consumer notification workflow:
 - Automated notification to all registered consumers when schema changes are registered
 - For breaking changes: personal outreach to each consumer team, migration support offered

Return: change classification guide, schema registry setup, deprecation process, and versioned table migration procedure. 
```

## When to use this prompt 
Use case 01 
When producer teams need a safe schema evolution policy. 
Use case 02 
When consumers depend on stable structures over time. 
Use case 03 
When setting up schema registry compatibility rules. 
Use case 04 
When versioned table migration may be needed for breaking changes. 

## What the AI should return 

Return a change-classification guide, schema-registry configuration approach, deprecation workflow, and versioned-table migration process. Clearly label backward-compatible, forward-compatible, and breaking changes with examples. Include consumer notification rules and retention periods for deprecated fields. 

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
