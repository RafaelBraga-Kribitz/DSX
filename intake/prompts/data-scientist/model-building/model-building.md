# Model Building *AI Prompts *

12 Data Scientist prompts in Model Building. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 11 single prompts · 1 chain. 

## AI prompts in Model Building 
12 prompts Intermediate Single prompt 01 
### AutoML Benchmark 

This prompt benchmarks AutoML against manual baselines to see whether automated search is adding real value. It is especially useful when you want a quick but serious search over model families and hyperparameters without abandoning interpretability. The output also helps decide whether to continue manual optimization. 
Prompt text Run an AutoML benchmark on this dataset to find the best model for predicting {{target_variable}}.

1. Run MLJAR AutoML with mode='Compete' for 60 minutes on the training set
2. Evaluate using 5-fold cross-validation with {{primary_metric}} as the optimization target
3. Report the top 5 models found by AutoML: algorithm, hyperparameters, CV score, training time
4. Compare AutoML's best model against manually built baselines (Logistic Regression, Random Forest with defaults)
5. Extract the best model's feature importances and compare to manual feature selection
6. Report: what type of model won? What hyperparameter ranges worked best? What did AutoML find that manual search missed?

Return the leaderboard table, best model details, and a recommendation on whether to use the AutoML model or continue manual optimization. Copy prompt Open prompt details Beginner Single prompt 02 
### Baseline Model 

This prompt establishes honest baseline performance before more complex modeling begins. It is useful because many projects jump straight to sophisticated algorithms without proving that they beat trivial or simple alternatives. The prompt helps define the minimum bar a useful model must clear. 
Prompt text Build baseline models for predicting {{target_variable}} in this dataset.

1. Determine the problem type: binary classification, multiclass classification, or regression
2. Choose the correct evaluation metric: AUC-ROC for binary, accuracy/F1 for multiclass, RMSE/MAE for regression
3. Build a naive baseline first:
 - Regression: predict the training set mean for all observations
 - Classification: predict the majority class for all observations
4. Build two simple baselines: Logistic Regression (or Linear Regression) and a Decision Tree with max_depth=3
5. Evaluate all three on a held-out validation set (20% split, stratified for classification)

Return a comparison table: model | train score | validation score | fit time
Identify which baseline to beat before calling any model 'useful'. Copy prompt Open prompt details Intermediate Single prompt 03 
### Class Imbalance Handling 

This prompt tackles classification problems where the minority class matters more than raw accuracy. It compares common resampling and weighting approaches under a consistent evaluation setup. The goal is to choose the strategy that aligns best with both data imbalance and business costs. 
Prompt text Handle class imbalance in this classification dataset where {{minority_class}} is the minority class.

1. First, quantify the imbalance: ratio of majority to minority class
2. Explain why accuracy is a misleading metric for this problem
3. Implement and compare four strategies:
 a. Class weight adjustment (class_weight='balanced' in sklearn)
 b. Random oversampling of the minority class (RandomOverSampler)
 c. SMOTE — Synthetic Minority Oversampling Technique
 d. Undersampling the majority class (RandomUnderSampler)
4. For each strategy, train a LightGBM model and evaluate using: AUC-ROC, Precision, Recall, F1, and the confusion matrix
5. Recommend the best strategy for this specific imbalance ratio and business context

Note: apply all resampling only to the training set, never to validation or test sets. Copy prompt Open prompt details Advanced Single prompt 04 
### Custom Loss Function 

This prompt builds a model objective around business cost instead of default statistical loss. It is useful when false positives and false negatives have very different consequences, such as fraud, medical screening, or retention interventions. The output translates model quality into financial terms. 
Prompt text Implement a custom loss function for this problem that better reflects the business cost of different types of errors.

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

Return the custom loss code and the business cost comparison table. Copy prompt Open prompt details Advanced Chain 05 
### End-to-End ML Experiment 

This prompt runs a complete supervised learning experiment from definition to model card. It is useful when you want one rigorous workflow that covers preparation, selection, tuning, test evaluation, and error analysis. It supports reproducible experimentation rather than isolated notebook steps. 
Prompt text Step 1: Define the problem — target variable, problem type, evaluation metric, and business success threshold (e.g. AUC > 0.85).
Step 2: Prepare data — clean, encode, engineer features, split into train/val/test with no leakage.
Step 3: Run a model comparison with 5 algorithms, default hyperparameters, 5-fold cross-validation. Select top 2.
Step 4: Tune the top 2 models using Optuna (50 trials each). Select the winner.
Step 5: Evaluate the winning model on the held-out test set — report all metrics, confusion matrix, and calibration curve.
Step 6: Analyze errors — inspect the 20 worst-predicted examples. What do they have in common? What does this suggest about the model or data?
Step 7: Write a 1-page model card: problem, approach, final metrics, known limitations, and deployment recommendations. Copy prompt Open prompt details Advanced Single prompt 06 
### Ensemble and Stacking 

