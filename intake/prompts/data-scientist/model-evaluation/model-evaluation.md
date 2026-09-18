# Model Evaluation *AI Prompts *

10 Data Scientist prompts in Model Evaluation. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 9 single prompts · 1 chain. 

## AI prompts in Model Evaluation 
10 prompts Intermediate Single prompt 01 
### Calibration Analysis 

This prompt checks whether predicted probabilities can be trusted as probabilities, not just rankings. It is useful for decision systems that depend on calibrated risk estimates, thresholds, or expected value calculations. The workflow compares raw and calibrated models with proper holdout discipline. 
Prompt text Assess and improve the probability calibration of this classification model.

1. Plot a reliability diagram (calibration curve): predicted probability vs actual fraction of positives, using 10 bins
2. Compute the Expected Calibration Error (ECE) and Maximum Calibration Error (MCE)
3. Determine if the model is overconfident (predictions too extreme) or underconfident (predictions too moderate)
4. Apply two calibration methods and compare:
 a. Platt Scaling (logistic regression on model outputs)
 b. Isotonic Regression
5. Plot calibration curves before and after each method
6. Report ECE before and after calibration

Note: calibration must be fitted on a held-out calibration set (not the training set) to avoid overfitting. Copy prompt Open prompt details Beginner Single prompt 02 
### Classification Report 

This prompt produces a full evaluation package for a classification model, not just one headline metric. It is useful when threshold choice, trade-offs between precision and recall, and class-specific behavior matter. The output is meant to support model review and decision-making. 
Prompt text Produce a comprehensive evaluation report for this classification model.

1. Compute and display the full classification report: precision, recall, F1-score, and support for each class
2. Plot the confusion matrix as a heatmap — show both counts and percentages
3. Plot the ROC curve with AUC value (for binary classification)
4. Plot the Precision-Recall curve with Average Precision score
5. Find the optimal classification threshold using:
 - F1 maximization
 - Youden's J statistic (max sensitivity + specificity - 1)
6. Show how precision, recall, and F1 change across threshold values (threshold plot)

Interpret: which class is hardest to predict? What type of error is more costly in this business context? Copy prompt Open prompt details Intermediate Single prompt 03 
### Cross-Validation Deep Dive 

This prompt stress-tests performance estimates across multiple cross-validation schemes. It is useful when you want to understand score stability and whether a single CV result is overly optimistic or noisy. It also helps explain discrepancies between CV and test performance. 
Prompt text Run a rigorous cross-validation analysis for this model.

1. Evaluate using 5-fold, 10-fold, and stratified 5-fold cross-validation
2. For each fold strategy, report: mean score, std, min, max across folds
3. Plot fold scores as a box plot to visualize variance across folds
4. Run repeated k-fold (5-fold × 3 repeats) to get a more stable estimate
5. Check for fold-to-fold variance — high variance suggests the model is sensitive to the training data composition
6. Compare cross-validated score vs test set score — are they consistent?

If the cross-validated score and test score diverge by more than 5%, investigate potential causes: data leakage, distribution shift, or overfitting. Copy prompt Open prompt details Advanced Single prompt 04 
### Drift Detection 

This prompt detects whether the data or predictions seen in production have drifted away from the training environment. It is useful for model monitoring and retraining decisions after deployment. The analysis prioritizes drift in features that the model actually depends on most. 
Prompt text Detect whether this model's input data or predictions have drifted from the training distribution.

1. Feature drift (data drift): for each feature, compare the training distribution to the current serving distribution using:
 - Kolmogorov-Smirnov test for continuous features
 - Chi-squared test for categorical features
 - Population Stability Index (PSI) for all features
2. Flag features with PSI > 0.2 (significant drift) or PSI 0.1–0.2 (moderate drift)
3. Prediction drift: compare the distribution of model outputs in training vs serving. Has the prediction distribution shifted?
4. Concept drift (if labels are available): compare model performance in recent data vs training data. Has accuracy degraded?
5. Prioritize: which drifting features are most important to the model (high SHAP importance)? These pose the greatest risk.

Return: drift report table per feature, PSI heatmap, and a retraining recommendation: retrain now / monitor / no action needed. Copy prompt Open prompt details Advanced Single prompt 05 
### Error Analysis 

This prompt dives into the model's most damaging mistakes to uncover systematic failure modes. It is useful when overall metrics look acceptable but users still complain or critical edge cases remain unresolved. Clustering the worst errors can reveal missing features, bad data, or segment-specific model gaps. 
Prompt text Conduct a deep error analysis on this model's worst predictions.

1. Identify the 50 most confidently wrong predictions (highest predicted probability for the wrong class, or largest absolute residual for regression)
2. Profile these error cases:
 - What is the distribution of their feature values compared to correctly predicted cases?
 - Are they concentrated in a specific subgroup, time period, or region?
 - Do they share a common pattern in the raw data?
