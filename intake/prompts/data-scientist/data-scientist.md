# Data Scientist *AI Prompts *

Data Scientist AI prompt library with 50 prompts in 5 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 5 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Data Scientist prompt categories 
5 categories 
### Model Building 

AI prompts for model building, algorithm selection, baseline creation, training strategies, and machine learning development. 
12 prompts AutoML Benchmark Baseline Model → 
### Feature Engineering 

AI prompts for feature engineering, data transformations, feature selection, and creating predictive representations for models. 
11 prompts Date Feature Extraction Embedding Features from Text → 
### Model Evaluation 

AI prompts for model evaluation, performance metrics, validation strategies, error analysis, and fair model comparison. 
10 prompts Calibration Analysis Classification Report → 
### Experimentation 

AI prompts for experimentation workflows in machine learning, iterative testing, hypothesis validation, and model improvement cycles. 
9 prompts A/B Test Analysis Bayesian A/B Analysis → 
### Explainability 

AI prompts for model explainability, feature importance, interpretable machine learning, and communicating predictions clearly. 
8 prompts Counterfactual Explanations Decision Tree Proxy → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 50 Model Building 12 Feature Engineering 11 Model Evaluation 10 Experimentation 9 Explainability 8 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **50 **of 50 prompts 
## Model Building 
12 prompt s Model Building Intermediate Prompt 01 
### AutoML Benchmark 
Run an AutoML benchmark on this dataset to find the best model for predicting {{target_variable}}.

1. Run MLJAR AutoML with mode='Compete' for 60 minutes on the training set
2. Evaluate using 5-fold cross-validation with {{primary_metric}} as the optimization target
3. Report the top 5 models found by AutoML: algorithm, hyperparameters, CV score, training time
4. Compare AutoML's best model against manually built baselines (Logistic Regression, Random Forest with defaults)
5. Extract the best model's feature importances and compare to manual feature selection
6. Report: what type of model won? What hyperparameter ranges worked best? What did AutoML find that manual search missed?

Return the leaderboard table, best model details, and a recommendation on whether to use the AutoML model or continue manual optimization. Copy prompt View page Show more ↓ Model Building Beginner Prompt 02 
### Baseline Model 
Build baseline models for predicting {{target_variable}} in this dataset.

1. Determine the problem type: binary classification, multiclass classification, or regression
2. Choose the correct evaluation metric: AUC-ROC for binary, accuracy/F1 for multiclass, RMSE/MAE for regression
3. Build a naive baseline first:
 - Regression: predict the training set mean for all observations
 - Classification: predict the majority class for all observations
4. Build two simple baselines: Logistic Regression (or Linear Regression) and a Decision Tree with max_depth=3
5. Evaluate all three on a held-out validation set (20% split, stratified for classification)

Return a comparison table: model | train score | validation score | fit time
Identify which baseline to beat before calling any model 'useful'. Copy prompt View page Show more ↓ Model Building Intermediate Prompt 03 
### Class Imbalance Handling 
Handle class imbalance in this classification dataset where {{minority_class}} is the minority class.

1. First, quantify the imbalance: ratio of majority to minority class
2. Explain why accuracy is a misleading metric for this problem
3. Implement and compare four strategies:
 a. Class weight adjustment (class_weight='balanced' in sklearn)
 b. Random oversampling of the minority class (RandomOverSampler)
 c. SMOTE — Synthetic Minority Oversampling Technique
 d. Undersampling the majority class (RandomUnderSampler)
4. For each strategy, train a LightGBM model and evaluate using: AUC-ROC, Precision, Recall, F1, and the confusion matrix
5. Recommend the best strategy for this specific imbalance ratio and business context

Note: apply all resampling only to the training set, never to validation or test sets. Copy prompt View page Show more ↓ Model Building Advanced Prompt 04 
### Custom Loss Function 
Implement a custom loss function for this problem that better reflects the business cost of different types of errors.

Business context: {{business_context}}
Cost structure:
- False positive cost: {{fp_cost}} (e.g. unnecessary intervention costs $10)
- False negative cost: {{fn_cost}} (e.g. missed fraud costs $500)

1. Define the asymmetric cost matrix
2. Implement a custom objective function for LightGBM/XGBoost that minimizes expected business cost
3. Implement a custom evaluation metric that reports cost in business units
4. Train the model with the custom loss and compare to cross-entropy loss:
 - Standard accuracy / AUC / F1
 - Business cost per 1000 predictions
 - Optimal decision threshold under the cost structure
5. Show the threshold vs business cost curve — at what threshold is business cost minimized?