This prompt explores whether combining diverse models can outperform the best single learner. It is useful when individual models are competitive but capture different patterns or error modes. The workflow moves from simple averaging to optimized weights and full stacking. 
Prompt text Build an ensemble model to improve performance beyond any single model.

1. Train 4 diverse base models: LightGBM, XGBoost, Random Forest, and Logistic Regression
2. Evaluate each independently with 5-fold cross-validation
3. Build a simple average ensemble — average the predicted probabilities from all 4 models
4. Build a weighted average ensemble — optimize weights using scipy minimize on the validation set
5. Build a stacking ensemble:
 - Level 0: generate out-of-fold predictions from all base models
 - Level 1 meta-learner: train a Logistic Regression on the Level 0 predictions
6. Compare: individual models vs simple average vs weighted average vs stacking

Return: performance comparison table, optimal weights for the weighted ensemble, and inference code for the final stacked model. Copy prompt Open prompt details Intermediate Single prompt 07 
### Hyperparameter Tuning 

This prompt runs systematic hyperparameter optimization instead of manual guesswork. It is most useful after a promising model family has been identified and you want measurable gains from tuning. The workflow emphasizes Bayesian search, reproducibility, and comparison to defaults. 
Prompt text Tune the hyperparameters of this model to maximize performance on {{target_variable}}.

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

Return: best params dict, improvement table, and training code using the best params. Copy prompt Open prompt details Intermediate Single prompt 08 
### Model Comparison 

This prompt compares several common algorithm families on equal footing. It is useful when you want to identify strong candidates before investing in tuning or ensembling. It also adds operational context through training time, inference speed, and memory usage. 
Prompt text Train and compare multiple candidate models for predicting {{target_variable}}.

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
Flag any model that is significantly overfitting (train score >> validation score). Copy prompt Open prompt details Advanced Single prompt 09 
### Model Deployment Readiness 

This prompt evaluates whether a trained model is operationally ready, not just statistically strong. It is useful right before deployment when latency, memory, robustness, reproducibility, and monitoring all matter. The result should support a go/no-go launch decision. 
Prompt text Assess whether this model is ready for production deployment.

Run the following checks and report pass / fail / needs review for each:

1. Performance: does the model meet the minimum performance threshold of {{performance_threshold}} on the test set?
2. Latency: can the model produce a single prediction in under {{latency_ms}}ms? Test with 1000 sequential predictions.
3. Memory: what is the model's memory footprint in MB? Is it within the deployment limit of {{memory_limit_mb}}MB?
4. Robustness: does performance degrade by more than 5% when tested on data from the last month vs the training period?
5. Edge cases: test with 10 adversarial inputs (nulls, extreme values, empty strings). Does the model throw errors or return sensible predictions?
6. Reproducibility: given the same inputs, does the model return identical outputs on repeated calls?
7. Monitoring plan: are feature drift and prediction drift monitors in place? Is there an alert for performance degradation?

Return: deployment readiness checklist and a go/no-go recommendation. Copy prompt Open prompt details Beginner Single prompt 10 
### Overfitting Diagnosis 

This prompt diagnoses whether a model is memorizing training data more than it generalizes. It is useful when train metrics look strong but validation performance disappoints. The output compares regularization and simplification strategies in a structured way rather than relying on one fix. 
Prompt text Diagnose and fix overfitting in this machine learning model.

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

Return: overfitting diagnosis, regularization comparison table, and final recommended configuration. Copy prompt Open prompt details Intermediate Single prompt 11 
### Time Series Cross-Validation 

This prompt applies proper walk-forward evaluation to forecasting problems where ordinary cross-validation would leak future data. It is useful for getting realistic estimates of how the model behaves in production-like temporal settings. It also checks whether performance worsens over time. 
Prompt text Implement correct cross-validation for this time series forecasting problem.

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

Return: fold performance table, actual vs predicted plot, and degradation analysis. Copy prompt Open prompt details Beginner Single prompt 12 
### Train Test Split Strategy 

This prompt chooses the right data splitting strategy based on the actual structure of the problem. It prevents common leakage mistakes caused by random splits on temporal, grouped, or imbalanced datasets. The result is a defensible train/validation/test design and matching code. 
Prompt text Design the correct train/validation/test split strategy for this dataset and problem.

1. Examine the data: is it time-ordered? Does it have multiple entities (users, stores)? Is the target class imbalanced?
2. Recommend the split strategy:
 - Random split if i.i.d. data with balanced classes
 - Stratified split if class imbalance > 3:1
 - Time-based split if data is time-ordered (never use future data to predict the past)
 - Group-based split if the same entity appears multiple times (prevent entity leakage)
3. Recommend the split ratio and justify it given the dataset size
4. Implement the split in code with a fixed random_state for reproducibility
5. Verify the split: check that target distribution is similar across all splits

Return the split code and a distribution comparison table for train/val/test. Copy prompt Open prompt details 
## Recommended Model Building workflow 
1 
### AutoML Benchmark 

Start with a focused prompt in Model Building so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Baseline Model 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Class Imbalance Handling 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Custom Loss Function 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
