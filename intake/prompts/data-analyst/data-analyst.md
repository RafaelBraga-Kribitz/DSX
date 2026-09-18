# Data Analyst *AI Prompts *

Data Analyst AI prompt library with 72 prompts in 7 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 7 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Data Analyst prompt categories 
7 categories 
### Visualization 

AI prompts for data visualization, charts, dashboards, storytelling, and communicating insights through visual design. 
16 prompts Auto Exploratory Dashboard Bar Chart with Ranking → 
### Data Cleaning 

AI prompts for data cleaning, handling missing values, removing duplicates, fixing schema issues, and improving dataset quality. 
15 prompts Automated Cleaning Code Generator Column Renaming Plan → 
### Data Exploration 

AI prompts for exploratory data analysis (EDA), dataset understanding, distributions, correlations, and initial data investigation. 
14 prompts Bivariate Relationship Analysis Categorical Column Profiling → 
### Business Insights 

AI prompts for generating business insights, summarizing analysis, identifying trends, and delivering actionable recommendations. 
8 prompts 5 Key Findings Churn Risk Analysis → 
### Forecasting 

AI prompts for forecasting, time series analysis, trend detection, seasonality modeling, and future value prediction. 
7 prompts Demand Forecast with External Factors Full Forecast Benchmark Chain → 
### SQL 

AI prompts for SQL queries, analytical queries, data profiling, joins, aggregations, and database-driven data analysis. 
7 prompts Cohort Retention Analysis Customer Lifetime Value Query → 
### Anomaly Detection 

AI prompts for anomaly detection, outlier analysis, unusual patterns, time series spikes, and identifying data inconsistencies. 
5 prompts Business Metric Spike Detection Multivariate Anomaly Detection → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 72 Visualization 16 Data Cleaning 15 Data Exploration 14 Business Insights 8 Forecasting 7 SQL 7 Anomaly Detection 5 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **72 **of 72 prompts 
## Visualization 
16 prompt s Visualization Beginner Prompt 01 
### Auto Exploratory Dashboard 
Create an exploratory visualization dashboard for this dataset using matplotlib and seaborn.

Include:
- Histogram for each numeric column (up to 6, pick the most interesting)
- Bar chart showing the top 10 values of the highest-cardinality categorical column
- Correlation heatmap for all numeric columns
- Line chart showing the trend over time if a date column exists

Layout: a 2×2 or 2×3 grid of subplots.
Style: clean white background, readable font sizes, meaningful titles and axis labels.
Do not use default matplotlib styles — apply a clean, minimal look. Copy prompt View page Show more ↓ Visualization Beginner Prompt 02 
### Bar Chart with Ranking 
Create a ranked bar chart for the most important categorical breakdown in this dataset:

1. Identify the best categorical column to use as the dimension (highest analytical value)
2. Identify the primary numeric metric to measure
3. Calculate the metric per category and sort from highest to lowest
4. Create a horizontal bar chart (easier to read category labels)
5. Color the top 3 bars in a highlight color, the rest in a neutral color
6. Add data labels at the end of each bar showing the exact value
7. Add a vertical dashed line at the average value
8. Title the chart: '[Metric] by [Category] — [period]'

Use a clean, minimal style with no unnecessary gridlines or chart elements. Copy prompt View page Show more ↓ Visualization Beginner Prompt 03 
### Correlation Heatmap 
Create a well-designed correlation heatmap for the numeric columns in this dataset:

1. Compute the Pearson correlation matrix for all numeric columns
2. Plot as a heatmap using a diverging colormap: dark blue for strong positive correlation, dark red for strong negative, white for zero
3. Show only the lower triangle (remove redundant upper triangle)
4. Add the correlation coefficient value inside each cell, rounded to 2 decimal places
5. Bold or highlight cells where |r| > 0.7
6. Sort columns and rows so that highly correlated variables are clustered together (use hierarchical clustering on the correlation matrix)
7. Set figure size so all labels are readable without overlapping

Add a subtitle explaining what the strongest correlation means in business terms. Copy prompt View page Show more ↓ Visualization Advanced Template 04 
### Custom Report Chart Pack 
Create a complete chart pack for a {{report_type}} report on {{subject}} covering {{time_range}}.

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
- Export as a 5-page PDF or a 5-slide PowerPoint layout Copy prompt View page Show more ↓ Visualization Intermediate Prompt 05 
### Distribution Comparison Plot 
Create a visualization comparing the distribution of a key metric across multiple groups or segments:

1. Identify the primary numeric metric and the best grouping column in the dataset
2. Create a violin plot showing the full distribution shape per group
3. Overlay individual data points using a strip plot (jittered) for transparency
4. Add a box plot overlay to show median and quartiles clearly
5. Annotate each group with its median value and sample size (n=)
6. Sort groups from highest to lowest median
7. Use a color palette that distinguishes groups clearly without being distracting

Add a title that describes what comparison is being shown. Copy prompt View page Show more ↓ Visualization Intermediate Prompt 06 
### Executive KPI Dashboard 
Create an executive-ready KPI dashboard for this dataset.

1. Identify the 4–6 most important business metrics from the column names and data context
2. For each metric, create a time-series line chart with:
 - A trend line (7-day rolling average)
 - An annotation marking the most significant change point
 - Clear title, axis labels, and current value callout
3. Add a summary row at the top showing: current value, % change vs prior period, and a directional arrow (▲▼)
4. Use a consistent color palette — brand-neutral (blues and grays)
5. Layout should be presentation-ready (16:9 aspect ratio) Copy prompt View page Show more ↓ Visualization Advanced Chain 07 
### Full Chart Story Chain 
Step 1: Identify the single most important insight in this dataset that deserves a visual treatment.
Step 2: Choose the most appropriate chart type for that insight and justify the choice.
Step 3: Create the primary chart with full production styling: clean theme, annotated key points, descriptive title, subtitle with the insight stated explicitly.
Step 4: Create one supporting chart that provides necessary context or comparison for the primary chart.
Step 5: Write a 3-sentence data caption for the primary chart that a non-technical reader can understand — what is shown, what is the key finding, and what action does it suggest. Copy prompt View page Show more ↓ Visualization Intermediate Prompt 08 
### Heatmap Calendar for Daily Patterns 
Create a calendar heatmap to reveal daily and weekly patterns in this time series:

