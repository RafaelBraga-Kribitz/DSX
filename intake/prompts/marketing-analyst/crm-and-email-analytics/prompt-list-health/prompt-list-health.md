# Email List Health Audit *AI Prompt *

Audit the health of this email list and build a re-engagement and list hygiene plan. List data: {{list_data}} (subscriber_id, subscribe_date, last_open_date, last_click_date, em... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Audit the health of this email list and build a re-engagement and list hygiene plan.

List data: {{list_data}} (subscriber_id, subscribe_date, last_open_date, last_click_date, email_type)
List size: {{list_size}}
Current engagement rate: {{engagement_rate}}

1. Engagement segmentation:
 Classify every subscriber into engagement tiers:
 - Active: opened or clicked in the last 90 days
 - Warming: opened or clicked 90-180 days ago
 - At-risk: last engaged 180-365 days ago
 - Inactive: no engagement in > 365 days
 - Never engaged: subscribed but never opened a single email

 Size and % of list in each tier.

2. List decay rate:
 - How quickly is the active tier shrinking as a % of total?
 - Monthly new subscribers vs monthly subscribers moving to inactive
 - If inactive subscribers > 30% of list: email deliverability is at risk

3. Impact on deliverability:
 - High inactive rates signal to ISPs that your emails are unwanted
 - Gmail, Outlook, and Apple Mail track engagement heavily
 - Estimated deliverability risk: at current inactive %, what is the projected impact on inbox placement?

4. Re-engagement campaign design:
 For the 'At-risk' tier:
 - Trigger: 180 days since last open
 - Sequence: 3-email re-engagement series
 - Email 1: 'We miss you' + best recent content
 - Email 2: Incentive offer or value reminder
 - Email 3: 'Last chance' + explicit opt-down/unsubscribe option
 - Success criteria: any open or click = move back to 'Warming' tier

5. Sunset policy:
 - After the re-engagement sequence: move non-responders to suppression list
 - Do NOT delete: keep suppressed for compliance (unsubscribe proof)
 - Expected list size reduction and engagement rate improvement from sunset

6. List growth quality:
 - Which acquisition sources are producing the highest-engagement subscribers?
 - Which sources produce low-engagement (likely purchased or low-intent) subscribers?
 - Stop acquiring from low-quality sources even if it slows list growth

Return: engagement tier breakdown, list decay analysis, re-engagement sequence, sunset policy, and acquisition source quality assessment. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin crm and email analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in CRM and Email Analytics or the wider Marketing Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Engagement segmentation:, Active: opened or clicked in the last 90 days, Warming: opened or clicked 90-180 days ago. The final answer should stay clear, actionable, and easy to review inside a crm and email analytics workflow for marketing analyst work. 

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

Once you have the first result, continue deeper with related prompts in CRM and Email Analytics.
