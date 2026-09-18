# Behavioral User Segmentation *AI Prompt *

Segment users based on behavioral patterns in this product. Behavioral data: {{behavior_data}} (event logs: user_id, event_type, timestamp, session_id) Segmentation goal: {{goal... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Segment users based on behavioral patterns in this product.

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

Return: feature engineering code/SQL, RFM segment definitions, cluster profiles, segment sizing table, and recommended actions. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin user segmentation work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in User Segmentation or the wider Product Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Feature engineering for segmentation:, Recency: days since last active, Frequency: sessions per week. The final answer should stay clear, actionable, and easy to review inside a user segmentation workflow for product analyst work. 

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

Once you have the first result, continue deeper with related prompts in User Segmentation.
