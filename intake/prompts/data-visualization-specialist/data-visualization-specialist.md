# Data Visualization Specialist *AI Prompts *

Data Visualization Specialist AI prompt library with 23 prompts in 6 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 6 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Data Visualization Specialist prompt categories 
6 categories 
### Chart Design Principles 

AI prompts for chart design principles, including chart-type selection, visual hierarchy, annotation, and clarity-first communication. 
5 prompts Annotation and Labeling Guide Chart Type Selector → 
### Dashboard Architecture 

AI prompts for dashboard architecture, including metric hierarchy, layout strategy, interactivity patterns, and governance for maintainable reporting. 
5 prompts Dashboard Layout Design Dashboard Performance Optimization → 
### Advanced Visualization Types 

AI prompts for advanced visualization types, including layered charts, interactive techniques, and specialized plots for complex analytical stories. 
4 prompts Funnel and Cohort Visualization Geospatial Visualization Design → 
### Data Storytelling 

AI prompts for data storytelling, including narrative framing, audience adaptation, visual sequencing, and insight-to-action communication. 
4 prompts Before and After Comparison Design Executive Presentation Chart Set → 
### Tool-Specific Implementation 

AI prompts for tool-specific implementation, including practical setup patterns, workflow translation, and environment-aware execution guidance. 
3 prompts Power BI Best Practices Python Visualization Code → 
### Accessibility and Standards 

AI prompts for visualization accessibility and standards, including color contrast, labeling, assistive readability, and inclusive chart design practices. 
2 prompts Accessibility Audit for Data Viz Style Guide for Data Visualization → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 23 Chart Design Principles 5 Dashboard Architecture 5 Advanced Visualization Types 4 Data Storytelling 4 Tool-Specific Implementation 3 Accessibility and Standards 2 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **23 **of 23 prompts 
## Chart Design Principles 
5 prompt s Chart Design Principles Intermediate Prompt 01 
### Annotation and Labeling Guide 
Design the annotation and labeling strategy for this chart.

Chart type: {{chart_type}}
Key insight to communicate: {{key_insight}}
Audience: {{audience}}

1. Title and subtitle strategy:
 - Title: state the insight, not the data. 'Revenue grew 34% in Q3' beats 'Quarterly Revenue.'
 - Title should be answerable by 'so what?' — not just 'what is this?'
 - Subtitle: add essential context (time period, geography, unit, data source)
 - Format: title bold and prominent, subtitle smaller and lighter

2. Axis labels:
 - Label axes only when the unit is not obvious from the title or context
 - Remove redundant axis label if values are labeled on the chart directly
 - Rotate x-axis labels only as a last resort — prefer angled labels or flipping to horizontal bar chart
 - Units belong on the axis label or in parentheses, NOT repeated on every tick

3. Data labels (value annotations on data points):
 Guideline: use data labels OR axis + gridlines, not both.
 - Use data labels when: there are few data points and exact values matter
 - Use gridlines when: there are many data points and relative position matters more than exact values
 - For bar charts: place labels inside the bar (for long bars) or just outside (for short bars), left-aligned
 - For line charts: label only the final value, or highlight specific notable points
 - Format: use the same number formatting as the axis (1 decimal place if axis uses 1)

4. Callout annotations (highlighting specific insight):
 - Use sparingly: maximum 2–3 annotations per chart
 - Format: brief text (5–10 words) + arrow pointing to the relevant data point or region
 - Content: explain WHY this point is notable, not just WHAT the value is
 - Example: 'Spike caused by holiday campaign (Dec 15–Jan 3)' is better than 'Peak value: 42,000'

5. Reference lines and bands:
 - Target / goal line: show with a dashed line, labeled directly on the line
 - Historical average: light dashed line
 - Confidence interval or forecast range: semi-transparent shaded band, not heavy borders
 - Crisis or event periods: shaded background band with a text label at the top

6. Legend placement:
 - Prefer: direct labeling at the end of each line / top of each series (no separate legend)
 - If legend is needed: place inside the plot area (top-right or bottom-right)
 - Never: use a legend positioned below a wide chart that requires eye travel

7. What NOT to annotate:
 - Every data point (creates noise, defeats the purpose)
 - Obvious features the viewer can see clearly
 - Multiple overlapping annotations in the same chart region

Return: title and subtitle for this specific chart, axis label specification, data label strategy, callout annotation text, and legend placement decision. Copy prompt View page Show more ↓ Chart Design Principles Beginner Prompt 02 
### Chart Type Selector 
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

Return: recommended chart type, alternative, anti-pattern warning, and a mockup description of what the chart should look like. Copy prompt View page Show more ↓ Chart Design Principles Intermediate Prompt 03 
### Color Strategy for Data Viz 
Design a color strategy for this data visualization or dashboard.

Visualization type: {{viz_type}}
Data encoding needs: {{encoding_needs}} (categorical groups, sequential scale, diverging scale, highlighting)
Brand colors: {{brand_colors}}
Accessibility requirement: {{accessibility}} (must pass WCAG AA color contrast, colorblind-safe)