1. Aggregate the primary metric by day
2. Create a GitHub-style calendar heatmap where:
 - Rows are days of the week (Mon–Sun)
 - Columns are weeks
 - Cell color intensity represents the metric value (lighter = lower, darker = higher)
3. Use a sequential color palette (e.g. light yellow to dark green)
4. Add month labels along the top
5. Add a color bar legend showing the value scale
6. Annotate the 3 highest and 3 lowest days with their exact values

Below the chart, answer: Is there a clear day-of-week pattern? Is there a clear seasonal pattern across months? Copy prompt View page Show more ↓ Visualization Advanced Chain 09 
### Insight-First Visualization Chain 
Step 1: Analyze the dataset and identify the top 3 most important insights — each should be a specific, quantified finding that could drive a business decision.
Step 2: For each insight, select the single best chart type to communicate it visually. Justify your choice in one sentence.
Step 3: Build chart 1 with full production styling: meaningful title, subtitle stating the insight explicitly, annotated key data points, clean minimal theme.
Step 4: Build charts 2 and 3 in the same visual style as chart 1, ensuring a consistent look across all three.
Step 5: Arrange all three charts into a single figure with a shared title. Write a 50-word executive caption that tells the complete story across all three charts in sequence.
Step 6: Export the figure at 300 DPI. Suggest the most appropriate slide or document format for sharing with a non-technical audience. Copy prompt View page Show more ↓ Visualization Beginner Prompt 10 
### Missing Data Heatmap 
Create a visualization of missing data patterns in this dataset:

1. Generate a heatmap where rows are observations and columns are variables — missing values shown in a distinct color (e.g. red), present values in white or light gray
2. Sort columns left to right by missing value percentage (most missing on the left)
3. Add a bar chart below the heatmap showing the missing percentage per column
4. Add annotations for any columns with more than 20% missing values
5. Check for patterns: are missing values random, or do they cluster in certain rows or time periods?

Write a 2-sentence interpretation: what is the overall completeness of the dataset, and is the missing data pattern random or systematic? Copy prompt View page Show more ↓ Visualization Advanced Prompt 11 
### Multi-Metric Dashboard with Sparklines 
Create a compact multi-metric summary dashboard using sparklines:

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

This format is designed for a weekly business review where space is limited. Copy prompt View page Show more ↓ Visualization Beginner Prompt 12 
### Pie and Donut Chart for Composition 
Create a composition chart showing how a total is broken down across categories:

1. Identify the best categorical column for the breakdown (5–8 categories ideal)
2. Calculate each category's share of the total
3. Create a donut chart (not a pie — donut is cleaner and leaves room for a center label)
4. Place the total value and a label ('Total [metric]') in the center of the donut
5. Show percentage labels on each segment, but only if the segment is larger than 3% (suppress tiny labels)
6. Group all segments smaller than 2% into an 'Other' category
7. Use a qualitative color palette — no gradients, each category a distinct color
8. Add a clean legend outside the chart

Also create a companion table showing: category, count, percentage, ranked from largest to smallest. Copy prompt View page Show more ↓ Visualization Intermediate Prompt 13 
### Scatter Plot with Regression Line 
Create an annotated scatter plot showing the relationship between two key variables:

1. Identify the two most interesting numeric variables to compare (ideally a cause and an effect)
2. Create a scatter plot with:
 - Each point representing one row
 - A linear regression line with confidence band (95%)
 - The R² value displayed in the top corner
3. Color points by a categorical variable if one exists (e.g. region, product type)
4. Label the top 5 and bottom 5 outlier points with their identifier
5. Add axis labels that describe what each variable measures, including units
6. If the relationship is non-linear, also fit and plot a polynomial regression line

Write a one-sentence interpretation below the chart: what does the relationship mean in business terms? Copy prompt View page Show more ↓ Visualization Intermediate Template 14 
### Segment Comparison Chart 
Create a comparison chart for {{metric}} broken down by {{segment_column}}.

Chart specifications:
- Chart type: {{chart_type}} — bar chart for categorical comparison, line chart for time-series comparison, box plot for distribution comparison
- Time range: {{time_range}}
- Highlight the top 3 and bottom 3 segments with distinct colors
- Add a dashed reference line at the overall average value
- Annotate the highest and lowest data points with their exact values
- Title: '{{metric}} by {{segment_column}} — {{time_range}}'
- Export at 300 DPI suitable for a slide deck Copy prompt View page Show more ↓ Visualization Beginner Prompt 15 
### Single Metric Time Series Chart 
Create a clean time series chart for the primary metric in this dataset:

1. Plot the raw values as a thin line in a neutral color
2. Overlay a 7-day rolling average as a thicker, more prominent line
3. Add a horizontal reference line at the overall average
4. Annotate the global maximum and minimum points with their values and dates
5. Shade the area under the rolling average line with low opacity
6. Use a minimal style: no gridlines on the x-axis, light gridlines on y-axis, clean legend

Title the chart with the metric name and the date range shown. Copy prompt View page Show more ↓ Visualization Intermediate Prompt 16 
### Waterfall Chart for Change Analysis 
Create a waterfall chart to show how a metric changed between two periods:

1. Identify the starting value (e.g. last month's total) and ending value (this month's total)
2. Decompose the change into its contributing factors — what drove the increase or decrease? (look for dimension columns like region, product, channel)
3. Build a waterfall chart where:
 - First bar: starting value (blue)
 - Middle bars: positive contributors (green, going up) and negative contributors (red, going down)
 - Final bar: ending value (blue)
4. Add value labels on top of each bar
5. Add a dashed horizontal reference line at the starting value
6. Sort contributing factors from largest positive to largest negative

