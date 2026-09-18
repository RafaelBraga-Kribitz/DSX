# Referential Integrity Check *AI Prompt *

Referential Integrity Check is a intermediate prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Check referential integrity across the tables or joined datasets provided:

1. Identify all foreign key – primary key relationships between tables
2. For each relationship, count:
 - Orphaned records: foreign key values with no matching primary key
 - Unmatched primary keys: records in the parent table with no children
3. Calculate the match rate for each join: what percentage of records join successfully?
4. Show examples of orphaned records and identify the most common missing foreign key values
5. Assess the impact: if orphaned records are dropped, what percentage of rows would be lost from each table?

Return an integrity report table and recommend whether to: drop orphans, impute, or flag for manual review. 
```

## When to use this prompt 
Use case 01 
When the dataset contains missing values, inconsistent formatting, or suspicious records. 
Use case 02 
When analysis results look unreliable and you need to validate the raw data first. 
Use case 03 
When you are preparing data for dashboards, machine learning, or SQL pipelines. 
Use case 04 
When you need a documented cleaning plan rather than ad hoc fixes. 

## What the AI should return 

The AI should return a practical cleaning assessment with issue-by-issue recommendations or actions, ideally in tables and clearly labeled sections. It should explain what was found, why it matters, and what fix is recommended or applied for each column or record type. When code is requested, the code should be runnable and aligned with the decisions described in the narrative. The final output should make the cleaning process auditable and easy to implement. 

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

Once you have the first result, continue deeper with related prompts in Data Cleaning.