Return the custom loss code and the business cost comparison table. Copy prompt View page Show more ↓ Model Building Advanced Chain 05 
### End-to-End ML Experiment 
Step 1: Define the problem — target variable, problem type, evaluation metric, and business success threshold (e.g. AUC > 0.85).
Step 2: Prepare data — clean, encode, engineer features, split into train/val/test with no leakage.
Step 3: Run a model comparison with 5 algorithms, default hyperparameters, 5-fold cross-validation. Select top 2.
Step 4: Tune the top 2 models using Optuna (50 trials each). Select the winner.
Step 5: Evaluate the winning model on the held-out test set — report all metrics, confusion matrix, and calibration curve.
Step 6: Analyze errors — inspect the 20 worst-predicted examples. What do they have in common? What does this suggest about the model or data?
Step 7: Write a 1-page model card: problem, approach, final metrics, known limitations, and deployment recommendations. Copy prompt View page Show more ↓ Model Building Advanced Prompt 06 
### Ensemble and Stacking 
Build an ensemble model to improve performance beyond any single model.

1. Train 4 diverse base models: LightGBM, XGBoost, Random Forest, and Logistic Regression
2. Evaluate each independently with 5-fold cross-validation
3. Build a simple average ensemble — average the predicted probabilities from all 4 models
4. Build a weighted average ensemble — optimize weights using scipy minimize on the validation set
5. Build a stacking ensemble:
 - Level 0: generate out-of-fold predictions from all base models
 - Level 1 meta-learner: train a Logistic Regression on the Level 0 predictions
6. Compare: individual models vs simple average vs weighted average vs stacking

Return: performance comparison table, optimal weights for the weighted ensemble, and inference code for the final stacked model. Copy prompt View page Show more ↓ Model Building Intermediate Prompt 07 
### Hyperparameter Tuning 
Tune the hyperparameters of this model to maximize performance on {{target_variable}}.

Model to tune: {{model_type}} (e.g. LightGBM, XGBoost, Random Forest)

Approach:
1. Define the hyperparameter search space:
 - For tree models: n_estimators, max_depth, learning_rate, min_child_samples, subsample, colsample_bytree, reg_alpha, reg_lambda
 - For linear models: C, penalty, solver
2. Use Optuna (Bayesian optimization) with 100 trials
3. Evaluate each trial with 5-fold cross-validation
4. Plot the optimization history: score vs trial number
5. Report the best hyperparameters and best cross-validated score
6. Compare: default params vs tuned params — how much did tuning improve performance?

Return: best params dict, improvement table, and training code using the best params. Copy prompt View page Show more ↓ Model Building Intermediate Prompt 08 
### Model Comparison 
Train and compare multiple candidate models for predicting {{target_variable}}.

Train these models with default hyperparameters:
1. Logistic Regression / Linear Regression
2. Random Forest (n_estimators=200)
3. Gradient Boosting — XGBoost or LightGBM
4. Support Vector Machine (RBF kernel, scaled features)
5. k-Nearest Neighbors (k=10)

For each model:
- 5-fold cross-validated score (mean ± std)
- Training time
- Inference time per 1000 rows
- Memory usage

Return a ranked comparison table.
Recommend the top 2 models to take forward for hyperparameter tuning, with justification.
Flag any model that is significantly overfitting (train score >> validation score). Copy prompt View page Show more ↓ Model Building Advanced Prompt 09 
### Model Deployment Readiness 
Assess whether this model is ready for production deployment.

Run the following checks and report pass / fail / needs review for each:

1. Performance: does the model meet the minimum performance threshold of {{performance_threshold}} on the test set?
2. Latency: can the model produce a single prediction in under {{latency_ms}}ms? Test with 1000 sequential predictions.
3. Memory: what is the model's memory footprint in MB? Is it within the deployment limit of {{memory_limit_mb}}MB?
4. Robustness: does performance degrade by more than 5% when tested on data from the last month vs the training period?
5. Edge cases: test with 10 adversarial inputs (nulls, extreme values, empty strings). Does the model throw errors or return sensible predictions?
6. Reproducibility: given the same inputs, does the model return identical outputs on repeated calls?
7. Monitoring plan: are feature drift and prediction drift monitors in place? Is there an alert for performance degradation?

Return: deployment readiness checklist and a go/no-go recommendation. Copy prompt View page Show more ↓ Model Building Beginner Prompt 10 
### Overfitting Diagnosis 
Diagnose and fix overfitting in this machine learning model.

1. Measure the overfitting gap: training score vs validation score. A gap > 5% is a concern.
2. Plot learning curves to confirm overfitting (training score high, validation score lower and not converging)
3. Test regularization techniques in order of invasiveness:
 a. Increase regularization parameters (L1, L2 penalty, or min_child_samples for trees)
 b. Reduce model complexity (max_depth, n_estimators, hidden layer size)
 c. Add dropout (neural networks) or feature subsampling (trees)
 d. Reduce the feature set — remove low-importance features that may add noise
 e. Get more training data if available
4. For each technique, report: training score, validation score, and overfitting gap
5. Select the technique that minimizes the overfitting gap with the smallest validation score sacrifice

Return: overfitting diagnosis, regularization comparison table, and final recommended configuration. Copy prompt View page Show more ↓ Model Building Intermediate Prompt 11 
### Time Series Cross-Validation 
Implement correct cross-validation for this time series forecasting problem.

Standard k-fold cross-validation is not appropriate for time series because it causes data leakage (future data used to predict the past).