3. Cluster the error cases using k-means (k=3–5) — describe what characterizes each error cluster
4. For each cluster, propose a specific model improvement: more training data of that type, a new feature, a separate model for that segment, or a data quality fix
5. Estimate: if the top error cluster were fixed, how much would overall model performance improve?

Return the error profile table, cluster descriptions, and prioritized improvement recommendations. Copy prompt Open prompt details Intermediate Single prompt 06 
### Learning Curve Analysis 

This prompt shows whether the model is limited by data, model complexity, or both. It is valuable when you need to decide whether to collect more data, regularize, or redesign features. Learning curves provide a practical diagnosis of overfitting versus underfitting. 
Prompt text Generate and interpret learning curves for this model.

1. Train the model on increasing fractions of the training data: 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%
2. For each fraction, record: training score and cross-validated validation score
3. Plot both curves on the same chart with the x-axis as training set size
4. Interpret the curves:
 - If training score >> validation score: overfitting → more data or regularization needed
 - If both scores are low and converged: underfitting → more complex model or better features needed
 - If validation score is still increasing at 100% data: adding more training data would help
5. Estimate: how much more data would be needed to close the train/val gap?

Return the learning curve plot and a 3-sentence diagnosis of the model's current state. Copy prompt Open prompt details Advanced Chain 07 
### Model Audit Chain 

This prompt audits a model across multiple trust dimensions instead of reporting only aggregate accuracy. It is designed for higher-stakes reviews where robustness, subgroup behavior, fairness, and leakage all matter. The result should function as a structured technical risk assessment. 
Prompt text Step 1: Performance audit — evaluate on test set using all relevant metrics. Compare to baseline. Does the model meet the business performance threshold?
Step 2: Robustness audit — test performance on subgroups (by region, time period, user segment, etc.). Does performance degrade significantly for any group?
Step 3: Fairness audit — if sensitive attributes exist (age, gender, geography), check for disparate impact: does the false positive rate or false negative rate differ significantly across groups?
Step 4: Stability audit — add small amounts of Gaussian noise to input features and measure performance degradation. Is the model brittle to small input changes?
Step 5: Leakage audit — inspect the top 10 most important features. Do any of them look like they might encode the target or use future information?
Step 6: Write a model audit report: pass/fail for each audit, severity of any failures, and recommended mitigations. Copy prompt Open prompt details Beginner Single prompt 08 
### Model Card 

This prompt writes a model card that documents what the model is for, how it was trained, how well it performs, and where it should not be used. It is useful for handoff, governance, stakeholder communication, and production readiness. The language is designed to work for both technical and business readers. 
Prompt text Write a model card for this machine learning model following the standard format.

The model card should include:

1. Model details — name, type, version, training date, author
2. Intended use — what task does this model solve? Who should use it? What are the out-of-scope uses?
3. Training data — what dataset was used, date range, size, and any known limitations or biases
4. Evaluation results — primary metric on test set, broken down by key subgroups if available
5. Ethical considerations — what sensitive attributes are present? Is there potential for disparate impact?
6. Caveats and limitations — what situations might cause the model to fail? What assumptions does it make?
7. How to use — code snippet showing how to load and run inference

Write in clear, non-technical language suitable for both engineers and business stakeholders. Copy prompt Open prompt details Beginner Single prompt 09 
### Regression Evaluation 

This prompt evaluates regression models from several complementary angles. It is useful for checking raw accuracy, residual structure, bias patterns, and specific failure cases. The aim is to understand not only how wrong the model is, but where and why. 
Prompt text Evaluate this regression model comprehensively.

1. Compute: MAE, RMSE, MAPE, R², and Adjusted R²
2. Plot predicted vs actual values — how close are points to the diagonal?
3. Plot residuals vs predicted values — check for patterns (heteroscedasticity, non-linearity)
4. Plot residual distribution — should be approximately normal with mean near zero
5. Identify the top 10 largest errors (by absolute residual) — do they share any characteristics?
6. Check for systematic bias: does the model over-predict or under-predict for certain segments?

Return: metric table, 4 diagnostic plots, a table of worst predictions with row details, and a one-paragraph model assessment. Copy prompt Open prompt details Intermediate Single prompt 10 
### Threshold Optimization 

This prompt chooses a classification threshold based on explicit business objectives rather than the default 0.5 cutoff. It is useful when recall floors, precision targets, or asymmetric costs drive operational decisions. The result makes threshold choice transparent and defensible. 
Prompt text Find the optimal classification threshold for this model given the business context.

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

Return: threshold analysis table, metric curves plot, 3 confusion matrices, and final recommendation. Copy prompt Open prompt details 
## Recommended Model Evaluation workflow 
1 
### Calibration Analysis 

Start with a focused prompt in Model Evaluation so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Classification Report 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Cross-Validation Deep Dive 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Drift Detection 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
