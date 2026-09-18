# Bivariate Relationship Analysis *AI Prompt *

Bivariate Relationship Analysis is a intermediate prompt for data exploration. This prompt helps the user understand the structure, meaning, and analytical potential of a dataset before moving into deeper work. It is designed to surface what is in the data, how trustworthy it looks, and which columns, relationships, or patterns deserve attention first. Use it early in an analysis workflow to reduce guesswork and create a shared understanding of the dataset. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze pairwise relationships between the key variables in this dataset:

1. Identify the most important target or outcome variable
2. For each other numeric column, create a scatter plot vs the target variable and compute the correlation coefficient
3. For each categorical column, show the mean target value per category (group-by analysis)
4. Flag any non-linear relationships that a correlation coefficient would miss
5. Identify the single variable that has the strongest relationship with the target, linear or otherwise
6. Note any interaction effects — pairs of variables that together predict the target better than either alone

Return a ranked list of variables by predictive relationship strength. 
```

## When to use this prompt 
Use case 01 
When you have a new dataset and need a fast but structured first assessment. 
Use case 02 
When you want to understand columns, grain, date coverage, or basic quality before analysis. 
Use case 03 
When you need to decide which variables are worth deeper investigation. 
Use case 04 
When you want a repeatable starting point for exploratory data analysis. 

## What the AI should return 

The AI should return a structured analysis of the dataset, using clear headings, compact tables where useful, and a short narrative that explains the main takeaways. It should explicitly call out quality issues, notable patterns, and any assumptions it had to make about the data. Where the prompt asks for calculations or plots, those should be included with concise interpretation. The final answer should help the user understand both what the data contains and what to inspect next. 

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

Once you have the first result, continue deeper with related prompts in Data Exploration.
