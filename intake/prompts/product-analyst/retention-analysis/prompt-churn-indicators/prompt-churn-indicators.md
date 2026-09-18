# Churn Prediction Indicators *AI Prompt *

Identify the leading behavioral indicators that predict user churn before it happens. User behavior data: {{behavior_data}} Churn definition: {{churn_definition}} (e.g. no activ... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Identify the leading behavioral indicators that predict user churn before it happens.

User behavior data: {{behavior_data}}
Churn definition: {{churn_definition}} (e.g. no activity for 30 days, subscription cancelled)
Observation window: {{observation_window}} (behavioral features measured in the N days before churn)

1. Feature engineering for churn prediction:
 Compute these behavioral features for each user in the observation window:
 - Login frequency: sessions per week
 - Days since last active
 - Core action completion rate: % of sessions where {{core_action}} was completed
 - Feature breadth: number of distinct features used
 - Engagement trend: comparing last 7 days vs prior 7 days
 - Support contacts: number of support tickets or error events
 - Billing events: failed payments, plan downgrades

2. Univariate analysis:
 For each feature, compare the distribution between:
 - Users who churned within {{horizon}} days
 - Users who did not churn
 Compute: mean, median, and statistical significance of the difference (Mann-Whitney U test)

3. Predictive ranking:
 - Which features show the largest and most statistically significant difference between churners and non-churners?
 - Rank features by predictive power (use AUC of a simple logistic regression per feature)

4. Early warning thresholds:
 - For the top 3 features: what threshold value separates high-churn-risk from low-churn-risk users?
 - Example: users with > 14 days since last login have a 3x higher churn rate than average

5. Churn risk segmentation:
 - Combine the top 3 indicators into a simple churn risk score (Low / Medium / High)
 - What % of users currently fall into each risk tier?
 - What intervention should each tier receive?

Return: feature importance table, threshold analysis, risk tier definitions, and intervention recommendations. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin retention analysis work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Retention Analysis or the wider Product Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Feature engineering for churn prediction:, Login frequency: sessions per week, Days since last active. The final answer should stay clear, actionable, and easy to review inside a retention analysis workflow for product analyst work. 

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

Once you have the first result, continue deeper with related prompts in Retention Analysis.
