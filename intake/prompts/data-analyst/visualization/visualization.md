# Visualization *AI Prompts *

16 Data Analyst prompts in Visualization. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 12 single prompts · 2 chains · 2 templates. 

## AI prompts in Visualization 
16 prompts Beginner Single prompt 01 
### Auto Exploratory Dashboard 

Auto Exploratory Dashboard is a beginner prompt for visualization. This prompt helps the AI turn raw data into charts or dashboards that communicate insight clearly. It goes beyond simply plotting values by asking for chart choice, layout, annotations, and business interpretation. Use it when you need visuals that are ready for exploration, reporting, or stakeholder communication. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Create an exploratory visualization dashboard for this dataset using matplotlib and seaborn.

Include:
- Histogram for each numeric column (up to 6, pick the most interesting)
- Bar chart showing the top 10 values of the highest-cardinality categorical column
- Correlation heatmap for all numeric columns
- Line chart showing the trend over time if a date column exists

Layout: a 2×2 or 2×3 grid of subplots.
Style: clean white background, readable font sizes, meaningful titles and axis labels.
Do not use default matplotlib styles — apply a clean, minimal look. Copy prompt Open prompt details Beginner Single prompt 02 
### Bar Chart with Ranking 

Bar Chart with Ranking is a beginner prompt for visualization. This prompt helps the AI turn raw data into charts or dashboards that communicate insight clearly. It goes beyond simply plotting values by asking for chart choice, layout, annotations, and business interpretation. Use it when you need visuals that are ready for exploration, reporting, or stakeholder communication. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Create a ranked bar chart for the most important categorical breakdown in this dataset:

1. Identify the best categorical column to use as the dimension (highest analytical value)
2. Identify the primary numeric metric to measure
3. Calculate the metric per category and sort from highest to lowest
4. Create a horizontal bar chart (easier to read category labels)
5. Color the top 3 bars in a highlight color, the rest in a neutral color
6. Add data labels at the end of each bar showing the exact value
7. Add a vertical dashed line at the average value
8. Title the chart: '[Metric] by [Category] — [period]'

Use a clean, minimal style with no unnecessary gridlines or chart elements. Copy prompt Open prompt details Beginner Single prompt 03 
### Correlation Heatmap 

Correlation Heatmap is a beginner prompt for visualization. This prompt helps the AI turn raw data into charts or dashboards that communicate insight clearly. It goes beyond simply plotting values by asking for chart choice, layout, annotations, and business interpretation. Use it when you need visuals that are ready for exploration, reporting, or stakeholder communication. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Create a well-designed correlation heatmap for the numeric columns in this dataset:

1. Compute the Pearson correlation matrix for all numeric columns
2. Plot as a heatmap using a diverging colormap: dark blue for strong positive correlation, dark red for strong negative, white for zero
3. Show only the lower triangle (remove redundant upper triangle)
4. Add the correlation coefficient value inside each cell, rounded to 2 decimal places
5. Bold or highlight cells where |r| > 0.7
6. Sort columns and rows so that highly correlated variables are clustered together (use hierarchical clustering on the correlation matrix)
7. Set figure size so all labels are readable without overlapping

Add a subtitle explaining what the strongest correlation means in business terms. Copy prompt Open prompt details Advanced Template 04 
### Custom Report Chart Pack 

Custom Report Chart Pack is a advanced template for visualization. This prompt helps the AI turn raw data into charts or dashboards that communicate insight clearly. It goes beyond simply plotting values by asking for chart choice, layout, annotations, and business interpretation. Use it when you need visuals that are ready for exploration, reporting, or stakeholder communication. It is structured as a reusable template, so placeholders can be filled in for a specific table, metric, or business context. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. 
Prompt text Create a complete chart pack for a {{report_type}} report on {{subject}} covering {{time_range}}.

The pack should include exactly these chart types in order:
1. An overview trend chart: {{primary_metric}} over time with 30-day moving average
2. A breakdown chart: {{primary_metric}} by {{dimension_column}} as a ranked bar chart
3. A comparison chart: current {{time_range}} vs prior {{time_range}} for top 5 {{dimension_column}} values
4. A composition chart: share of {{primary_metric}} by {{segment_column}} as a donut chart
5. A scatter or correlation chart: {{primary_metric}} vs {{secondary_metric}} with regression line

