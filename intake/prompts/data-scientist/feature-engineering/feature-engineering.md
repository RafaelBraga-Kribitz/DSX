# Feature Engineering *AI Prompts *

11 Data Scientist prompts in Feature Engineering. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 10 single prompts · 1 chain. 

## AI prompts in Feature Engineering 
11 prompts Beginner Single prompt 01 
### Date Feature Extraction 

This prompt turns raw date and datetime columns into practical model-ready features. It is useful when temporal information exists but has not yet been decomposed into parts that models can learn from easily. It also encourages creation of interval features when multiple time columns exist. 
Prompt text Extract all useful features from the date and datetime columns in this dataset.

For each date column, create:
- year, month, day, day_of_week (0=Monday), day_of_year
- quarter, week_of_year
- is_weekend (boolean)
- is_month_start, is_month_end (boolean)
- is_quarter_start, is_quarter_end (boolean)
- days_since_epoch (numeric, for ordinal encoding)
- If the column is a datetime: hour, minute, part_of_day (morning/afternoon/evening/night)

Also compute time-difference features if multiple date columns exist:
- days_between_[col1]_and_[col2] for all meaningful pairs

Return the feature creation code in pandas and a list of all new column names created. Copy prompt Open prompt details Advanced Single prompt 02 
### Embedding Features from Text 

This prompt converts text columns into usable numerical representations at several levels of sophistication. It is appropriate when text may contain sentiment, topic, style, or semantic meaning that can improve predictive performance. It combines lightweight handcrafted features with sparse and dense text representations. 
Prompt text Generate numeric features from the text columns in this dataset for use in a machine learning model.

For each text column:
1. Basic statistical features: character count, word count, sentence count, average word length, punctuation count
2. Lexical features: unique word ratio (vocabulary richness), stopword ratio, uppercase ratio
3. Sentiment features: positive score, negative score, neutral score, compound score using VADER
4. TF-IDF features: top 50 unigrams and top 20 bigrams (sparse matrix)
5. Dense embedding: use sentence-transformers (all-MiniLM-L6-v2) to produce a 384-dimensional embedding, then reduce to 10 dimensions using UMAP or PCA

Return code for each feature group as a modular function.
Note which features are suitable for tree models vs neural networks. Copy prompt Open prompt details Beginner Single prompt 03 
### Feature Ideas Generator 

This prompt helps brainstorm high-value engineered features before you start coding. It is especially useful when you have a decent understanding of the target but want structured, model-oriented ideas rather than random transformations. The goal is to surface features with a realistic chance of improving signal while keeping build effort visible. 
Prompt text Suggest 15 new features I could engineer from this dataset to improve predictive power for {{target_variable}}.

For each feature:
- Feature name
- How to compute it (formula or logic)
- Why it might help the model
- Estimated difficulty to build: Easy / Medium / Hard

Cover these types:
- Interaction features (multiplication or ratio of two existing columns)
- Aggregation features (rolling mean, cumulative sum, group-by statistics)
- Date/time decompositions if a date column exists
- Lag features if data is time-ordered
- Domain-specific features based on the apparent business context

Prioritize features that are likely to have the highest signal-to-noise ratio. Copy prompt Open prompt details Intermediate Single prompt 04 
### Feature Selection 

This prompt compares several feature selection philosophies to identify a smaller and more robust predictor set. It is useful when the raw feature space is large or when you need stability rather than one lucky importance ranking. The final recommendation rewards agreement across multiple methods. 
Prompt text Select the optimal feature subset for predicting {{target_variable}}.

Run four feature selection methods and compare their results:

1. Filter method: correlation with target (keep features with |r| > 0.05)
2. Wrapper method: Recursive Feature Elimination (RFE) with a Random Forest estimator, 5-fold CV
3. Embedded method: SHAP values from a LightGBM model — keep top features by mean |SHAP|
4. Stability method: run SHAP selection 5 times with different random seeds — keep only features that appear in all 5 runs (stable features)

