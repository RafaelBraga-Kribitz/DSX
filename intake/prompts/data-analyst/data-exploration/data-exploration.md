# Data Exploration *AI Prompts *

14 Data Analyst prompts in Data Exploration. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 13 single prompts · 1 chain. 

## AI prompts in Data Exploration 
14 prompts Intermediate Single prompt 01 
### Bivariate Relationship Analysis 

Bivariate Relationship Analysis is a intermediate prompt for data exploration. This prompt helps the user understand the structure, meaning, and analytical potential of a dataset before moving into deeper work. It is designed to surface what is in the data, how trustworthy it looks, and which columns, relationships, or patterns deserve attention first. Use it early in an analysis workflow to reduce guesswork and create a shared understanding of the dataset. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Analyze pairwise relationships between the key variables in this dataset:

1. Identify the most important target or outcome variable
2. For each other numeric column, create a scatter plot vs the target variable and compute the correlation coefficient
3. For each categorical column, show the mean target value per category (group-by analysis)
4. Flag any non-linear relationships that a correlation coefficient would miss
5. Identify the single variable that has the strongest relationship with the target, linear or otherwise
6. Note any interaction effects — pairs of variables that together predict the target better than either alone

Return a ranked list of variables by predictive relationship strength. Copy prompt Open prompt details Intermediate Single prompt 02 
### Categorical Column Profiling 

Categorical Column Profiling is a intermediate prompt for data exploration. This prompt helps the user understand the structure, meaning, and analytical potential of a dataset before moving into deeper work. It is designed to surface what is in the data, how trustworthy it looks, and which columns, relationships, or patterns deserve attention first. Use it early in an analysis workflow to reduce guesswork and create a shared understanding of the dataset. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Profile all categorical and text columns in this dataset:
- For each column: unique value count, top 10 most frequent values with percentages
- Flag high-cardinality columns (more than 50 unique values)
- Identify columns that look like free text vs controlled vocabulary
- Check for inconsistent formatting within the same column (e.g. 'USA' vs 'United States' vs 'us')
- Identify any categorical column that could be useful as a grouping or segmentation dimension

Return a profile table and highlight the 3 most analytically useful categorical columns. Copy prompt Open prompt details Beginner Single prompt 03 
### Column Relationship Map 

Column Relationship Map is a beginner prompt for data exploration. This prompt helps the user understand the structure, meaning, and analytical potential of a dataset before moving into deeper work. It is designed to surface what is in the data, how trustworthy it looks, and which columns, relationships, or patterns deserve attention first. Use it early in an analysis workflow to reduce guesswork and create a shared understanding of the dataset. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Map the relationships between columns in this dataset:

1. Identify likely primary key columns (unique identifiers)
2. Identify likely foreign key columns (references to other entities)
3. Group columns into logical categories: identifiers, dimensions, measures, dates, flags
4. For each measure column, identify which dimension columns are most likely used to slice or filter it
5. Draw a simple text-based entity map showing how columns relate to each other

This should help me understand the data model before I start querying. Copy prompt Open prompt details Intermediate Single prompt 04 
### Correlation Deep Dive 

Correlation Deep Dive is a intermediate prompt for data exploration. This prompt helps the user understand the structure, meaning, and analytical potential of a dataset before moving into deeper work. It is designed to surface what is in the data, how trustworthy it looks, and which columns, relationships, or patterns deserve attention first. Use it early in an analysis workflow to reduce guesswork and create a shared understanding of the dataset. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Find all significant correlations in this dataset:
- Compute the full correlation matrix for all numeric columns
- List the top 10 strongest positive and negative correlations with their r values
- Flag any pairs with |r| > 0.85 as multicollinearity risks
- For each flagged pair, recommend which column to keep based on relationship to the target or business relevance
- Visualize the correlation matrix as a heatmap with annotations
- Note any correlations that are surprising or counterintuitive Copy prompt Open prompt details Intermediate Single prompt 05 
### Data Freshness and Latency Check 

Data Freshness and Latency Check is a intermediate prompt for data exploration. This prompt helps the user understand the structure, meaning, and analytical potential of a dataset before moving into deeper work. It is designed to surface what is in the data, how trustworthy it looks, and which columns, relationships, or patterns deserve attention first. Use it early in an analysis workflow to reduce guesswork and create a shared understanding of the dataset. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Check how fresh and timely this dataset is:

1. What is the most recent record date in the dataset?
2. How many hours or days old is the most recent data compared to today?
3. Is there evidence of data latency — events that happened recently but haven't appeared yet?
4. Are records added in batches (e.g. large jumps at specific times) or continuously?
5. Compare record volume in the most recent period vs the equivalent prior period — does it look complete or truncated?
6. Flag any columns that suggest pipeline delays (e.g. processing_date significantly later than event_date)

Return a freshness verdict: Real-time / Near real-time / Daily batch / Delayed / Stale. Copy prompt Open prompt details Beginner Single prompt 06 
### Dataset Overview 

Dataset Overview is a beginner prompt for data exploration. This prompt helps the user understand the structure, meaning, and analytical potential of a dataset before moving into deeper work. It is designed to surface what is in the data, how trustworthy it looks, and which columns, relationships, or patterns deserve attention first. Use it early in an analysis workflow to reduce guesswork and create a shared understanding of the dataset. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Give me a complete overview of this dataset. Include:
- Shape (rows, columns)
- Column names and data types
- Missing values per column (%)
- Basic statistics for numeric columns (mean, std, min, max, quartiles)
- Sample of first 5 rows

Highlight any immediate data quality issues you notice. Copy prompt Open prompt details Advanced Single prompt 07 
### Dimensionality Assessment 

Dimensionality Assessment is a advanced prompt for data exploration. This prompt helps the user understand the structure, meaning, and analytical potential of a dataset before moving into deeper work. It is designed to surface what is in the data, how trustworthy it looks, and which columns, relationships, or patterns deserve attention first. Use it early in an analysis workflow to reduce guesswork and create a shared understanding of the dataset. It is best suited for direct execution against a real dataset. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. 
Prompt text Assess the dimensionality and information density of this dataset:

1. How many features are there relative to the number of rows? Is this dataset wide, tall, or balanced?
2. Apply PCA and report how many components explain 80%, 90%, and 95% of the variance — this shows the true effective dimensionality
3. Identify groups of highly correlated features that are effectively measuring the same thing
4. Flag any features that appear to be near-linear combinations of others (redundant features)
5. Identify features with near-zero variance — they carry almost no information
6. Recommend a minimum feature set that retains 90% of the information in the dataset

Return a dimensionality report with: original features, effective dimensions, redundant groups, and recommended feature set. Copy prompt Open prompt details Intermediate Single prompt 08 
### Distribution Analysis 

Distribution Analysis is a intermediate prompt for data exploration. This prompt helps the user understand the structure, meaning, and analytical potential of a dataset before moving into deeper work. It is designed to surface what is in the data, how trustworthy it looks, and which columns, relationships, or patterns deserve attention first. Use it early in an analysis workflow to reduce guesswork and create a shared understanding of the dataset. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Analyze the distribution of every numeric column in this dataset:
- Compute mean, median, std, skewness, and kurtosis
- Identify columns with skewness above 1 or below -1
- Flag outliers using the IQR method (1.5× IQR rule)
- Suggest an appropriate transformation for skewed columns (log, sqrt, Box-Cox)
- Plot a histogram for each numeric column

Return a summary table: column | skewness | outlier count | recommended transformation. Copy prompt Open prompt details Beginner Single prompt 09 
### First Look at a New Dataset 

First Look at a New Dataset is a beginner prompt for data exploration. This prompt helps the user understand the structure, meaning, and analytical potential of a dataset before moving into deeper work. It is designed to surface what is in the data, how trustworthy it looks, and which columns, relationships, or patterns deserve attention first. Use it early in an analysis workflow to reduce guesswork and create a shared understanding of the dataset. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text I just received this dataset and have never seen it before. Help me understand it from scratch:

1. What does this dataset appear to be about? What business domain or process does it describe?
2. What is the grain of the data — what does one row represent?
3. What are the most important columns, and what do they measure?
4. What time period does it cover?
5. What are the top 3 questions this data could answer?
6. What are the top 3 questions it clearly cannot answer?

Write your response in plain English, as if explaining to someone seeing data for the first time. Copy prompt Open prompt details Advanced Chain 10 
### Full EDA Chain 

