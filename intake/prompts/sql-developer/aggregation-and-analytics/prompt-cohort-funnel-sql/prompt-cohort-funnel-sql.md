# Cohort and Funnel Analysis in SQL *AI Prompt *

Write SQL to perform cohort retention analysis and funnel analysis. Event table: {{event_table}} User table: {{user_table}} Cohort definition: {{cohort}} (acquisition month, fir... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write SQL to perform cohort retention analysis and funnel analysis.

Event table: {{event_table}}
User table: {{user_table}}
Cohort definition: {{cohort}} (acquisition month, first purchase date, etc.)
Database: {{database}}

1. Cohort retention matrix:

 WITH user_cohorts AS (
 -- Assign each user to a cohort based on their first activity
 SELECT user_id,
 DATE_TRUNC('month', MIN(event_date)) AS cohort_month
 FROM events
 GROUP BY user_id
 ),
 user_activity AS (
 -- Find each user's activity by month
 SELECT e.user_id,
 DATE_TRUNC('month', e.event_date) AS activity_month,
 c.cohort_month,
 EXTRACT(EPOCH FROM DATE_TRUNC('month', e.event_date) - c.cohort_month)
 / (30 * 24 * 3600) AS month_number
 FROM events e
 JOIN user_cohorts c USING (user_id)
 )
 SELECT
 cohort_month,
 month_number,
 COUNT(DISTINCT user_id) AS retained_users,
 COUNT(DISTINCT user_id) / FIRST_VALUE(COUNT(DISTINCT user_id))
 OVER (PARTITION BY cohort_month ORDER BY month_number) AS retention_rate
 FROM user_activity
 GROUP BY cohort_month, month_number
 ORDER BY cohort_month, month_number;

2. Funnel analysis (ordered step completion):

 WITH funnel_steps AS (
 SELECT user_id,
 MIN(CASE WHEN event_name = 'signup' THEN event_time END) AS step1_time,
 MIN(CASE WHEN event_name = 'onboarding_complete' THEN event_time END) AS step2_time,
 MIN(CASE WHEN event_name = 'first_purchase' THEN event_time END) AS step3_time
 FROM events
 GROUP BY user_id
 )
 SELECT
 COUNT(*) AS entered_funnel,
 COUNT(step2_time) AS completed_step2,
 COUNT(step3_time) AS completed_step3,
 ROUND(COUNT(step2_time)::NUMERIC / COUNT(*) * 100, 1) AS step1_to_step2_pct,
 ROUND(COUNT(step3_time)::NUMERIC / NULLIF(COUNT(step2_time),0) * 100, 1) AS step2_to_step3_pct
 FROM funnel_steps
 WHERE step1_time IS NOT NULL;

3. Ordered funnel (steps must occur in sequence):
 Add: AND step2_time > step1_time AND step3_time > step2_time
 to enforce that steps happened in the correct order.

Return: cohort retention matrix SQL, funnel analysis SQL, ordered funnel variant, and a description of how to pivot the cohort matrix for a heatmap. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin aggregation and analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Aggregation and Analytics or the wider SQL Developer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Cohort retention matrix:, Funnel analysis (ordered step completion):, Ordered funnel (steps must occur in sequence):. The final answer should stay clear, actionable, and easy to review inside a aggregation and analytics workflow for sql developer work. 

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

Once you have the first result, continue deeper with related prompts in Aggregation and Analytics.