1. Implement expanding window cross-validation (walk-forward validation):
 - Start with the first 60% of data as training
 - Predict the next 10% (first validation fold)
 - Expand training to 70%, predict the next 10% (second fold)
 - Continue until all data is used
2. Report performance metrics (MAPE, RMSE) for each fold and the overall mean ± std
3. Plot: actual vs predicted values across all folds in a single chart, with fold boundaries marked
4. Compare expanding window vs sliding window cross-validation — which gives more stable estimates for this dataset?
5. Check for temporal degradation: does model performance worsen for more recent folds? This indicates distribution shift.

Return: fold performance table, actual vs predicted plot, and degradation analysis. Copy prompt View page Show more ↓ Model Building Beginner Prompt 12 
### Train Test Split Strategy 
Design the correct train/validation/test split strategy for this dataset and problem.

1. Examine the data: is it time-ordered? Does it have multiple entities (users, stores)? Is the target class imbalanced?
2. Recommend the split strategy:
 - Random split if i.i.d. data with balanced classes
 - Stratified split if class imbalance > 3:1
 - Time-based split if data is time-ordered (never use future data to predict the past)
 - Group-based split if the same entity appears multiple times (prevent entity leakage)
3. Recommend the split ratio and justify it given the dataset size
4. Implement the split in code with a fixed random_state for reproducibility
5. Verify the split: check that target distribution is similar across all splits

Return the split code and a distribution comparison table for train/val/test. Copy prompt View page Show more ↓ 
## Feature Engineering 
11 prompt s Feature Engineering Beginner Prompt 01 
### Date Feature Extraction 
Extract all useful features from the date and datetime columns in this dataset.

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

Return the feature creation code in pandas and a list of all new column names created. Copy prompt View page Show more ↓ Feature Engineering Advanced Prompt 02 
### Embedding Features from Text 
Generate numeric features from the text columns in this dataset for use in a machine learning model.

For each text column:
1. Basic statistical features: character count, word count, sentence count, average word length, punctuation count
2. Lexical features: unique word ratio (vocabulary richness), stopword ratio, uppercase ratio
3. Sentiment features: positive score, negative score, neutral score, compound score using VADER
4. TF-IDF features: top 50 unigrams and top 20 bigrams (sparse matrix)
5. Dense embedding: use sentence-transformers (all-MiniLM-L6-v2) to produce a 384-dimensional embedding, then reduce to 10 dimensions using UMAP or PCA

Return code for each feature group as a modular function.
Note which features are suitable for tree models vs neural networks. Copy prompt View page Show more ↓ Feature Engineering Beginner Prompt 03 
### Feature Ideas Generator 
Suggest 15 new features I could engineer from this dataset to improve predictive power for {{target_variable}}.

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

Prioritize features that are likely to have the highest signal-to-noise ratio. Copy prompt View page Show more ↓ Feature Engineering Intermediate Prompt 04 
### Feature Selection 
Select the optimal feature subset for predicting {{target_variable}}.

Run four feature selection methods and compare their results:

1. Filter method: correlation with target (keep features with |r| > 0.05)
2. Wrapper method: Recursive Feature Elimination (RFE) with a Random Forest estimator, 5-fold CV
3. Embedded method: SHAP values from a LightGBM model — keep top features by mean |SHAP|
4. Stability method: run SHAP selection 5 times with different random seeds — keep only features that appear in all 5 runs (stable features)

Compare: how many features does each method select? How much do the selected sets overlap?

Final recommendation: the intersection of features selected by at least 3 of the 4 methods.

Return: selected feature list, overlap Venn diagram, and CV performance with all features vs selected features. Copy prompt View page Show more ↓ Feature Engineering Advanced Chain 05 
### Full Feature Pipeline Chain 
Step 1: Profile the raw features — types, missing rates, cardinality, correlation with {{target_variable}}. Identify the weakest features (near-zero variance, low target correlation).
Step 2: Clean and encode — impute missing values, encode categoricals (ordinal for low-cardinality, target encoding for high-cardinality), scale numerics.
Step 3: Engineer new features — create interaction features, lag features if time-ordered, group aggregations, and domain-specific features based on the dataset context.
Step 4: Select features — use SHAP values from a quick LightGBM model to rank all features. Drop features with SHAP importance below a threshold.
Step 5: Check for leakage — verify no feature uses future information. Check correlation of each feature with the target is not suspiciously perfect (>0.95).
Step 6: Output a final feature list with: name, description, type, importance rank, and the code to reproduce it end-to-end. Copy prompt View page Show more ↓ Feature Engineering Intermediate Prompt 06 
### Group Aggregation Features 
Create group-level aggregation features by computing statistics at the level of each categorical group.

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

Return code using pandas groupby + transform, and a list of all features created. Copy prompt View page Show more ↓ Feature Engineering Intermediate Prompt 07 
### Interaction Features 
Generate and evaluate interaction features between the most important variables in this dataset.

