# Train Test Split Strategy *AI Prompt *

This prompt chooses the right data splitting strategy based on the actual structure of the problem. It prevents common leakage mistakes caused by random splits on temporal, grouped, or imbalanced datasets. The result is a defensible train/validation/test design and matching code. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design the correct train/validation/test split strategy for this dataset and problem.

1. Examine the data: is it time-ordered? Does it have multiple entities (users, stores)? Is the target class imbalanced?
2. Recommend the split strategy:
 - Random split if i.i.d. data with balanced classes
 - Stratified split if class imbalance > 3:1
 - Time-based split if data is time-ordered (never use future data to predict the past)
 - Group-based split if the same entity appears multiple times (prevent entity leakage)
3. Recommend the split ratio and justify it given the dataset size
4. Implement the split in code with a fixed random_state for reproducibility
5. Verify the split: check that target distribution is similar across all splits

Return the split code and a distribution comparison table for train/val/test. 
```

## When to use this prompt 
Use case 01 
You are unsure whether to use random, stratified, grouped, or time-based splits. 
Use case 02 
The dataset may contain repeated entities or temporal order. 
Use case 03 
You want reproducible split code and validation of target balance across splits. 
Use case 04 
You want to avoid leakage before model training begins. 

## What the AI should return 

A recommended split strategy with rationale, reproducible code implementing it, suggested ratios, and a distribution comparison table showing how train, validation, and test sets differ. 

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

Once you have the first result, continue deeper with related prompts in Model Building.
