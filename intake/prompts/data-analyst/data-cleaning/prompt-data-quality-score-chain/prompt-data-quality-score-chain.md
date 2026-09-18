# Data Quality Score Chain *AI Prompt *

Data Quality Score Chain is a advanced chain for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is structured as a multi-step chain so the AI can reason through the problem in a deliberate order and produce a more complete result. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Assess completeness — calculate the percentage of non-null values across all columns and rows. Score: (non-null cells / total cells) × 100.
Step 2: Assess consistency — count type mismatches, formatting inconsistencies, and constraint violations. Score: 100 minus one point per violation type found.
Step 3: Assess uniqueness — count exact duplicate rows and near-duplicate rows. Score: (unique rows / total rows) × 100.
Step 4: Assess validity — count values that fail domain rules (impossible numbers, invalid dates, unexpected categoricals). Score: (valid rows / total rows) × 100.
Step 5: Compute an overall Data Quality Score as a weighted average: completeness 30%, consistency 25%, uniqueness 20%, validity 25%.
Step 6: Return a one-page Data Quality Report: score per dimension, overall score, top 5 issues to fix, and estimated effort to resolve each. 
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
