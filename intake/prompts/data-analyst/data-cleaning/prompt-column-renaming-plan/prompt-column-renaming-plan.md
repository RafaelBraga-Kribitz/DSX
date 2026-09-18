# Column Renaming Plan *AI Prompt *

Column Renaming Plan is a beginner prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Review all column names in this dataset and produce a renaming plan:

1. Identify columns that violate snake_case convention (spaces, camelCase, PascalCase, hyphens, special characters)
2. Identify columns with unclear or ambiguous abbreviations (e.g. 'qty', 'amt', 'dt', 'flg')
3. Identify columns where the name doesn't match the apparent content based on sample values
4. Propose a clear, descriptive snake_case name for each column that needs renaming

Return a table: original_name | issue | proposed_name | reason
Also return a Python code snippet using df.rename() to apply all changes at once. 
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
