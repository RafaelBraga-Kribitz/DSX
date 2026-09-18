# LIME Explanation *AI Prompt *

This prompt generates simple local explanations for selected individual predictions using LIME. It is most helpful when stakeholders care about case-by-case reasoning in language that is easy to communicate. The chosen set of examples covers typical, extreme, borderline, and wrong predictions. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Use LIME to explain individual predictions from this model in plain English.

Generate LIME explanations for 5 specific predictions:
1. One very high prediction (top 5% of predicted values)
2. One very low prediction (bottom 5% of predicted values)
3. One borderline prediction (near the decision threshold)
4. The single prediction the model got most wrong
5. A randomly selected typical prediction

For each explanation:
- Show the top 10 features that pushed the prediction up or down
- Display as a horizontal bar chart with green bars (positive contribution) and red bars (negative contribution)
- Write a 2-sentence plain-English explanation: 'The model predicted [value] primarily because [top driver]. This was offset by [top negative driver].'

Return all 5 explanations with plots and text summaries. 
```

## When to use this prompt 
Use case 01 
You need easy-to-read explanations for specific individual cases. 
Use case 02 
The audience cares about examples more than global theory. 
Use case 03 
You want to compare high, low, borderline, and failure cases. 
Use case 04 
You need short human-readable summaries to accompany plots. 

## What the AI should return 

Five LIME-based local explanations with contribution plots and short plain-English summaries explaining what pushed each prediction up or down. 

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

Once you have the first result, continue deeper with related prompts in Explainability.