Style requirements:
- Consistent color palette across all 5 charts: primary color {{brand_color}}, accent {{accent_color}}
- All charts use the same font family and font sizes
- Each chart has a title, subtitle (one-sentence insight), and data source label
- Export as a 5-page PDF or a 5-slide PowerPoint layout Copy prompt Open prompt details Intermediate Single prompt 05 
### Distribution Comparison Plot 

Distribution Comparison Plot is a intermediate prompt for visualization. This prompt helps the AI turn raw data into charts or dashboards that communicate insight clearly. It goes beyond simply plotting values by asking for chart choice, layout, annotations, and business interpretation. Use it when you need visuals that are ready for exploration, reporting, or stakeholder communication. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Create a visualization comparing the distribution of a key metric across multiple groups or segments:

1. Identify the primary numeric metric and the best grouping column in the dataset
2. Create a violin plot showing the full distribution shape per group
3. Overlay individual data points using a strip plot (jittered) for transparency
4. Add a box plot overlay to show median and quartiles clearly
5. Annotate each group with its median value and sample size (n=)
6. Sort groups from highest to lowest median
7. Use a color palette that distinguishes groups clearly without being distracting

Add a title that describes what comparison is being shown. Copy prompt Open prompt details Intermediate Single prompt 06 
### Executive KPI Dashboard 

Executive KPI Dashboard is a intermediate prompt for visualization. This prompt helps the AI turn raw data into charts or dashboards that communicate insight clearly. It goes beyond simply plotting values by asking for chart choice, layout, annotations, and business interpretation. Use it when you need visuals that are ready for exploration, reporting, or stakeholder communication. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Create an executive-ready KPI dashboard for this dataset.

1. Identify the 4–6 most important business metrics from the column names and data context
2. For each metric, create a time-series line chart with:
 - A trend line (7-day rolling average)
 - An annotation marking the most significant change point
 - Clear title, axis labels, and current value callout
3. Add a summary row at the top showing: current value, % change vs prior period, and a directional arrow (▲▼)
4. Use a consistent color palette — brand-neutral (blues and grays)
5. Layout should be presentation-ready (16:9 aspect ratio) Copy prompt Open prompt details Advanced Chain 07 
### Full Chart Story Chain 

Full Chart Story Chain is a advanced chain for visualization. This prompt helps the AI turn raw data into charts or dashboards that communicate insight clearly. It goes beyond simply plotting values by asking for chart choice, layout, annotations, and business interpretation. Use it when you need visuals that are ready for exploration, reporting, or stakeholder communication. It is structured as a multi-step chain so the AI can reason through the problem in a deliberate order and produce a more complete result. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. 
Prompt text Step 1: Identify the single most important insight in this dataset that deserves a visual treatment.
Step 2: Choose the most appropriate chart type for that insight and justify the choice.
Step 3: Create the primary chart with full production styling: clean theme, annotated key points, descriptive title, subtitle with the insight stated explicitly.
Step 4: Create one supporting chart that provides necessary context or comparison for the primary chart.
Step 5: Write a 3-sentence data caption for the primary chart that a non-technical reader can understand — what is shown, what is the key finding, and what action does it suggest. Copy prompt Open prompt details Intermediate Single prompt 08 
### Heatmap Calendar for Daily Patterns 

Heatmap Calendar for Daily Patterns is a intermediate prompt for visualization. This prompt helps the AI turn raw data into charts or dashboards that communicate insight clearly. It goes beyond simply plotting values by asking for chart choice, layout, annotations, and business interpretation. Use it when you need visuals that are ready for exploration, reporting, or stakeholder communication. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Create a calendar heatmap to reveal daily and weekly patterns in this time series:

1. Aggregate the primary metric by day
2. Create a GitHub-style calendar heatmap where:
 - Rows are days of the week (Mon–Sun)
 - Columns are weeks
 - Cell color intensity represents the metric value (lighter = lower, darker = higher)
3. Use a sequential color palette (e.g. light yellow to dark green)
4. Add month labels along the top
5. Add a color bar legend showing the value scale
6. Annotate the 3 highest and 3 lowest days with their exact values

Below the chart, answer: Is there a clear day-of-week pattern? Is there a clear seasonal pattern across months? Copy prompt Open prompt details Advanced Chain 09 
### Insight-First Visualization Chain 

