# Demand Generation Funnel Analysis *AI Prompt *

Analyze the B2B demand generation funnel from awareness to closed revenue. Funnel data: {{funnel_data}} (leads by stage, conversion rates, time in stage, revenue closed) Sales c... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze the B2B demand generation funnel from awareness to closed revenue.

Funnel data: {{funnel_data}} (leads by stage, conversion rates, time in stage, revenue closed)
Sales cycle: {{avg_sales_cycle}} days
ACV: {{average_contract_value}}

1. Funnel stage definitions and metrics:
 - MQL (Marketing Qualified Lead): lead meeting the scoring threshold
 - SQL (Sales Qualified Lead): MQL accepted by sales
 - Opportunity: SQL with discovery meeting completed
 - Proposal: opportunity with proposal sent
 - Closed-Won: contracted revenue

 For each stage: volume, conversion rate to next stage, average days in stage

2. Conversion rate analysis:
 - MQL to SQL: what % of marketing leads are accepted by sales?
 Below 50% may indicate a lead quality problem
 - SQL to Opportunity: what % of accepted leads convert to active pipeline?
 - Opportunity to Close: win rate against proposals sent
 - Overall funnel conversion: leads to closed-won

3. Revenue forecast from current pipeline:
 - Pipeline by stage: weighted by stage probability
 - Expected revenue in next 90 days from current pipeline
 - Pipeline coverage ratio: pipeline / quota (target > 3x for 90-day quota)

4. Lead source contribution:
 - MQL volume by source (content/SEO, paid, events, outbound, referral)
 - Conversion rates by source: which sources produce the highest quality leads?
 - Revenue contribution by source: where does closed revenue actually come from?
 - Cost per MQL and cost per closed deal by source

5. Sales cycle and velocity:
 - Average days from MQL to close by source and segment
 - Deals stalling in specific stages: which stage has the longest dwell time?
 - Pipeline velocity: (Opportunities x Win Rate x ACV) / Sales Cycle Length

6. Marketing contribution to revenue:
 - Marketing-sourced revenue: deals where marketing generated the first touch
 - Marketing-influenced revenue: deals where marketing contributed at some point
 - Marketing's % contribution to total revenue

Return: funnel conversion table, pipeline forecast, lead source ROI, sales velocity analysis, and marketing revenue attribution. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin campaign analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Campaign Analytics or the wider Marketing Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Funnel stage definitions and metrics:, MQL (Marketing Qualified Lead): lead meeting the scoring threshold, SQL (Sales Qualified Lead): MQL accepted by sales. The final answer should stay clear, actionable, and easy to review inside a campaign analytics workflow for marketing analyst work. 

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

Once you have the first result, continue deeper with related prompts in Campaign Analytics.