1. Identify the top 6 numeric features by correlation with {{target_variable}}
2. Create all pairwise interactions between them:
 - Multiplication: feature_a × feature_b
 - Ratio: feature_a / (feature_b + epsilon)
 - Difference: feature_a - feature_b
3. For each interaction feature, compute its correlation with {{target_variable}}
4. Keep only interaction features with |r| > 0.05 with the target and that outperform their parent features
5. Check for multicollinearity between interaction features and parents

Return the top 10 interaction features ranked by correlation with the target, with code to create them. Copy prompt View page Show more ↓ Feature Engineering Intermediate Prompt 08 
### Lag and Rolling Features 
Create lag and rolling window features for this time-ordered dataset.

Assume the data is ordered by {{date_column}} with one row per {{entity_column}} per time period.

Create per entity:
- Lag features: value at t-1, t-2, t-3, t-7, t-14, t-28 periods back
- Rolling mean: 7-period, 14-period, 28-period window
- Rolling standard deviation: 7-period and 28-period window
- Rolling min and max: 7-period window
- Exponentially weighted moving average (alpha=0.3)
- Trend: slope of a linear regression fitted on the last 7 values

Critical: ensure no data leakage — all features must use only information available at prediction time (strictly historical).

Return the feature creation code and confirm the leakage-free construction. Copy prompt View page Show more ↓ Feature Engineering Beginner Prompt 09 
### Missing Value Imputation for ML 
Implement missing value imputation for machine learning on this dataset.

1. Profile missing values: count, percentage, and missingness pattern (MCAR, MAR, or MNAR) for each column
2. Implement and compare three imputation strategies:
 a. Simple imputation: median for numeric, mode for categorical
 b. KNN imputation: k=5 nearest neighbors based on complete features
 c. Iterative imputation (MICE): model each feature as a function of others, iterate until convergence
3. Evaluate each strategy by: artificially masking 10% of known values and measuring reconstruction error (RMSE)
4. Add missingness indicator columns (is_missing_[col]) for columns with more than 5% missing — these can be predictive features
5. Always fit imputation on training data only, then apply to validation and test sets

Return: comparison table of imputation strategies, code for the best strategy, and list of missingness indicator columns created. Copy prompt View page Show more ↓ Feature Engineering Advanced Prompt 10 
### Polynomial and Spline Features 
Create polynomial and spline features to capture non-linear relationships in this dataset.

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

Return: relationship type table, feature code, and CV performance comparison. Copy prompt View page Show more ↓ Feature Engineering Intermediate Prompt 11 
### Target Encoding 
Apply target encoding to the high-cardinality categorical columns in this dataset for predicting {{target_variable}}.

For each high-cardinality categorical column (more than 10 unique values):
1. Compute the mean of {{target_variable}} per category value
2. Apply smoothing to avoid overfitting on rare categories: smoothed_mean = (n × category_mean + m × global_mean) / (n + m) where m = smoothing_factor (default 10)
3. Handle unseen categories at inference time by defaulting to the global mean
4. Use 5-fold out-of-fold encoding to prevent target leakage on the training set

Return:
- The encoded features as new columns (keep originals)
- A table showing the top 10 and bottom 10 category values for each encoded column
- Code to apply the same encoding to a test set without leakage Copy prompt View page Show more ↓ 
## Model Evaluation 
10 prompt s Model Evaluation Intermediate Prompt 01 
### Calibration Analysis 
Assess and improve the probability calibration of this classification model.

1. Plot a reliability diagram (calibration curve): predicted probability vs actual fraction of positives, using 10 bins
2. Compute the Expected Calibration Error (ECE) and Maximum Calibration Error (MCE)
3. Determine if the model is overconfident (predictions too extreme) or underconfident (predictions too moderate)
4. Apply two calibration methods and compare:
 a. Platt Scaling (logistic regression on model outputs)
 b. Isotonic Regression
5. Plot calibration curves before and after each method
6. Report ECE before and after calibration

Note: calibration must be fitted on a held-out calibration set (not the training set) to avoid overfitting. Copy prompt View page Show more ↓ Model Evaluation Beginner Prompt 02 
### Classification Report 
Produce a comprehensive evaluation report for this classification model.

1. Compute and display the full classification report: precision, recall, F1-score, and support for each class
2. Plot the confusion matrix as a heatmap — show both counts and percentages
3. Plot the ROC curve with AUC value (for binary classification)
4. Plot the Precision-Recall curve with Average Precision score
5. Find the optimal classification threshold using:
 - F1 maximization
 - Youden's J statistic (max sensitivity + specificity - 1)
6. Show how precision, recall, and F1 change across threshold values (threshold plot)

Interpret: which class is hardest to predict? What type of error is more costly in this business context? Copy prompt View page Show more ↓ Model Evaluation Intermediate Prompt 03 
### Cross-Validation Deep Dive 
Run a rigorous cross-validation analysis for this model.