1. Choose the right color palette type:

 CATEGORICAL (for distinguishing unordered groups):
 - Max 8 colors (human perceptual limit for distinct hues)
 - Colors should be equally distinct — avoid mixing light and dark versions of similar hues
 - Recommended: ColorBrewer Qualitative, Okabe-Ito (colorblind-safe), Tableau 10
 - Primary choice for: bar charts with multiple categories, multi-line charts, map choropleth regions

 SEQUENTIAL (for ordered numeric data, low to high):
 - Single hue: light (low values) → dark (high values)
 - Or perceptually uniform multi-hue: e.g. yellow → green → blue
 - Avoid: rainbow (jet) colormap — perceptually non-uniform, not colorblind-safe
 - Primary choice for: heatmaps, choropleth maps, scatter plots with continuous color encoding

 DIVERGING (for data with a meaningful midpoint):
 - Two hues diverging from a neutral center: e.g. blue — white — red
 - Center (zero or baseline) must be a neutral color (white, light grey)
 - Primary choice for: correlation matrices, market share vs benchmark, profit/loss maps

 HIGHLIGHT (single color to draw attention):
 - Use one accent color for the key data point or series; make everything else grey
 - Most powerful technique for directing viewer attention

2. Colorblind accessibility:
 Approximately 8% of males have red-green color blindness (deuteranopia/protanopia).
 - NEVER rely on red vs green alone to encode meaning (e.g. positive vs negative)
 - Safe alternatives for red/green distinction: use blue vs orange, or add symbols/patterns
 - Test: convert the palette to greyscale — can values still be distinguished?
 - Use: Okabe-Ito palette, Viridis, Cividis — these are designed to be distinguishable by all
 - Tool: Sim Daltonism, Color Oracle, or Coblis for simulating colorblind views

3. Color contrast (WCAG AA):
 - Text on colored background: minimum contrast ratio 4.5:1 (3:1 for large text)
 - Data elements (bars, lines, dots): minimum 3:1 contrast ratio against the background
 - Test using: WebAIM Contrast Checker or Figma plugins

4. Brand color integration:
 - Use the primary brand color for the most important data series only
 - Avoid using brand colors if they are not colorblind-safe (common for red-dominant brands)
 - Build a secondary palette around the brand primary using ColorBrewer rules

5. Color encoding rules:
 - Encode one thing at a time: don't use color AND size AND shape all for different dimensions
 - Be consistent: the same color always means the same thing across the dashboard
 - Don't use color for ordinal data: use sequential shades, not arbitrary colors

Return: palette specification (hex codes), palette type with rationale, colorblind test plan, contrast check, and usage rules. Copy prompt View page Show more ↓ Chart Design Principles Beginner Prompt 04 
### Data-Ink Ratio Audit 
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

Return: element-by-element audit table, removal recommendations, and a description of the simplified version. Copy prompt View page Show more ↓ Chart Design Principles Advanced Prompt 05 
### Small Multiples Design 
Design a small multiples layout for this dataset instead of a cluttered single chart.

Dataset: {{dataset_description}}
Dimension to facet by: {{facet_dimension}} (region, product, segment, etc.)
Number of facets: {{n_facets}}
Key metric: {{metric}}

Small multiples (trellis charts, faceted charts) show the same chart type repeated for each value of a dimension. They enable comparison across groups while keeping each individual panel clean and readable.

1. When to use small multiples vs overlaid series:
 Use small multiples when:
 - More than 4–5 series on a single chart becomes tangled (spaghetti chart)
 - The comparison is across rather than within the dimension
 - Patterns within each panel are more important than the exact values between panels

 Use overlaid series (single chart) when:
 - You need exact value comparison between series at the same time point
 - There are only 2–3 series and they don't overlap heavily

2. Layout design:
 - Grid arrangement: prefer rows × columns that are wider than tall (landscape orientation)
 - Panel count guideline: 4–12 panels is the readable range. > 20 panels requires a different approach.
 - Panel size: large enough to show the pattern clearly, small enough that all panels fit on one screen/page
 - Aspect ratio: each panel should follow the banking to 45° rule — line slopes close to 45° are most readable

3. Shared axes (critical for comparability):
 - ALL panels must share the same x and y axis scales unless explicitly communicating within-panel patterns
 - Do NOT use independent (free) scales unless the goal is to show pattern shape, not magnitude
 - If scales differ substantially between panels: use a log scale or explicitly label each panel's scale range

4. Ordering of panels:
 - By magnitude: sort panels by the most meaningful summary statistic (e.g. total revenue)
 - Alphabetically: only if magnitude order is not meaningful
 - By natural order: time, geography, hierarchy
 - Never: random order

5. Labeling in small multiples:
 - Panel titles: short and above each panel (not below)
 - Remove x-axis labels from all but the bottom row
 - Remove y-axis labels from all but the leftmost column
 - Shared axis titles: one title spanning the entire grid edge, not repeated per panel
 - Highlight a reference pattern: add a light grey copy of the overall average/total in each panel for reference

6. Highlighting across panels:
 - Use the same highlight color in each panel to emphasize the same element (e.g. the current period)
 - Add a reference line at the overall average in each panel so viewers can see which panels are above or below

Return: layout specification (rows × columns, panel size), axis sharing rules, panel ordering recommendation, and labeling specification. Copy prompt View page Show more ↓ 
## Dashboard Architecture 
5 prompt s Dashboard Architecture Beginner Prompt 01 
### Dashboard Layout Design 
Design the layout and information hierarchy for this dashboard.

Dashboard purpose: {{purpose}}
Audience: {{audience}}
Key decisions it supports: {{decisions}}
Available metrics: {{metrics}}
Tool: {{tool}} (Tableau, Power BI, Looker, Grafana, custom web)

1. F-pattern and Z-pattern reading order:
 - Eyes enter top-left and move right, then sweep left and down
 - Most important information: top-left
 - Secondary importance: top-right and left side
 - Supporting detail: bottom and center
 - Apply this: place the single most important KPI top-left, supporting context bottom-right