Title the chart: '[Metric]: [Start Period] to [End Period] — What Changed and Why' Copy prompt View page Show more ↓ 
## Data Cleaning 
15 prompt s Data Cleaning Advanced Prompt 01 
### Automated Cleaning Code Generator 
Analyze this dataset and generate a complete, production-ready Python cleaning script.

The script must:
1. Load the data
2. Fix all data type issues (with explicit dtype mapping)
3. Handle all missing values with the appropriate strategy per column
4. Remove or flag duplicate rows
5. Apply all string standardizations needed
6. Fix date columns to ISO 8601 format
7. Clip or remove outliers where appropriate
8. Assert data quality at the end: row count within expected range, no nulls in key columns, all dates in valid range

Code style requirements:
- Use pandas
- Add a comment above every transformation explaining why it is needed
- Include a final print() summary: rows before, rows after, columns changed
- Make the script idempotent — safe to run multiple times Copy prompt View page Show more ↓ Data Cleaning Beginner Prompt 02 
### Column Renaming Plan 
Review all column names in this dataset and produce a renaming plan:

1. Identify columns that violate snake_case convention (spaces, camelCase, PascalCase, hyphens, special characters)
2. Identify columns with unclear or ambiguous abbreviations (e.g. 'qty', 'amt', 'dt', 'flg')
3. Identify columns where the name doesn't match the apparent content based on sample values
4. Propose a clear, descriptive snake_case name for each column that needs renaming

Return a table: original_name | issue | proposed_name | reason
Also return a Python code snippet using df.rename() to apply all changes at once. Copy prompt View page Show more ↓ Data Cleaning Advanced Chain 03 
### Data Quality Score Chain 
Step 1: Assess completeness — calculate the percentage of non-null values across all columns and rows. Score: (non-null cells / total cells) × 100.
Step 2: Assess consistency — count type mismatches, formatting inconsistencies, and constraint violations. Score: 100 minus one point per violation type found.
Step 3: Assess uniqueness — count exact duplicate rows and near-duplicate rows. Score: (unique rows / total rows) × 100.
Step 4: Assess validity — count values that fail domain rules (impossible numbers, invalid dates, unexpected categoricals). Score: (valid rows / total rows) × 100.
Step 5: Compute an overall Data Quality Score as a weighted average: completeness 30%, consistency 25%, uniqueness 20%, validity 25%.
Step 6: Return a one-page Data Quality Report: score per dimension, overall score, top 5 issues to fix, and estimated effort to resolve each. Copy prompt View page Show more ↓ Data Cleaning Beginner Prompt 04 
### Data Type Fixer 
Audit and fix the data types in this dataset:
- Identify all columns where the stored type does not match the semantic type (e.g. dates stored as strings, IDs stored as floats, booleans stored as integers)
- For each mismatch: show current type, correct type, and a code snippet to convert it
- Check numeric columns for values that contain currency symbols, commas, or percent signs that prevent proper numeric parsing
- Identify any column that should be treated as an ordered categorical rather than a plain string

Return corrected pandas dtype assignments for the full dataset. Copy prompt View page Show more ↓ Data Cleaning Intermediate Prompt 05 
### Date and Time Standardization 
Standardize all date and time columns in this dataset:

1. Identify every column that contains dates or times, including those stored as strings
2. Detect all date format variations in use (e.g. 'MM/DD/YYYY', 'DD-Mon-YYYY', 'YYYY-MM-DD', Unix timestamps)
3. Convert all date columns to a single standard format: ISO 8601 (YYYY-MM-DD for dates, YYYY-MM-DDTHH:MM:SS for datetimes)
4. Handle timezone information: identify columns with mixed timezones and convert all to UTC
5. Extract useful components as new columns where relevant: year, month, day_of_week, hour, is_weekend
6. Flag any ambiguous dates where format is unclear (e.g. 01/02/03 could be Jan 2, 2003 or Feb 1, 2003)

Return the conversion code and a before/after sample for each date column. Copy prompt View page Show more ↓ Data Cleaning Intermediate Prompt 06 
### Duplicate Detection and Deduplication 
Find and handle all duplicate records in this dataset:

1. Exact duplicates — rows identical across all columns. Count them and show 3 examples.
2. Key duplicates — rows with the same primary key or identifier column but different values elsewhere. Which columns differ?
3. Fuzzy duplicates — near-identical records in string columns (name, email, address). Use fuzzy matching with a similarity threshold of 0.85.

For each type, recommend a deduplication strategy (keep first, keep last, merge, manual review).
Apply the strategy and report how many rows were removed. Copy prompt View page Show more ↓ Data Cleaning Intermediate Chain 07 
### Full Cleaning Pipeline 
Step 1: Audit the dataset — list all data quality issues: missing values, duplicates, type mismatches, impossible values, encoding problems, inconsistent formatting.
Step 2: Propose a prioritized cleaning plan. Order tasks from highest to lowest impact. Justify each decision.
Step 3: Execute every cleaning step. Show before and after statistics for each transformation.
Step 4: Validate the cleaned dataset — confirm row count retained, zero remaining missing values (or document intentional exceptions), type consistency.
Step 5: Generate a cleaning report: one row per transformation, with column name, issue type, action taken, and rows affected. Copy prompt View page Show more ↓ Data Cleaning Beginner Prompt 08 
### Impossible Value Detector 
Scan this dataset for values that are logically impossible or highly implausible:

1. Numeric impossibilities: negative ages, negative prices, quantities above a plausible maximum, percentages above 100 or below 0
2. Date impossibilities: future dates in historical columns, dates before the business existed, end dates before start dates
3. Cross-column contradictions: e.g. refund amount greater than original order amount, child account older than parent account
4. Statistical implausibility: values more than 6 standard deviations from the mean (not just outliers — true anomalies)

For each impossible value found: column, row index, value, why it is impossible, and recommended fix. Copy prompt View page Show more ↓ Data Cleaning Beginner Prompt 09 
### Missing Value Strategy 
Analyze all missing values in this dataset and recommend a handling strategy for each column.

