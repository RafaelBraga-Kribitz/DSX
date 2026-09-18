# Prediction Model Setup Guide *AI Prompt *

Guide me through setting up a prediction model for my problem using a low-code or AutoML tool. I want to predict: {{target_variable}} Using data from: {{data_source}} Tool I am... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Guide me through setting up a prediction model for my problem using a low-code or AutoML tool.

I want to predict: {{target_variable}}
Using data from: {{data_source}}
Tool I am using: {{tool_name}} (e.g. MLJAR Studio, DataRobot, Google AutoML, H2O.ai)

1. Before I build the model — data preparation:
 - What does my data need to look like before I feed it to the model?
 - Which columns should I include as inputs and which should I exclude? (e.g. exclude columns that would not be available at prediction time, exclude columns that directly reveal the answer)
 - How many rows do I need? Is my current dataset large enough?
 - Does my target variable (the thing I want to predict) need any preparation?

2. Common mistakes to avoid before pressing 'build':
 - Data leakage: including a column that tells the model the answer directly (e.g. using 'was refunded' to predict 'will churn' — if someone was refunded they already churned)
 - Using the future to predict the past: make sure all your input columns only use information that was available at the time you would have made the prediction
 - Predicting something that does not actually need prediction: if 95% of cases are one class, always predicting that class will look accurate but is useless

3. Setting up the model in {{tool_name}}:
 - Walk me through the key settings I need to configure: target column, problem type, training/test split, and the main metric to optimize
 - Which metric should I use to evaluate this model given my business goal?

4. Interpreting the first results:
 - What should I look at first in the results?
 - What does 'good enough' look like for my use case?
 - What are the most common reasons a first model underperforms?

5. If the model is not good enough:
 - What are my options? (more data, better features, different model type, different problem framing) 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin no-code and low-code ml work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in No-Code and Low-Code ML or the wider Citizen Data Scientist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Before I build the model — data preparation:, What does my data need to look like before I feed it to the model?, Which columns should I include as inputs and which should I exclude? (e.g. exclude columns that would not be available at prediction time, exclude columns that directly reveal the answer). The final answer should stay clear, actionable, and easy to review inside a no-code and low-code ml workflow for citizen data scientist work. 

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

Once you have the first result, continue deeper with related prompts in No-Code and Low-Code ML.
