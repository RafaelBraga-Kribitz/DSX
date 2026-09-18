# Error Analysis *AI Prompt *

This prompt dives into the model's most damaging mistakes to uncover systematic failure modes. It is useful when overall metrics look acceptable but users still complain or critical edge cases remain unresolved. Clustering the worst errors can reveal missing features, bad data, or segment-specific model gaps. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Conduct a deep error analysis on this model's worst predictions.

1. Identify the 50 most confidently wrong predictions (highest predicted probability for the wrong class, or largest absolute residual for regression)
2. Profile these error cases:
 - What is the distribution of their feature values compared to correctly predicted cases?
 - Are they concentrated in a specific subgroup, time period, or region?
 - Do they share a common pattern in the raw data?
3. Cluster the error cases using k-means (k=3–5) — describe what characterizes each error cluster
4. For each cluster, propose a specific model improvement: more training data of that type, a new feature, a separate model for that segment, or a data quality fix
5. Estimate: if the top error cluster were fixed, how much would overall model performance improve?

Return the error profile table, cluster descriptions, and prioritized improvement recommendations. 
```

## When to use this prompt 
Use case 01 
You want to improve a model by understanding where it fails hardest. 
Use case 02 
Topline metrics hide concentrated failure pockets. 
Use case 03 
You need concrete ideas for the next iteration based on real errors. 
Use case 04 
You want error cases grouped into interpretable patterns. 

## What the AI should return 

A profile of the worst predictions, clusters of error cases with descriptions, likely causes, and prioritized recommendations for the improvements most likely to reduce future errors. 

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

Once you have the first result, continue deeper with related prompts in Model Evaluation.
