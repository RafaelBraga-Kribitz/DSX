# Impossible Value Detector *AI Prompt *

Impossible Value Detector is a beginner prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Scan this dataset for values that are logically impossible or highly implausible:

1. Numeric impossibilities: negative ages, negative prices, quantities above a plausible maximum, percentages above 100 or below 0
2. Date impossibilities: future dates in historical columns, dates before the business existed, end dates before start dates
3. Cross-column contradictions: e.g. refund amount greater than original order amount, child account older than parent account
4. Statistical implausibility: values more than 6 standard deviations from the mean (not just outliers — true anomalies)

For each impossible value found: column, row index, value, why it is impossible, and recommended fix. 
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