2. Dashboard sections (top to bottom):

 Row 1 — Header KPIs (always visible):
 - 3–5 key numbers with period-over-period change and direction indicator
 - These answer 'is everything okay?' at a glance
 - Format: large number + small label + change % + arrow color

 Row 2 — Trend overview:
 - Primary time series chart showing the main metric over the full period
 - Answers: 'what is the trend?'

 Row 3 — Breakdown charts:
 - How does the main metric break down by the most important dimension?
 - Typically 2–3 charts side by side (by region, by product, by channel)

 Row 4 — Supporting detail:
 - Tables, secondary metrics, drill-down content
 - Content that contextualizes the summary above

3. Filter placement:
 - Global filters (date range, region, segment): top of dashboard, always visible
 - Local filters (applying only to one section): near the section they affect
 - Filter defaults: set to the most common use case, not blank

4. Whitespace:
 - Sufficient padding between charts (minimum 16px)
 - Grouped charts have smaller internal padding, larger padding from other groups
 - Do not compress charts to fit more — whitespace is not wasted space

5. Responsive considerations:
 - Will this be viewed on mobile? Design for the smallest screen first.
 - Vertical stacking for mobile: the top KPI row must be fully visible without scrolling

6. Number of charts:
 - Rule of thumb: ≤ 8 charts on a single screen without scrolling
 - More than 8: split into multiple dashboard pages or tabs
 - Each chart must be independently interpretable — no 'see chart 3 for context'

Return: sketch layout description (rows, columns, chart assignments), filter specification, whitespace guidelines, and mobile adaptation notes. Copy prompt View page Show more ↓ Dashboard Architecture Advanced Prompt 02 
### Dashboard Performance Optimization 
Diagnose and fix slow dashboard performance.

Dashboard tool: {{tool}}
Current load time: {{load_time}}
Data size: {{data_size}}
User complaint: {{complaint}}

1. Diagnose the bottleneck:

 Data query bottleneck:
 - Is the slow part the query or the rendering?
 - Enable query profiling in the tool — how long does each query take?
 - Are queries running on a large uncached dataset?
 - Are there multiple queries running sequentially that could run in parallel?

 Rendering bottleneck:
 - Too many data points in a single chart (scatter plot with 1M points)
 - Too many charts on a single page requesting data simultaneously
 - Heavy chart types (maps, network graphs) with large geometries

 Filter bottleneck:
 - Every filter change triggers a full database query
 - Cascading filters that trigger multiple queries in sequence

2. Data-layer optimizations:

 Pre-aggregation:
 - Move aggregations from dashboard query time to ETL time
 - Create summary tables at the grain the dashboard needs (daily totals, not individual transactions)
 - Expected improvement: 10–100× faster queries

 Materialized views / extracts:
 - Tableau: extract to .hyper file instead of live connection
 - Power BI: import mode instead of DirectQuery for non-real-time data
 - Looker: persistent derived tables (PDTs)
 - When to use live connection: only when data must be real-time (< 15-minute latency required)

 Caching:
 - Enable dashboard-level query caching
 - Set cache refresh to match data update frequency (no point refreshing every minute if data updates hourly)
 - User-level vs shared cache: shared cache serves the same query result to all users

 Query optimization:
 - Add indexes on filter columns (date, region, product category)
 - Partition tables by date for time-filtered queries
 - Push filters to the query level (not post-query in the viz layer)

3. Dashboard-layer optimizations:

 Reduce chart count:
 - Each chart = one or more queries
 - Remove or consolidate charts that answer the same question
 - Move supporting detail to a second page / click-through

 Lazy loading:
 - Load above-the-fold charts first, load below-the-fold on scroll
 - Show a loading spinner per chart rather than blocking the whole page

 Limit data points per chart:
 - Time series: aggregate to a coarser granularity (weekly instead of daily if trend is what matters)
 - Scatter plots: sample or bin large datasets
 - Tables: paginate or limit to top N rows with a 'load more' option

4. Benchmarks:
 - Target load time: < 3 seconds for first meaningful paint
 - Filter response: < 2 seconds for filter changes
 - Table pagination: < 1 second per page load

Return: bottleneck diagnosis, prioritized optimization list with estimated improvement per action, and implementation steps for the tool specified. Copy prompt View page Show more ↓ Dashboard Architecture Intermediate Prompt 03 
### Drill-Down Navigation Design 
Design a drill-down navigation structure for this dashboard so users can move from summary to detail without losing context.

Dashboard: {{dashboard_name}}
Data hierarchy: {{hierarchy}} (e.g. Region → Country → Store → Product)
User journey: {{user_journey}} (what questions do users typically ask in sequence?)

1. The drill-down mental model:
 Users start at a high-level summary and need to progressively answer:
 Level 1: Is everything okay? (KPI overview)
 Level 2: Where is the problem? (Dimensional breakdown)
 Level 3: Why is it happening? (Root cause detail)
 Level 4: Which specific items? (Row-level detail table)

 Design each level to naturally lead to the next.

2. Navigation patterns:

 Click-through drill-down:
 - Clicking a bar/point navigates to a lower-level page filtered to that value
 - User knows they are drilling by the breadcrumb trail: All Regions > EMEA > UK
 - Back button returns to parent level
 - Best for: hierarchical data with many levels

 Tooltip drill-down:
 - Hovering reveals a mini chart or additional metrics in a tooltip
 - No navigation required
 - Best for: quick context without leaving the current view

 Filter-driven drill-down:
 - Clicking a dimension value filters all charts on the page
 - Charts update in place rather than navigating to a new page
 - Best for: exploratory analysis where users want to compare across the drill dimension

 Expandable rows (table drill-down):
 - Summary rows expand to show sub-rows
 - Best for: tabular hierarchies (product category → subcategory → SKU)

