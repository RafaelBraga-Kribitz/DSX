# Growth Analytics *AI Prompts *

2 Product Analyst prompts in Growth Analytics. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 2 single prompts. 

## AI prompts in Growth Analytics 
2 prompts Intermediate Single prompt 01 
### Growth Accounting Framework 

Apply a growth accounting framework to decompose MAU growth into its constituent components. User activity data: {{activity_data}} (user_id, active_month) Time period: {{period}... 
Prompt text Apply a growth accounting framework to decompose MAU growth into its constituent components.

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

Return: monthly growth accounting table, quick ratio trend, component analysis, and growth diagnosis. Copy prompt Open prompt details Advanced Single prompt 02 
### North Star Metric Decomposition 

Decompose the North Star Metric into its input metrics and build a measurement tree. North Star Metric: {{nsm}} (e.g. 'Weekly Active Engaged Users' or 'Messages Sent per Month')... 
Prompt text Decompose the North Star Metric into its input metrics and build a measurement tree.

North Star Metric: {{nsm}} (e.g. 'Weekly Active Engaged Users' or 'Messages Sent per Month')
Product context: {{product_description}}

1. Level 1 decomposition:
 Break the NSM into 2-3 multiplicative or additive components.
 Example: Weekly Active Engaged Users = Weekly Active Users x Engagement Rate
 Example: Revenue = Users x Conversion Rate x Average Order Value

2. Level 2 decomposition:
 Break each Level 1 component further.
 Example: Weekly Active Users = New Users + Retained Users + Resurrected Users
 Example: Engagement Rate = % Users Completing Core Action

3. Level 3 decomposition (where meaningful):
 Continue decomposing into actionable leaf metrics that specific teams own.

4. For each leaf metric:
 - Current value
 - Owner: which team or squad controls this metric?
 - Lever: what specific action moves this metric?
 - Effort to improve by 10%: Low / Medium / High

5. Sensitivity analysis:
 - If each leaf metric improves by 10%, which has the largest impact on the NSM?
 - This identifies the highest-leverage improvement opportunity

6. Metric tree dashboard spec:
 - Top level: NSM with trend
 - Second level: Level 1 components with trend
 - Third level: Level 2 components with owner labeled
 - Color coding: green = above target, yellow = near target, red = below target

Return: metric tree (all three levels), owner assignment, sensitivity analysis, and dashboard specification. Copy prompt Open prompt details 
## Recommended Growth Analytics workflow 
1 
### Growth Accounting Framework 

Start with a focused prompt in Growth Analytics so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### North Star Metric Decomposition 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt
