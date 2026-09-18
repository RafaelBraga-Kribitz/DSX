# Retention Analysis *AI Prompts *

2 Product Analyst prompts in Retention Analysis. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → intermediate levels and 2 single prompts. 

## AI prompts in Retention Analysis 
2 prompts Intermediate Single prompt 01 
### Churn Prediction Indicators 

Identify the leading behavioral indicators that predict user churn before it happens. User behavior data: {{behavior_data}} Churn definition: {{churn_definition}} (e.g. no activ... 
Prompt text Identify the leading behavioral indicators that predict user churn before it happens.

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

Return: feature importance table, threshold analysis, risk tier definitions, and intervention recommendations. Copy prompt Open prompt details Beginner Single prompt 02 
### User Retention Cohort Analysis 

Build and interpret a user retention cohort analysis. Event data: {{event_data}} (user_id, event_date, acquisition_date or cohort_date) Retention definition: {{retention_definit... 
Prompt text Build and interpret a user retention cohort analysis.

Event data: {{event_data}} (user_id, event_date, acquisition_date or cohort_date)
Retention definition: {{retention_definition}} (e.g. any login, completed core action, purchase)
Cohort granularity: {{granularity}} (weekly / monthly)

1. Build the retention matrix:
 - Rows: cohorts defined by {{cohort_period}} of first use or acquisition
 - Columns: periods since acquisition (Period 0, 1, 2, ... N)
 - Cell value: % of cohort still active in that period
 - Period 0 = 100% by definition (the acquisition period)

2. Key retention metrics:
 - Day 1 retention: % of users returning the day after first use
 - Day 7 retention: % returning in the first week
 - Day 30 retention: % returning within the first month
 - Long-term retention: at what period does the retention curve flatten? This is the product's natural retention floor.

3. Cohort comparison:
 - Are newer cohorts retaining better or worse than older ones?
 - Which cohort has the best Day 30 retention? What was happening during that acquisition period?
 - Plot cohort curves on the same chart: diverging curves indicate improving or worsening product health

4. Retention curve shape interpretation:
 - Sharp early drop then flat: high initial churn but strong core user base
 - Gradual continuous decline: no engaged user base, product is not habit-forming
 - Bump at specific period: seasonal return or notification-driven re-engagement

5. Retention by acquisition channel:
 - Which acquisition channels produce the highest Day 30 retention?
 - Are there channels bringing volume but low retention? (Wasted acquisition spend)

6. Recommendations:
 - At which period does the biggest retention drop occur? What is the likely cause?
 - What single change would most improve the retention curve shape?

Return: retention matrix, key metrics table, cohort comparison chart description, curve interpretation, and top recommendations. Copy prompt Open prompt details 
## Recommended Retention Analysis workflow 
1 
### Churn Prediction Indicators 

Start with a focused prompt in Retention Analysis so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### User Retention Cohort Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt
