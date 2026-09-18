# Feature Importance in Plain English *AI Prompt *

My model gave me a feature importance chart. Help me understand what it means and what to do with it. Feature importance output: {{feature_importance_output}} Model predicts: {{... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
My model gave me a feature importance chart. Help me understand what it means and what to do with it.

Feature importance output: {{feature_importance_output}}
Model predicts: {{target_variable}}

1. What feature importance means — in plain English:
 - Explain what feature importance is measuring: not 'which columns correlate with the target', but 'which columns the model actually relies on most to make its predictions'
 - Why does this matter? Because it tells us what the model believes drives the outcome

2. Walk through the top features:
 For each of the top 5 most important features:
 - Name: what is this column and what does it measure?
 - Direction: when this column has a high value, does the model predict a higher or lower outcome?
 - Business interpretation: what does this mean in business terms?
 - Does this make intuitive sense? If a feature ranks highly but you cannot explain why it matters, that is a warning sign.

3. Red flags to look for:
 - Is any feature suspiciously important? (e.g. a unique identifier like customer_id should not be important — it means the model memorized the training data)
 - Is any feature important that could not realistically be known at prediction time?
 - Is any feature important because it is a proxy for something else you should be measuring directly?

4. What is missing:
 - Are there features you expected to be important that are near the bottom? Why might the model not be using them?
 - Could an important column be missing from the data entirely?

5. What to do with this information:
 - Which features could I collect or engineer more of to improve the model?
 - Is there a feature so dominant that the model might be 'cheating'?
 - What does this feature importance tell us about the business problem — independent of the model? 
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

The AI should return a structured result that covers the main requested outputs, such as What feature importance means — in plain English:, Explain what feature importance is measuring: not 'which columns correlate with the target', but 'which columns the model actually relies on most to make its predictions', Why does this matter? Because it tells us what the model believes drives the outcome. The final answer should stay clear, actionable, and easy to review inside a no-code and low-code ml workflow for citizen data scientist work. 

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
