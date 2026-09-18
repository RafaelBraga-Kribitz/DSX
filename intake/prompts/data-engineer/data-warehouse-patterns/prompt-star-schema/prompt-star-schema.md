# Star Schema Design *AI Prompt *

This prompt designs a dimensional model centered on a business process and the questions analysts need to answer. It helps define grain, measures, dimensions, hierarchies, and surrogate keys in a way that supports performant analytics. The output should be practical enough to guide implementation, not just conceptual modeling. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a star schema for this business process: {{business_process}}

Source data: {{source_tables}}
Key business questions to answer: {{business_questions}}

1. Fact table design:
 - Identify the grain: what does one row represent? (e.g. one order line, one daily session, one claim)
 - State the grain explicitly — this is the most important design decision
 - Numeric measures: what is being measured? (revenue, quantity, duration, count)
 - Additive vs semi-additive vs non-additive measures:
 - Additive: sum across all dimensions (revenue, quantity)
 - Semi-additive: can sum across some dimensions but not time (account balance)
 - Non-additive: cannot sum at all (ratios, percentages — store numerator and denominator instead)
 - Foreign keys: one surrogate key per dimension
 - Degenerate dimensions: order_number, invoice_number (store in fact, no separate dim)

2. Dimension tables:
 - For each dimension: list the descriptive attributes
 - Surrogate key (integer) as primary key — never use the source system natural key as PK
 - Include the source natural key as an attribute for traceability
 - Slowly changing dimension type per attribute: Type 1 (overwrite), Type 2 (version), Type 3 (keep prior)

3. Dimension hierarchies:
 - Identify rollup hierarchies within each dimension (product → category → department)
 - Flatten hierarchy into the dimension table (denormalized) for query performance

4. Date dimension:
 - Always include a date dimension — never join on raw date columns
 - Generate one row per day for a 10-year range minimum
 - Include: date_key, full_date, year, quarter, month, week, day_of_week, is_weekend, is_holiday, fiscal_period

Return: fact table DDL, dimension table DDLs, date dimension generation SQL, and ER diagram (text). 
```

## When to use this prompt 
Use case 01 
When designing a warehouse model for reporting and BI. 
Use case 02 
When a source system must be translated into fact and dimension tables. 
Use case 03 
When stakeholders need clarity on the grain of analysis. 
Use case 04 
When you want DDL and a text ER representation, not only design notes. 

## What the AI should return 

Return a star schema design with an explicit fact grain, measures, dimension tables, hierarchy guidance, and a date dimension. Include fact and dimension DDLs plus a simple text ER diagram. Also explain any semi-additive or non-additive measures and how they should be represented. 

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
