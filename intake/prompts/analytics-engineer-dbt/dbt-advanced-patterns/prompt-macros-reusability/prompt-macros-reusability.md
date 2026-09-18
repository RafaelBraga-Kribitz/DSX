# dbt Macros and Reusability *AI Prompt *

Write reusable dbt macros for common transformation patterns in this project. Repetitive patterns identified: {{patterns}} (e.g. currency conversion, fiscal calendar, event dedu... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write reusable dbt macros for common transformation patterns in this project.

Repetitive patterns identified: {{patterns}} (e.g. currency conversion, fiscal calendar, event deduplication)
Warehouse: {{warehouse}}

1. Basic macro structure:
 {% macro cents_to_dollars(column_name, precision=2) %}
 ROUND({{ column_name }} / 100.0, {{ precision }})
 {% endmacro %}

 Usage in a model:
 SELECT {{ cents_to_dollars('amount_cents') }} AS amount_dollars

2. Deduplication macro (common pattern):
 {% macro deduplicate(relation, partition_by, order_by) %}
 SELECT *
 FROM (
 SELECT
 *,
 ROW_NUMBER() OVER (
 PARTITION BY {{ partition_by }}
 ORDER BY {{ order_by }} DESC
 ) AS _row_number
 FROM {{ relation }}
 )
 WHERE _row_number = 1
 {% endmacro %}

 Usage:
 {{ deduplicate(ref('stg_orders'), 'order_id', 'updated_at') }}

3. Date spine macro (dbt-utils built-in):
 {{ dbt_utils.date_spine(
 datepart='day',
 start_date=cast('2020-01-01' as date),
 end_date=cast(now() as date)
 ) }}

4. Generate surrogate key:
 {{ dbt_utils.generate_surrogate_key(['order_id', 'line_item_id']) }}
 - MD5 hash of concatenated key columns
 - Use as primary key for fact tables without a natural unique key

5. Star schema helper macros:
 - Union multiple tables of the same schema:
 {{ dbt_utils.union_relations(relations=[ref('orders_us'), ref('orders_eu')]) }}

 - Pivot rows to columns:
 {{ dbt_utils.pivot('metric_name', ['revenue', 'cost', 'profit'], agg='SUM', then_value='metric_value') }}

6. Macro testing:
 - Write a simple model that uses the macro and add generic tests on its output
 - Add a CI step: dbt compile → verify compiled SQL for macros is correct

Return: macro implementations for the identified patterns, usage examples, and testing approach. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin dbt advanced patterns work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in dbt Advanced Patterns or the wider Analytics Engineer (dbt) library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Basic macro structure:, Deduplication macro (common pattern):, Date spine macro (dbt-utils built-in):. The final answer should stay clear, actionable, and easy to review inside a dbt advanced patterns workflow for analytics engineer (dbt) work. 

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

Once you have the first result, continue deeper with related prompts in dbt Advanced Patterns.
