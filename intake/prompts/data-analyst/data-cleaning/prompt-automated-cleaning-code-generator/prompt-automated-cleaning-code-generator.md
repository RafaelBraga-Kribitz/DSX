# Automated Cleaning Code Generator *AI Prompt *

Automated Cleaning Code Generator is a advanced prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze this dataset and generate a complete, production-ready Python cleaning script.

The script must:
1. Load the data
2. Fix all data type issues (with explicit dtype mapping)
3. Handle all missing values with the appropriate strategy per column
4. Remove or flag duplicate rows
5. Apply all string standardizations needed
6. Fix date columns to ISO 8601 format
7. Clip or remove outliers where appropriate
8. Assert data quality at the end: row count within expected range, no nulls in key columns, all dates in valid range

Code style requirements:
- Use pandas
- Add a comment above every transformation explaining why it is needed
- Include a final print() summary: rows before, rows after, columns changed
- Make the script idempotent — safe to run multiple times 
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
