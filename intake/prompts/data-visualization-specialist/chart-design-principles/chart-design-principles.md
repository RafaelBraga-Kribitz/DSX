# Chart Design Principles *AI Prompts *

5 Data Visualization Specialist prompts in Chart Design Principles. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 5 single prompts. 

## AI prompts in Chart Design Principles 
5 prompts Intermediate Single prompt 01 
### Annotation and Labeling Guide 

Design the annotation and labeling strategy for this chart. Chart type: {{chart_type}} Key insight to communicate: {{key_insight}} Audience: {{audience}} 1. Title and subtitle s... 
Prompt text Design the annotation and labeling strategy for this chart.

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

Return: title and subtitle for this specific chart, axis label specification, data label strategy, callout annotation text, and legend placement decision. Copy prompt Open prompt details Beginner Single prompt 02 
### Chart Type Selector 

Help me choose the right chart type for this data and communication goal. Data description: {{data_description}} Communication goal: {{goal}} (compare, show trend, show distribu... 
Prompt text Help me choose the right chart type for this data and communication goal.

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

Return: recommended chart type, alternative, anti-pattern warning, and a mockup description of what the chart should look like. Copy prompt Open prompt details Intermediate Single prompt 03 
### Color Strategy for Data Viz 

Design a color strategy for this data visualization or dashboard. Visualization type: {{viz_type}} Data encoding needs: {{encoding_needs}} (categorical groups, sequential scale,... 
Prompt text Design a color strategy for this data visualization or dashboard.

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

Return: palette specification (hex codes), palette type with rationale, colorblind test plan, contrast check, and usage rules. Copy prompt Open prompt details Beginner Single prompt 04 
### Data-Ink Ratio Audit 

Audit this chart for unnecessary visual elements and recommend how to reduce chartjunk while preserving information. Chart description: {{chart_description}} Edward Tufte's prin... 
Prompt text Audit this chart for unnecessary visual elements and recommend how to reduce chartjunk while preserving information.

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

Return: element-by-element audit table, removal recommendations, and a description of the simplified version. Copy prompt Open prompt details Advanced Single prompt 05 
### Small Multiples Design 

Design a small multiples layout for this dataset instead of a cluttered single chart. Dataset: {{dataset_description}} Dimension to facet by: {{facet_dimension}} (region, produc... 
Prompt text Design a small multiples layout for this dataset instead of a cluttered single chart.

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

Return: layout specification (rows × columns, panel size), axis sharing rules, panel ordering recommendation, and labeling specification. Copy prompt Open prompt details 
## Recommended Chart Design Principles workflow 
1 
### Annotation and Labeling Guide 

Start with a focused prompt in Chart Design Principles so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Chart Type Selector 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Color Strategy for Data Viz 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Data-Ink Ratio Audit 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