For numeric columns, choose between: drop, mean imputation, median imputation, forward fill, or model-based imputation.
For categorical columns, choose between: drop, mode imputation, 'Unknown' category, or indicator variable.
For any column with more than 50% missing values, recommend dropping it.

Also scan for hidden nulls: empty strings, 'N/A', 'null', 'None', 'nan', '-', whitespace-only values.

Return a table: column | missing % | recommended strategy | rationale. Copy prompt View page Show more ↓ Data Cleaning Intermediate Prompt 10 
### Numeric Precision and Rounding Audit 
Audit the numeric precision in this dataset:

1. For each numeric column, check the number of decimal places used — is it consistent?
2. Identify columns where values are suspiciously round (e.g. all multiples of 100 or 1000) — this may indicate estimation or truncation
3. Check for floating point precision issues (e.g. 0.1 + 0.2 ≠ 0.3 artifacts stored as data)
4. Identify columns that should be integers but are stored as floats (e.g. counts, quantities, IDs)
5. Flag any columns where precision varies significantly across rows (some with 0 decimals, some with 8)

Return recommendations for the correct data type and precision for each numeric column, plus code to apply the corrections. Copy prompt View page Show more ↓ Data Cleaning Intermediate Prompt 11 
### Outlier Treatment 
Identify and treat outliers in all numeric columns:

1. Detect outliers using IQR (flag values beyond Q1 - 1.5×IQR and Q3 + 1.5×IQR)
2. For each outlier cluster, determine: data entry error, legitimate extreme, or distribution tail?
3. Apply appropriate treatment per column:
 - Cap at percentile boundary (Winsorization) if legitimate extremes
 - Replace with null then impute if likely data error
 - Keep as-is if confirmed legitimate
4. Show before/after statistics for each treated column
5. Document every decision made Copy prompt View page Show more ↓ Data Cleaning Intermediate Prompt 12 
### Referential Integrity Check 
Check referential integrity across the tables or joined datasets provided:

1. Identify all foreign key – primary key relationships between tables
2. For each relationship, count:
 - Orphaned records: foreign key values with no matching primary key
 - Unmatched primary keys: records in the parent table with no children
3. Calculate the match rate for each join: what percentage of records join successfully?
4. Show examples of orphaned records and identify the most common missing foreign key values
5. Assess the impact: if orphaned records are dropped, what percentage of rows would be lost from each table?

Return an integrity report table and recommend whether to: drop orphans, impute, or flag for manual review. Copy prompt View page Show more ↓ Data Cleaning Advanced Prompt 13 
### Schema and Constraint Validation 
Validate this dataset against data engineering best practices:

Naming: Are column names in snake_case? Any spaces, special characters, or ambiguous abbreviations?
Types: Do types match the semantic meaning? (e.g., IDs stored as float, dates stored as string, booleans stored as int)
Ranges: Are there numeric values outside a plausible range? (negative ages, prices, quantities; future dates in a historical column)
Cardinality: Do categorical columns contain unexpected values or obvious typos?
Referential integrity: If multiple tables are provided, do foreign keys match primary keys?

Return a validation report with columns: field | issue type | severity (error / warning / info) | description | suggested fix. Copy prompt View page Show more ↓ Data Cleaning Intermediate Prompt 14 
### String Standardization 
Standardize all text and string columns in this dataset:

1. Trim leading and trailing whitespace from all string fields
2. Detect and normalize inconsistent casing (e.g. 'new york', 'New York', 'NEW YORK' → 'New York')
3. Find and consolidate equivalent values using different spellings or abbreviations (e.g. 'US', 'USA', 'United States', 'U.S.A.')
4. Detect and fix common OCR or data entry errors (e.g. '0' vs 'O', '1' vs 'l')
5. Standardize phone numbers, postcodes, and email addresses to consistent formats where present

Return the full set of replacements applied and the number of rows affected by each. Copy prompt View page Show more ↓ Data Cleaning Beginner Prompt 15 
### Whitespace and Encoding Audit 
Audit this dataset for whitespace, encoding, and character set issues:

1. Find all string columns that contain leading or trailing whitespace
2. Detect non-printable characters, null bytes, or control characters embedded in string fields
3. Identify any columns with mixed encodings (UTF-8 vs Latin-1 artifacts like Ã© instead of é)
4. Find columns with inconsistent use of quotes, apostrophes, or escaped characters
5. Detect columns where numeric values are stored with thousands separators (1,234 vs 1234) or currency symbols ($1,234)
6. Check for Windows-style line endings (\r\n) in text fields

Return a list of affected columns, the issue type, an example, and the cleaning code to fix it. Copy prompt View page Show more ↓ 
## Data Exploration 
14 prompt s Data Exploration Intermediate Prompt 01 
### Bivariate Relationship Analysis 
Analyze pairwise relationships between the key variables in this dataset:

1. Identify the most important target or outcome variable
2. For each other numeric column, create a scatter plot vs the target variable and compute the correlation coefficient
3. For each categorical column, show the mean target value per category (group-by analysis)
4. Flag any non-linear relationships that a correlation coefficient would miss
5. Identify the single variable that has the strongest relationship with the target, linear or otherwise
6. Note any interaction effects — pairs of variables that together predict the target better than either alone

Return a ranked list of variables by predictive relationship strength. Copy prompt View page Show more ↓ Data Exploration Intermediate Prompt 02 
### Categorical Column Profiling 
Profile all categorical and text columns in this dataset:
- For each column: unique value count, top 10 most frequent values with percentages
- Flag high-cardinality columns (more than 50 unique values)
- Identify columns that look like free text vs controlled vocabulary
- Check for inconsistent formatting within the same column (e.g. 'USA' vs 'United States' vs 'us')
- Identify any categorical column that could be useful as a grouping or segmentation dimension

Return a profile table and highlight the 3 most analytically useful categorical columns. Copy prompt View page Show more ↓ Data Exploration Beginner Prompt 03 
### Column Relationship Map 
Map the relationships between columns in this dataset:

1. Identify likely primary key columns (unique identifiers)
2. Identify likely foreign key columns (references to other entities)
3. Group columns into logical categories: identifiers, dimensions, measures, dates, flags
4. For each measure column, identify which dimension columns are most likely used to slice or filter it
5. Draw a simple text-based entity map showing how columns relate to each other

