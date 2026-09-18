# Geospatial Visualization Design *AI Prompt *

Design an effective geospatial visualization for this data. Data: {{data_description}} (geographic level: country, region, state, city, zip code, lat/lon) Metric to show: {{metr... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design an effective geospatial visualization for this data.

Data: {{data_description}} (geographic level: country, region, state, city, zip code, lat/lon)
Metric to show: {{metric}}
Key question to answer: {{question}}

1. Map type selection:

 Choropleth map:
 - Colors geographic regions by a metric value
 - Best for: showing variation in a metric across well-known geographic boundaries
 - Danger: choropleth maps are biased toward large areas — large regions dominate perception even if their values are typical
 - Fix: use a cartogram or pair with a bar chart for small-area analysis

 Proportional symbol map:
 - Places circles or shapes at each location, sized by the metric value
 - Best for: showing absolute counts or totals where geography is context, not the unit
 - Better than choropleth for showing concentration vs dispersion

 Dot density map:
 - Places one dot per N events at the event location
 - Best for: showing distribution of individual events (crime incidents, store locations)
 - Reveals clustering that choropleth aggregation hides

 Flow map:
 - Arrows showing movement between origins and destinations
 - Best for: trade flows, migration, commuting patterns
 - Danger: quickly becomes unreadable with many flows — limit to top 10–20

 Heat map (geographic):
 - Continuous color gradient showing density of events
 - Best for: high-volume point data where individual dots overlap

2. Choropleth design:
 - Color scale: sequential for single direction (more → less). Diverging for above/below baseline.
 - Classification scheme:
 - Quantile: equal number of areas in each class — good for comparing areas to each other
 - Natural breaks (Jenks): class breaks at natural data gaps — good for showing clustering
 - Equal interval: mathematically equal class widths — good for absolute scale comparison
 - Number of classes: 5–7 classes for most maps
 - Projection: choose a projection appropriate to the geographic extent
 - World maps: Robinson or Winkel Tripel (avoid Mercator for choropleth — distorts area)
 - Country maps: use a projection that preserves area for that country

3. Accessibility for maps:
 - Color: always pair color with a supplementary encoding (pattern or label) for colorblind users
 - Tooltip: rich tooltips with exact values on hover
 - Table alternative: provide a sortable table of the data alongside the map

4. What maps cannot show:
 - Causation or correlation between geographic proximity and outcomes
 - Temporal patterns (use small multiples of the same map, or an animated time series)
 - Non-geographic relationships (use a chart, not a map)

Return: map type recommendation with rationale, color scheme specification, classification method, projection, and tooltip design. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin advanced visualization types work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Advanced Visualization Types or the wider Data Visualization Specialist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Map type selection:, Colors geographic regions by a metric value, Best for: showing variation in a metric across well-known geographic boundaries. The final answer should stay clear, actionable, and easy to review inside a advanced visualization types workflow for data visualization specialist work. 

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

Once you have the first result, continue deeper with related prompts in Advanced Visualization Types.
