# Group Aggregation Features *AI Prompt *

This prompt creates within-group statistical context so each row can be compared to its peers. It is useful when categories such as region, segment, product family, or store define meaningful local baselines. These features often help models understand relative position, not just absolute value. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Create group-level aggregation features by computing statistics at the level of each categorical group.

For each meaningful categorical column in the dataset:
1. Group by that column and compute these statistics for each numeric column:
 - mean, median, std, min, max
 - count of rows in the group
 - percentile rank of each row within its group
 - deviation of each row from its group mean (row_value - group_mean)
 - ratio of each row to its group mean (row_value / group_mean)

2. Name features systematically: [numeric_col]_[statistic]_by_[group_col]
 Example: revenue_mean_by_region, revenue_rank_by_region

3. Flag any group with fewer than 10 members — statistics on tiny groups are unreliable

Return code using pandas groupby + transform, and a list of all features created. 
```

## When to use this prompt 
Use case 01 
Your dataset contains categorical groupings with informative local structure. 
Use case 02 
You want features like group mean deviation, within-group rank, or ratio to group average. 
Use case 03 
Rows should be interpreted relative to peer groups rather than in isolation. 
Use case 04 
You need transform-based pandas code that preserves row count. 

## What the AI should return 

Groupby-transform code, a well-named list of generated aggregation features, and warnings about unstable statistics for very small groups. 

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
