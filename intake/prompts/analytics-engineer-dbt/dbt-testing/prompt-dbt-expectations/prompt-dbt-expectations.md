# dbt-expectations Test Suite *AI Prompt *

Implement advanced data quality tests using the dbt-expectations package. Model: {{model_name}} Quality requirements: {{requirements}} (SLA, business rules, statistical threshol... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement advanced data quality tests using the dbt-expectations package.

Model: {{model_name}}
Quality requirements: {{requirements}} (SLA, business rules, statistical thresholds)

1. Install dbt-expectations:
 packages.yml:
 packages:
 - package: calogica/dbt_expectations
 version: [">=0.10.0", "<0.11.0"]

2. Column value tests:

 Numeric range:
 - dbt_expectations.expect_column_values_to_be_between:
 min_value: 0
 max_value: 1000000
 strictly: false

 Non-negative:
 - dbt_expectations.expect_column_values_to_be_positive:
 severity: error

 String pattern (regex):
 - dbt_expectations.expect_column_values_to_match_regex:
 regex: '^[A-Z]{2}-[0-9]{6}$'

 Date range:
 - dbt_expectations.expect_column_values_to_be_of_type:
 column_type: date

3. Table-level tests:

 Row count bounds:
 - dbt_expectations.expect_table_row_count_to_be_between:
 min_value: 1000
 max_value: 10000000

 Column count:
 - dbt_expectations.expect_table_column_count_to_equal:
 value: 15

 Schema completeness:
 - dbt_expectations.expect_table_columns_to_contain_set:
 column_list: ['order_id', 'customer_id', 'order_amount_usd', 'order_date']

4. Distribution tests:

 Proportion of null values:
 - dbt_expectations.expect_column_proportion_of_unique_values_to_be_between:
 min_value: 0.95
 max_value: 1.0

 Mean value range (catches data quality regressions):
 - dbt_expectations.expect_column_mean_to_be_between:
 min_value: 50
 max_value: 500

5. Cross-column tests:
 - dbt_expectations.expect_column_pair_values_A_to_be_greater_than_B:
 column_A: total_amount
 column_B: discount_amount
 or_equal: true

Return: complete schema.yml with dbt-expectations tests, severity assignments, and interpretation of each test's business meaning. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin dbt testing work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in dbt Testing or the wider Analytics Engineer (dbt) library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Install dbt-expectations:, package: calogica/dbt_expectations, Column value tests:. The final answer should stay clear, actionable, and easy to review inside a dbt testing workflow for analytics engineer (dbt) work. 

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

Once you have the first result, continue deeper with related prompts in dbt Testing.
