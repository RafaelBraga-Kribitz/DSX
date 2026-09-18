# Customer Segmentation for Marketing *AI Prompt *

Build and operationalize customer segments for targeted marketing. Customer data: {{customer_data}} (demographics, behavioral, transactional, engagement) Marketing goals: {{goal... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build and operationalize customer segments for targeted marketing.

Customer data: {{customer_data}} (demographics, behavioral, transactional, engagement)
Marketing goals: {{goals}}
Channels available: {{channels}}

1. Segmentation approach selection:

 Demographic segmentation:
 - Age, gender, location, income, job title
 - Pros: easy to understand and action
 - Cons: weak predictor of behavior for most products

 Behavioral segmentation:
 - Purchase history, product usage, channel preferences, engagement frequency
 - Pros: directly tied to marketing-relevant actions
 - Best for: personalization, cross-sell, win-back

 RFM (Recency, Frequency, Monetary):
 - Recency: how recently did they purchase?
 - Frequency: how often do they purchase?
 - Monetary: how much do they spend?
 - Quintile score (1-5) on each dimension; combine into segment labels

 Psychographic / attitudinal:
 - Values, motivations, lifestyle
 - Pros: powerful for brand messaging
 - Cons: requires survey data, harder to operationalize

2. RFM segmentation execution:
 For each customer, compute R, F, M scores (1-5):
 - Champions: RFM = 5,5,5 (buy often, recently, high value)
 - Loyal customers: 4+,4+,3+
 - At-risk: previously high RFM but R has dropped
 - Potential loyalists: recent but low frequency
 - Win-back: low R, previously decent F and M
 - Lost: low on all three dimensions

3. Segment sizing and value:
 - Size (count and % of customers)
 - Average order value, purchase frequency, LTV by segment
 - Total revenue contribution by segment

4. Segment-to-channel mapping:
 For each segment: which channels and messages are most appropriate?
 - Champions: VIP program, referral program, early access
 - At-risk: re-engagement email, win-back offer
 - Potential loyalists: loyalty nudge, second purchase incentive

5. Personalization rules:
 - What content, offer, and message should each segment receive?
 - Build a segment x message matrix

Return: RFM segment definitions and scoring logic, segment sizing table, revenue contribution, channel mapping, and personalization rules. 
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

The AI should return a structured result that covers the main requested outputs, such as Segmentation approach selection:, Age, gender, location, income, job title, Pros: easy to understand and action. The final answer should stay clear, actionable, and easy to review inside a audience segmentation workflow for marketing analyst work. 

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
