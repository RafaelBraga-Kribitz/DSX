# Churn Prediction for Marketing *AI Prompt *

Build a churn prediction model to identify at-risk customers for proactive marketing intervention. Customer data: {{customer_data}} Churn definition: {{churn_definition}} Market... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a churn prediction model to identify at-risk customers for proactive marketing intervention.

Customer data: {{customer_data}}
Churn definition: {{churn_definition}}
Marketing interventions available: {{interventions}}

1. Feature engineering:
 Build predictive features for each customer (measured over the last 30/60/90 days):
 - Recency: days since last purchase or login
 - Frequency: purchase count in the last 90 days vs prior 90 days (trend)
 - Monetary: spend in last 90 days vs prior 90 days (trend)
 - Product usage: number of distinct products/features used
 - Engagement: email open rate, app sessions
 - Support signals: number of complaints or returns
 - Payment signals: failed payments, subscription downgrades

2. Churn probability model:
 - Logistic regression for interpretability (preferred for marketing teams)
 - Or gradient boosted trees for accuracy
 - Training: last 6 months of data; validation: most recent 30-60 days
 - Output: probability of churn within the next {{horizon}} days per customer

3. Risk tier definition:
 - High risk: churn probability > 60%
 - Medium risk: churn probability 30-60%
 - Low risk: churn probability < 30%
 - Size each tier: count and revenue at risk

4. Expected value of intervention:
 - For high-risk tier: Expected savings = (customers x churn probability x avg LTV x save rate)
 - Save rate: historical % of at-risk customers who respond to an intervention
 - Compare to intervention cost: is the program economically justified?

5. Intervention strategy by tier:
 - High risk: highest-value offer, personal outreach from CSM or account manager
 - Medium risk: automated personalized email with value reminder + soft incentive
 - Low risk: monitor; include in standard engagement program

6. Measurement plan:
 - Control group: randomly hold out 10% of at-risk customers from interventions
 - Measure: 60-day churn rate in treated vs control group
 - Calculate: incremental save rate and revenue impact

Return: feature engineering spec, model approach, risk tier definitions, intervention strategy, expected value calculation, and measurement plan. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin audience segmentation work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Audience Segmentation or the wider Marketing Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Feature engineering:, Recency: days since last purchase or login, Frequency: purchase count in the last 90 days vs prior 90 days (trend). The final answer should stay clear, actionable, and easy to review inside a audience segmentation workflow for marketing analyst work. 

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

Once you have the first result, continue deeper with related prompts in Audience Segmentation.
