# Slowly Changing Dimension *AI Prompt *

This prompt builds a Type 2 Slowly Changing Dimension pattern for attributes that require full history. It is useful when descriptive records such as customers, products, or account metadata change over time and reporting must reflect both current and historical truth. The answer should separate tracked and non-tracked changes clearly. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement a Type 2 Slowly Changing Dimension (SCD2) for the table {{dim_table}} in {{database_type}}.

Natural key: {{natural_key}}
Tracked attributes (trigger new version): {{tracked_columns}}
Non-tracked attributes (overwrite in place): {{non_tracked_columns}}

1. Table design:
 - Add columns: surrogate_key (BIGINT IDENTITY), valid_from (DATE), valid_to (DATE), is_current (BOOLEAN)
 - valid_to for current rows = '9999-12-31' (sentinel value)
 - is_current = TRUE for current rows (redundant but improves query performance)

2. Initial load: INSERT all rows with valid_from = first_seen_date, valid_to = '9999-12-31', is_current = TRUE

3. Incremental merge logic:
 For each incoming row:
 a. NEW RECORD (natural key not in dim): INSERT with valid_from = today, valid_to = '9999-12-31', is_current = TRUE
 b. CHANGED RECORD (tracked columns differ from current version):
 - UPDATE existing current row: valid_to = today - 1, is_current = FALSE
 - INSERT new row: valid_from = today, valid_to = '9999-12-31', is_current = TRUE
 c. UNCHANGED RECORD: no action
 d. DELETED RECORD (exists in dim but not in source): optionally set is_current = FALSE

4. Point-in-time query:
 SELECT * FROM {{dim_table}} WHERE {{natural_key}} = 'X' AND valid_from <= '{{as_of_date}}' AND valid_to > '{{as_of_date}}'

5. Current records query:
 SELECT * FROM {{dim_table}} WHERE is_current = TRUE
 (Always faster than the date range query — index on is_current)

6. Non-tracked attribute updates: UPDATE current row in-place, no new version needed

Return: CREATE TABLE DDL, MERGE statement, point-in-time query, and current records query. 
```

## When to use this prompt 
Use case 01 
When dimension history must be preserved for point-in-time analytics. 
Use case 02 
When implementing SCD2 logic in a warehouse or dbt model. 
Use case 03 
When a team needs a reusable template for versioned dimensions. 
Use case 04 
When both current and as-of historical views are required. 

## What the AI should return 

Return the table DDL, incremental SCD2 load logic, and example queries for current and point-in-time records. Clearly show how new, changed, unchanged, and optionally deleted records are handled. Include notes on performance, indexing, and how non-tracked attributes are updated in place. 

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

Once you have the first result, continue deeper with related prompts in Data Warehouse Patterns.