1. Evaluate using 5-fold, 10-fold, and stratified 5-fold cross-validation
2. For each fold strategy, report: mean score, std, min, max across folds
3. Plot fold scores as a box plot to visualize variance across folds
4. Run repeated k-fold (5-fold × 3 repeats) to get a more stable estimate
5. Check for fold-to-fold variance — high variance suggests the model is sensitive to the training data composition
6. Compare cross-validated score vs test set score — are they consistent?

If the cross-validated score and test score diverge by more than 5%, investigate potential causes: data leakage, distribution shift, or overfitting. Copy prompt View page Show more ↓ Model Evaluation Advanced Prompt 04 
### Drift Detection 
Detect whether this model's input data or predictions have drifted from the training distribution.

1. Feature drift (data drift): for each feature, compare the training distribution to the current serving distribution using:
 - Kolmogorov-Smirnov test for continuous features
 - Chi-squared test for categorical features
 - Population Stability Index (PSI) for all features
2. Flag features with PSI > 0.2 (significant drift) or PSI 0.1–0.2 (moderate drift)
3. Prediction drift: compare the distribution of model outputs in training vs serving. Has the prediction distribution shifted?
4. Concept drift (if labels are available): compare model performance in recent data vs training data. Has accuracy degraded?
5. Prioritize: which drifting features are most important to the model (high SHAP importance)? These pose the greatest risk.

Return: drift report table per feature, PSI heatmap, and a retraining recommendation: retrain now / monitor / no action needed. Copy prompt View page Show more ↓ Model Evaluation Advanced Prompt 05 
### Error Analysis 
Conduct a deep error analysis on this model's worst predictions.

1. Identify the 50 most confidently wrong predictions (highest predicted probability for the wrong class, or largest absolute residual for regression)
2. Profile these error cases:
 - What is the distribution of their feature values compared to correctly predicted cases?
 - Are they concentrated in a specific subgroup, time period, or region?
 - Do they share a common pattern in the raw data?
3. Cluster the error cases using k-means (k=3–5) — describe what characterizes each error cluster
4. For each cluster, propose a specific model improvement: more training data of that type, a new feature, a separate model for that segment, or a data quality fix
5. Estimate: if the top error cluster were fixed, how much would overall model performance improve?

Return the error profile table, cluster descriptions, and prioritized improvement recommendations. Copy prompt View page Show more ↓ Model Evaluation Intermediate Prompt 06 
### Learning Curve Analysis 
Generate and interpret learning curves for this model.

1. Train the model on increasing fractions of the training data: 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%
2. For each fraction, record: training score and cross-validated validation score
3. Plot both curves on the same chart with the x-axis as training set size
4. Interpret the curves:
 - If training score >> validation score: overfitting → more data or regularization needed
 - If both scores are low and converged: underfitting → more complex model or better features needed
 - If validation score is still increasing at 100% data: adding more training data would help
5. Estimate: how much more data would be needed to close the train/val gap?

Return the learning curve plot and a 3-sentence diagnosis of the model's current state. Copy prompt View page Show more ↓ Model Evaluation Advanced Chain 07 
### Model Audit Chain 
Step 1: Performance audit — evaluate on test set using all relevant metrics. Compare to baseline. Does the model meet the business performance threshold?
Step 2: Robustness audit — test performance on subgroups (by region, time period, user segment, etc.). Does performance degrade significantly for any group?
Step 3: Fairness audit — if sensitive attributes exist (age, gender, geography), check for disparate impact: does the false positive rate or false negative rate differ significantly across groups?
Step 4: Stability audit — add small amounts of Gaussian noise to input features and measure performance degradation. Is the model brittle to small input changes?
Step 5: Leakage audit — inspect the top 10 most important features. Do any of them look like they might encode the target or use future information?
Step 6: Write a model audit report: pass/fail for each audit, severity of any failures, and recommended mitigations. Copy prompt View page Show more ↓ Model Evaluation Beginner Prompt 08 
### Model Card 
Write a model card for this machine learning model following the standard format.

The model card should include:

1. Model details — name, type, version, training date, author
2. Intended use — what task does this model solve? Who should use it? What are the out-of-scope uses?
3. Training data — what dataset was used, date range, size, and any known limitations or biases
4. Evaluation results — primary metric on test set, broken down by key subgroups if available
5. Ethical considerations — what sensitive attributes are present? Is there potential for disparate impact?
6. Caveats and limitations — what situations might cause the model to fail? What assumptions does it make?
7. How to use — code snippet showing how to load and run inference

Write in clear, non-technical language suitable for both engineers and business stakeholders. Copy prompt View page Show more ↓ Model Evaluation Beginner Prompt 09 
### Regression Evaluation 
Evaluate this regression model comprehensively.

1. Compute: MAE, RMSE, MAPE, R², and Adjusted R²
2. Plot predicted vs actual values — how close are points to the diagonal?
3. Plot residuals vs predicted values — check for patterns (heteroscedasticity, non-linearity)
4. Plot residual distribution — should be approximately normal with mean near zero
5. Identify the top 10 largest errors (by absolute residual) — do they share any characteristics?
6. Check for systematic bias: does the model over-predict or under-predict for certain segments?

