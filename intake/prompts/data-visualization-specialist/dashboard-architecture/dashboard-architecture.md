# Dashboard Architecture *AI Prompts *

5 Data Visualization Specialist prompts in Dashboard Architecture. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 4 single prompts · 1 chain. 

## AI prompts in Dashboard Architecture 
5 prompts Beginner Single prompt 01 
### Dashboard Layout Design 

Design the layout and information hierarchy for this dashboard. Dashboard purpose: {{purpose}} Audience: {{audience}} Key decisions it supports: {{decisions}} Available metrics:... 
Prompt text Design the layout and information hierarchy for this dashboard.

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

Return: sketch layout description (rows, columns, chart assignments), filter specification, whitespace guidelines, and mobile adaptation notes. Copy prompt Open prompt details Advanced Single prompt 02 
### Dashboard Performance Optimization 

Diagnose and fix slow dashboard performance. Dashboard tool: {{tool}} Current load time: {{load_time}} Data size: {{data_size}} User complaint: {{complaint}} 1. Diagnose the bot... 
Prompt text Diagnose and fix slow dashboard performance.

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

Return: bottleneck diagnosis, prioritized optimization list with estimated improvement per action, and implementation steps for the tool specified. Copy prompt Open prompt details Intermediate Single prompt 03 
### Drill-Down Navigation Design 

Design a drill-down navigation structure for this dashboard so users can move from summary to detail without losing context. Dashboard: {{dashboard_name}} Data hierarchy: {{hier... 
Prompt text Design a drill-down navigation structure for this dashboard so users can move from summary to detail without losing context.

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

Return: navigation pattern recommendation, breadcrumb design specification, filter persistence rules, and mobile navigation approach. Copy prompt Open prompt details Advanced Chain 04 
### Full Dashboard Design Chain 

Step 1: Requirements — define the dashboard's purpose in one sentence. Identify the audience (technical level, role, decision they need to make). List the top 5 questions the da... 
Prompt text Step 1: Requirements — define the dashboard's purpose in one sentence. Identify the audience (technical level, role, decision they need to make). List the top 5 questions the dashboard must answer. Define the data sources and refresh frequency.
Step 2: KPI selection — from all available metrics, select the 3–5 most important for the stated purpose. For each: define the metric precisely, specify the comparison periods, identify the direction of good (up or down), and assign an owner.
Step 3: Layout design — sketch the dashboard layout (rows and columns). Apply F-pattern reading order. Assign each chart to a position based on importance. Specify filter placement, whitespace, and scroll behavior.
Step 4: Chart design — for each chart position, specify: chart type (using the chart selection framework), data it displays, color encoding, axis labels, data labels vs gridlines decision, and title (insight statement, not label).
Step 5: Color and typography — define the color palette (categorical, sequential, diverging). Check all colors for colorblind safety and WCAG contrast compliance. Specify font, font sizes, and number formatting.
Step 6: Interactivity design — specify: which elements are clickable (and what happens), filter behavior (what each filter affects), drill-down paths, and tooltip content for each chart.
Step 7: Performance and accessibility — estimate query count and data volume. Identify pre-aggregation opportunities. Write alt text for each chart. Verify keyboard navigability. Document the refresh schedule and caching strategy.
Step 8: Review and iteration — list 3 questions to ask stakeholders in the first review. Define the success criteria: what would make this dashboard 'done'? Specify how usage will be measured post-launch. Copy prompt Open prompt details Intermediate Single prompt 05 
### KPI Card Design 

Design KPI summary cards for the top section of this dashboard. Metrics to display: {{metrics}} Comparison periods: {{comparisons}} (vs last week, vs last year, vs target) Audie... 
Prompt text Design KPI summary cards for the top section of this dashboard.

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

Return: KPI card specification for each metric, formatting rules, color coding decisions, and sparkline design. Copy prompt Open prompt details 
## Recommended Dashboard Architecture workflow 
1 
### Dashboard Layout Design 

Start with a focused prompt in Dashboard Architecture so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Dashboard Performance Optimization 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Drill-Down Navigation Design 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Full Dashboard Design Chain 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