This should help me understand the data model before I start querying. Copy prompt View page Show more ↓ Data Exploration Intermediate Prompt 04 
### Correlation Deep Dive 
Find all significant correlations in this dataset:
- Compute the full correlation matrix for all numeric columns
- List the top 10 strongest positive and negative correlations with their r values
- Flag any pairs with |r| > 0.85 as multicollinearity risks
- For each flagged pair, recommend which column to keep based on relationship to the target or business relevance
- Visualize the correlation matrix as a heatmap with annotations
- Note any correlations that are surprising or counterintuitive Copy prompt View page Show more ↓ Data Exploration Intermediate Prompt 05 
### Data Freshness and Latency Check 
Check how fresh and timely this dataset is:

1. What is the most recent record date in the dataset?
2. How many hours or days old is the most recent data compared to today?
3. Is there evidence of data latency — events that happened recently but haven't appeared yet?
4. Are records added in batches (e.g. large jumps at specific times) or continuously?
5. Compare record volume in the most recent period vs the equivalent prior period — does it look complete or truncated?
6. Flag any columns that suggest pipeline delays (e.g. processing_date significantly later than event_date)

Return a freshness verdict: Real-time / Near real-time / Daily batch / Delayed / Stale. Copy prompt View page Show more ↓ Data Exploration Beginner Prompt 06 
### Dataset Overview 
Give me a complete overview of this dataset. Include:
- Shape (rows, columns)
- Column names and data types
- Missing values per column (%)
- Basic statistics for numeric columns (mean, std, min, max, quartiles)
- Sample of first 5 rows

Highlight any immediate data quality issues you notice. Copy prompt View page Show more ↓ Data Exploration Advanced Prompt 07 
### Dimensionality Assessment 
Assess the dimensionality and information density of this dataset:

1. How many features are there relative to the number of rows? Is this dataset wide, tall, or balanced?
2. Apply PCA and report how many components explain 80%, 90%, and 95% of the variance — this shows the true effective dimensionality
3. Identify groups of highly correlated features that are effectively measuring the same thing
4. Flag any features that appear to be near-linear combinations of others (redundant features)
5. Identify features with near-zero variance — they carry almost no information
6. Recommend a minimum feature set that retains 90% of the information in the dataset

Return a dimensionality report with: original features, effective dimensions, redundant groups, and recommended feature set. Copy prompt View page Show more ↓ Data Exploration Intermediate Prompt 08 
### Distribution Analysis 
Analyze the distribution of every numeric column in this dataset:
- Compute mean, median, std, skewness, and kurtosis
- Identify columns with skewness above 1 or below -1
- Flag outliers using the IQR method (1.5× IQR rule)
- Suggest an appropriate transformation for skewed columns (log, sqrt, Box-Cox)
- Plot a histogram for each numeric column

Return a summary table: column | skewness | outlier count | recommended transformation. Copy prompt View page Show more ↓ Data Exploration Beginner Prompt 09 
### First Look at a New Dataset 
I just received this dataset and have never seen it before. Help me understand it from scratch:

1. What does this dataset appear to be about? What business domain or process does it describe?
2. What is the grain of the data — what does one row represent?
3. What are the most important columns, and what do they measure?
4. What time period does it cover?
5. What are the top 3 questions this data could answer?
6. What are the top 3 questions it clearly cannot answer?

Write your response in plain English, as if explaining to someone seeing data for the first time. Copy prompt View page Show more ↓ Data Exploration Advanced Chain 10 
### Full EDA Chain 
Step 1: Profile the dataset — shape, column types, missing values, duplicates, memory usage.
Step 2: Analyze distributions and detect outliers in all numeric columns.
Step 3: Analyze cardinality and value frequencies in all categorical columns. Flag any with high cardinality (>50 unique values).
Step 4: Compute and visualize the correlation matrix. Flag pairs with |r| > 0.85.
Step 5: Identify the 5 most interesting patterns, anomalies, or relationships in the data.
Step 6: Write a 1-page EDA summary report: dataset description, key findings, data quality issues, and recommended next steps. Copy prompt View page Show more ↓ Data Exploration Beginner Prompt 11 
### Numeric Column Summary Table 
Create a clean summary table for all numeric columns in this dataset.

For each numeric column include:
- Count of non-null values
- Mean and median
- Standard deviation
- Min and max
- 25th, 50th, and 75th percentiles
- Number of zeros
- Number of negative values
- Number of unique values

Format as a transposed table where each column name is a row.
Highlight any column where the mean and median differ by more than 20% — this indicates skewness.
Highlight any column with more than 10% zero values — these may need special treatment. Copy prompt View page Show more ↓ Data Exploration Intermediate Prompt 12 
### Outlier Landscape Overview 
Give me a comprehensive map of extreme values across this entire dataset:

1. For every numeric column, show the top 5 highest and bottom 5 lowest values with their row indices
2. Flag any value that exceeds 5 standard deviations from the mean — these are extreme outliers
3. Check whether extreme values cluster in the same rows (a single row that is extreme across many columns is suspicious)
4. Classify each extreme value: plausible business value, likely data error, or needs investigation
5. Calculate what percentage of rows contain at least one extreme value

Return a summary table and highlight the 3 rows most deserving of manual inspection. Copy prompt View page Show more ↓ Data Exploration Beginner Prompt 13 
### Quick Data Health Check 
Run a quick health check on this dataset and return a traffic-light summary:

🟢 Good / 🟡 Needs attention / 🔴 Critical issue

Check:
1. Completeness — missing values above 5% per column?
2. Consistency — mixed data types, formatting issues, encoding errors?
3. Timeliness — what is the date range? Are there gaps?
4. Accuracy — values that seem impossible or implausible?
5. Uniqueness — duplicate rows present?

