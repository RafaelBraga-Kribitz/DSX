# Numeric Column Summary Table *AI Prompt *

Numeric Column Summary Table is a beginner prompt for data exploration. This prompt helps the user understand the structure, meaning, and analytical potential of a dataset before moving into deeper work. It is designed to surface what is in the data, how trustworthy it looks, and which columns, relationships, or patterns deserve attention first. Use it early in an analysis workflow to reduce guesswork and create a shared understanding of the dataset. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Create a clean summary table for all numeric columns in this dataset.

For each numeric column include:
- Count of non-null values
- Mean and median
- Standard deviation
- Min and max
- 25th, 50th, and 75th percentiles
- Number of zeros
- Number of negative values
- Number of unique values

Format as a transposed table where each column name is a row.
Highlight any column where the mean and median differ by more than 20% — this indicates skewness.
Highlight any column with more than 10% zero values — these may need special treatment. 
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
