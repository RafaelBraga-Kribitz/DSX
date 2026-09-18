# Advanced Visualization Types *AI Prompts *

4 Data Visualization Specialist prompts in Advanced Visualization Types. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 4 single prompts. 

## AI prompts in Advanced Visualization Types 
4 prompts Advanced Single prompt 01 
### Funnel and Cohort Visualization 

Design visualizations for funnel analysis and cohort retention. Funnel stages: {{funnel_stages}} Cohort definition: {{cohort_definition}} Metric: {{metric}} (retention rate, rev... 
Prompt text Design visualizations for funnel analysis and cohort retention.

Funnel stages: {{funnel_stages}}
Cohort definition: {{cohort_definition}}
Metric: {{metric}} (retention rate, revenue, engagement)

1. Funnel visualization options:

 Standard funnel chart:
 - Trapezoid shapes decreasing in width at each stage
 - Width proportional to the count at that stage
 - Show: absolute count AND conversion rate (%) between each stage
 - Color: use color to highlight the stage with the biggest drop-off
 - Limitation: difficult to compare multiple funnels (e.g. mobile vs desktop)

 Bar-based funnel:
 - Horizontal bars ranked by stage, sorted top to bottom
 - Easier to read exact values than the trapezoid format
 - Add conversion rate labels between bars: '→ 42% converted'
 - Add a secondary bar showing the 'lost' volume in each stage (grey bar)

 Funnel comparison (best for multiple segments):
 - Grouped or overlaid bars for each stage
 - Each group = one stage; bars within = one segment each
 - Better for: mobile vs desktop, new vs returning users, A vs B variant

 Waterfall funnel:
 - Shows how volume flows from one stage to the next
 - Each bar shows: volume entering the stage, volume converting (green), volume lost (red)
 - Good for showing absolute loss at each stage rather than just conversion rate

2. Cohort retention heatmap (standard format):
 - Rows: cohorts (typically by acquisition month/week)
 - Columns: periods since acquisition (Period 0, Period 1, Period 2...)
 - Cell value: retention rate (% of cohort still active in that period)
 - Color: sequential scale — dark = high retention, light = low retention
 - Period 0 is always 100% (the baseline)
 - Reading the diagonal: shows same calendar period across different cohorts (seasonality effect)

3. Retention visualization variants:
 - Line chart overlay: multiple cohort lines on the same chart — shows which cohorts retain better
 - Cumulative retention: useful for subscription products (when does the subscriber cancel?)
 - Retention cliff: annotate the period where the sharpest drop occurs

4. Actionable design:
 - For funnels: highlight the single biggest drop-off stage in red
 - For cohort heatmaps: add reference lines at 30-day and 90-day columns
 - Add a 'benchmark' row to the cohort heatmap showing the company average

Return: funnel chart design (type, labels, color coding), cohort heatmap specification, color scale, and actionability annotations. Copy prompt Open prompt details Advanced Single prompt 02 
### Geospatial Visualization Design 

Design an effective geospatial visualization for this data. Data: {{data_description}} (geographic level: country, region, state, city, zip code, lat/lon) Metric to show: {{metr... 
Prompt text Design an effective geospatial visualization for this data.

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

Return: map type recommendation with rationale, color scheme specification, classification method, projection, and tooltip design. Copy prompt Open prompt details Intermediate Single prompt 03 
### Heatmap Design Guide 

Design an effective heatmap for this data. Data: {{data_description}} Rows: {{row_dimension}} Columns: {{column_dimension}} Values: {{value_metric}} 1. When to use a heatmap: -... 
Prompt text Design an effective heatmap for this data.

Data: {{data_description}}
Rows: {{row_dimension}}
Columns: {{column_dimension}}
Values: {{value_metric}}

1. When to use a heatmap:
 - When the combination of two categorical or ordinal dimensions determines an outcome
 - When there are too many cells for individual bar charts
 - When the pattern across the full matrix is the insight (not individual values)
 - Classic uses: hour-of-day × day-of-week, correlation matrix, cohort retention

2. Color scale selection:
 - Sequential (one direction): light = low, dark = high. Use for: volume, count, positive metrics.
 - Diverging (two directions from midpoint): use for: correlation (-1 to +1), deviation from target (negative to positive), profit/loss.
 - Categorical: only if cells represent categories, not values

 Color scale specifics:
 - For retention or positive rates: white/light → brand color
 - For correlation matrices: blue → white → red (standard in statistics)
 - For profit/loss: red → white → green
 - Always: make the color scale legend visible with clear breakpoints labeled

3. Ordering rows and columns:
 - Do NOT use alphabetical order unless that is meaningful
 - Order by: magnitude (row total descending), natural order (Mon–Sun, Jan–Dec), or hierarchical clustering
 - Hierarchical clustering: groups similar rows and columns together, revealing pattern blocks

4. Cell annotations:
 - Add the value in each cell when: precision matters AND the matrix is small (< 100 cells)
 - For large matrices: use color only, with hover tooltips for exact values
 - Number format: 1 decimal for percentages; abbreviate large numbers (1.2M)
 - Text color: use dark text on light cells, light text on dark cells (auto-switch at midpoint)

5. Size and aspect ratio:
 - Square cells: ideal for correlation matrices where both dimensions are the same concept
 - Rectangular cells: for matrices where row and column dimensions differ substantially
 - Target: cells large enough to read the annotation (minimum 30×30px for annotated cells)

6. Marginal summaries:
 - Add row totals (right side) and column totals (bottom)
 - Use a lighter shade or a bar chart strip for marginals
 - This helps interpret relative importance of each row/column

Return: color scale specification, ordering recommendation, annotation rules, and marginal summary design. Copy prompt Open prompt details Advanced Single prompt 04 
### Network and Flow Visualization 

Design a visualization for network or flow data. Data type: {{data_type}} (customer journey, supply chain, relationship network, conversion funnel, Sankey flow) Nodes: {{nodes}}... 
Prompt text Design a visualization for network or flow data.

Data type: {{data_type}} (customer journey, supply chain, relationship network, conversion funnel, Sankey flow)
Nodes: {{nodes}} (entities)
Edges: {{edges}} (relationships or flows between entities)
Key question: {{question}}

1. Chart type selection:

 Sankey diagram:
 - Shows flow volumes between stages or categories
 - Best for: conversion funnels, budget allocation, material flows
 - Read: width of each flow proportional to volume
 - Limit: < 20 nodes; > 20 becomes unreadable without interaction
 - Tool: Plotly, D3.js, Google Charts

 Alluvial diagram:
 - A Sankey variant showing how categories change over time or across dimensions
 - Best for: before-after category changes, cohort migration
 - Example: how customers moved between subscription tiers from Q1 to Q4

 Network graph:
 - Nodes and edges showing relationships
 - Best for: social networks, dependency graphs, knowledge graphs
 - Layouts:
 - Force-directed: natural clustering, no hierarchy
 - Hierarchical: for tree structures (org chart, taxonomy)
 - Circular: for dense networks where crossing edges are unavoidable
 - Color nodes by: category, cluster membership, or a metric
 - Size nodes by: degree centrality, importance, volume
 - Edge width: proportional to relationship strength

 Chord diagram:
 - Circular diagram showing flows between all pairs of groups
 - Best for: mutual flows (trade between countries, team collaboration)
 - Harder to read than Sankey — use only when bidirectional flows are both important

 Arc diagram:
 - Nodes on a line with arcs above showing connections
 - Best for: temporal networks where order matters

2. Managing complexity:
 - > 50 nodes: aggregate less important nodes into 'Other' category
 - Filter controls: allow users to filter to relevant subgraphs
 - Highlight on hover: fade all non-connected nodes and edges when hovering
 - Community detection: use clustering algorithm to group related nodes; color by cluster

3. Performance for large networks:
 - > 500 nodes: use WebGL-based rendering (Sigma.js, GPU.js)
 - Static alternative: aggregate to a summary view with interactive drill-down

Return: chart type recommendation, layout specification, node and edge encoding, complexity management approach, and tool recommendation. Copy prompt Open prompt details 
## Recommended Advanced Visualization Types workflow 
1 
### Funnel and Cohort Visualization 

Start with a focused prompt in Advanced Visualization Types so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Geospatial Visualization Design 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Heatmap Design Guide 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Network and Flow Visualization 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