3. Breadcrumb design:
 - Always show the current position in the hierarchy: Home > Sales > EMEA > UK
 - Each level is clickable to navigate back
 - Current level is not a link (it is where you are)
 - Place breadcrumb at the top of the page, below the header

4. Preserving filter context:
 - When drilling down, carry all existing filters to the lower level
 - Clearly show which filters are active at all times
 - Provide a 'Reset all filters' option
 - If a filter is incompatible with the drill-down target, warn the user

5. Back navigation:
 - Always provide a back button or breadcrumb link
 - Browser back button should also work (no JavaScript state navigation that breaks back button)
 - Return to parent level with the same view state the user left

6. Mobile drill-down:
 - Tap a chart element to reveal a details panel (not navigate away)
 - Full-screen detail view for tables on mobile

Return: navigation pattern recommendation, breadcrumb design specification, filter persistence rules, and mobile navigation approach. Copy prompt View page Show more ↓ Dashboard Architecture Advanced Chain 04 
### Full Dashboard Design Chain 
Step 1: Requirements — define the dashboard's purpose in one sentence. Identify the audience (technical level, role, decision they need to make). List the top 5 questions the dashboard must answer. Define the data sources and refresh frequency.
Step 2: KPI selection — from all available metrics, select the 3–5 most important for the stated purpose. For each: define the metric precisely, specify the comparison periods, identify the direction of good (up or down), and assign an owner.
Step 3: Layout design — sketch the dashboard layout (rows and columns). Apply F-pattern reading order. Assign each chart to a position based on importance. Specify filter placement, whitespace, and scroll behavior.
Step 4: Chart design — for each chart position, specify: chart type (using the chart selection framework), data it displays, color encoding, axis labels, data labels vs gridlines decision, and title (insight statement, not label).
Step 5: Color and typography — define the color palette (categorical, sequential, diverging). Check all colors for colorblind safety and WCAG contrast compliance. Specify font, font sizes, and number formatting.
Step 6: Interactivity design — specify: which elements are clickable (and what happens), filter behavior (what each filter affects), drill-down paths, and tooltip content for each chart.
Step 7: Performance and accessibility — estimate query count and data volume. Identify pre-aggregation opportunities. Write alt text for each chart. Verify keyboard navigability. Document the refresh schedule and caching strategy.
Step 8: Review and iteration — list 3 questions to ask stakeholders in the first review. Define the success criteria: what would make this dashboard 'done'? Specify how usage will be measured post-launch. Copy prompt View page Show more ↓ Dashboard Architecture Intermediate Prompt 05 
### KPI Card Design 
Design KPI summary cards for the top section of this dashboard.

Metrics to display: {{metrics}}
Comparison periods: {{comparisons}} (vs last week, vs last year, vs target)
Audience: {{audience}}

1. KPI card anatomy:
 Each card should contain:
 - Metric name: short, plain English (not internal code names)
 - Current value: large, prominent, formatted appropriately
 - Change indicator: absolute and % change vs comparison period
 - Direction arrow: ↑ or ↓
 - Color coding: green (positive) / red (negative) — but ONLY if direction = good/bad is unambiguous
 - Sparkline (optional): tiny trend line showing last 30 days of history

2. Value formatting rules:
 - Revenue: $1.2M not $1,234,567 (abbreviate at thousands/millions)
 - Percentages: 23.4% (one decimal), not 23.4567%
 - Ratios: 2.3× not 2.3x (typographically correct)
 - Counts: 12,345 with comma separator
 - Duration: 4m 23s not 263 seconds
 - Never use more decimal places than the measurement precision warrants

3. Change formatting:
 - Show BOTH absolute and percentage change where meaningful
 - Example: '+$42K (+8.3%) vs last month'
 - For metrics where % change is misleading (small denominators): show absolute only
 - Time period label must be explicit: 'vs last month' not just 'MoM'

4. Color coding — apply carefully:
 - Only use red/green when the direction of 'better' is universally agreed
 - Revenue up → green ✓. Cost up → red ✓. Refund rate up → red ✓.
 - Customer support tickets up → could be red OR green depending on context → use neutral
 - When in doubt: use blue/grey for the value, let the arrow indicate direction without color judgment
 - Always provide an alternative indicator beyond color (arrow shape, +/- sign) for colorblind accessibility

5. Card sizing and hierarchy:
 - Primary KPI: largest card, most prominent position
 - Secondary KPIs: equal-sized cards in a row below or beside
 - Supporting context: smaller, lower visual weight
 - Do not show more than 5 KPI cards in the top row — choose the most important ones

6. Sparkline design:
 - No axis labels or gridlines — the shape is what matters
 - Highlight the most recent point with a dot
 - Use the same color as the metric
 - Width: sufficient to show 4 weeks or 12 months of history at a glance

7. What to omit:
 - Percentage change without the baseline value (uninformative)
 - Three comparison periods on the same card (confusing)
 - Conditional formatting that changes the card color (distracting)

Return: KPI card specification for each metric, formatting rules, color coding decisions, and sparkline design. Copy prompt View page Show more ↓ 
## Advanced Visualization Types 
4 prompt s Advanced Visualization Types Advanced Prompt 01 
### Funnel and Cohort Visualization 
Design visualizations for funnel analysis and cohort retention.

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

