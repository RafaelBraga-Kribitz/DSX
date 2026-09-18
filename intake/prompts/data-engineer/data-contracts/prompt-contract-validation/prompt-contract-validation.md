# Contract Validation Pipeline *AI Prompt *

This prompt builds a gate that validates data against its contract before consumers can access it. It is useful for enforcing trust boundaries where producers must prove that schema, semantics, and freshness commitments were met on each run. The output should describe both validation behavior and promotion mechanics. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build an automated contract validation pipeline that verifies produced data meets all contract commitments before it is made available to consumers.

Data contract: {{contract_name}}

1. Validation gate architecture:
 - Produce data to a staging location (not the production table)
 - Run all contract validations against the staging data
 - Only promote to production if ALL blocking validations pass
 - If any blocking validation fails: halt, alert producer, do not expose data to consumers

2. Schema validation:
 - All required columns are present
 - All column data types match the contract definition
 - No unexpected new columns (flag as warning — possible unplanned schema evolution)

3. Semantic validation:
 - Primary key is unique and non-null
 - All NOT NULL columns have no nulls
 - All categorical columns contain only contract-defined values
 - Business rule assertions: {{business_rules}}

4. Freshness validation:
 - MAX(event_timestamp) is within the contract-defined freshness window
 - Row count is within ±{{tolerance}}% of the expected count for this time period

5. Promotion to production:
 - Atomic swap: rename staging table to production (or INSERT OVERWRITE the partition)
 - Log promotion: contract_name, run_id, validation_results, promotion_timestamp
 - Notify downstream consumers that fresh data is available (via event or polling endpoint)

6. Consumer-facing freshness endpoint:
 - GET /contracts/{{contract_name}}/freshness → returns: last_updated, row_count, validation_status
 - Consumers can poll this endpoint to know when new data is ready

Return: validation pipeline code, promotion logic, freshness endpoint spec, and consumer notification design. 
```

## When to use this prompt 
Use case 01 
When contract compliance must be enforced automatically. 
Use case 02 
When producers publish data to a staging area before release. 
Use case 03 
When consumers need confidence that fresh data is validated. 
Use case 04 
When a freshness endpoint or readiness signal is required. 

## What the AI should return 

Return the validation pipeline design, checks for schema and semantics, freshness rules, promotion logic, and freshness endpoint specification. Explain which failures block promotion and which produce warnings. Also include how consumers are notified that validated data is ready. 

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
