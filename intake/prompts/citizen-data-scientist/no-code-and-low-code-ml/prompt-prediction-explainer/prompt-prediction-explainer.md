# Model Prediction Explainer *AI Prompt *

My model made a prediction for a specific case. Help me explain to a business stakeholder why the model predicted what it did. Case details: {{case_details}} Model prediction: {... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
My model made a prediction for a specific case. Help me explain to a business stakeholder why the model predicted what it did.

Case details: {{case_details}}
Model prediction: {{prediction}}
Model explanation output (SHAP or similar): {{explanation_output}}

1. What did the model predict and how confident is it:
 - State the prediction in plain English: 'The model predicts that [outcome] with [confidence]%'
 - Put the confidence in context: is 72% confidence high or low for this type of problem?

2. Why did the model predict this:
 - Using the explanation data, describe in plain English the top 3 reasons the model made this prediction
 - Format each reason as: '[Feature name] = [value] pushed the prediction [up/down] because [plain English reason]'
 - Avoid technical terms. Say 'the customer has been inactive for 90 days which increased the churn risk' not 'the days_since_last_purchase feature had a positive SHAP value'

3. What would change the prediction:
 - If the business wants to change this outcome, which factors could realistically be changed?
 - Example: 'If the customer made one purchase in the next 30 days, the churn risk would likely drop from 78% to around 45%'

4. Should we trust this specific prediction:
 - Is this customer/case similar to the training data? Or is it an unusual case where the model may be less reliable?
 - Are any of the input values unusual or possibly wrong?

5. How to communicate this to the business:
 - Write a 2-sentence explanation of this prediction that a sales manager or account manager could understand and use to take action 
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

The AI should return a structured result that covers the main requested outputs, such as What did the model predict and how confident is it:, State the prediction in plain English: 'The model predicts that [outcome] with [confidence]%', Put the confidence in context: is 72% confidence high or low for this type of problem?. The final answer should stay clear, actionable, and easy to review inside a no-code and low-code ml workflow for citizen data scientist work. 

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
