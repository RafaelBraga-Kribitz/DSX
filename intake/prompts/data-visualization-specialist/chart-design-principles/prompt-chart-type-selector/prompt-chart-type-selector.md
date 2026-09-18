# Chart Type Selector *AI Prompt *

Help me choose the right chart type for this data and communication goal. Data description: {{data_description}} Communication goal: {{goal}} (compare, show trend, show distribu... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Help me choose the right chart type for this data and communication goal.

Data description: {{data_description}}
Communication goal: {{goal}} (compare, show trend, show distribution, show composition, show relationship)
Audience: {{audience}}
Number of data points: {{n_points}}

1. Apply the chart selection framework:

 COMPARISON (how do items differ?):
 - 2–6 categories, single metric → Bar chart (horizontal preferred for long labels)
 - 2–6 categories, multiple metrics → Grouped bar or radar chart
 - Many categories, ranked → Lollipop chart or dot plot (cleaner than dense bar charts)
 - Over time with few series → Line chart
 - Over time with many series → Heatmap or small multiples

 TREND (how does a metric change over time?):
 - Single metric → Line chart
 - Multiple metrics, same scale → Multi-line chart (max 4–5 lines before it becomes unreadable)
 - Multiple metrics, different scales → Dual-axis line chart (use with caution — can mislead)
 - Showing cumulative growth → Area chart
 - Percentage change emphasis → Slope chart

 DISTRIBUTION (how are values spread?):
 - Few data points → Dot plot or strip plot
 - Many data points → Histogram or density plot
 - Comparing distributions across groups → Box plot or violin plot
 - Showing outliers prominently → Box plot with jitter overlay

 COMPOSITION (how do parts make up a whole?):
 - Few parts, single time point → Pie chart (only if ≤ 5 segments, all > 5%)
 - Few parts, prefer comparison → Stacked bar or 100% stacked bar
 - Hierarchical composition → Treemap or sunburst
 - Changing composition over time → Stacked area chart

 RELATIONSHIP (how do variables correlate?):
 - Two continuous variables → Scatter plot
 - Two continuous + third variable (size) → Bubble chart
 - Many variable pairs → Scatter plot matrix or correlation heatmap
 - Categorical vs continuous → Box plot or violin plot

2. Anti-patterns to avoid:
 - 3D charts: distort perception — never use
 - Pie charts with > 5 slices: use bar chart instead
 - Dual-axis charts with different units: often mislead — require explicit justification
 - Area charts for non-cumulative data: implies accumulation — use line chart instead

3. Recommendation:
 - Primary recommendation with rationale
 - Alternative if the primary is not available in the tool
 - One chart type to explicitly avoid for this data and why

Return: recommended chart type, alternative, anti-pattern warning, and a mockup description of what the chart should look like. 
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

The AI should return a structured result that covers the main requested outputs, such as Apply the chart selection framework:, 2–6 categories, single metric → Bar chart (horizontal preferred for long labels), 2–6 categories, multiple metrics → Grouped bar or radar chart. The final answer should stay clear, actionable, and easy to review inside a chart design principles workflow for data visualization specialist work. 

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
