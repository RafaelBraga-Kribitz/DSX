# Drift Detection *AI Prompts *

9 MLOps prompts in Drift Detection. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 8 single prompts · 1 chain. 

## AI prompts in Drift Detection 
9 prompts Intermediate Single prompt 01 
### Concept Drift Localization 

This prompt localizes concept drift by estimating when it started, which features changed, and which user segments are most affected. It is designed for post-detection investigation and root cause analysis rather than first-pass monitoring. 
Prompt text When concept drift is detected, implement methods to localize where and when the drift occurred.

Concept drift has been confirmed (performance degradation with available labels). Now identify the specifics.

1. Temporal localization — when did the drift start?:
 - Use CUSUM (Cumulative Sum) change point detection on the rolling performance metric
 - Alternatively: Page-Hinkley test for online change point detection
 - Binary search approach: is performance worse in the last week vs the week before? If yes, recurse into the worse half.
 - Report the estimated change point date with a confidence interval

2. Feature-space localization — what changed?:
 - If labels are available: train a model to predict where errors occur
 - Features that predict model errors are candidates for concept drift
 - Compare SHAP values from the original model on recent data vs reference data
 - Features with the largest SHAP distribution shift are likely driving the concept drift

3. Segment localization — which user segments are most affected?:
 - Compute performance metrics separately for each dimension (region, device, user_type, price_tier)
 - Rank segments by performance degradation: which segment shows the largest drop?
 - Check if the worst-performing segment has grown in volume (could amplify overall degradation)

4. Root cause hypothesis:
 Based on localization results, form hypotheses:
 - Temporal drift on specific date → check for: product change, external event, data pipeline issue
 - Feature-driven drift → check for: upstream data source change, feature engineering bug, new user behavior
 - Segment-driven drift → check for: new customer segment entered the product, regional regulation change

5. Remediation options:
 - Retrain on recent data (weights recent data more heavily)
 - Targeted retraining: only retrain on the drifted segment
 - Feature replacement: if a feature is no longer predictive, replace it
 - Model architecture change: if the relationship structure has fundamentally changed

Return: CUSUM change point detection, feature importance drift analysis, segment performance comparison, and root cause hypothesis framework. Copy prompt Open prompt details Beginner Single prompt 02 
### Data Drift vs Concept Drift 

This prompt explains the major kinds of drift and connects each one to detection and response strategies. It is useful when a team needs both conceptual clarity and implementation guidance for diagnosing why model quality is changing. 
Prompt text Explain and implement detection methods for the different types of drift this model may experience.

1. Definitions with examples:

 Data drift (covariate shift): P(X) changes, P(Y|X) stays the same
 - Input feature distributions change, but the relationship between features and target is unchanged
 - Example: your fraud model was trained on 2023 data. In 2024, transaction amounts increased due to inflation. The fraud patterns are the same, but the feature distributions shifted.
 - Detection: monitor feature distributions (PSI, KS test)
 - Impact: model may make more errors on out-of-distribution inputs

 Concept drift: P(Y|X) changes, P(X) may stay the same
 - The underlying relationship between features and target changes
 - Example: consumer behavior changed post-COVID. Features that predicted churn in 2019 no longer predict churn in 2023.
 - Detection: requires ground truth labels — monitor model performance over time
 - Impact: model becomes fundamentally wrong, not just uncertain

 Label drift: P(Y) changes
 - The prevalence of the target class changes
 - Example: fraud rate drops from 2% to 0.5% due to a new prevention system
 - Detection: monitor positive prediction rate and, when available, actual label rate
 - Impact: model calibration becomes off, decision threshold may need adjustment

 Prior probability shift: combination of covariate and label drift

2. Detection implementation for each type:
 - Data drift: daily PSI on all features
 - Concept drift: rolling model performance on labeled data (AUC, precision, recall)
 - Label drift: daily positive rate monitoring with statistical significance test

3. Diagnosis flowchart:
 - Performance degrading + feature drift detected → likely data drift
 - Performance degrading + no feature drift → likely concept drift
 - Calibration off + positive rate changed → likely label drift
 - All metrics stable + business impact → investigate downstream factors

4. Response strategy per drift type:
 - Data drift: retrain on recent data, update preprocessing normalization parameters
 - Concept drift: retrain with new data, potentially redesign features
 - Label drift: recalibrate the model, adjust decision threshold

Return: drift type detection implementation, diagnosis flowchart, and response playbook per type. Copy prompt Open prompt details Advanced Chain 03 
### Drift Detection Setup Chain 

