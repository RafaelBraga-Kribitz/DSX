# Data-Ink Ratio Audit *AI Prompt *

Audit this chart for unnecessary visual elements and recommend how to reduce chartjunk while preserving information. Chart description: {{chart_description}} Edward Tufte's prin... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Audit this chart for unnecessary visual elements and recommend how to reduce chartjunk while preserving information.

Chart description: {{chart_description}}

Edward Tufte's principle: maximize the data-ink ratio. Every drop of ink should be earning its place by communicating data. Remove everything else.

1. Elements to audit and recommendations:

 GRIDLINES:
 - Remove: dense gridlines that compete with the data
 - Keep: light, sparse reference gridlines (every major interval, not every minor one)
 - Better: label the key data points directly rather than requiring gridline reference

 AXIS LINES:
 - Remove: the heavy axis frame / box around the chart (chartjunk)
 - Keep: the y-axis line if bars/lines need a baseline reference
 - Remove: both axes in scatter plots (replace with reference lines at means if needed)

 TICK MARKS:
 - Remove: tick marks that just repeat the gridline
 - Keep: tick marks only where they aid reading (longer ticks at major intervals)

 BACKGROUNDS:
 - Remove: shaded chart backgrounds (grey, blue — adds no information)
 - Remove: gradient fills on any element
 - Keep: white or transparent background

 LEGENDS:
 - Prefer: direct labeling at the end of lines / top of bars over a separate legend
 - Remove: legends when there is only one data series
 - If legend is needed: place inside the chart area, not in a separate box

 BORDERS AND SHADOWS:
 - Remove: borders around charts, shadows on bars, rounded corners on bar charts
 - Remove: drop shadows on any element

 DECORATIVE ELEMENTS:
 - Remove: clip art, icons, 3D effects, excessive color
 - Remove: chart titles that are just labels (e.g. 'Bar Chart of Revenue') — replace with insight title

 COLOR:
 - Remove: color used for decoration rather than encoding data
 - Use: a single color for single-series charts
 - Use: color to highlight only the key point

2. Before vs after assessment:
 - List each element present in the current chart
 - Mark each: Keep / Remove / Simplify
 - Estimate the data-ink ratio improvement (rough %)

3. The one change with the biggest impact:
 - What single change would most improve this chart's readability?

Return: element-by-element audit table, removal recommendations, and a description of the simplified version. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin chart design principles work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Chart Design Principles or the wider Data Visualization Specialist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Elements to audit and recommendations:, Remove: dense gridlines that compete with the data, Keep: light, sparse reference gridlines (every major interval, not every minor one). The final answer should stay clear, actionable, and easy to review inside a chart design principles workflow for data visualization specialist work. 

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

Once you have the first result, continue deeper with related prompts in Chart Design Principles.
