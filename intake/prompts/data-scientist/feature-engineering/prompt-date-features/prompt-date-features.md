# Date Feature Extraction *AI Prompt *

This prompt turns raw date and datetime columns into practical model-ready features. It is useful when temporal information exists but has not yet been decomposed into parts that models can learn from easily. It also encourages creation of interval features when multiple time columns exist. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Extract all useful features from the date and datetime columns in this dataset.

For each date column, create:
- year, month, day, day_of_week (0=Monday), day_of_year
- quarter, week_of_year
- is_weekend (boolean)
- is_month_start, is_month_end (boolean)
- is_quarter_start, is_quarter_end (boolean)
- days_since_epoch (numeric, for ordinal encoding)
- If the column is a datetime: hour, minute, part_of_day (morning/afternoon/evening/night)

Also compute time-difference features if multiple date columns exist:
- days_between_[col1]_and_[col2] for all meaningful pairs

Return the feature creation code in pandas and a list of all new column names created. 
```

## When to use this prompt 
Use case 01 
The dataset contains one or more date or timestamp columns. 
Use case 02 
You want fast, leakage-safe temporal feature extraction in pandas. 
Use case 03 
You need a complete list of standard calendar features without missing important ones. 
Use case 04 
You want reproducible feature code rather than only conceptual suggestions. 

## What the AI should return 

Pandas code that creates all relevant date-derived columns, a clear list of every new feature generated, and notes on any pairwise time-difference features created from multiple date columns. 

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

Once you have the first result, continue deeper with related prompts in Feature Engineering.