Full EDA Chain is a advanced chain for data exploration. This prompt helps the user understand the structure, meaning, and analytical potential of a dataset before moving into deeper work. It is designed to surface what is in the data, how trustworthy it looks, and which columns, relationships, or patterns deserve attention first. Use it early in an analysis workflow to reduce guesswork and create a shared understanding of the dataset. It is structured as a multi-step chain so the AI can reason through the problem in a deliberate order and produce a more complete result. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. 
Prompt text Step 1: Profile the dataset — shape, column types, missing values, duplicates, memory usage.
Step 2: Analyze distributions and detect outliers in all numeric columns.
Step 3: Analyze cardinality and value frequencies in all categorical columns. Flag any with high cardinality (>50 unique values).
Step 4: Compute and visualize the correlation matrix. Flag pairs with |r| > 0.85.
Step 5: Identify the 5 most interesting patterns, anomalies, or relationships in the data.
Step 6: Write a 1-page EDA summary report: dataset description, key findings, data quality issues, and recommended next steps. Copy prompt Open prompt details Beginner Single prompt 11 
### Numeric Column Summary Table 

Numeric Column Summary Table is a beginner prompt for data exploration. This prompt helps the user understand the structure, meaning, and analytical potential of a dataset before moving into deeper work. It is designed to surface what is in the data, how trustworthy it looks, and which columns, relationships, or patterns deserve attention first. Use it early in an analysis workflow to reduce guesswork and create a shared understanding of the dataset. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Create a clean summary table for all numeric columns in this dataset.

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
Highlight any column with more than 10% zero values — these may need special treatment. Copy prompt Open prompt details Intermediate Single prompt 12 
### Outlier Landscape Overview 

Outlier Landscape Overview is a intermediate prompt for data exploration. This prompt helps the user understand the structure, meaning, and analytical potential of a dataset before moving into deeper work. It is designed to surface what is in the data, how trustworthy it looks, and which columns, relationships, or patterns deserve attention first. Use it early in an analysis workflow to reduce guesswork and create a shared understanding of the dataset. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Give me a comprehensive map of extreme values across this entire dataset:

1. For every numeric column, show the top 5 highest and bottom 5 lowest values with their row indices
2. Flag any value that exceeds 5 standard deviations from the mean — these are extreme outliers
3. Check whether extreme values cluster in the same rows (a single row that is extreme across many columns is suspicious)
4. Classify each extreme value: plausible business value, likely data error, or needs investigation
5. Calculate what percentage of rows contain at least one extreme value

Return a summary table and highlight the 3 rows most deserving of manual inspection. Copy prompt Open prompt details Beginner Single prompt 13 
### Quick Data Health Check 

Quick Data Health Check is a beginner prompt for data exploration. This prompt helps the user understand the structure, meaning, and analytical potential of a dataset before moving into deeper work. It is designed to surface what is in the data, how trustworthy it looks, and which columns, relationships, or patterns deserve attention first. Use it early in an analysis workflow to reduce guesswork and create a shared understanding of the dataset. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Run a quick health check on this dataset and return a traffic-light summary:

🟢 Good / 🟡 Needs attention / 🔴 Critical issue

Check:
1. Completeness — missing values above 5% per column?
2. Consistency — mixed data types, formatting issues, encoding errors?
3. Timeliness — what is the date range? Are there gaps?
4. Accuracy — values that seem impossible or implausible?
5. Uniqueness — duplicate rows present?

For each check, state the status and a one-sentence finding. Copy prompt Open prompt details Intermediate Single prompt 14 
### Time Series Structure Check 

Time Series Structure Check is a intermediate prompt for data exploration. This prompt helps the user understand the structure, meaning, and analytical potential of a dataset before moving into deeper work. It is designed to surface what is in the data, how trustworthy it looks, and which columns, relationships, or patterns deserve attention first. Use it early in an analysis workflow to reduce guesswork and create a shared understanding of the dataset. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Inspect the temporal structure of this dataset:
- Identify all date, datetime, or timestamp columns
- For each: min date, max date, total time span, and inferred frequency (daily, weekly, monthly)
- Check for gaps in the time series — are there missing periods?
- Check for duplicate timestamps
- Identify any time-zone inconsistencies
- Plot the number of records per time period to visualize data volume over time

Summarise whether this dataset is suitable for time series analysis and flag any issues that must be resolved first. Copy prompt Open prompt details 
## Recommended Data Exploration workflow 
1 
### Bivariate Relationship Analysis 

Start with a focused prompt in Data Exploration so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Categorical Column Profiling 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Column Relationship Map 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Correlation Deep Dive 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
