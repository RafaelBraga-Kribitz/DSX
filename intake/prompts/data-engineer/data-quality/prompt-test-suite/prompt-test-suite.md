# Data Quality Test Suite *AI Prompt *

This prompt creates a complete data quality testing package for a table, combining structural, freshness, consistency, and business-rule checks. It helps standardize what ‘good data’ means and how failures should be treated operationally. It is most useful when a team wants repeatable automated checks rather than manual spot checks. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write a comprehensive data quality test suite for the table {{table_name}}.

Use dbt tests, Great Expectations, or SQL assertions (specify preference: {{testing_tool}}).

1. Schema tests (run on every load):
 - All NOT NULL columns contain no nulls
 - Primary key is unique and not null
 - Foreign keys reference valid records in parent tables
 - Categorical columns contain only accepted values
 - Numeric columns are within expected ranges (no negative IDs, no future dates)

2. Freshness tests (run on every load):
 - Max(updated_at) is within {{freshness_threshold}} hours of current time
 - Row count is within [mean ± 3σ] of the historical daily row count
 - No date partition has zero rows (empty partitions indicate pipeline failure)

3. Consistency tests (run daily):
 - Row count in this table matches row count in the source system (reconciliation)
 - SUM of key measures matches source system totals (financial reconciliation)
 - No duplicate rows on the natural key

4. Business rule tests (run daily):
 - Specific rules from the domain: {{business_rules}}
 - Example: order_total = SUM(line_items) for all orders
 - Example: all active customers have at least one contact record

5. Test severity levels:
 - ERROR: test failure blocks downstream tables from running
 - WARN: test failure logs a warning but does not block
 - Assign each test to the appropriate severity level

Return: complete test suite code, severity assignments, and a test execution schedule. 
```

## When to use this prompt 
Use case 01 
When adding DQ coverage for a critical table. 
Use case 02 
When choosing between dbt, Great Expectations, or SQL assertions. 
Use case 03 
When pipeline failures should be blocked by quality gates. 
Use case 04 
When you want both tests and a run schedule with severity levels. 

## What the AI should return 

Return the full test suite in the requested tool or framework, with each test labeled ERROR or WARN. Include schema tests, freshness checks, reconciliations, and business rules, plus when each test should run. End with a concise execution schedule and notes on which failures should block downstream jobs. 

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

Once you have the first result, continue deeper with related prompts in Data Quality.
