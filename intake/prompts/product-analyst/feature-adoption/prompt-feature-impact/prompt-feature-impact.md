# Feature Impact Assessment *AI Prompt *

Assess the business impact of this recently launched feature. Feature: {{feature_name}} Launch date: {{launch_date}} Primary success metric: {{primary_metric}} Data available: {... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Assess the business impact of this recently launched feature.

Feature: {{feature_name}}
Launch date: {{launch_date}}
Primary success metric: {{primary_metric}}
Data available: {{data}}

1. Pre/post comparison:
 - Define the pre-period (same length as post, ending at launch date)
 - Compare primary metric: pre-period average vs post-period average
 - Absolute change and % change
 - Account for trends: was the metric already trending up/down before launch?

2. Confound check:
 - What else changed during the post-period? (Seasonality, marketing campaigns, other feature launches)
 - How might these confounds explain the observed change?
 - Can any confounds be controlled for or isolated?

3. Adoption-outcome correlation:
 - Segment users by adoption level: non-adopters, light adopters, heavy adopters
 - Compare primary metric across adoption segments
 - Does heavier feature usage correlate with better outcomes?

4. Counterfactual estimation:
 - If possible: use a holdout group (users who did not have access to the feature) as a control
 - Difference-in-differences: compare the change in metric for treatment vs control groups
 - If no holdout: use synthetic control (similar product/market as proxy)

5. Secondary effects:
 - Did the feature have any unintended effects on other metrics?
 - Check: session length, support tickets, error rates, other feature usage

6. ROI estimate:
 - Translate the metric impact into business value: what is the estimated annual impact in revenue or cost?
 - How does this compare to the development cost of the feature?

Return: pre/post comparison, confound analysis, adoption-outcome correlation, counterfactual estimate, and ROI. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin feature adoption work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Feature Adoption or the wider Product Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Pre/post comparison:, Define the pre-period (same length as post, ending at launch date), Compare primary metric: pre-period average vs post-period average. The final answer should stay clear, actionable, and easy to review inside a feature adoption workflow for product analyst work. 

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

Once you have the first result, continue deeper with related prompts in Feature Adoption.