This chain prompt lays out a full drift detection program, from feature ranking and baselines to univariate and multivariate monitors, concept drift tracking, alert routing, and runbooks. It is useful when building a comprehensive drift detection stack from scratch. 
Prompt text Step 1: Feature importance ranking — use SHAP values from the production model to rank all features by their average impact on predictions. These are the features where drift matters most.
Step 2: Reference distribution computation — compute reference statistics (mean, std, histogram, PSI bins) for the top 20 features and the prediction output on the training validation set. Store in a metadata table.
Step 3: Univariate drift monitors — implement daily PSI checks for all top-20 features and the prediction distribution. Set alert thresholds: PSI > 0.1 warning, PSI > 0.2 alert. Test with synthetic drift to validate sensitivity.
Step 4: Multivariate drift monitor — implement classifier-based multivariate drift detection running weekly. Validate that it detects joint distribution shifts that the univariate monitors miss.
Step 5: Concept drift monitor — implement rolling performance tracking using the ground truth feedback loop. Set retraining trigger: performance drops below {{threshold}} for {{n}} consecutive days.
Step 6: Alerting and routing — configure alert routing: feature drift → Slack to ML team, prediction drift → Slack + email, performance drift → PagerDuty. Test all alert paths end-to-end.
Step 7: Runbook — document for each alert: what it means, first 3 investigation steps, escalation path, and how to silence a false alarm. Conduct a fire drill with the on-call team. Copy prompt Open prompt details Advanced Single prompt 04 
### Drift Root Cause Report 

This prompt produces a structured report after drift has been detected, combining severity, scope, onset, likely causes, business impact, and recommended actions. It is useful for communicating drift investigations to technical and non-technical stakeholders. 
Prompt text Generate a structured drift root cause report when drift has been detected in this model.

Drift detected: {{drift_description}}
Model: {{model_name}}
Detection date: {{detection_date}}

The report should contain:

1. Executive summary (3 sentences):
 - What was detected, when, and how severe?
 - What is the estimated business impact if unaddressed?
 - What is the recommended immediate action?

2. Drift characterization:
 - Type: data drift / concept drift / label drift / combined
 - Severity: PSI scores, AUC degradation, or performance metric change
 - Onset: estimated date when drift began (from change point detection)
 - Scope: which features are most affected? Which user segments?
 - Trajectory: is the drift stable, accelerating, or decelerating?

3. Root cause investigation:
 - Timeline of events: deployments, data pipeline changes, external events near the drift onset date
 - Feature analysis: top 5 drifting features with their PSI scores and distribution visualizations
 - Upstream data quality: any anomalies in the data pipeline feeding this model?
 - External context: market events, seasonality, product changes that could explain the drift?

4. Impact assessment:
 - Estimated accuracy degradation: current performance vs baseline
 - Affected prediction volume: how many predictions per day are impacted?
 - Downstream business impact: estimated revenue, risk, or operational impact

5. Recommended actions (prioritized):
 - Immediate (< 24 hours): quick mitigations to limit damage
 - Short-term (< 1 week): retraining, threshold adjustment, feature fixes
 - Long-term (< 1 month): systematic fixes to prevent recurrence

6. Monitoring update:
 - What new tests or tighter thresholds should be added to catch this pattern earlier next time?

Return: complete drift root cause report template with all sections filled based on available data. Copy prompt Open prompt details Beginner Single prompt 05 
### Feature Drift Detection 

This prompt implements feature drift monitoring with reference statistics, daily statistical tests, prioritized alerts, and visualizations. It is a practical choice when an ML team wants interpretable drift checks on the most important input features. 
Prompt text Implement feature drift detection to identify when the distribution of input features shifts from the training distribution.

Model: {{model_name}}
Top features to monitor: {{top_features}} (recommend top 10–20 by model importance)

1. Reference distribution (computed once from training or first 2 weeks of production):
 - Numeric features: mean, std, min, max, and histogram with 20 fixed bins
 - Categorical features: value frequency distribution
 - Store reference statistics in a metadata table