Return: funnel chart design (type, labels, color coding), cohort heatmap specification, color scale, and actionability annotations. Copy prompt View page Show more ↓ Advanced Visualization Types Advanced Prompt 02 
### Geospatial Visualization Design 
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

Return: map type recommendation with rationale, color scheme specification, classification method, projection, and tooltip design. Copy prompt View page Show more ↓ Advanced Visualization Types Intermediate Prompt 03 
### Heatmap Design Guide 
Design an effective heatmap for this data.

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

Return: color scale specification, ordering recommendation, annotation rules, and marginal summary design. Copy prompt View page Show more ↓ Advanced Visualization Types Advanced Prompt 04 
### Network and Flow Visualization 
Design a visualization for network or flow data.

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

Return: chart type recommendation, layout specification, node and edge encoding, complexity management approach, and tool recommendation. Copy prompt View page Show more ↓ 
## Data Storytelling 
4 prompt s Data Storytelling Intermediate Prompt 01 
### Before and After Comparison Design 
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

Return: recommended chart type with rationale, design specification, and statistical context requirements. Copy prompt View page Show more ↓ Data Storytelling Intermediate Prompt 02 
### Executive Presentation Chart Set 
Design a set of 3–5 charts for an executive presentation on this topic.

Topic: {{topic}}
Key message: {{key_message}}
Audience: C-suite / senior leadership
Time available: {{time}} minutes
Data available: {{data_available}}

Executive audiences have specific needs: they want the conclusion first, they need context without detail overload, and they make decisions — so every chart must point to an action.

1. Chart 1 — The headline chart (30 seconds):
 - Must communicate the single most important finding
 - Should be readable in < 5 seconds
 - Title IS the conclusion: 'EMEA Revenue Is 23% Below Target — Driven by Germany'
 - Minimal detail — highlight only the critical element
 - Maximum 1 annotation

2. Chart 2 — The context chart (60 seconds):
 - Shows the trend or baseline that explains why the headline matters
 - Answers: 'Is this getting better or worse?'
 - Time series with the key threshold or target line shown

3. Chart 3 — The breakdown chart (60 seconds):
 - Decomposes the headline into its components
 - Answers: 'Where is this concentrated?'
 - A ranked breakdown by the most actionable dimension (by team, by product, by region)

4. Chart 4 (optional) — The root cause chart (60 seconds):
 - Shows what is driving the breakdown
 - Answers: 'Why is this happening?'
 - A correlation, funnel, or attribution chart

5. Chart 5 (optional) — The implication chart (30 seconds):
 - Projects the impact if no action is taken
 - Or shows the potential gain if the recommended action is taken
 - Answers: 'What happens if we do / don't act?'

6. Executive chart design rules:
 - Use only one key message per chart — no chart with two conclusions
 - No table with more than 5 rows (executives do not read tables in presentations)
 - Font size minimum 18pt for any text in the chart
 - Never show error bars, confidence intervals, or p-values in executive presentations
 - Remove every axis, gridline, and label that is not strictly necessary
 - Color: use brand colors + one highlight color only

Return: chart set specification (title, chart type, data elements, key message per chart) and presentation flow narrative. Copy prompt View page Show more ↓ Data Storytelling Beginner Prompt 03 
### Insight Narrative Builder 
Build a visual narrative around this data insight for a presentation or report.

Key insight: {{insight}}
Supporting data: {{data}}
Audience: {{audience}}
Medium: {{medium}} (slide deck, scrollytelling web page, printed report, video)

1. The one-chart story structure:
 Every visualization that tells a story has three parts:
 - Setup: what is the context? What should the audience expect or know before seeing the data?
 - Tension: what is the surprising or important finding?
 - Resolution: what does this mean and what should we do?

 Apply these three parts to my specific insight.

2. Chart sequence for presentations (one chart per slide):
 Slide 1 — Context chart:
 - Show the baseline situation: the overall trend or the 'before' state
 - No highlighting yet — just the context
 - Title: a neutral statement of what is shown

 Slide 2 — Revelation chart:
 - Same chart, but now highlight the key finding
 - Grey out everything except the critical data point, region, or series
 - Title: the insight stated as a declarative sentence
 - Annotation: 1–2 callouts explaining the highlighted element

 Slide 3 — Implication chart:
 - A different chart showing the consequences or the 'so what'
 - If the finding is a problem: show the cost or impact
 - If the finding is an opportunity: show the potential gain
 - Title: the action or question this finding raises

3. Progressive disclosure technique:
 - Build the chart incrementally: start with one line/bar, add the others one by one
 - Each addition is a new point in the story
 - Reveal the key comparison last, after the audience understands the baseline

4. The scrollytelling version (for web):
 - Section 1: static chart with neutral context
 - Section 2: as user scrolls, highlight the anomaly
 - Section 3: annotate with the explanation
 - Section 4: transition to a different view showing the implication

5. What NOT to do:
 - Do not show all the data at once and hope the audience finds the insight
 - Do not use a single chart with 5 callouts — one chart, one point
 - Do not let the title be a label ('Revenue by Quarter') — make it the insight

Return: three-slide story structure with specific chart descriptions, title for each slide, and annotation text. Copy prompt View page Show more ↓ Data Storytelling Advanced Prompt 04 
### Uncertainty and Error Visualization 
Design visualizations that communicate uncertainty, ranges, and confidence intervals without misleading the audience.

