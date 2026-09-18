# Date and Time Standardization *AI Prompt *

Date and Time Standardization is a intermediate prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Standardize all date and time columns in this dataset:

1. Identify every column that contains dates or times, including those stored as strings
2. Detect all date format variations in use (e.g. 'MM/DD/YYYY', 'DD-Mon-YYYY', 'YYYY-MM-DD', Unix timestamps)
3. Convert all date columns to a single standard format: ISO 8601 (YYYY-MM-DD for dates, YYYY-MM-DDTHH:MM:SS for datetimes)
4. Handle timezone information: identify columns with mixed timezones and convert all to UTC
5. Extract useful components as new columns where relevant: year, month, day_of_week, hour, is_weekend
6. Flag any ambiguous dates where format is unclear (e.g. 01/02/03 could be Jan 2, 2003 or Feb 1, 2003)

Return the conversion code and a before/after sample for each date column. 
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
