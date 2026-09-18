# Feature Ideas Generator *AI Prompt *

This prompt helps brainstorm high-value engineered features before you start coding. It is especially useful when you have a decent understanding of the target but want structured, model-oriented ideas rather than random transformations. The goal is to surface features with a realistic chance of improving signal while keeping build effort visible. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Suggest 15 new features I could engineer from this dataset to improve predictive power for {{target_variable}}.

For each feature:
- Feature name
- How to compute it (formula or logic)
- Why it might help the model
- Estimated difficulty to build: Easy / Medium / Hard

Cover these types:
- Interaction features (multiplication or ratio of two existing columns)
- Aggregation features (rolling mean, cumulative sum, group-by statistics)
- Date/time decompositions if a date column exists
- Lag features if data is time-ordered
- Domain-specific features based on the apparent business context

Prioritize features that are likely to have the highest signal-to-noise ratio. 
```

## When to use this prompt 
Use case 01 
You are starting a supervised ML project and need strong first feature ideas. 
Use case 02 
You want to go beyond raw columns without overengineering too early. 
Use case 03 
The dataset may contain dates, groups, time order, or business context worth exploiting. 
Use case 04 
You want a prioritized shortlist before building a feature pipeline. 

## What the AI should return 

A ranked list of 15 candidate features with feature name, exact computation logic, expected modeling value, estimated implementation difficulty, and brief notes on why each feature could help predict the target. 

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