For each check, state the status and a one-sentence finding. Copy prompt View page Show more ↓ Data Exploration Intermediate Prompt 14 
### Time Series Structure Check 
Inspect the temporal structure of this dataset:
- Identify all date, datetime, or timestamp columns
- For each: min date, max date, total time span, and inferred frequency (daily, weekly, monthly)
- Check for gaps in the time series — are there missing periods?
- Check for duplicate timestamps
- Identify any time-zone inconsistencies
- Plot the number of records per time period to visualize data volume over time

Summarise whether this dataset is suitable for time series analysis and flag any issues that must be resolved first. Copy prompt View page Show more ↓ 
## Business Insights 
8 prompt s Business Insights Beginner Prompt 01 
### 5 Key Findings 
Analyze this dataset and return exactly 5 key findings, ordered from most to least important.

For each finding:
- A bold one-sentence headline stating the finding
- Two to three supporting sentences with specific numbers from the data
- One sentence on the business implication

Rules:
- No filler or vague statements. Every sentence must contain a specific number or comparison.
- Findings must be distinct — no overlapping insights.
- Use plain language a non-analyst could understand.

End with one sentence: 'The finding that most urgently requires action is [finding N] because [reason].' Copy prompt View page Show more ↓ Business Insights Advanced Prompt 02 
### Churn Risk Analysis 
Identify customers or users at risk of churning based on behavioral signals in this dataset:

1. Define churn signals from the available columns (e.g. declining purchase frequency, reduced engagement, support ticket spikes, payment failures)
2. Score each customer on a churn risk scale of 1–10 based on the strength of signals present
3. Identify the top 20 highest-risk customers with their risk score and primary churn signal
4. Segment at-risk customers by reason: price sensitivity, product dissatisfaction, competitive alternative, inactivity
5. Recommend one targeted retention action per segment

Return a churn risk table and a 2-sentence executive summary of the overall churn risk level. Copy prompt View page Show more ↓ Business Insights Advanced Chain 03 
### Data Storytelling Chain 
Step 1: Identify the single most important insight in this dataset. State it in one sentence, as if telling a non-technical colleague.
Step 2: Find exactly 3 data points that serve as compelling evidence for this insight. For each: state the number, what it means, and why it matters.
Step 3: Find one counterintuitive or surprising finding that adds nuance and prevents oversimplification.
Step 4: Identify the top 2 questions this data cannot answer — what additional data would you need to be fully confident in your recommendation?
Step 5: Write a complete data narrative: opening hook, central insight with evidence, nuance, data gap acknowledgement, and a clear call to action. Copy prompt View page Show more ↓ Business Insights Beginner Prompt 04 
### Executive Summary 
Analyze this dataset and write a concise executive summary in exactly 3 paragraphs:

Paragraph 1 — Situation: What does this data describe? What is the main trend over the period shown?
Paragraph 2 — Complication: What is the most significant risk, anomaly, or missed opportunity hidden in the data? Cite at least two specific numbers.
Paragraph 3 — Recommendation: What is the single most important action to take, who should own it, and by when?

Tone: direct, data-driven, no jargon. Max 200 words total. Write as if presenting to a C-suite audience. Copy prompt View page Show more ↓ Business Insights Intermediate Template 05 
### KPI Status Report 
Generate a KPI status report for {{reporting_period}} using the data provided.

For each key metric:
- Current value and target (source: {{target_source}})
- Absolute and percentage change vs {{comparison_period}}
- Status label: ✅ On Track / ⚠️ At Risk / 🔴 Off Track
- One-sentence explanation of the primary driver behind the change
- If Off Track: one specific recommended corrective action

Format: a clean table with one KPI per row.
At the bottom, add a 2-sentence overall summary: is the business trending in the right direction, and what is the most urgent issue to address? Copy prompt View page Show more ↓ Business Insights Intermediate Prompt 06 
### Opportunity Sizing 
Use this dataset to size the biggest business opportunity available:

1. Identify the metric that has the largest gap between current performance and best-in-class performance (either internal top performer or industry benchmark if known)
2. Calculate the revenue or metric impact of closing 25%, 50%, and 100% of that gap
3. Identify which segment, region, or cohort offers the fastest path to closing the gap
4. Estimate the effort level: is this gap likely due to a process issue (fixable quickly) or a structural issue (requires longer investment)?
5. Write a one-paragraph opportunity statement suitable for an internal business case Copy prompt View page Show more ↓ Business Insights Intermediate Prompt 07 
### Pricing Analysis 
Analyze pricing patterns and their relationship to business outcomes in this dataset:

1. Show the distribution of prices across products, tiers, or regions
2. Identify any price clustering (common price points that appear frequently)
3. Calculate the correlation between price and volume/quantity — is there a clear demand elasticity signal?
4. Find the price point with the highest total revenue contribution (price × quantity)
5. Identify any products or segments where price and margin seem misaligned
6. Recommend 2–3 pricing adjustments based on the data, with estimated revenue impact of each Copy prompt View page Show more ↓ Business Insights Intermediate Prompt 08 
### Segment Performance Breakdown 
Analyze the performance of every segment in this dataset.

For each segment, compute:
- Size (row count and % of total)
- Mean and median of the primary metric
- Growth rate vs the prior period
- Share of total metric contribution

Then:
- Rank segments from highest to lowest performing
- Flag any segment with an unusual growth rate (more than 2 standard deviations from the average segment growth)
- Identify the segment with the highest untapped potential
- Write 3 concrete strategic recommendations based on the segment findings Copy prompt View page Show more ↓ 
## Forecasting 
7 prompt s Forecasting Advanced Template 01 
### Demand Forecast with External Factors 
Build a demand forecast that incorporates external factors:

1. Base model: fit a Prophet or ARIMA model on historical {{target_metric}} alone. Record baseline MAPE.
2. Add external regressors: {{external_factors}} (e.g. price, promotions, marketing spend, economic index). Fit a new model including these.
3. Compare accuracy: does adding external factors improve MAPE by more than 5%? If yes, use the richer model.
4. Identify which external factor has the highest predictive power (use feature importance or correlation with residuals)
5. Generate a {{forecast_horizon}}-day forecast with three scenarios: optimistic, base, pessimistic — varying the {{key_lever}} assumption.