Return: metric table, 4 diagnostic plots, a table of worst predictions with row details, and a one-paragraph model assessment. Copy prompt View page Show more ↓ Model Evaluation Intermediate Prompt 10 
### Threshold Optimization 
Find the optimal classification threshold for this model given the business context.

1. Generate predicted probabilities for the validation set
2. Evaluate performance across all thresholds from 0.01 to 0.99 (step 0.01):
 - Precision, Recall, F1, FPR, TPR at each threshold
3. Plot the threshold vs each metric curve
4. Identify the optimal threshold for three different objectives:
 a. Maximize F1-score
 b. Maximize precision while keeping recall ≥ {{min_recall}}
 c. Minimize total cost given: FP cost = {{fp_cost}}, FN cost = {{fn_cost}}
5. Show the confusion matrix at each of the three optimal thresholds
6. Recommend the final threshold with a business justification

Return: threshold analysis table, metric curves plot, 3 confusion matrices, and final recommendation. Copy prompt View page Show more ↓ 
## Experimentation 
9 prompt s Experimentation Beginner Prompt 01 
### A/B Test Analysis 
Analyze the results of this A/B test.

1. Describe the experiment: what was tested, what is the primary metric, how many users in each group?
2. Check for sample ratio mismatch (SRM): is the split between control and treatment what was intended? Use a chi-squared test.
3. Run the primary hypothesis test:
 - For conversion rates: two-proportion z-test or chi-squared test
 - For continuous metrics: two-sample t-test or Mann-Whitney U test
4. Report: p-value, observed difference, 95% confidence interval for the difference, and statistical power
5. Calculate practical significance: is the observed effect large enough to matter for the business? Compare to the minimum detectable effect.
6. State the recommendation clearly: ship, do not ship, or run a follow-up experiment — and why. Copy prompt View page Show more ↓ Experimentation Advanced Prompt 02 
### Bayesian A/B Analysis 
Analyze this A/B test using a Bayesian framework instead of frequentist hypothesis testing.

1. Model the conversion rate for control and treatment as Beta distributions:
 - Prior: Beta(1, 1) — uninformative
 - Posterior: Beta(1 + conversions, 1 + non-conversions) for each variant
2. Plot the posterior distributions for control and treatment on the same chart
3. Compute:
 - Probability that treatment beats control: P(θ_treatment > θ_control) using Monte Carlo sampling (100k samples)
 - Expected lift: mean of (θ_treatment - θ_control) / θ_control
 - 95% credible interval for the lift
 - Expected loss from choosing the wrong variant
4. Apply a decision rule: ship treatment if P(treatment > control) > 0.95 AND expected lift > MDE of {{mde}}
5. Compare the Bayesian conclusion to a frequentist t-test conclusion — do they agree?

Return: posterior plots, probability table, decision recommendation, and a plain-English interpretation. Copy prompt View page Show more ↓ Experimentation Advanced Prompt 03 
### Causal Inference Analysis 
Estimate the causal effect of {{treatment_variable}} on {{outcome_variable}} from this observational dataset (no random assignment).

1. Describe the confounding problem: which variables are likely confounders that affect both treatment assignment and the outcome?
2. Apply Propensity Score Matching (PSM):
 - Estimate propensity scores using logistic regression
 - Match treated to control units on propensity score (1:1, nearest neighbor)
 - Check covariate balance before and after matching (standardized mean differences)
3. Estimate the Average Treatment Effect on the Treated (ATT) using matched pairs
4. Apply Inverse Probability of Treatment Weighting (IPTW) as a cross-check
5. Apply a Doubly Robust estimator combining propensity score and outcome model
6. Compare ATT estimates from all three methods — are they consistent?

Return: balance table, ATT estimates with 95% CIs, and a plain-English interpretation of the causal effect. Copy prompt View page Show more ↓ Experimentation Intermediate Prompt 04 
### Experiment Guardrail Check 
Check the guardrail metrics for this experiment to ensure no unintended harm was caused.

Guardrail metrics are metrics that must not be significantly degraded even if the primary metric improves.

1. List all guardrail metrics provided in the dataset (e.g. page load time, error rate, support tickets, refund rate)
2. For each guardrail metric, test whether treatment significantly degraded it vs control (one-sided test, α=0.05)
3. Report: guardrail metric | control mean | treatment mean | % change | p-value | status (✅ Safe / 🔴 Degraded)
4. Flag any guardrail metric that is significantly degraded — this may block shipping even if the primary metric improved
5. Compute the trade-off: if a guardrail is degraded, what is the net business impact of the primary metric gain minus the guardrail loss?

