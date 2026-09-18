# Data Quality Red Flags *AI Prompt *

Review this dataset for data quality issues that could lead me to wrong conclusions if I do not address them first. I am not a data engineer — I need you to explain each issue i... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Review this dataset for data quality issues that could lead me to wrong conclusions if I do not address them first.

I am not a data engineer — I need you to explain each issue in plain terms and tell me what to do about it.

1. Completeness problems:
 - Which columns are missing data, and how many rows are affected?
 - For each column with significant missing data (more than 5%): could the missing values be a problem, or is it normal for that field to be blank?
 - Is there a pattern to what is missing? (e.g. missing values are concentrated in one region or time period — that is more concerning than random gaps)

2. Accuracy problems:
 - Are there values that look impossible? (negative quantities, prices of $0 on paid products, ages of 150, dates in the future)
 - Are there values that are technically possible but suspiciously unlikely? (every sale is exactly $100, all customer ages are round numbers)
 - Are there columns where the same thing is written in different ways? ('New York', 'new york', 'NY', 'N.Y.' — these are all the same but will be counted separately)

3. Consistency problems:
 - If the same information appears in multiple columns, do they agree with each other?
 - Are there rows where related columns contradict each other? (an order with a delivery date before the order date)

4. Duplicates:
 - Are there exact duplicate rows that should not exist?
 - Are there near-duplicates — the same customer or order appearing twice with slightly different details?

5. What to do:
 For each issue found, tell me:
 - How serious it is: will this issue mislead my analysis (serious) or is it minor (cosmetic)?
 - What I should do before I analyze: fix it, exclude affected rows, note it as a caveat, or ignore it safely
 - How to describe this limitation honestly when I share my findings 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin exploratory analysis work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Exploratory Analysis or the wider Citizen Data Scientist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Completeness problems:, Which columns are missing data, and how many rows are affected?, For each column with significant missing data (more than 5%): could the missing values be a problem, or is it normal for that field to be blank?. The final answer should stay clear, actionable, and easy to review inside a exploratory analysis workflow for citizen data scientist work. 

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

Once you have the first result, continue deeper with related prompts in Exploratory Analysis.