Return: accuracy comparison table, feature importance chart, and the 3-scenario forecast plot. Copy prompt View page Show more ↓ Forecasting Advanced Chain 02 
### Full Forecast Benchmark Chain 
Step 1: Decompose the time series using STL decomposition. Identify and plot trend, seasonality, and residual components. Note the dominant seasonality period.
Step 2: Test for stationarity using the ADF test. If non-stationary, apply first differencing or log transformation and retest.
Step 3: Train three competing models on the first 80% of the data: (a) ARIMA with auto-selected p,d,q parameters, (b) Facebook Prophet with default settings, (c) Exponential Smoothing (Holt-Winters).
Step 4: Evaluate all three models on the held-out 20% test window. Report MAPE, RMSE, and MAE for each. Declare a winner.
Step 5: Use the winning model to generate a {{forecast_horizon}}-day forecast. Include 80% and 95% confidence intervals. Plot forecast vs actuals.
Step 6: Write a one-paragraph forecast commentary: expected trend, key risks, seasonality effects to watch for, and the confidence level in this forecast. Copy prompt View page Show more ↓ Forecasting Intermediate Prompt 03 
### Growth Rate Analysis 
Calculate and analyze growth rates for the primary metric in this dataset:

1. Compute week-over-week (WoW), month-over-month (MoM), and year-over-year (YoY) growth rates for each time period
2. Plot all three growth rate series on a single chart with a zero reference line
3. Identify the periods of fastest and slowest growth
4. Calculate whether growth is accelerating or decelerating — fit a trend to the MoM growth rate itself
5. Compare growth rates across segments if a segment column exists
6. Project where the metric will be in 90 days if the current growth trajectory continues unchanged

Return a growth rate table and a plain-English summary: is the business growing faster or slower than before, and is the trend improving or deteriorating? Copy prompt View page Show more ↓ Forecasting Intermediate Prompt 04 
### Prophet Forecast with Seasonality 
Build a time series forecast using Facebook Prophet on this dataset.

1. Prepare the data: rename the date column to 'ds' and the target column to 'y'
2. Configure Prophet with:
 - Yearly seasonality: auto-detect
 - Weekly seasonality: enabled if data frequency is daily
 - Country holidays: {{country_code}} if applicable
3. Split: use the last 20% of data as a test set
4. Fit the model on the training set and evaluate on the test set: report MAPE, MAE, and RMSE
5. Generate a forecast for the next {{forecast_horizon}} days with 80% and 95% uncertainty intervals
6. Plot: actual vs forecast, trend component, and seasonality components separately Copy prompt View page Show more ↓ Forecasting Intermediate Template 05 
### Scenario Planning Forecast 
Generate a 3-scenario forecast for {{metric}} over the next {{forecast_horizon}}:

Scenario definitions:
- Pessimistic: assume {{pessimistic_assumption}} (e.g. growth slows to half the current rate, churn increases by 20%)
- Base case: continue current trend with normal seasonality
- Optimistic: assume {{optimistic_assumption}} (e.g. growth accelerates by 50%, a new product launch captures additional market)

For each scenario:
- Plot the forecast line with a distinct color
- Show the projected value at 30, 60, and 90 days
- State the key assumption driving each scenario

Highlight the range between pessimistic and optimistic as a shaded uncertainty band.
Add a plain-English paragraph explaining what would need to be true for the optimistic scenario to materialize. Copy prompt View page Show more ↓ Forecasting Intermediate Prompt 06 
### Seasonality Decomposition 
Decompose this time series to understand its underlying components:

1. Apply STL (Seasonal-Trend decomposition using LOESS) to separate the series into trend, seasonality, and residual components
2. Plot all three components with the original series
3. Quantify the strength of the seasonal component: what percentage of variance does it explain?
4. Identify the dominant seasonality period (daily, weekly, monthly, annual)
5. Check the residual component — does it look like white noise or does it contain unexplained structure?
6. Describe in plain English: what is the underlying growth trend, what is the seasonal pattern, and are there any unusual residuals that need investigation? Copy prompt View page Show more ↓ Forecasting Beginner Prompt 07 
### Trend Projection 
Project the future trend of the primary metric in this dataset.

1. Fit both a linear and a polynomial (degree 2) trend line. Compare R² values — which fits better?
2. Calculate the compound growth rate (CAGR) over the full observed period
3. Project the metric 30, 60, and 90 days into the future using the better-fitting model
4. Check for seasonal patterns and, if found, describe how they affect the projection
5. State the 3 key assumptions behind this forecast and one external factor that could invalidate it Copy prompt View page Show more ↓ 
## SQL 
7 prompt s SQL Intermediate Template 01 
### Cohort Retention Analysis 
Write a SQL cohort retention analysis using the table {{table_name}} in {{database_type}}.

Definitions:
- Cohort: the month of a user's first {{cohort_event}} recorded in {{date_column}}
- Retention: whether the user performed {{retention_event}} in each subsequent month

The query should:
1. Define cohorts using a CTE that finds each user's first event month
2. Join back to activity data to find which months each user was active
3. Calculate cohort size and retention count per month offset (0, 1, 2, ... N)
4. Return a cohort × month offset matrix with retention percentages

Include comments on each CTE. Database: {{database_type}}. Copy prompt View page Show more ↓ SQL Advanced Template 02 
### Customer Lifetime Value Query 
Write a SQL query to calculate customer lifetime value (LTV) from the transactions table {{table_name}} in {{database_type}}.

The query should compute per customer:
- First purchase date and most recent purchase date
- Total number of orders
- Total revenue
- Average order value
- Purchase frequency (orders per month since first purchase)
- Predicted LTV using the formula: avg_order_value × purchase_frequency × customer_lifespan_months

Also segment customers into LTV tiers: Top 10%, Mid 40%, Bottom 50%.
Return one row per customer with all metrics and the LTV tier label.
Database: {{database_type}}. Copy prompt View page Show more ↓ SQL Beginner Template 03 
### Date Range and Gap Analysis 
Write a SQL query to analyze the date coverage of the table {{table_name}} using the date column {{date_column}} in {{database_type}}.