Return the guardrail report and a final ship/no-ship recommendation considering both primary and guardrail results. Copy prompt View page Show more ↓ Experimentation Advanced Chain 05 
### Full Experiment Design Chain 
Step 1: Define the experiment — what hypothesis are we testing, what is the primary metric, what is the minimum detectable effect, and what is the business rationale?
Step 2: Calculate sample size — given baseline metric, MDE, α=0.05, power=0.80. Calculate required experiment duration based on available traffic.
Step 3: Design the assignment — define unit of randomization (user, session, device). Check for network effects or contamination risks. Define the holdout strategy.
Step 4: Define guardrail metrics — list 3–5 metrics that must not degrade. Define the threshold for each guardrail.
Step 5: Design the analysis plan — specify the primary statistical test, multiple testing correction method, and pre-registration of hypotheses.
Step 6: Write the experiment brief: hypothesis, primary metric, guardrail metrics, sample size, duration, assignment method, analysis plan, decision criteria for ship/no-ship. Copy prompt View page Show more ↓ Experimentation Intermediate Prompt 06 
### Multivariate Test Analysis 
Analyze the results of this multivariate (A/B/n) test with {{num_variants}} variants.

1. Check for sample ratio mismatch across all variants
2. Run omnibus test first: is there any significant difference across all variants? (chi-squared or ANOVA)
3. If significant, run pairwise comparisons between all variant pairs using:
 - Bonferroni correction for multiple comparisons
 - Report adjusted p-values and whether each pair is significant at α=0.05 after correction
4. Compute the effect size for each variant vs control: Cohen's d (continuous) or relative lift (proportions)
5. Plot: mean metric value per variant with 95% confidence intervals
6. Identify the winning variant — highest metric value with statistical significance vs control
7. Flag any variants that are significantly worse than control (degradation alert) Copy prompt View page Show more ↓ Experimentation Beginner Prompt 07 
### Pre-Experiment Sanity Check 
Run a pre-experiment sanity check before launching this A/B test.

1. AA test simulation: randomly split the existing data into two equal groups and test for significant differences on the primary metric — there should be none (p > 0.05). If there is a significant difference, the randomization is broken.
2. Check metric variance: compute the standard deviation of the primary metric per user over the past 4 weeks. High variance increases required sample size.
3. Check for seasonality: does the primary metric vary significantly by day of week or time of year? Adjust experiment timing accordingly.
4. Check for novelty effects: does the user base regularly respond to any UI changes with a short-term spike that fades? How long should the experiment run to see past this?
5. Verify logging: confirm the event tracking is firing correctly for both the primary metric and guardrail metrics by spot-checking recent data.

Return: AA test result, variance estimate, seasonality assessment, and recommended experiment start date and duration. Copy prompt View page Show more ↓ Experimentation Beginner Prompt 08 
### Sample Size Calculator 
Calculate the required sample size for this experiment.

Inputs:
- Baseline conversion rate or metric value: {{baseline_value}}
- Minimum detectable effect (MDE): {{mde}} — the smallest change worth detecting
- Significance level (α): 0.05 (two-tailed)
- Statistical power (1 - β): 0.80
- Number of variants: {{num_variants}} (control + treatment)

Calculate:
1. Required sample size per variant
2. Total sample size across all variants
3. Required experiment duration given the current daily traffic of {{daily_traffic}} users
4. Show how the required sample size changes if MDE is varied: ±50%, ±25%, ±10% from the specified MDE
5. Plot a power curve: sample size vs statistical power for the specified MDE

Return: sample size, experiment duration, and the power curve plot. Copy prompt View page Show more ↓ Experimentation Intermediate Prompt 09 
### Segment Lift Analysis 
Analyze treatment lift across different user segments in this experiment.

1. Compute the overall lift: (treatment metric - control metric) / control metric
2. Compute lift separately for each segment defined by the available dimension columns (age group, region, device, acquisition channel, etc.)
3. Plot lift per segment as a forest plot (point estimate ± 95% CI for each segment)
4. Test for heterogeneous treatment effects: is the lift significantly different across segments? (interaction test)
5. Identify the segments with the highest and lowest lift
6. Flag any segment where the treatment caused a statistically significant negative effect
7. Recommend: should the feature be shipped to all users, or only to the highest-lift segments?

Return: segment lift table, forest plot, and a targeting recommendation. Copy prompt View page Show more ↓ 
## Explainability 
8 prompt s Explainability Intermediate Prompt 01 
### Counterfactual Explanations 
Generate counterfactual explanations for rejected or unfavorable predictions from this model.

A counterfactual answers the question: 'What is the minimal change to the input that would flip the prediction?'

For the top 10 most impactful negative predictions (e.g. loan rejected, churn predicted, fraud flagged):
1. Find the nearest counterfactual: the smallest change to input features that would result in a positive prediction
2. Constraints: only change features that are actionable (not age, not historical data — only things the person can change)
3. For each counterfactual show: original values | counterfactual values | what changed | magnitude of change
4. Rank the required changes from easiest to hardest to achieve
5. Generate a plain-English 'what you could do differently' explanation for each case

Return: counterfactual table for each case and template text suitable for a customer-facing explanation. Copy prompt View page Show more ↓ Explainability Beginner Prompt 02 
### Decision Tree Proxy 
Build a simple decision tree that approximates the behavior of this complex model.