2. Statistical tests for drift detection (run daily on last 24h of production data):

 For numeric features:
 - Kolmogorov-Smirnov (KS) test: sensitive to distribution shape changes
 - Population Stability Index (PSI): standard industry metric, interpretable thresholds
 - Wasserstein distance (Earth Mover's Distance): good for detecting small but systematic shifts

 For categorical features:
 - Chi-squared test: tests if observed frequencies match expected frequencies
 - PSI on each category's frequency
 - Jensen-Shannon divergence: symmetric, bounded [0,1], good for comparing distributions

3. PSI interpretation and thresholds:
 - PSI < 0.1: no significant drift → continue
 - PSI 0.1–0.2: moderate drift → log warning, increase monitoring frequency
 - PSI > 0.2: significant drift → alert ML team, evaluate for retraining
 - PSI > 0.5: severe drift → escalate, consider emergency rollback investigation

4. Prioritized alerting:
 - Weight drift severity by feature importance: drift in a top-5 feature is more critical than drift in a low-importance feature
 - Composite drift score: weighted average of PSI scores across all monitored features

5. Visualization:
 - Side-by-side histogram: reference vs current distribution for each drifting feature
 - Drift heatmap: features × time with PSI color coding (green/yellow/red)

Return: reference statistics computation, daily drift detection script, PSI calculation, composite score, and visualization code. Copy prompt Open prompt details Intermediate Single prompt 06 
### Multivariate Drift Detection 

This prompt detects multivariate drift using classifier-based methods, MMD, and PCA-based monitoring so that joint-distribution changes are not missed. It is especially useful when univariate checks show stability but production behavior still looks suspicious. 
Prompt text Implement multivariate drift detection to catch drift patterns that are invisible in individual feature monitors.

Limitation of univariate drift detection: features A and B may individually look stable, but their joint distribution has shifted — a pattern that only multivariate detection catches.

1. Classifier-based drift detection (the most powerful general method):
 - Train a binary classifier to distinguish between reference data (label=0) and current data (label=1)
 - If the classifier achieves AUC significantly above 0.5, the distributions are distinguishable → drift detected
 - Use a lightweight classifier: LightGBM or Logistic Regression for speed
 - AUC interpretation:
 - AUC ≈ 0.5: no detectable drift
 - AUC 0.5–0.6: slight drift — monitor
 - AUC 0.6–0.7: moderate drift — investigate
 - AUC > 0.7: significant drift — alert
 - Bonus: the classifier's feature importances tell you WHICH features drive the drift

2. MMD (Maximum Mean Discrepancy):
 - Non-parametric test based on kernel embeddings
 - Works well for high-dimensional data
 - Use a Gaussian RBF kernel: MMD² = E[k(X,X')] - 2E[k(X,Y)] + E[k(Y,Y')]
 - Significance test: permutation test (shuffle reference/current labels and recompute MMD 1000 times)

3. PCA-based drift:
 - Fit PCA on the reference data (retain components explaining 95% of variance)
 - Project current data onto the reference PCA space
 - Monitor drift in the top 3–5 principal components using KS test
 - Advantage: reduces dimensionality, makes drift easier to visualize

4. When to use each method:
 - < 50 features: classifier-based (best explanability)
 - 50–500 features: PCA → KS test (scalable)
 - > 500 features or embeddings: MMD (handles high-dimensional spaces)

Return: classifier-based drift detector, MMD implementation, PCA-based drift, and a comparison of the three methods on synthetic drift scenarios. Copy prompt Open prompt details Advanced Single prompt 07 
### Online Drift Detection 

This prompt implements online drift detection for high-throughput systems using stream-based algorithms such as ADWIN, DDM, and KSWIN. It is useful when waiting for daily batch jobs is too slow and drift must be detected within minutes. 
Prompt text Implement online (stream-based) drift detection that detects drift in real time as predictions arrive, rather than in daily batch jobs.

Use case: model serving at > {{throughput}} RPS where drift needs to be detected within {{detection_window}} minutes.

1. ADWIN (Adaptive Windowing) for concept drift:
 - ADWIN maintains a sliding window of recent accuracy values
 - Automatically adjusts window size based on detected distribution changes
 - When the mean of the window changes significantly (using Hoeffding bound), drift is flagged
 - Suitable for: streaming accuracy monitoring when labels are near-real-time
 - Implementation: use the River library (formerly scikit-multiflow)

2. DDM (Drift Detection Method):
 - Tracks error rate mean and standard deviation over a stream of binary correct/incorrect outcomes
 - WARNING level: error_rate + std > baseline + 2×std_baseline
 - DRIFT level: error_rate + std > baseline + 3×std_baseline
 - Reset warning level statistics when drift is detected
 - Lightweight: O(1) memory, suitable for very high throughput

3. KSWIN (Kolmogorov-Smirnov Windowing):
 - Sliding window KS test on a chosen feature or prediction score
 - Compare the oldest {{reference_window}} samples vs newest {{detection_window}} samples
 - Drift flagged when KS p-value < {{alpha}} (e.g. 0.001)
 - Suitable for: feature drift detection in streaming pipelines

4. Integration with serving pipeline:
 - Run drift detectors as a side-car process alongside the serving container
 - Consume from the prediction log stream
 - Emit drift events to an alert topic when drift is detected
 - Circuit breaker: if drift exceeds a critical threshold, automatically route traffic to a fallback model

5. False positive management:
 - Online detectors are sensitive — apply a minimum detection window (don't alert on single anomalous batch)
 - Require drift to be sustained for {{min_sustained_window}} consecutive windows before alerting

Return: ADWIN, DDM, and KSWIN implementations, serving integration design, and false positive management. Copy prompt Open prompt details Intermediate Single prompt 08 
### PSI Implementation 

This prompt implements Population Stability Index for numeric and categorical features in a production-ready way, including edge cases, vectorization, and tests. It is best when PSI needs to be a reusable library component rather than a one-off notebook calculation. 
Prompt text Implement a production-grade Population Stability Index (PSI) calculation for both numeric and categorical features.

1. PSI formula:
 PSI = Σ (Actual% - Expected%) × ln(Actual% / Expected%)
 Where bins are defined on the reference (expected) distribution

2. Numeric feature PSI:
 - Define bins on the reference distribution (use quantile-based bins for robustness to outliers)
 - Number of bins: 10 for PSI (more bins = more sensitive but noisier)
 - Bin definition: [min, q10, q20, ..., q90, max] from the reference distribution
 - For the current distribution: count observations falling into each reference bin
 - Edge cases:
 - Empty bin in reference: replace with a small value (0.001) to avoid division by zero
 - Empty bin in current: replace with a small value (0.001) to avoid log(0)
 - Values outside reference range: assign to the first or last bin

3. Categorical feature PSI:
 - Each category is a bin
 - Reference frequencies: category counts / total reference rows
 - Current frequencies: category counts / total current rows
 - New categories (in current but not in reference): assign to an 'OTHER' bin
 - Missing categories (in reference but not in current): use 0.001 floor

4. Batch PSI computation (for multiple features at once):
 - Vectorized implementation using pandas or NumPy
 - Return a DataFrame: feature_name | psi_score | num_bins | reference_date | current_date | status

5. Validation:
 - Unit test: PSI of identical distributions should be ≈ 0
 - Unit test: PSI of completely different distributions should be > 0.5
 - Smoke test: PSI is always ≥ 0

6. Performance:
 - For large datasets (>10M rows): compute PSI on a random 10% sample — PSI is stable with sampling
 - Benchmark: should compute PSI for 100 features in < 30 seconds

Return: PSI implementation for numeric and categorical features, unit tests, batch computation function, and performance benchmark. Copy prompt Open prompt details Intermediate Single prompt 09 
### Training-Serving Skew Detection 

This prompt detects training-serving skew, which is a deployment bug caused by inconsistent preprocessing or feature logic rather than natural distribution drift. It is valuable for launch validation and for diagnosing surprising production failures after deployment. 
Prompt text Detect and diagnose training-serving skew — when the feature distributions at serving time differ from those at training time due to preprocessing inconsistencies.

Training-serving skew is distinct from drift. It is a bug, not a statistical phenomenon. It means the model is receiving different data at serving time than it was trained on, even when the underlying reality has not changed.

1. Common causes:
 - Different preprocessing code paths for training and serving
 - Feature computation at different points in time (training uses future data, serving uses only past)
 - Different handling of nulls (training fills with 0, serving fills with mean)
 - Different categorical encoding mappings stored in different places
 - Unit differences (training in km, serving in miles)
 - Different normalization parameters (training uses training set stats, serving uses different stats)

2. Detection method:
 - Log the exact feature vector received by the model at serving time
 - At regular intervals: take a sample of serving feature vectors and compare their distribution to the corresponding training feature vectors
 - Compare: mean, std, min, max, and null rate for every feature
 - Flag any feature where the serving distribution differs from training distribution AND this difference appeared at launch (not gradually — that would be drift, not skew)

3. Automated skew scan (run at every new model deployment):
 - Deploy model in shadow mode for 24 hours
 - Compare shadow period feature distributions to training feature distributions
 - Block promotion to production if any feature has PSI > 0.1 at deployment time

4. Prevention:
 - Use a shared feature transformation library for both training and serving
 - Store fitted preprocessing artifacts (scalers, encoders, imputers) in the model artifact
 - Apply the same artifact at both training evaluation and serving
 - Integration test: run the serving preprocessing code on a training sample and compare outputs

Return: skew detection implementation, automated deployment scan, prevention checklist, and diagnosis guide. Copy prompt Open prompt details 
## Recommended Drift Detection workflow 
1 
### Concept Drift Localization 

Start with a focused prompt in Drift Detection so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Data Drift vs Concept Drift 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Drift Detection Setup Chain 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Drift Root Cause Report 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