The query should:
1. Return min date, max date, and total days spanned
2. Count distinct dates present vs expected dates in the range
3. Identify any missing dates (gaps in the sequence)
4. Show the top 5 largest gaps with start date, end date, and gap length in days
5. Count records per month to show data volume over time

Add a comment explaining how to interpret each section. Copy prompt View page Show more ↓ SQL Intermediate Prompt 04 
### Funnel Analysis Query 
Write a SQL funnel analysis for a multi-step user journey in this dataset.

1. Identify the funnel steps from the event data (look for event_name or action columns)
2. For each step, count: users who reached it, users who converted to the next step, and the conversion rate
3. Calculate time between steps for users who completed each transition (median and p90)
4. Identify where the biggest drop-off occurs
5. Segment the funnel by at least one dimension (e.g., device type, acquisition channel, country) if the column exists

Return the full funnel table and a plain-English summary of the biggest opportunity for improvement. Copy prompt View page Show more ↓ SQL Intermediate Template 05 
### Running Metrics with Window Functions 
Write a SQL query for the table {{table_name}} using window functions to compute:

1. Running total of {{metric}} ordered by {{date_column}}
2. 7-day and 30-day moving average of {{metric}}
3. Rank of each {{entity_column}} by {{metric}} within each {{partition_column}}
4. Each row's {{metric}} as a percentage of its {{partition_column}} total
5. Period-over-period change: vs prior row and vs same period last year

Database: {{database_type}}. Add a comment explaining each window function used. Copy prompt View page Show more ↓ SQL Advanced Template 06 
### Slowly Changing Dimension Query 
Write a SQL Type 2 Slowly Changing Dimension (SCD) implementation for the dimension table {{dim_table}} in {{database_type}}.

The table structure uses:
- Natural key: {{natural_key}}
- Tracked attributes that trigger a new version: {{tracked_columns}}
- SCD columns to manage: surrogate_key, valid_from, valid_to, is_current

Write:
1. The CREATE TABLE statement with all required columns
2. The MERGE / UPSERT logic to handle: new records, changed records (expire old, insert new), unchanged records
3. A query to retrieve the current version of each record
4. A query to retrieve the historical version valid at a specific point in time: {{as_of_date}}

Add comments explaining the SCD logic at each step. Copy prompt View page Show more ↓ SQL Beginner Template 07 
### Table Profiling Query 
Write a SQL query to profile the table {{table_name}} in {{database_type}}.

The query should return:
- Total row count
- Distinct value count per column
- NULL count and NULL percentage per column
- Min, max, and average for numeric columns
- Top 5 most frequent values for categorical columns

Structure the output so each column appears as a separate row with all metrics in one result set.
Add comments explaining each section. Copy prompt View page Show more ↓ 
## Anomaly Detection 
5 prompt s Anomaly Detection Intermediate Prompt 01 
### Business Metric Spike Detection 
Scan all business metrics in this dataset for unusual spikes or drops:

1. For each metric, compute the week-over-week and month-over-month percentage change
2. Flag any change greater than 2 standard deviations from the historical average change rate
3. For flagged metrics, check whether the spike is isolated to one dimension (e.g. one region, one product) or affects the whole metric
4. Determine whether the spike is a one-off event or the start of a new trend
5. Rank flagged metrics by business impact (highest volume or revenue first)

Return a spike report table and a plain-English summary of the top 3 most concerning changes. Copy prompt View page Show more ↓ Anomaly Detection Advanced Prompt 02 
### Multivariate Anomaly Detection 
Detect anomalies that only appear in the combination of multiple variables:

1. Apply Isolation Forest to the full numeric feature matrix
2. Apply Local Outlier Factor (LOF) with n_neighbors=20
3. Find rows flagged as anomalous by both methods — these are high-confidence anomalies
4. For each high-confidence anomaly: show the full row, which features deviate most, and how they relate to each other
5. Compare anomalous rows against the median row to quantify how extreme each feature value is

Return a ranked anomaly report with confidence score and a plain-English description of what makes each anomaly unusual. Copy prompt View page Show more ↓ Anomaly Detection Advanced Chain 03 
### Root Cause Analysis Chain 
Step 1: Identify the anomaly — which metric, which timestamp, and how large is the deviation from expected?
Step 2: Slice the anomalous metric by every available dimension (region, product, channel, user segment, etc.). Where is the anomaly most concentrated?
Step 3: Check all other metrics in the same time window. Are there correlated anomalies that suggest a common cause?
Step 4: Compare the anomaly period against the same period from the prior week, prior month, and prior year. Is this pattern seasonal or truly novel?
Step 5: Synthesize your findings into a root cause report: top 3 hypotheses ranked by likelihood, supporting evidence for each, and recommended next diagnostic step. Copy prompt View page Show more ↓ Anomaly Detection Beginner Prompt 04 
### Statistical Outlier Detection 
Detect outliers across all numeric columns using three methods:

1. Z-score — flag values beyond ±3 standard deviations
2. IQR — flag values below Q1 − 1.5×IQR or above Q3 + 1.5×IQR
3. Isolation Forest — use if the dataset has more than 1,000 rows

For each outlier detected:
- Column, row index, value, and which method(s) flagged it
- Your assessment: likely data error, or genuine extreme value?

Return a ranked list sorted by severity (most extreme first). Copy prompt View page Show more ↓ Anomaly Detection Intermediate Prompt 05 
### Time Series Anomaly Detection 
Detect anomalies in this time series data:

1. Build a rolling mean ± 2 standard deviation envelope (window = 7 periods)
2. Flag all points outside the envelope as anomalies
3. Check for abrupt level shifts using a changepoint detection method
4. Identify seasonality anomalies — values that are unusual specifically for their time of day, weekday, or month

For each anomaly found:
- Timestamp, observed value, expected range
- Severity score from 1 (mild) to 10 (extreme)
- Hypothesis: what might have caused this anomaly? Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
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
