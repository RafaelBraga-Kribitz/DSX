# Segment Comparison Guide *AI Prompt *

Help me compare different groups or segments in this dataset to understand what drives differences in performance. I want to understand which groups are performing differently a... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Help me compare different groups or segments in this dataset to understand what drives differences in performance.

I want to understand which groups are performing differently and why — not just that they are different.

1. Identify the segments:
 - What categories in this dataset naturally divide the data into groups? (region, product type, customer tier, age group, channel, etc.)
 - Which of these segmentations is likely to be most meaningful for the business?

2. Compare the groups on the key metric:
 - What is the average (and range) of the main metric for each group?
 - Rank the groups from best to worst
 - Which group is the biggest outlier — far above or far below the average?

3. Is the difference meaningful or just noise?
 - Is the gap between the best and worst group large enough to act on?
 - Are some groups so small that their results are unreliable? (if a group has fewer than 30 rows, its average can swing wildly by chance)
 - What would the result look like if the worst group performed as well as the average group?

4. What else is different about the groups?
 - Look beyond the main metric: do the high-performing groups share other characteristics? (different mix of products, longer customer tenure, different geography)
 - Could any of these characteristics explain why they perform better?

5. The actionable insight:
 - Based on this comparison, what is the one thing the business should investigate or act on?
 - Be specific: name the group, the gap, and the potential action.

Explain your findings in plain language. Avoid using terms like 'statistically significant' without explaining what that means. 
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

The AI should return a structured result that covers the main requested outputs, such as Identify the segments:, What categories in this dataset naturally divide the data into groups? (region, product type, customer tier, age group, channel, etc.), Which of these segmentations is likely to be most meaningful for the business?. The final answer should stay clear, actionable, and easy to review inside a exploratory analysis workflow for citizen data scientist work. 

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
