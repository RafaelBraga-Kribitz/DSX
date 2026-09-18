# Multi-Touch Attribution Analysis *AI Prompt *

Analyze marketing attribution using multiple models to understand channel contribution. Customer journey data: {{journey_data}} (user_id, touchpoint, timestamp, channel, convert... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze marketing attribution using multiple models to understand channel contribution.

Customer journey data: {{journey_data}} (user_id, touchpoint, timestamp, channel, converted: Y/N)
Conversion event: {{conversion_event}}
Lookback window: {{lookback_window}} days

1. Attribution model comparison:
 Build all five standard models and compare:

 Last click: 100% credit to the final touchpoint
 First click: 100% credit to the first touchpoint
 Linear: equal credit to all touchpoints in the path
 Time decay: more credit to recent touchpoints (decay factor: 0.5 per day)
 Position-based (U-shaped): 40% to first, 40% to last, 20% split across middle

 For each model: credits per channel (absolute and %).

2. Channel contribution shift across models:
 - Which channels gain the most credit in first-click vs last-click?
 - First-click favors awareness channels (social, display); last-click favors intent channels (search)
 - Create a heatmap: channels x attribution models showing credit share

3. Path analysis:
 - Top 10 converting path sequences (e.g. Display → Organic Search → Paid Search → Convert)
 - Average path length (touchpoints) for converting vs non-converting journeys
 - Most common first touchpoints for converters

4. Assisted vs direct conversions:
 - % of conversions with only one touchpoint vs multi-touch paths
 - Channels that primarily assist (appear in paths but not at end) vs channels that primarily close

5. Data-driven attribution (if sample size permits):
 - Shapley value attribution: fair allocation based on marginal contribution of each channel
 - Requires: enough paths where each channel appears with and without others
 - Provides the most theoretically correct attribution

6. Budget implication:
 - If we moved budget based on last-click attribution: which channels would be over or under-invested?
 - Recommended budget allocation change based on the most appropriate model

Return: model comparison table, path analysis, assisted vs direct breakdown, and budget implications. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin attribution work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Attribution or the wider Marketing Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Attribution model comparison:, Channel contribution shift across models:, Which channels gain the most credit in first-click vs last-click?. The final answer should stay clear, actionable, and easy to review inside a attribution workflow for marketing analyst work. 

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

Once you have the first result, continue deeper with related prompts in Attribution.