Insight-First Visualization Chain is a advanced chain for visualization. This prompt helps the AI turn raw data into charts or dashboards that communicate insight clearly. It goes beyond simply plotting values by asking for chart choice, layout, annotations, and business interpretation. Use it when you need visuals that are ready for exploration, reporting, or stakeholder communication. It is structured as a multi-step chain so the AI can reason through the problem in a deliberate order and produce a more complete result. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. 
Prompt text Step 1: Analyze the dataset and identify the top 3 most important insights — each should be a specific, quantified finding that could drive a business decision.
Step 2: For each insight, select the single best chart type to communicate it visually. Justify your choice in one sentence.
Step 3: Build chart 1 with full production styling: meaningful title, subtitle stating the insight explicitly, annotated key data points, clean minimal theme.
Step 4: Build charts 2 and 3 in the same visual style as chart 1, ensuring a consistent look across all three.
Step 5: Arrange all three charts into a single figure with a shared title. Write a 50-word executive caption that tells the complete story across all three charts in sequence.
Step 6: Export the figure at 300 DPI. Suggest the most appropriate slide or document format for sharing with a non-technical audience. Copy prompt Open prompt details Beginner Single prompt 10 
### Missing Data Heatmap 

Missing Data Heatmap is a beginner prompt for visualization. This prompt helps the AI turn raw data into charts or dashboards that communicate insight clearly. It goes beyond simply plotting values by asking for chart choice, layout, annotations, and business interpretation. Use it when you need visuals that are ready for exploration, reporting, or stakeholder communication. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Create a visualization of missing data patterns in this dataset:

1. Generate a heatmap where rows are observations and columns are variables — missing values shown in a distinct color (e.g. red), present values in white or light gray
2. Sort columns left to right by missing value percentage (most missing on the left)
3. Add a bar chart below the heatmap showing the missing percentage per column
4. Add annotations for any columns with more than 20% missing values
5. Check for patterns: are missing values random, or do they cluster in certain rows or time periods?

Write a 2-sentence interpretation: what is the overall completeness of the dataset, and is the missing data pattern random or systematic? Copy prompt Open prompt details Advanced Single prompt 11 
### Multi-Metric Dashboard with Sparklines 

Multi-Metric Dashboard with Sparklines is a advanced prompt for visualization. This prompt helps the AI turn raw data into charts or dashboards that communicate insight clearly. It goes beyond simply plotting values by asking for chart choice, layout, annotations, and business interpretation. Use it when you need visuals that are ready for exploration, reporting, or stakeholder communication. It is best suited for direct execution against a real dataset. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. 
Prompt text Create a compact multi-metric summary dashboard using sparklines:

1. Identify the top 6–8 business metrics in this dataset
2. For each metric, create one row in a summary table containing:
 - Metric name
 - Current value (latest period)
 - Change vs prior period: absolute and percentage, with colored arrow (▲ green / ▼ red)
 - A sparkline — a tiny inline line chart showing the last 12 periods of trend
 - A status indicator: ✅ On track / ⚠️ Watch / 🔴 Alert (based on whether the trend is improving or deteriorating)
3. Sort metrics by business importance, not alphabetically
4. Use a clean table layout — no heavy borders, subtle row alternation
5. The whole dashboard should fit on a single A4 page or slide

This format is designed for a weekly business review where space is limited. Copy prompt Open prompt details Beginner Single prompt 12 
### Pie and Donut Chart for Composition 

Pie and Donut Chart for Composition is a beginner prompt for visualization. This prompt helps the AI turn raw data into charts or dashboards that communicate insight clearly. It goes beyond simply plotting values by asking for chart choice, layout, annotations, and business interpretation. Use it when you need visuals that are ready for exploration, reporting, or stakeholder communication. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Create a composition chart showing how a total is broken down across categories:

1. Identify the best categorical column for the breakdown (5–8 categories ideal)
2. Calculate each category's share of the total
3. Create a donut chart (not a pie — donut is cleaner and leaves room for a center label)
4. Place the total value and a label ('Total [metric]') in the center of the donut
5. Show percentage labels on each segment, but only if the segment is larger than 3% (suppress tiny labels)
6. Group all segments smaller than 2% into an 'Other' category
7. Use a qualitative color palette — no gradients, each category a distinct color
8. Add a clean legend outside the chart

