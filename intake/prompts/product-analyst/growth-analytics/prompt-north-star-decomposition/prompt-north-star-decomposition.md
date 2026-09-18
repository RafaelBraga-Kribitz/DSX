# North Star Metric Decomposition *AI Prompt *

Decompose the North Star Metric into its input metrics and build a measurement tree. North Star Metric: {{nsm}} (e.g. 'Weekly Active Engaged Users' or 'Messages Sent per Month')... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Decompose the North Star Metric into its input metrics and build a measurement tree.

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

Return: metric tree (all three levels), owner assignment, sensitivity analysis, and dashboard specification. 
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

The AI should return a structured result that covers the main requested outputs, such as Level 1 decomposition:, Level 2 decomposition:, Level 3 decomposition (where meaningful):. The final answer should stay clear, actionable, and easy to review inside a growth analytics workflow for product analyst work. 

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