Data type: {{data_type}} (forecast, survey results, experimental results, model output)
Audience: {{audience}}
Uncertainty type: {{uncertainty_type}} (sampling uncertainty, forecast range, measurement error)

1. Why uncertainty visualization matters:
 - A single line or point estimate implies false precision
 - Decision-makers need to understand the range of plausible outcomes
 - But: uncertainty visualizations are often misread — design for correct interpretation

2. Chart options for uncertainty:

 Error bars:
 - Show ±1 SD, ±1 SE, or 95% CI around a point estimate
 - Common mistake: error bars are often mislabeled — always state what they represent in the caption
 - Better for: point estimates with few comparisons

 Confidence bands:
 - Semi-transparent shaded region around a line
 - The line represents the central estimate; the band is the interval
 - Use low opacity (20–30%) to avoid obscuring the data
 - Better for: time series forecasts with uncertainty growing over time

 Gradient bands:
 - Multiple nested bands for different confidence levels (e.g. 50%, 80%, 95%)
 - Darker center = higher confidence; lighter outer = wider range
 - Better for: forecast fans where showing multiple scenarios is important

 Violin plots:
 - Show the full probability distribution of values for each group
 - Better than box plots for showing bimodal or skewed distributions
 - Combine with a box plot overlay to show median and quartiles

 Dot plots with distribution:
 - Individual observations as dots with a density curve overlay
 - Shows both the spread and any outliers
 - Better than summary statistics alone for small samples

 Hypothetical outcome plots (HOPs):
 - Animate multiple possible outcomes sampled from the distribution
 - Studies show HOPs lead to more accurate uncertainty interpretation than static bands
 - Suitable for: interactive web visualizations, not static reports

3. Common mistakes to avoid:
 - Showing only the point estimate without any range
 - Using error bars without labeling what they represent
 - Showing 95% CI and calling it 'possible range' — it excludes 5% of outcomes
 - Making the uncertainty band so wide it is useless
 - Hiding uncertainty because it 'looks bad' — this is dishonest and dangerous

4. Language for uncertainty:
 - Label: '95% confidence interval' not 'margin of error' (unless you mean exactly that)
 - Caption: always explain what the shaded region represents in plain language
 - For forecasts: show a plain-language probability statement: 'There is a 20% chance of exceeding $10M'

Return: recommended uncertainty visualization for this specific data, design specification, labeling language, and a caption explaining the uncertainty to a non-technical audience. Copy prompt View page Show more ↓ 
## Tool-Specific Implementation 
3 prompt s Tool-Specific Implementation Intermediate Prompt 01 
### Power BI Best Practices 
Apply Power BI best practices to build a robust, performant report.

Report goal: {{goal}}
Data model: {{data_model}}
Power BI version / license: {{license}}

1. Data model best practices:
 - Star schema: always model as star schema — fact tables with foreign keys to dimension tables. Never use flat tables with denormalized data.
 - Relationships: one-to-many only in the model — many-to-many relationships cause performance problems. Resolve many-to-many with a bridge table.
 - Import vs DirectQuery: use Import mode for anything not requiring < 1-hour freshness. DirectQuery limits DAX features and is slow.
 - Composite model: use when some tables must be real-time (DirectQuery) and others can be imported.

2. DAX best practices:
 - Use variables (VAR ... RETURN): improves readability and performance by evaluating an expression only once
 - Avoid CALCULATE inside iterators (SUMX, COUNTX): nested iteration is slow
 - Time intelligence: always use a proper Date table marked as Date table in the model
 - Measures vs calculated columns: always prefer measures for aggregations. Calculated columns are stored in memory; measures compute on demand.

3. Report design:
 - Page tabs: meaningful names, not 'Page 1, Page 2'
 - Slicer placement: top or left of page, never inside the report body
 - Visual interactions: configure interactions explicitly — by default every visual cross-filters every other
 - Bookmarks: use bookmarks for show/hide panels, not for navigation (navigation pages are better)
 - Tooltips: create tooltip pages for rich hover details

4. Performance optimization:
 - Turn off 'Auto date/time': in Options > Data load. Auto date creates hidden date tables for every date column — major performance killer.
 - Reduce cardinality: avoid high-cardinality text columns in the fact table. Use integer keys and dimension tables.
 - Disable cross-highlighting on visuals not requiring it: each cross-highlight = a DAX query
 - Use Performance Analyzer (View > Performance Analyzer) to identify slow visuals

5. Governance:
 - Deployment pipelines: use Dev → Test → Production pipeline for enterprise reports
 - Row-level security (RLS): implement in the model, not in the report layer
 - Naming conventions: [Measure Name], d_DimensionTable, f_FactTable

Return: data model validation checklist, DAX pattern examples for this use case, performance optimization steps, and naming conventions. Copy prompt View page Show more ↓ Tool-Specific Implementation Intermediate Prompt 02 
### Python Visualization Code 
Write production-quality Python visualization code for this chart.

Chart type: {{chart_type}}
Data: {{data_description}}
Library preference: {{library}} (matplotlib, seaborn, plotly, altair, bokeh)
Output format: {{output}} (static PNG/PDF, interactive HTML, Jupyter notebook)

