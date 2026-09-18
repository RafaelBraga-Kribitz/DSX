# User Segmentation *AI Prompts *

2 Product Analyst prompts in User Segmentation. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate levels and 2 single prompts. 

## AI prompts in User Segmentation 
2 prompts Intermediate Single prompt 01 
### Behavioral User Segmentation 

Segment users based on behavioral patterns in this product. Behavioral data: {{behavior_data}} (event logs: user_id, event_type, timestamp, session_id) Segmentation goal: {{goal... 
Prompt text Segment users based on behavioral patterns in this product.

Behavioral data: {{behavior_data}} (event logs: user_id, event_type, timestamp, session_id)
Segmentation goal: {{goal}} (personalization, intervention targeting, resource allocation)

1. Feature engineering for segmentation:
 Create behavioral features per user over the last {{window}} days:
 - Recency: days since last active
 - Frequency: sessions per week
 - Depth: average actions per session
 - Breadth: number of distinct features used
 - Tenure: days since account creation
 - Core action rate: % of sessions with {{core_action}}

2. RFM-style segmentation (rule-based, interpretable):
 Apply percentile-based segmentation on Recency, Frequency, and Depth:
 - Champions: recent, frequent, deep engagement
 - At-risk: previously frequent but declining
 - Dormant: not active in > 30 days
 - New users: tenure < 14 days
 - Casual: low frequency, low depth

3. Cluster-based segmentation (data-driven):
 - Apply k-means clustering on the behavioral features
 - Test k = 3, 4, 5, 6 clusters; select using silhouette score
 - Profile each cluster: mean values for each behavioral feature
 - Name each cluster with a business-friendly label based on its profile

4. Segment stability:
 - How stable are segments over time? (Do users move between segments frequently?)
 - A good segment is both meaningful and stable

5. Segment sizing and value:
 - Count and % of users in each segment
 - Revenue, retention, or other outcome metric per segment
 - Which segment represents the highest business value?

6. Recommended actions per segment:
 - Champions: retain and leverage as advocates
 - At-risk: trigger a win-back flow
 - Dormant: re-engagement campaign or sunset
 - New users: accelerate activation

Return: feature engineering code/SQL, RFM segment definitions, cluster profiles, segment sizing table, and recommended actions. Copy prompt Open prompt details Intermediate Single prompt 02 
### Power User Analysis 

Identify and analyze the power users of this product to understand what drives exceptional engagement. Engagement data: {{engagement_data}} Power user definition: {{definition}}... 
Prompt text Identify and analyze the power users of this product to understand what drives exceptional engagement.

Engagement data: {{engagement_data}}
Power user definition: {{definition}} (top 10% by usage frequency, or specific behavior threshold)

1. Power user identification:
 - Define power users quantitatively: users who {{criterion}} in the last 30 days
 - What % of total users are power users?
 - What % of total activity or revenue do power users account for? (Often 80% of value from 20% of users)

2. Power user profile:
 - Demographics: tenure, acquisition channel, plan type, company size (if B2B)
 - Behavioral fingerprint: which features do they use most? What is their typical session pattern?
 - Onboarding: did they complete onboarding differently? How quickly did they activate?
 - First week behavior: what did power users do in their first 7 days that non-power users did not?

3. The aha moment:
 - Is there a specific action in the first week that strongly predicts becoming a power user?
 - Compute: % of power users who completed {{action}} in week 1 vs % of all users
 - This is the aha moment candidate - the action to optimize for in onboarding

4. Power user journey:
 - Map the typical sequence of feature adoption for power users
 - At what tenure do most users reach power user status?
 - Is there a specific feature or workflow that accelerates the journey?

5. Implications for product and growth:
 - How can onboarding be redesigned to guide more users toward the power user path?
 - Which acquisition channels produce the most power users? (Not just the most users)
 - What does retaining power users require? (Are they at risk of churning for any reason?)

Return: power user definition and sizing, behavioral profile, aha moment analysis, journey map, and product/growth implications. Copy prompt Open prompt details 
## Recommended User Segmentation workflow 
1 
### Behavioral User Segmentation 

Start with a focused prompt in User Segmentation so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Power User Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt
