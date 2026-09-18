# Growth Accounting Framework *AI Prompt *

Apply a growth accounting framework to decompose MAU growth into its constituent components. User activity data: {{activity_data}} (user_id, active_month) Time period: {{period}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Apply a growth accounting framework to decompose MAU growth into its constituent components.

User activity data: {{activity_data}} (user_id, active_month)
Time period: {{period}}

1. User state classification:
 For each user in each month, classify their state:
 - New: first month of activity
 - Retained: active this month AND last month
 - Resurrected: active this month but NOT last month (but active at some prior point)
 - Churned: active last month but NOT this month (not visible in current month counts)

2. Growth accounting equation:
 MAU(t) = MAU(t-1) + New(t) + Resurrected(t) - Churned(t)
 - Verify this equation balances in the data

3. Monthly trend of each component:
 - Plot New, Retained, Resurrected, and Churned users over time
 - Quick ratio = (New + Resurrected) / Churned
 Quick ratio > 1: growing. < 1: shrinking. = 1: flat.
 - What is the trend in the quick ratio?

4. Component deep dive:
 - New users: growing or declining? What is driving acquisition?
 - Churn: is the churn count growing as MAU grows? (Structural churn problem if yes)
 - Resurrection: what brings users back? Is resurrection a meaningful growth driver?
 - Retention: what % of users are retained month over month? Is it improving?

5. Diagnosis:
 - Is this a new user problem (top of funnel), a retention problem, or both?
 - If the quick ratio < 1: which component needs improvement most?
 - If the quick ratio > 1 but slowing: is churn keeping pace with new user growth?

Return: monthly growth accounting table, quick ratio trend, component analysis, and growth diagnosis. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin growth analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Growth Analytics or the wider Product Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as User state classification:, New: first month of activity, Retained: active this month AND last month. The final answer should stay clear, actionable, and easy to review inside a growth analytics workflow for product analyst work. 

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

Once you have the first result, continue deeper with related prompts in Growth Analytics.