1. Library selection guide:

 Matplotlib:
 - Best for: publication-quality static charts, full control over every element
 - Pros: complete control, widely supported, PDF/SVG export
 - Cons: verbose API, interactive features require additional work

 Seaborn:
 - Best for: statistical charts (distributions, regressions, heatmaps)
 - Pros: high-level API, beautiful defaults, statistical integration
 - Cons: built on matplotlib, limited interactivity

 Plotly:
 - Best for: interactive web-based charts
 - Pros: interactive by default, Plotly Express high-level API, Dash integration
 - Cons: larger files, not ideal for publication

 Altair:
 - Best for: declarative grammar-of-graphics style charts
 - Pros: concise code, vega-altair grammar, responsive
 - Cons: data size limit in browser (5000 rows default)

2. Code standards:
 - Use matplotlib style sheets or seaborn themes for consistent styling
 - Set figure size explicitly: fig, ax = plt.subplots(figsize=(10, 6))
 - Use clear variable names that match the data (not ax1, ax2)
 - Add docstring explaining what the function produces
 - Save with appropriate DPI: plt.savefig('chart.png', dpi=300, bbox_inches='tight')

3. Accessibility in code:
 - Set colorblind-safe palette: plt.rcParams['axes.prop_cycle'] = cycler(color=okabe_ito_palette)
 - Add alt text for web outputs
 - Ensure minimum font sizes: plt.rcParams['font.size'] = 12

4. Reusable function template:
 Write the chart as a function that accepts data and styling parameters:
 def create_[chart_name](data, title, color_col=None, highlight=None, save_path=None):
 'Creates a [description] chart from the provided DataFrame.'
 ...
 return fig, ax

5. For this specific chart:
 - Import statements needed
 - Data preparation steps
 - Chart creation code with full styling
 - Annotation code
 - Save/display code

Return: complete, runnable Python code with comments, color palette definition, and example usage. Copy prompt View page Show more ↓ Tool-Specific Implementation Intermediate Prompt 03 
### Tableau Best Practices 
Apply Tableau-specific best practices to build a high-quality, performant visualization.

Visualization goal: {{goal}}
Data source: {{data_source}}
Tableau version: {{version}}

1. Data source best practices:
 - Extract vs live connection: use extract (.hyper) for anything not requiring real-time updates. Extract = 10–100× faster than live connections to most databases.
 - Data modeling in Tableau: use relationships (not joins) for multi-table data sources in Tableau 2020.2+. Relationships avoid row duplication from joins.
 - Calculated fields: compute in the data source (database/ETL) when possible. Tableau calculated fields that run on every row are slow.
 - LOD expressions: use for aggregations at a different level of detail than the viz. FIXED LOD does not respect dimension filters — use INCLUDE/EXCLUDE for filter-sensitive aggregations.

2. Performance best practices:
 - Limit mark count: < 5,000 marks for smooth interaction. > 50,000 marks = investigate alternatives (aggregation, sampling).
 - Filter order: context filters first → dimension filters → measure filters. Context filters run before the rest, dramatically reducing query scope.
 - Dashboard loading: disable 'Automatically update' for slow dashboards; provide a 'Run' button.
 - Hide unused fields: remove fields from the data source that are not used in the workbook.

3. Formatting standards:
 - Remove borders from all worksheets embedded in dashboards
 - Set background to 'None' on worksheets; control background at the dashboard layout level
 - Use Layout Containers (horizontal/vertical) to control spacing and alignment
 - Font: set a single font in Format > Workbook for consistency
 - Tooltip: customize all tooltips — default tooltips show field names (ugly)

4. Color in Tableau:
 - Use a custom color palette: Tableau's default palette is acceptable but not brand-aligned
 - For sequential palettes: use ColorBrewer palettes imported as custom palettes
 - Diverging palettes: always set the midpoint explicitly (not the data average unless that is meaningful)

5. Publishing and access:
 - Add descriptions to all worksheets and dashboards (used in Tableau Server search)
 - Tag dashboards by business domain for discoverability
 - Set refresh schedule to match data update frequency (not default 'never')

6. Calculated field documentation:
 - Add a comment to every complex calculated field explaining what it computes and why
 - Format: // Revenue excl. returns = gross revenue less refunds processed in the same period

Return: implementation checklist, LOD expression examples for this use case, performance configuration, and formatting specification. Copy prompt View page Show more ↓ 
## Accessibility and Standards 
2 prompt s Accessibility and Standards Intermediate Prompt 01 
### Accessibility Audit for Data Viz 
Audit this visualization for accessibility and recommend improvements.

Visualization: {{visualization_description}}
Deployment context: {{context}} (web, print, presentation, embedded application)
Target WCAG level: {{wcag_level}} (AA is the standard; AAA for government/public sector)

1. Color accessibility:
 - Color contrast: check foreground vs background for all text and key visual elements
 - Normal text: minimum 4.5:1 contrast ratio (WCAG AA)
 - Large text (18pt+ or 14pt bold): minimum 3:1
 - Visual elements (charts, icons): minimum 3:1 against adjacent colors
 - Color independence: can the chart be understood by someone who cannot see color?
 - Add: patterns, shapes, textures, or direct labels as alternatives to color-only encoding
 - Colorblind simulation: run the chart through a deuteranopia / protanopia simulator

2. Text accessibility:
 - Minimum font size: 12pt for body text, 10pt minimum for chart labels
 - Font choice: avoid decorative or condensed fonts for data labels
 - Text alternatives: all charts need alt text describing the key finding (not just 'a bar chart')
 - Alt text format: 'Bar chart showing [metric] by [dimension]. [Key insight in one sentence]. [Data source and date range].'