1. Generate predictions from the complex model on the full training set
2. Train a decision tree on those predictions (use model outputs as the new target)
3. Limit the tree depth to 4 levels maximum for interpretability
4. Tune: find the depth (1–6) that maximizes fidelity (agreement with the complex model) while staying interpretable
5. Visualize the decision tree using graphviz or a text representation
6. Extract the top 5 decision rules as plain-English if-then statements
7. Report fidelity: what percentage of predictions does the proxy tree agree with the complex model?

Note: this is a surrogate model, not the real model. Flag where the proxy disagrees most with the original. Copy prompt View page Show more ↓ Explainability Beginner Prompt 03 
### Feature Importance 
Explain which features matter most to this model.

1. Extract built-in feature importances from the model (gain, split count, or permutation importance)
2. Plot a horizontal bar chart of the top 20 features, ranked by importance
3. Compute permutation importance on the validation set as a cross-check — compare to built-in importances
4. Flag any features where built-in and permutation importances disagree significantly
5. Identify features with near-zero importance in both methods — candidates for removal
6. Group features by type (original vs engineered) and show which group contributes more total importance

Return: importance table, bar chart, and a one-paragraph plain-English explanation of what the model is learning. Copy prompt View page Show more ↓ Explainability Advanced Chain 04 
### Full XAI Chain 
Step 1: Global importance — compute and plot SHAP feature importances (beeswarm). Identify the top 5 features driving predictions.
Step 2: Effect direction — create SHAP dependence plots for the top 5 features. Describe the relationship between each feature and the prediction (linear, threshold, non-linear).
Step 3: Interaction analysis — compute SHAP interaction values. Identify the strongest pairwise interaction and plot it as a 2D PDP.
Step 4: Local explanation — generate waterfall plots for 3 representative predictions: high, low, and borderline.
Step 5: Business translation — write a 1-page non-technical explanation of how the model makes decisions, using analogies and avoiding all technical terms.
Step 6: Risk flagging — identify any feature effects that seem counterintuitive or potentially problematic from a fairness or business logic perspective. Copy prompt View page Show more ↓ Explainability Intermediate Prompt 05 
### LIME Explanation 
Use LIME to explain individual predictions from this model in plain English.

Generate LIME explanations for 5 specific predictions:
1. One very high prediction (top 5% of predicted values)
2. One very low prediction (bottom 5% of predicted values)
3. One borderline prediction (near the decision threshold)
4. The single prediction the model got most wrong
5. A randomly selected typical prediction

For each explanation:
- Show the top 10 features that pushed the prediction up or down
- Display as a horizontal bar chart with green bars (positive contribution) and red bars (negative contribution)
- Write a 2-sentence plain-English explanation: 'The model predicted [value] primarily because [top driver]. This was offset by [top negative driver].'

Return all 5 explanations with plots and text summaries. Copy prompt View page Show more ↓ Explainability Advanced Prompt 06 
### Model Behavior Report 
Write a complete model behavior report suitable for a technical stakeholder review.

The report should cover:

1. What the model learned — top 10 features and their direction of effect, in plain English
2. Decision rules — extract the top 5 decision paths from the model using SHAP or tree rules
3. Edge cases — what input combinations lead to extreme predictions (very high and very low)?
4. Monotonicity check — for features where a directional relationship is expected (e.g. more experience → higher salary), does the model respect that direction?
5. Interaction effects — which two features interact the most strongly? How does their interaction affect predictions?
6. Sensitivity analysis — which single feature, if changed by 10%, has the largest average impact on predictions?

Format as a structured report with section headings, plots, and a non-technical executive summary at the top. Copy prompt View page Show more ↓ Explainability Intermediate Prompt 07 
### Partial Dependence Plots 
Generate partial dependence plots (PDPs) and individual conditional expectation (ICE) plots for the top features in this model.

For each of the top 5 most important features:
1. Plot the PDP: how does the average model prediction change as this feature varies across its range?
2. Overlay 50 randomly sampled ICE curves to show individual variation around the average
3. Highlight the average ICE curve in bold
4. Mark the actual data distribution (rug plot) on the x-axis to show where data is sparse
5. Describe the relationship: monotonic increasing, monotonic decreasing, non-linear, threshold effect?

Also create one 2D PDP for the top pair of interacting features (identified from SHAP interaction values).

Return all plots and a table summarizing the relationship type for each feature. Copy prompt View page Show more ↓ Explainability Intermediate Prompt 08 
### SHAP Analysis 
Generate a complete SHAP-based model explanation.

1. Compute SHAP values for all predictions in the validation set
2. Global explanations:
 - Beeswarm plot: feature importance + direction of effect
 - Bar plot: mean absolute SHAP value per feature (top 20)
3. Dependence plots for the top 3 most important features:
 - SHAP value on y-axis, feature value on x-axis
 - Color by the most important interaction feature
4. Local explanations — waterfall plots for:
 - The most confidently correct prediction
 - The most confidently wrong prediction
 - One typical prediction near the decision boundary
5. Plain-English summary: what are the top 3 drivers of high predictions vs low predictions?

Return all plots and the plain-English summary. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
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
