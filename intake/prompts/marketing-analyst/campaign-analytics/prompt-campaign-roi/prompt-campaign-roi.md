# Campaign ROI Analysis *AI Prompt *

Calculate the true ROI of this marketing campaign including all costs and revenue attribution. Campaign: {{campaign_name}} Spend data: {{spend_data}} Revenue attribution data: {... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Calculate the true ROI of this marketing campaign including all costs and revenue attribution.

Campaign: {{campaign_name}}
Spend data: {{spend_data}}
Revenue attribution data: {{revenue_data}}
Product margin: {{gross_margin_pct}}

1. Total cost of campaign:
 - Media spend (by channel)
 - Agency or creative fees
 - Technology platform costs
 - Internal labor cost (estimate: hours x fully-loaded cost per hour)
 - Total cost of campaign

2. Revenue attribution:
 - Direct response revenue: conversions directly attributed to the campaign
 - Assisted revenue: conversions where the campaign appeared in the path but was not the last touch
 - Attribution model used: last click, first click, linear, data-driven
 - Note the sensitivity: how much does attributed revenue change across attribution models?

3. ROI calculation:
 - Gross revenue attributed
 - Gross profit attributed (Revenue x Gross Margin %)
 - Net ROI = (Gross Profit - Total Cost) / Total Cost x 100%
 - ROAS = Gross Revenue / Media Spend (this overstates ROI; use gross profit ROI for real decisions)

4. Payback analysis:
 - For acquisition campaigns: CAC from this campaign
 - LTV of customers acquired: estimated LTV from this campaign's cohort
 - LTV / CAC ratio: is this campaign economically attractive?

5. Comparison to alternatives:
 - ROI vs other campaigns in the same period
 - ROI vs the cost of capital (hurdle rate)
 - Incremental ROI: what additional revenue vs a no-campaign baseline?

6. ROI by channel:
 - Compute net ROI for each channel in the campaign mix
 - Which channel delivered the highest gross profit ROI?
 - Where should budget shift in the next campaign based on this analysis?

Return: total cost breakdown, attribution analysis, net ROI, LTV/CAC, and channel-level ROI comparison. 
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

The AI should return a structured result that covers the main requested outputs, such as Total cost of campaign:, Media spend (by channel), Agency or creative fees. The final answer should stay clear, actionable, and easy to review inside a campaign analytics workflow for marketing analyst work. 

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