3. Chart-specific accessibility:
 - Tables as alternatives: complex visualizations should have a data table option for screen readers
 - Keyboard navigation: interactive charts must be navigable by keyboard (Tab, Enter, Arrow keys)
 - Focus indicators: visible focus highlight for all interactive elements
 - ARIA labels: for web-based charts, add aria-label attributes to chart containers

4. Motion and animation:
 - Respect 'prefers-reduced-motion' media query — animations should be disableable
 - No flashing content at > 3Hz (seizure risk)
 - Provide static alternative for all animated charts

5. Cognitive accessibility:
 - Consistent layout: same chart types in the same position across pages/dashboards
 - Clear headings: descriptive titles and section headings
 - Plain language: chart titles use plain language, not industry jargon
 - Consistent color coding: same color always means the same thing
 - Avoid information overload: maximum 5–7 items requiring comparison per chart

6. Testing tools:
 - WebAIM Contrast Checker for color contrast
 - Deque's aXe browser extension for WCAG compliance
 - Screen reader testing: NVDA (Windows), VoiceOver (Mac/iOS)
 - Colorblind simulators: Coblis, Sim Daltonism

Return: accessibility audit table (issue, WCAG criterion, severity, fix), specific fixes for the visualization described, and alt text for the chart. Copy prompt View page Show more ↓ Accessibility and Standards Advanced Prompt 02 
### Style Guide for Data Visualization 
Create a data visualization style guide for this organization.

Organization: {{organization}}
Brand colors: {{brand_colors}}
Primary tools: {{tools}}
Typography system: {{typography}}
Audience for the style guide: {{audience}} (data analysts, developers, designers)

A style guide ensures all visualizations across the organization look coherent, communicate clearly, and meet accessibility standards.

1. Color system:
 PRIMARY PALETTE (for data encoding):
 - Primary: {{primary_color}} — use for the most important series or highlight
 - Secondary: 3–5 supporting colors for categorical series
 - Neutral: grey scale for non-data elements (axes, gridlines, background text)
 - Alert: one red/orange for negative values or warnings

 SEQUENTIAL PALETTES:
 - Single-hue: light-to-dark of the primary color
 - Multi-hue: define the start and end color (perceptually uniform progression)

 DIVERGING PALETTES:
 - Define: negative color, neutral midpoint color, positive color

 RULES:
 - Maximum 8 colors in any single chart
 - Never use color as the only encoding (add labels, patterns, or shapes)
 - All palettes must pass colorblind-safe test

2. Typography:
 - Chart title: {{heading_font}}, {{title_size}}pt, bold
 - Axis labels: {{body_font}}, 11pt, regular
 - Data labels: {{body_font}}, 10pt, regular
 - Annotations: {{body_font}}, 10pt, italic
 - Numbers: use tabular figures (all same width) for alignment in tables

3. Chart formatting standards:
 - Minimum chart width: 480px (for web); 3 inches (for print)
 - Minimum height: 60% of width for most charts
 - Background: white (#FFFFFF) or transparent
 - Gridlines: horizontal only, light grey (#E0E0E0), 0.5pt
 - No chart borders or shadows
 - Axis lines: left axis only (y-axis), light grey, 0.5pt
 - Tick marks: none unless necessary

4. Chart title standards:
 - Format: insight statement (not a label)
 - Length: 1 line maximum for presentation; 2 lines for reports
 - Capitalization: sentence case (not title case)
 - No period at end of title

5. Number formatting:
 - Revenue: $1.2M (> $1M), $456K (> $1K), $123 (< $1K)
 - Percentages: 23.4% (1 decimal), 100% (no decimal)
 - Counts: comma separator every 3 digits
 - Dates: 'Jan 2024' for months, 'Q1 2024' for quarters, '2024' for years
 - Ratios: 2.3× (not 2.3x)

6. Template files:
 - Provide: Tableau workbook template, Power BI template file, Python rcParams settings

Return: complete style guide document with all specifications, hex codes, template settings for each tool, and a one-page quick reference card. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
- Terms of Service 
- Privacy Policy 
- AI Policy 
- Licenses 
### AI Data Analysis Examples 

- LLM Benchmark on AI Data Analysis 
- Air Passengers Forecast 
- Iris Classification 
- Customer Churn Prediction 
- Energy Consumption Forecast 
### Resources 

- Example Python notebooks 
- Fix ModuleNotFoundError 
- Glossary 
- Brand 
- Answers 
- ML Algorithm Comparison 
- Research 
- Solutions 
### Products 

- MLJAR Studio 
- MLJAR AutoML 
- AI Data Analyst 
- AutoLab Experiments 
- Mercury 
### Tutorials 

- AutoML in Python: Beginner Tutorial with House Prices 
### Open Source 

- MLJAR AutoML 
- Mercury 
- More ... 
### AI Prompts 

- Prompts for Data Professionals 
- Data Analyst prompts 
- Business Analyst prompts 
- Data Scientist prompts 
- ML Engineer prompts 
- Data Engineer prompts 
- MLOps prompts 
### Compare 

- MLJAR Studio vs Julius 
- MLJAR Studio vs H2O 
- MLJAR Studio vs DataRobot 
- MLJAR Studio vs Jupyter 
- MLJAR Studio vs ChatGPT 
- MLJAR Studio vs Cursor 
### Company 

- Contact us 
- Services 
- About us 
- Blog Made by MLJAR. All rights reserved. Created in 🇵🇱 We ❤ you! 
We collect traffic information to improve the site. 

Data is collected in a privacy-friendly way (IP anonymization, no ads, no cross-site tracking). 
Analytics are only enabled if you accept. 
Read Privacy Policy Reject Accept