Compare: how many features does each method select? How much do the selected sets overlap?

Final recommendation: the intersection of features selected by at least 3 of the 4 methods.

Return: selected feature list, overlap Venn diagram, and CV performance with all features vs selected features. Copy prompt Open prompt details Advanced Chain 05 
### Full Feature Pipeline Chain 

This prompt designs a full feature pipeline from profiling through selection. It is useful when you want a disciplined end-to-end approach instead of ad hoc transformations. The chain connects cleaning, encoding, feature creation, leakage checks, and importance-based pruning into one workflow. 
Prompt text Step 1: Profile the raw features — types, missing rates, cardinality, correlation with {{target_variable}}. Identify the weakest features (near-zero variance, low target correlation).
Step 2: Clean and encode — impute missing values, encode categoricals (ordinal for low-cardinality, target encoding for high-cardinality), scale numerics.
Step 3: Engineer new features — create interaction features, lag features if time-ordered, group aggregations, and domain-specific features based on the dataset context.
Step 4: Select features — use SHAP values from a quick LightGBM model to rank all features. Drop features with SHAP importance below a threshold.
Step 5: Check for leakage — verify no feature uses future information. Check correlation of each feature with the target is not suspiciously perfect (>0.95).
Step 6: Output a final feature list with: name, description, type, importance rank, and the code to reproduce it end-to-end. Copy prompt Open prompt details Intermediate Single prompt 06 
### Group Aggregation Features 

This prompt creates within-group statistical context so each row can be compared to its peers. It is useful when categories such as region, segment, product family, or store define meaningful local baselines. These features often help models understand relative position, not just absolute value. 
Prompt text Create group-level aggregation features by computing statistics at the level of each categorical group.

For each meaningful categorical column in the dataset:
1. Group by that column and compute these statistics for each numeric column:
 - mean, median, std, min, max
 - count of rows in the group
 - percentile rank of each row within its group
 - deviation of each row from its group mean (row_value - group_mean)
 - ratio of each row to its group mean (row_value / group_mean)

2. Name features systematically: [numeric_col]_[statistic]_by_[group_col]
 Example: revenue_mean_by_region, revenue_rank_by_region

3. Flag any group with fewer than 10 members — statistics on tiny groups are unreliable

Return code using pandas groupby + transform, and a list of all features created. Copy prompt Open prompt details Intermediate Single prompt 07 
### Interaction Features 

This prompt searches for pairwise feature interactions that add predictive value beyond the original variables. It is useful when the target may depend on combinations, contrasts, or ratios rather than single features alone. The output focuses on interactions that are both meaningful and not excessively redundant. 
Prompt text Generate and evaluate interaction features between the most important variables in this dataset.

1. Identify the top 6 numeric features by correlation with {{target_variable}}
2. Create all pairwise interactions between them:
 - Multiplication: feature_a × feature_b
 - Ratio: feature_a / (feature_b + epsilon)
 - Difference: feature_a - feature_b
3. For each interaction feature, compute its correlation with {{target_variable}}
4. Keep only interaction features with |r| > 0.05 with the target and that outperform their parent features
5. Check for multicollinearity between interaction features and parents

Return the top 10 interaction features ranked by correlation with the target, with code to create them. Copy prompt Open prompt details Intermediate Single prompt 08 
### Lag and Rolling Features 

This prompt builds historical lag and rolling statistics for panel or time series data without leaking future information. It is meant for forecasting, churn, risk, and behavioral models where recent history is often the strongest signal. The structure keeps everything grouped by entity and aligned to prediction time. 
Prompt text Create lag and rolling window features for this time-ordered dataset.

Assume the data is ordered by {{date_column}} with one row per {{entity_column}} per time period.

