# Before and After Comparison Design *AI Prompt *

Design a visualization that effectively communicates before-and-after comparison. Scenario: {{scenario}} (policy change, product launch, intervention, etc.) Before period: {{bef... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a visualization that effectively communicates before-and-after comparison.

Scenario: {{scenario}} (policy change, product launch, intervention, etc.)
Before period: {{before}}
After period: {{after}}
Metric: {{metric}}

1. Chart options for before/after:

 Slope chart (most effective for 2-point comparison):
 - Two vertical axes (Before | After)
 - Each entity is a line connecting its before value to its after value
 - Lines going up = improved, lines going down = declined
 - Color-code by direction: green for improvement, red for decline, grey for neutral
 - Best for: comparing many entities before/after a single event

 Paired bar chart:
 - Two bars per entity (before in grey, after in color)
 - Sort by the change magnitude (largest improvement first)
 - Add a difference annotation between each pair
 - Best for: few entities with absolute value comparison needed

 Dumbbell chart:
 - A horizontal dot plot variant
 - One dot for before, one dot for after, connected by a line
 - Dot size can encode a third variable (e.g. sample size)
 - Best for: clean, minimal presentation of many entities

 Difference area chart:
 - Two lines (before and after) with the area between them shaded
 - Green shading where after > before, red shading where after < before
 - Best for: showing the cumulative effect over time

 Bump chart:
 - Showing rank changes rather than absolute changes
 - Lines connecting before-rank to after-rank for each entity
 - Best for: rankings, leaderboards, or relative position changes

2. Choosing the right chart:
 - 2 entities: paired bar or slope chart
 - 3–10 entities: slope chart or dumbbell
 - > 10 entities: dumbbell or filtered slope (highlight top/bottom movers)
 - Rank focus: bump chart
 - Time series with intervention line: annotated line chart with shaded 'after' region

3. Statistical context:
 - Is the before-after difference statistically significant?
 - Add error bars or confidence intervals where sample sizes are small
 - Label the change magnitude on the chart (not just the before and after values)

4. Intervention line:
 - On a time series: mark the exact intervention date with a vertical dashed line
 - Label the line: 'Campaign launch (Mar 15)'
 - Shade the before period lightly grey, the after period white

Return: recommended chart type with rationale, design specification, and statistical context requirements. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin data storytelling work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Data Storytelling or the wider Data Visualization Specialist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Chart options for before/after:, Two vertical axes (Before | After), Each entity is a line connecting its before value to its after value. The final answer should stay clear, actionable, and easy to review inside a data storytelling workflow for data visualization specialist work. 

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

Once you have the first result, continue deeper with related prompts in Data Storytelling.
