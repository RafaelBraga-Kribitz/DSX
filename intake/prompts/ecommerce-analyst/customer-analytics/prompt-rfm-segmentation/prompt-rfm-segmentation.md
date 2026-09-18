# RFM Segmentation for E-commerce *AI Prompt *

Build an RFM (Recency, Frequency, Monetary) segmentation model for this e-commerce customer base. Order data: {{order_data}} (customer_id, order_date, order_value) Analysis date... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build an RFM (Recency, Frequency, Monetary) segmentation model for this e-commerce customer base.

Order data: {{order_data}} (customer_id, order_date, order_value)
Analysis date: {{analysis_date}}
Total customers: {{customer_count}}

1. RFM metric computation:
 For each customer:
 - Recency (R): days since most recent purchase
 - Frequency (F): total number of orders
 - Monetary (M): total revenue generated

2. Quintile scoring:
 - Rank all customers on each dimension from 1 (worst) to 5 (best)
 - R score: 5 = purchased most recently, 1 = purchased least recently
 - F score: 5 = highest order frequency
 - M score: 5 = highest total spend
 - Combined RFM score: concatenate the three scores (e.g. '555', '411', '123')

3. Segment definition:
 - Champions (RFM 444-555): bought recently, buy often, high spend
 - Loyal Customers (R3-5, F3-5, M3-5): frequent but not cutting-edge recency
 - Potential Loyalists (R4-5, F1-2, M1-3): recent but low frequency - new customers showing promise
 - At-Risk (R1-2, F3-5, M3-5): used to be great customers but haven't bought recently
 - Can't Lose Them (R1, F4-5, M4-5): previously highest-value, now gone
 - Hibernating (R1-2, F1-2, M1-2): low on all dimensions
 - Lost (R1, F1, M1): low on all, no recent activity

4. Segment sizing and value:
 - Count and % of customers in each segment
 - Total revenue and % of revenue per segment
 - Average AOV and purchase frequency per segment

5. Marketing actions per segment:
 - Champions: VIP treatment, loyalty program invitation, referral ask
 - At-Risk: re-engagement campaign, exclusive offer, personal outreach for high-value
 - Can't Lose Them: win-back campaign with strong offer, survey why they left
 - Hibernating: last-chance reactivation email before sunset
 - Potential Loyalists: second-purchase nurture, loyalty points accelerator

6. Segment migration tracking:
 - Run the RFM model monthly
 - Track how many customers move between segments
 - Net migration to Champions: leading indicator of business health

Return: RFM scoring methodology, segment definitions and sizes, revenue contribution table, marketing actions per segment, and migration tracking plan. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin customer analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Customer Analytics or the wider Ecommerce Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as RFM metric computation:, Recency (R): days since most recent purchase, Frequency (F): total number of orders. The final answer should stay clear, actionable, and easy to review inside a customer analytics workflow for ecommerce analyst work. 

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

Once you have the first result, continue deeper with related prompts in Customer Analytics.