Also create a companion table showing: category, count, percentage, ranked from largest to smallest. Copy prompt Open prompt details Intermediate Single prompt 13 
### Scatter Plot with Regression Line 

Scatter Plot with Regression Line is a intermediate prompt for visualization. This prompt helps the AI turn raw data into charts or dashboards that communicate insight clearly. It goes beyond simply plotting values by asking for chart choice, layout, annotations, and business interpretation. Use it when you need visuals that are ready for exploration, reporting, or stakeholder communication. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Create an annotated scatter plot showing the relationship between two key variables:

1. Identify the two most interesting numeric variables to compare (ideally a cause and an effect)
2. Create a scatter plot with:
 - Each point representing one row
 - A linear regression line with confidence band (95%)
 - The R² value displayed in the top corner
3. Color points by a categorical variable if one exists (e.g. region, product type)
4. Label the top 5 and bottom 5 outlier points with their identifier
5. Add axis labels that describe what each variable measures, including units
6. If the relationship is non-linear, also fit and plot a polynomial regression line

Write a one-sentence interpretation below the chart: what does the relationship mean in business terms? Copy prompt Open prompt details Intermediate Template 14 
### Segment Comparison Chart 

Segment Comparison Chart is a intermediate template for visualization. This prompt helps the AI turn raw data into charts or dashboards that communicate insight clearly. It goes beyond simply plotting values by asking for chart choice, layout, annotations, and business interpretation. Use it when you need visuals that are ready for exploration, reporting, or stakeholder communication. It is structured as a reusable template, so placeholders can be filled in for a specific table, metric, or business context. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Create a comparison chart for {{metric}} broken down by {{segment_column}}.

Chart specifications:
- Chart type: {{chart_type}} — bar chart for categorical comparison, line chart for time-series comparison, box plot for distribution comparison
- Time range: {{time_range}}
- Highlight the top 3 and bottom 3 segments with distinct colors
- Add a dashed reference line at the overall average value
- Annotate the highest and lowest data points with their exact values
- Title: '{{metric}} by {{segment_column}} — {{time_range}}'
- Export at 300 DPI suitable for a slide deck Copy prompt Open prompt details Beginner Single prompt 15 
### Single Metric Time Series Chart 

Single Metric Time Series Chart is a beginner prompt for visualization. This prompt helps the AI turn raw data into charts or dashboards that communicate insight clearly. It goes beyond simply plotting values by asking for chart choice, layout, annotations, and business interpretation. Use it when you need visuals that are ready for exploration, reporting, or stakeholder communication. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Create a clean time series chart for the primary metric in this dataset:

1. Plot the raw values as a thin line in a neutral color
2. Overlay a 7-day rolling average as a thicker, more prominent line
3. Add a horizontal reference line at the overall average
4. Annotate the global maximum and minimum points with their values and dates
5. Shade the area under the rolling average line with low opacity
6. Use a minimal style: no gridlines on the x-axis, light gridlines on y-axis, clean legend

Title the chart with the metric name and the date range shown. Copy prompt Open prompt details Intermediate Single prompt 16 
### Waterfall Chart for Change Analysis 

Waterfall Chart for Change Analysis is a intermediate prompt for visualization. This prompt helps the AI turn raw data into charts or dashboards that communicate insight clearly. It goes beyond simply plotting values by asking for chart choice, layout, annotations, and business interpretation. Use it when you need visuals that are ready for exploration, reporting, or stakeholder communication. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Create a waterfall chart to show how a metric changed between two periods:

1. Identify the starting value (e.g. last month's total) and ending value (this month's total)
2. Decompose the change into its contributing factors — what drove the increase or decrease? (look for dimension columns like region, product, channel)
3. Build a waterfall chart where:
 - First bar: starting value (blue)
 - Middle bars: positive contributors (green, going up) and negative contributors (red, going down)
 - Final bar: ending value (blue)
4. Add value labels on top of each bar
5. Add a dashed horizontal reference line at the starting value
6. Sort contributing factors from largest positive to largest negative

Title the chart: '[Metric]: [Start Period] to [End Period] — What Changed and Why' Copy prompt Open prompt details 
## Recommended Visualization workflow 
1 
### Auto Exploratory Dashboard 

Start with a focused prompt in Visualization so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Bar Chart with Ranking 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Correlation Heatmap 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Custom Report Chart Pack 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
