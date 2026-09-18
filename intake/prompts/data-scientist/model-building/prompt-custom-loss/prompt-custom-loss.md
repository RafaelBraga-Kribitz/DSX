# Custom Loss Function *AI Prompt *

This prompt builds a model objective around business cost instead of default statistical loss. It is useful when false positives and false negatives have very different consequences, such as fraud, medical screening, or retention interventions. The output translates model quality into financial terms. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement a custom loss function for this problem that better reflects the business cost of different types of errors.

Business context: {{business_context}}
Cost structure:
- False positive cost: {{fp_cost}} (e.g. unnecessary intervention costs $10)
- False negative cost: {{fn_cost}} (e.g. missed fraud costs $500)

1. Define the asymmetric cost matrix
2. Implement a custom objective function for LightGBM/XGBoost that minimizes expected business cost
3. Implement a custom evaluation metric that reports cost in business units
4. Train the model with the custom loss and compare to cross-entropy loss:
 - Standard accuracy / AUC / F1
 - Business cost per 1000 predictions
 - Optimal decision threshold under the cost structure
5. Show the threshold vs business cost curve — at what threshold is business cost minimized?

Return the custom loss code and the business cost comparison table. 
```

## When to use this prompt 
Use case 01 
Standard metrics do not reflect the true business cost of errors. 
Use case 02 
False positives and false negatives have asymmetric impact. 
Use case 03 
You want to optimize decision thresholds based on business value, not only AUC. 
Use case 04 
The project needs a custom objective for boosting models. 

## What the AI should return 

Custom loss and evaluation code, a business-cost comparison between standard and custom training, threshold-versus-cost analysis, and a recommendation for the cost-minimizing operating point. 

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