Create per entity:
- Lag features: value at t-1, t-2, t-3, t-7, t-14, t-28 periods back
- Rolling mean: 7-period, 14-period, 28-period window
- Rolling standard deviation: 7-period and 28-period window
- Rolling min and max: 7-period window
- Exponentially weighted moving average (alpha=0.3)
- Trend: slope of a linear regression fitted on the last 7 values

Critical: ensure no data leakage — all features must use only information available at prediction time (strictly historical).

Return the feature creation code and confirm the leakage-free construction. Copy prompt Open prompt details Beginner Single prompt 09 
### Missing Value Imputation for ML 

This prompt compares several imputation strategies specifically for machine learning use, not just data cleaning. It is helpful when missingness may itself be informative and the best imputation approach is not obvious. The masking evaluation adds evidence instead of relying on intuition alone. 
Prompt text Implement missing value imputation for machine learning on this dataset.

1. Profile missing values: count, percentage, and missingness pattern (MCAR, MAR, or MNAR) for each column
2. Implement and compare three imputation strategies:
 a. Simple imputation: median for numeric, mode for categorical
 b. KNN imputation: k=5 nearest neighbors based on complete features
 c. Iterative imputation (MICE): model each feature as a function of others, iterate until convergence
3. Evaluate each strategy by: artificially masking 10% of known values and measuring reconstruction error (RMSE)
4. Add missingness indicator columns (is_missing_[col]) for columns with more than 5% missing — these can be predictive features
5. Always fit imputation on training data only, then apply to validation and test sets

Return: comparison table of imputation strategies, code for the best strategy, and list of missingness indicator columns created. Copy prompt Open prompt details Advanced Single prompt 10 
### Polynomial and Spline Features 

This prompt adds polynomial and spline transformations to model non-linear feature effects explicitly. It is useful when simple linear representations miss curvature, thresholds, or diminishing returns in the relationship with the target. The workflow evaluates whether these richer forms actually improve cross-validated performance. 
Prompt text Create polynomial and spline features to capture non-linear relationships in this dataset.

1. Identify the top 5 numeric features by correlation with {{target_variable}}
2. For each, test whether the relationship is linear, quadratic, or higher-order:
 - Fit linear, quadratic, and cubic regression
 - Compare R² values and plot each fit
3. For features with non-linear relationships:
 a. Add polynomial features (degree 2 and 3)
 b. Add natural cubic spline features with 4 knots at the 25th, 50th, 75th, and 90th percentiles
4. Add the polynomial/spline features to the model and compare:
 - CV score before adding
 - CV score after adding
 - Risk of overfitting (train vs val gap)
5. Use SHAP to verify the model is using the polynomial features meaningfully

Return: relationship type table, feature code, and CV performance comparison. Copy prompt Open prompt details Intermediate Single prompt 11 
### Target Encoding 

This prompt applies target encoding to categorical variables with many levels while guarding against leakage. It is designed for cases where one-hot encoding would explode dimensionality or lose useful target signal. The emphasis is on out-of-fold encoding, smoothing, and safe inference-time handling. 
Prompt text Apply target encoding to the high-cardinality categorical columns in this dataset for predicting {{target_variable}}.

For each high-cardinality categorical column (more than 10 unique values):
1. Compute the mean of {{target_variable}} per category value
2. Apply smoothing to avoid overfitting on rare categories: smoothed_mean = (n × category_mean + m × global_mean) / (n + m) where m = smoothing_factor (default 10)
3. Handle unseen categories at inference time by defaulting to the global mean
4. Use 5-fold out-of-fold encoding to prevent target leakage on the training set

Return:
- The encoded features as new columns (keep originals)
- A table showing the top 10 and bottom 10 category values for each encoded column
- Code to apply the same encoding to a test set without leakage Copy prompt Open prompt details 
## Recommended Feature Engineering workflow 
1 
### Date Feature Extraction 

Start with a focused prompt in Feature Engineering so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Embedding Features from Text 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Feature Ideas Generator 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Feature Selection 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
