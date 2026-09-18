# MLOps *AI Prompts *

MLOps AI prompt library with 35 prompts in 5 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 5 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse MLOps prompt categories 
5 categories 
### Drift Detection 

AI prompts for data drift and concept drift detection, monitoring model inputs, identifying changes, and root cause analysis. 
9 prompts Concept Drift Localization Data Drift vs Concept Drift → 
### Model Monitoring 

AI prompts for model monitoring, tracking performance in production, alerting, drift detection, and post-deployment analysis. 
9 prompts Cost of Monitoring Analysis Ground Truth Feedback Loop → 
### CI/CD for ML 

AI prompts for CI/CD in machine learning, covering automated testing, model packaging, deployment gates, and reliable release workflows. 
8 prompts Automated Retraining Pipeline Canary Deployment → 
### Production Incident Response 

AI prompts for production incident response, debugging ML systems, root cause analysis, rollback strategies, and recovery workflows. 
6 prompts Emergency Rollback Procedure Incident Classification Matrix → 
### Model Governance and Compliance 

AI prompts for model governance, audit trails, documentation, regulatory compliance, and responsible AI practices. 
3 prompts Fairness Monitoring ML Audit Trail Chain → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 35 Drift Detection 9 Model Monitoring 9 CI/CD for ML 8 Production Incident Response 6 Model Governance and Compliance 3 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **35 **of 35 prompts 
## Drift Detection 
9 prompt s Drift Detection Intermediate Prompt 01 
### Concept Drift Localization 
When concept drift is detected, implement methods to localize where and when the drift occurred.

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

Return: CUSUM change point detection, feature importance drift analysis, segment performance comparison, and root cause hypothesis framework. Copy prompt View page Show more ↓ Drift Detection Beginner Prompt 02 
### Data Drift vs Concept Drift 
Explain and implement detection methods for the different types of drift this model may experience.

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

Return: drift type detection implementation, diagnosis flowchart, and response playbook per type. Copy prompt View page Show more ↓ Drift Detection Advanced Chain 03 
### Drift Detection Setup Chain 
Step 1: Feature importance ranking — use SHAP values from the production model to rank all features by their average impact on predictions. These are the features where drift matters most.
Step 2: Reference distribution computation — compute reference statistics (mean, std, histogram, PSI bins) for the top 20 features and the prediction output on the training validation set. Store in a metadata table.
Step 3: Univariate drift monitors — implement daily PSI checks for all top-20 features and the prediction distribution. Set alert thresholds: PSI > 0.1 warning, PSI > 0.2 alert. Test with synthetic drift to validate sensitivity.
Step 4: Multivariate drift monitor — implement classifier-based multivariate drift detection running weekly. Validate that it detects joint distribution shifts that the univariate monitors miss.
Step 5: Concept drift monitor — implement rolling performance tracking using the ground truth feedback loop. Set retraining trigger: performance drops below {{threshold}} for {{n}} consecutive days.
Step 6: Alerting and routing — configure alert routing: feature drift → Slack to ML team, prediction drift → Slack + email, performance drift → PagerDuty. Test all alert paths end-to-end.
Step 7: Runbook — document for each alert: what it means, first 3 investigation steps, escalation path, and how to silence a false alarm. Conduct a fire drill with the on-call team. Copy prompt View page Show more ↓ Drift Detection Advanced Prompt 04 
### Drift Root Cause Report 
Generate a structured drift root cause report when drift has been detected in this model.

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

Return: complete drift root cause report template with all sections filled based on available data. Copy prompt View page Show more ↓ Drift Detection Beginner Prompt 05 
### Feature Drift Detection 
Implement feature drift detection to identify when the distribution of input features shifts from the training distribution.

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

Return: reference statistics computation, daily drift detection script, PSI calculation, composite score, and visualization code. Copy prompt View page Show more ↓ Drift Detection Intermediate Prompt 06 
### Multivariate Drift Detection 
Implement multivariate drift detection to catch drift patterns that are invisible in individual feature monitors.

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

Return: classifier-based drift detector, MMD implementation, PCA-based drift, and a comparison of the three methods on synthetic drift scenarios. Copy prompt View page Show more ↓ Drift Detection Advanced Prompt 07 
### Online Drift Detection 
Implement online (stream-based) drift detection that detects drift in real time as predictions arrive, rather than in daily batch jobs.

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

Return: ADWIN, DDM, and KSWIN implementations, serving integration design, and false positive management. Copy prompt View page Show more ↓ Drift Detection Intermediate Prompt 08 
### PSI Implementation 
Implement a production-grade Population Stability Index (PSI) calculation for both numeric and categorical features.

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

Return: PSI implementation for numeric and categorical features, unit tests, batch computation function, and performance benchmark. Copy prompt View page Show more ↓ Drift Detection Intermediate Prompt 09 
### Training-Serving Skew Detection 
Detect and diagnose training-serving skew — when the feature distributions at serving time differ from those at training time due to preprocessing inconsistencies.

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

Return: skew detection implementation, automated deployment scan, prevention checklist, and diagnosis guide. Copy prompt View page Show more ↓ 
## Model Monitoring 
9 prompt s Model Monitoring Advanced Prompt 01 
### Cost of Monitoring Analysis 
Analyze and optimize the cost of the production model monitoring infrastructure.

Current monitoring stack: {{monitoring_stack}}
Number of models monitored: {{num_models}}
Current monthly monitoring cost: {{current_cost}}

1. Cost breakdown:
 - Log storage: how many GB of prediction logs are stored? At what cost per GB?
 - Compute: how many monitoring jobs run per day? What is the compute cost per job?
 - Query costs: how many analytical queries run against the monitoring database? Cost per query?
 - Alerting: external alerting services (PagerDuty, OpsGenie) cost per seat/alert
 - Dashboard: Grafana Cloud or self-hosted cost

2. Sampling strategy for high-throughput models:
 - For models with > 1M predictions/day: log a stratified sample instead of 100%
 - Sample rate recommendation: 10% for >1M/day, 50% for 100k-1M/day, 100% for <100k/day
 - Ensure sample is stratified by prediction score bucket (preserve distribution shape)
 - Log ALL anomalous predictions regardless of sample rate (score > 0.95 or < 0.05 for classifiers)

3. Log retention optimization:
 - Tiered storage: hot (last 7 days, queryable), warm (7–90 days, compressed), cold (>90 days, archival)
 - Pre-aggregate daily statistics (mean, std, percentiles) and retain indefinitely
 - Delete raw logs after 90 days — aggregate statistics are sufficient for long-term trend analysis

4. Monitoring frequency tiering:
 - Tier 1 (revenue-critical): real-time serving metrics, hourly drift checks, daily performance
 - Tier 2 (operational): hourly serving metrics, daily drift checks, weekly performance
 - Tier 3 (experimental): daily serving metrics, weekly drift checks, no automatic performance tracking

5. Estimated savings from each optimization:
 - Sampling: saves X% on log storage and compute
 - Tiered storage: saves Y% on storage
 - Monitoring frequency tiering: saves Z% on compute

Return: cost breakdown analysis, sampling implementation, tiered storage design, and total estimated savings. Copy prompt View page Show more ↓ Model Monitoring Intermediate Prompt 02 
### Ground Truth Feedback Loop 
Design a ground truth feedback loop that joins delayed labels to predictions for ongoing model performance tracking.

Model: {{model_name}}
Label delay: labels become available {{label_delay}} after prediction (e.g. 7 days for churn, 30 days for fraud)
Label source: {{label_source}}

1. Prediction storage for labeling:
 - Store predictions with: request_id, entity_id, model_version, prediction, score, prediction_timestamp
 - Retain predictions for at least label_delay + 30 days buffer
 - Index on entity_id and prediction_timestamp for efficient label joins

2. Label ingestion pipeline:
 - Daily job: fetch newly available labels from {{label_source}}
 - Join to prediction store on entity_id and the relevant time window
 - Handle multiple labels per entity: use the label with the timestamp closest to the prediction
 - Label match rate: what % of predictions received a label? Alert if < {{min_label_rate}}%

3. Performance tracking:
 - Compute rolling metrics over the last 30 days of labeled predictions:
 - Classification: AUC-ROC, precision, recall, F1, calibration error
 - Regression: MAE, RMSE, MAPE, prediction bias (mean(prediction - actual))
 - Compare to training/validation performance baseline
 - Plot metric trend: is performance stable, improving, or degrading?

4. Cohort analysis:
 - Break down performance by: prediction date cohort, model version, user segment
 - Identify if performance degradation is concentrated in a specific cohort or universal

5. Retraining trigger:
 - Define threshold: if rolling 30-day AUC drops below {{retrain_threshold}}, trigger retraining pipeline
 - Distinguish signal from noise: require the drop to persist for {{consecutive_days}} consecutive days

6. Feedback to training:
 - Append newly labeled examples to the training dataset for the next retraining run
 - Track data freshness: what % of the training set is from the last 90 days?

Return: prediction storage schema, label join pipeline, performance tracking queries, and retraining trigger logic. Copy prompt View page Show more ↓ Model Monitoring Intermediate Prompt 03 
### Model Performance Degradation Alert 
Build an early warning system for model performance degradation before ground truth labels arrive.

Since labels often arrive days or weeks after predictions, rely on proxy signals that correlate with model quality.

1. Proxy signal monitoring (no labels required):

 a. Confidence score degradation:
 - Track the distribution of model confidence scores daily
 - A well-calibrated model should have a stable confidence distribution
 - Alert if mean confidence drops > {{confidence_drop_threshold}} or if the distribution becomes more uniform (model is less certain)

 b. Prediction entropy (for classifiers):
 - Entropy = -Σ p_i × log(p_i) across classes
 - Higher entropy = less confident predictions
 - Alert if rolling 7-day mean entropy increases > 1σ above the baseline mean entropy

 c. Feature anomaly rate:
 - Track the % of incoming requests where at least one feature falls outside the training distribution
 - A rising anomaly rate predicts performance degradation before it appears in labels

 d. Business metric correlation (if available):
 - Track downstream business metrics that the model influences (conversion rate, fraud rate)
 - Unexplained movements in business metrics may indicate model degradation

2. Composite degradation score:
 - Combine multiple proxy signals into a single degradation score (0–100)
 - Weight by historical correlation with actual performance drops
 - Thresholds: score > 60 → Slack alert, score > 80 → PagerDuty

3. Alert content:
 - Current degradation score and contributing signals
 - Trend: is degradation accelerating or stable?
 - Recommended action: monitor / investigate / retrain
 - Link to monitoring dashboard and recent prediction sample for manual inspection

4. Validation:
 - Backtest the proxy signals on historical data: did they predict known past degradation events?
 - Report: lead time before degradation became visible in labels, false positive rate

Return: proxy signal monitoring code, composite score calculation, alerting logic, and backtest methodology. Copy prompt View page Show more ↓ Model Monitoring Advanced Chain 04 
### Monitoring Setup Chain 
Step 1: Define monitoring requirements — for this model, specify: what constitutes a healthy prediction distribution, the acceptable performance floor, the label availability timeline, and the business cost of undetected degradation vs false alarms.
Step 2: Instrument prediction logging — add async prediction logging to the serving layer. Log: request_id, model_version, features, prediction, confidence, latency. Verify logs are flowing to the storage layer.
Step 3: Establish baselines — compute reference distributions for all features and model outputs using the first 2 weeks of production data (or the validation set if launching new). Store baseline statistics.
Step 4: Deploy serving metrics — instrument Prometheus metrics (RPS, latency, error rate). Set up Grafana dashboard. Configure AlertManager rules for SLA violations.
Step 5: Deploy drift monitors — implement daily PSI checks for top features and prediction distribution. Set thresholds and alert routing. Run a backtest to validate alert sensitivity.
Step 6: Deploy performance tracking — implement ground truth join pipeline. Set up rolling performance metric computation. Define retraining trigger condition.
Step 7: Document and hand off — write the monitoring runbook: what each alert means, initial triage steps, escalation path, and how to silence a false alarm. Get sign-off from the on-call team before go-live. Copy prompt View page Show more ↓ Model Monitoring Advanced Prompt 05 
### Multi-Model Monitoring System 
Design a centralized monitoring system that scales to {{num_models}} production ML models.

Challenge: each model has different input features, output types, and business metrics. A one-size-fits-all approach does not work.

1. Model registry integration:
 - Each registered model provides a monitoring config alongside the model artifact
 - Monitoring config specifies: key features to monitor, output type and drift thresholds, business metric to track, retraining trigger conditions, and alert routing

2. Centralized collection layer:
 - Standardized prediction log schema with model-specific payload field for input/output details
 - All models write to the same Kafka topic, partitioned by model_name
 - Central consumer writes to a unified monitoring database partitioned by model_name/date

3. Per-model monitoring jobs:
 - Template monitoring job parameterized by model config
 - Spins up one monitoring job per registered model automatically on new model deployment
 - Each job: reads from the unified monitoring database, applies the model-specific config, and writes results to a monitoring metrics table

4. Unified monitoring dashboard:
 - Overview page: table of all models with health status (🟢/🟡/🔴) based on recent alerts
 - Drill-down per model: serving metrics, prediction distribution, drift scores, recent alerts
 - Cross-model comparison: compare drift patterns across models — correlated drift suggests a shared upstream data issue

5. Alert deduplication and routing:
 - Group alerts from the same model within a 1-hour window to avoid alert storms
 - Route to the correct on-call engineer based on model ownership in the registry
 - Escalation: if alert is not acknowledged within {{escalation_window}} minutes, page the team lead

6. Cost management:
 - Tier models by importance (Tier 1: revenue-critical, Tier 2: operational, Tier 3: experimental)
 - Different monitoring frequencies per tier: T1 = real-time, T2 = hourly, T3 = daily
 - Estimated monitoring cost per model per month

Return: monitoring config schema, centralized collection architecture, per-model job template, and unified dashboard spec. Copy prompt View page Show more ↓ Model Monitoring Intermediate Prompt 06 
### Prediction Distribution Monitor 
Build a system to monitor the distribution of model predictions over time and detect output drift.

Model type: {{model_type}} (binary classifier / multiclass / regression / ranking)

1. Baseline distribution:
 - Compute the prediction distribution on a held-out reference dataset (or first 2 weeks of production logs)
 - For classifiers: positive rate, score distribution (histogram with 20 bins), confusion matrix on labeled data
 - For regression: mean, std, percentiles (5th, 25th, 50th, 75th, 95th), histogram
 - Store baseline statistics in a metadata table for comparison

2. Daily distribution comparison:
 - Compute the same statistics on the last 24 hours of predictions
 - Statistical tests:
 - Classifier scores: Kolmogorov-Smirnov test (KS test) vs baseline distribution
 - Classifier positive rate: two-proportion z-test vs baseline positive rate
 - Regression outputs: KS test + t-test for mean shift
 - Population Stability Index (PSI):
 - PSI < 0.1: no significant shift
 - PSI 0.1–0.2: moderate shift — investigate
 - PSI > 0.2: significant shift — alert

3. Temporal patterns:
 - Plot rolling 7-day mean prediction score over time
 - Plot rolling positive rate (for classifiers) over time
 - Flag: sudden jumps (step change) vs gradual drift (slow trend)
 - Annotate with model deployment dates to distinguish drift from deployment effects

4. Segment-level monitoring:
 - Compute prediction distribution separately for key segments (region, user type, device)
 - Flag any segment where distribution diverges significantly from the population

5. Alerting:
 - PSI > 0.2 on overall prediction distribution: Slack alert to ML team (P2)
 - Positive rate changes > 2× std from 30-day rolling average: Slack alert (P2)
 - Positive rate changes > 5× std: PagerDuty (P1) — likely a model or feature pipeline failure

Return: baseline computation script, daily comparison script, PSI calculation function, and alerting configuration. Copy prompt View page Show more ↓ Model Monitoring Beginner Prompt 07 
### Prediction Logging Setup 
Design and implement a production prediction logging system for this ML model.

Model: {{model_name}}
Serving framework: {{serving_framework}}
Expected throughput: {{requests_per_second}} requests/sec

1. What to log per prediction:
 - request_id: unique identifier for traceability
 - model_name and model_version: which exact artifact served this request
 - timestamp: ISO 8601, UTC
 - input_features: the feature vector sent to the model (after preprocessing)
 - raw_input: the original unprocessed input (for debugging preprocessing bugs)
 - prediction: the model's output (class label, score, or generated value)
 - prediction_probability or confidence: confidence score where applicable
 - latency_ms: total inference time
 - serving_node: which pod/instance served the request (for debugging node-specific issues)

2. Async logging (never block the serving path):
 - Write to an in-memory queue in the request handler
 - Background thread drains the queue and writes to the log sink in batches
 - If the log sink is unavailable: drop logs gracefully, do not fail the prediction

3. Log sink options by throughput:
 - < 1k RPS: write directly to a structured log file, ship with Fluentd/Logstash
 - 1k–100k RPS: write to Kafka topic, consume to object storage and OLAP table
 - > 100k RPS: write to a high-throughput sink (Kinesis Data Firehose, Pub/Sub) with batching

4. Storage and retention:
 - Raw logs: object storage (S3/GCS), partitioned by model_name/date, retained for 90 days
 - Queryable table: OLAP warehouse (BigQuery/Snowflake), retained for 1 year
 - PII handling: mask or hash any PII fields in the feature log before storage

5. Log schema versioning:
 - Version the log schema alongside the model version
 - Never remove fields from the log schema — add new fields with NULL backfill for old records

Return: prediction log schema (JSON), async logging implementation, sink configuration for the given throughput, and PII masking approach. Copy prompt View page Show more ↓ Model Monitoring Beginner Prompt 08 
### Serving Metrics Dashboard 
Design a production model serving metrics dashboard using Prometheus and Grafana.

Model: {{model_name}}
SLA targets: p99 latency < {{latency_sla_ms}}ms, error rate < {{error_rate_sla}}%, availability > {{availability_sla}}%

1. Prometheus metrics to instrument (add to the serving application):

 Service-level metrics:
 - model_requests_total (counter): labeled by model_version, endpoint, status_code
 - model_request_duration_seconds (histogram): labeled by model_version, endpoint
 Buckets: [0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0]
 - model_errors_total (counter): labeled by model_version, error_type
 - model_in_flight_requests (gauge): current concurrent requests

 Model-level metrics:
 - prediction_score_distribution (histogram): distribution of output confidence scores
 - feature_value_distribution (histogram): one per key feature, for drift detection
 - model_load_time_seconds (gauge): time to load model at startup

 Infrastructure metrics:
 - gpu_utilization_percent (gauge): per serving node
 - gpu_memory_used_bytes (gauge): per serving node

2. Grafana dashboard panels:
 Row 1 — SLA Overview:
 - Current request rate (RPS)
 - p50 / p95 / p99 latency (time series)
 - Error rate % (time series, red threshold at SLA)
 - Availability % (stat panel, green/red)

 Row 2 — Model Health:
 - Prediction score distribution (heatmap over time)
 - Request volume by model version (stacked bar — useful during rollouts)
 - Top error types (table)

 Row 3 — Infrastructure:
 - GPU utilization per node (time series)
 - GPU memory used per node (time series)
 - Pod count (gauge)

3. Alerting rules (Prometheus AlertManager):
 - HighErrorRate: error_rate > {{error_rate_sla}}% for 5 minutes → PagerDuty (P1)
 - HighLatency: p99 > {{latency_sla_ms}}ms for 10 minutes → Slack (P2)
 - ModelDown: no successful requests for 2 minutes → PagerDuty (P0)
 - LowThroughput: RPS drops > 50% vs 1-hour average → Slack (P2)

Return: Prometheus instrumentation code, AlertManager rules YAML, and Grafana dashboard JSON. Copy prompt View page Show more ↓ Model Monitoring Intermediate Prompt 09 
### Shadow Mode Evaluation 
Implement shadow mode deployment to evaluate a new model version in production without serving its predictions to users.

In shadow mode: all requests are served by the champion model. The challenger model receives a copy of every request, runs inference, and logs its predictions — but its output is discarded and never returned to the user.

1. Shadow mode architecture:
 - Duplicate every incoming request to the challenger model asynchronously
 - The challenger call must never block or slow the champion response
 - Use a fire-and-forget async call with a timeout of {{shadow_timeout_ms}}ms
 - If the challenger times out or errors: log the failure, continue without impact to the user

2. Shadow prediction logging:
 - Log champion and challenger predictions with the same request_id for comparison
 - Schema: request_id, champion_prediction, champion_score, challenger_prediction, challenger_score, timestamp

3. Comparison analysis (run daily):
 - Agreement rate: % of requests where champion and challenger produce the same prediction
 - Score correlation: Pearson correlation between champion and challenger scores
 - Distribution comparison: KS test between champion and challenger score distributions
 - Disagreement analysis: for cases where they disagree, which model is likely correct? Sample 50 and manually inspect
 - Latency comparison: challenger p99 vs champion p99 (challenger must meet latency SLA)

4. Promotion criteria:
 - Run shadow mode for {{shadow_duration}} days minimum
 - Challenger must: pass all serving metric requirements, show better or equal distribution quality, meet latency SLA
 - If labels are available: measure challenger performance on labeled shadow period data

5. Shadow mode cost:
 - Shadow mode doubles compute cost — plan for this in the infrastructure budget
 - Use a smaller replica count for the challenger during shadow mode

Return: shadow mode routing implementation, comparison analysis script, and promotion decision criteria. Copy prompt View page Show more ↓ 
## CI/CD for ML 
8 prompt s CI/CD for ML Intermediate Prompt 01 
### Automated Retraining Pipeline 
Build an automated model retraining pipeline triggered by monitoring signals.

Trigger conditions (any one sufficient):
1. Performance trigger: rolling 7-day AUC drops below {{performance_threshold}}
2. Drift trigger: PSI > 0.2 on any of the top-5 most important features
3. Data volume trigger: {{new_labeled_samples}} new labeled samples accumulated since last training
4. Schedule trigger: weekly retrain regardless of performance (for models in fast-changing domains)

Pipeline steps:

1. Trigger detection job (runs daily):
 - Query monitoring database for each trigger condition
 - If any condition is met: log which trigger fired, create a retraining job request
 - Deduplication: if multiple triggers fire simultaneously, create only one retraining job
 - Rate limiting: do not trigger more than {{max_retrains_per_week}} retrains per week (prevents trigger storms)

2. Data preparation:
 - Fetch training data from the feature store: last {{training_window}} days of labeled data
 - Apply the same preprocessing pipeline as the current production model
 - Validate: training set must have ≥ {{min_training_samples}} labeled samples
 - Log dataset statistics: row count, label distribution, date range, feature means

3. Training job:
 - Use the same hyperparameters as the current production model (only data is updated)
 - Allow for hyperparameter re-search if triggered by {{hp_retune_trigger}} (e.g. monthly)
 - Track the run in the experiment tracker: link to trigger event, dataset version, git commit

4. Evaluation and gate:
 - Run the performance gate against the challenger model
 - If gate passes: register in model registry as 'Staging'
 - If gate fails: alert team, keep current production model, investigate why new data did not improve the model

5. Deployment:
 - Auto-deploy to staging environment
 - Run integration tests in staging
 - If all tests pass: auto-promote to production (or require human approval for high-stakes models)

Return: trigger detection script, pipeline orchestration code (Airflow DAG or Prefect flow), and gate integration. Copy prompt View page Show more ↓ CI/CD for ML Intermediate Prompt 02 
### Canary Deployment 
Implement a canary deployment strategy for safely rolling out a new model version.

Canary deployment: gradually shift traffic from the champion to the challenger while monitoring for regressions.

1. Traffic progression schedule:
 - Stage 1 (Day 1): 1% of traffic to challenger
 - Stage 2 (Day 2): 5% if Stage 1 metrics are healthy
 - Stage 3 (Day 3): 20% if Stage 2 metrics are healthy
 - Stage 4 (Day 5): 50% if Stage 3 metrics are healthy
 - Stage 5 (Day 7): 100% if Stage 4 metrics are healthy
 - Each stage requires minimum {{min_requests_per_stage}} requests before evaluation

2. Health checks at each stage:
 - Error rate: challenger error rate must not exceed champion error rate + {{error_tolerance}}%
 - Latency: challenger p99 must not exceed champion p99 × {{latency_tolerance_multiplier}}
 - Prediction distribution: PSI between challenger and champion must be < {{max_psi}} (unexpected distribution shift)
 - If labels are available: challenger performance must be ≥ champion performance - {{min_degradation_tolerance}}

3. Automated progression:
 - If all health checks pass at the end of each stage: automatically advance to the next stage
 - If any health check fails: automatically roll back to 0% challenger traffic and alert the team
 - Manual override: allow engineers to pause, advance, or roll back at any stage via CLI command

4. Traffic routing implementation:
 - Hash-based user assignment: consistent hashing ensures the same user always gets the same model
 - Feature flag service: traffic split percentage stored in a config service, updated without redeployment
 - Logging: every request tagged with model_version and stage_name for analysis

5. Canary analysis report:
 - After each stage: generate a canary analysis report comparing champion vs challenger
 - Highlight any metrics where challenger underperforms
 - Decision recommendation: advance / hold / rollback

Return: traffic routing implementation, health check automation, progressive rollout logic, and canary analysis report generator. Copy prompt View page Show more ↓ CI/CD for ML Advanced Chain 03 
### CI/CD Pipeline Design Chain 
Step 1: Test inventory — catalog all existing tests (unit, integration, smoke). Identify untested code paths in the preprocessing, feature engineering, training, and serving layers. Prioritize which gaps to fill first based on risk.
Step 2: CI pipeline (on every PR) — define the fast CI pipeline: linting, type checking, unit tests, smoke training test, serving health check. Target: completes in < 10 minutes. Block merge on any failure.
Step 3: Extended CI (on merge to main) — define the extended pipeline: full integration tests, performance gate against holdout set, training-serving skew check, latency benchmark. Target: completes in < 30 minutes.
Step 4: CD pipeline (on model registry promotion) — define the deployment pipeline: staging deploy, integration tests in staging, canary deployment to production (1% → 5% → 20% → 100%), automated rollback on health check failure.
Step 5: Retraining pipeline — design the automated retraining trigger, training job, evaluation gate, and staging promotion. Define the human-in-the-loop gates for high-stakes models.
Step 6: Rollback procedure — document and automate the rollback: config repo revert, GitOps reconciliation, verification that the previous model is serving. Target: rollback executable by any on-call engineer in < 5 minutes.
Step 7: Pipeline documentation — write the CI/CD runbook: what each pipeline stage does, how to debug a failing stage, how to manually trigger or skip a stage, and who to escalate to when the pipeline is broken. Copy prompt View page Show more ↓ CI/CD for ML Advanced Prompt 04 
### ML GitOps Workflow 
Design a GitOps workflow for managing ML model deployments where Git is the single source of truth.

In a GitOps workflow, the desired state of production is declared in Git. Changes to production happen only through Git commits, not manual operations.

1. Repository structure:
 - Application code repo: model code, training scripts, tests
 - Config repo: deployment manifests (Kubernetes YAML, serving config, model version to deploy)
 - ML platform watches the config repo and automatically reconciles the actual state to match

2. Model deployment workflow:
 - Developer trains a new model and registers it in the model registry
 - To deploy: submit a PR to the config repo updating the model_version field in the deployment manifest
 - PR triggers: automated validation (model exists in registry, performance gate passed, integration tests pass)
 - PR merge = deployment (GitOps operator applies the new config to the cluster)
 - Every deployment is a git commit: full audit trail with author, time, and reviewer

3. Rollback workflow:
 - Rollback = revert the config repo PR
 - git revert triggers the GitOps operator to restore the previous model version
 - Target rollback time: < 5 minutes from merge to previous version serving

4. Environment promotion:
 - Separate branches: dev → staging → production
 - Promotion = PR from staging branch to production branch
 - Automated checks before merge: performance gate, integration tests, canary analysis
 - Human approval required for production merges

5. Secret management in GitOps:
 - Never store secrets in Git (not even in private repos)
 - Use sealed secrets (Bitnami Sealed Secrets) or external secret operators (AWS Secrets Manager, Vault)
 - Seal secrets with the cluster's public key before committing

6. Drift detection on config:
 - Alert if the actual deployed model version diverges from the Git-declared version (configuration drift)

Return: repository structure, GitOps operator configuration (ArgoCD or Flux), PR workflow definition, and rollback procedure. Copy prompt View page Show more ↓ CI/CD for ML Intermediate Prompt 05 
### ML Pipeline Integration Tests 
Write integration tests for the end-to-end ML pipeline from feature ingestion to model serving.

Integration tests verify that all components work together correctly — unlike unit tests which test components in isolation.

1. Feature pipeline integration test:
 - Feed a synthetic but representative input event through the feature pipeline
 - Assert: output features have the correct schema, no null values in required fields, values in expected ranges
 - Assert: feature values match manually computed expected values for the synthetic input
 - Test the pipeline with a batch of 1000 synthetic records: performance and correctness at scale

2. Training pipeline integration test:
 - Run the full training pipeline on a small synthetic dataset (500 rows)
 - Assert: training completes without error
 - Assert: a model artifact is produced and saved to the expected location
 - Assert: the model artifact can be loaded and accepts the expected input format
 - Assert: validation metrics are logged to the experiment tracker
 - Runtime: must complete in < {{max_test_runtime}} minutes

3. Serving pipeline integration test:
 - Load the model from the registry (latest staging version)
 - Send a batch of 100 test requests through the full serving stack (HTTP → preprocessing → inference → postprocessing)
 - Assert: all 200 responses are returned without error
 - Assert: response schema matches the API contract
 - Assert: latency p99 < {{latency_sla_ms}}ms for the test batch
 - Assert: predictions are deterministic (same input → same output)

4. Data contract integration test:
 - Verify that the model's expected input schema matches what the feature pipeline actually produces
 - Any mismatch between feature pipeline output schema and model input schema is a deployment blocker

5. Rollback integration test:
 - Deploy a known-good model version, then trigger a rollback procedure
 - Assert: rollback completes in < {{rollback_time_limit}} seconds
 - Assert: serving resumes with the previous model version

Return: complete integration test suite, test data fixtures, CI/CD configuration to run tests on every PR and deployment. Copy prompt View page Show more ↓ CI/CD for ML Beginner Prompt 06 
### ML Unit Testing 
Write a comprehensive unit test suite for this ML codebase.

ML code has unique testing challenges: stochasticity, large data dependencies, and complex multi-step pipelines. These patterns address them.

1. Preprocessing tests:
 - Test each transformation function with a minimal synthetic DataFrame
 - Test edge cases: all-null column, single row, empty DataFrame, columns with extreme values
 - Test idempotency: applying the transformation twice produces the same result as applying it once
 - Test dtype contracts: output dtypes match expectations regardless of input variation

2. Feature engineering tests:
 - Test each feature computation function independently
 - Assert feature values are within expected ranges
 - Test for data leakage: features computed on a single row must not access other rows' data
 - Test lag/rolling features: verify the correct temporal offset is applied

3. Model architecture tests:
 - Test forward pass: model accepts the expected input shape and returns the expected output shape
 - Test output range: for classifiers, softmax outputs sum to 1; probabilities are in [0,1]
 - Test gradient flow: loss.backward() does not produce NaN or Inf gradients
 - Test model save/load: saved model produces identical outputs to the original model

4. Loss function tests:
 - Perfect predictions → loss = 0 (or near zero)
 - Random predictions → loss is within the expected range for the problem
 - Gradient check: torch.autograd.gradcheck passes

5. Metric tests:
 - Test each metric function: verify output equals a hand-calculated expected value on a small example
 - Test edge cases: all-same-class predictions, perfect predictions, all-wrong predictions

6. No-train test (smoke test for the training loop):
 - Run 1 training step on a tiny synthetic dataset
 - Assert: loss decreases after the first step, model parameters change, no errors thrown

Return: test suite covering all categories, with fixtures for synthetic data and a pytest configuration. Copy prompt View page Show more ↓ CI/CD for ML Beginner Prompt 07 
### Model Performance Gate 
Implement a model performance gate that automatically approves or blocks model promotion based on predefined quality criteria.

1. Gate design principles:
 - Evaluate the challenger model against a fixed, versioned holdout dataset — never the training or validation set
 - The holdout dataset must represent the real-world distribution (not just historical data)
 - Gate must be deterministic: same model + same dataset must always produce the same pass/fail decision

2. Gate criteria — the challenger must pass ALL of these to be promoted:

 a. Absolute performance floor:
 - Primary metric (e.g. AUC) > {{min_auc}} — if below this, the model is too weak to ship regardless of improvement

 b. Relative improvement vs champion:
 - Primary metric improvement > {{min_improvement_pct}}% vs current production model
 - This prevents promoting a model that is technically better but not meaningfully so

 c. Guardrail metrics — must not degrade:
 - Secondary metrics (precision, recall, F1) must not degrade by more than {{max_guardrail_degradation}}%
 - Inference latency p99 must not increase by more than {{max_latency_increase_pct}}%

 d. Fairness check (if applicable):
 - Performance disparity across demographic groups must be within {{max_disparity_pct}}%

 e. Calibration check:
 - Expected Calibration Error (ECE) < {{max_ece}}

3. Gate output:
 - PASS: all criteria met → auto-promote to staging
 - CONDITIONAL PASS: improvement is positive but small → require human approval
 - FAIL: one or more criteria not met → block promotion, notify team with specific reason
 - Gate report: a structured JSON with all metric values, thresholds, and pass/fail per criterion

4. Gate versioning:
 - Version the gate criteria alongside the model — different model families may have different gates
 - Audit log: record every gate evaluation with model version, criteria version, and outcome

Return: gate evaluation code, gate criteria configuration (YAML), pass/fail report generator, and CI/CD integration. Copy prompt View page Show more ↓ CI/CD for ML Intermediate Prompt 08 
### Model Registry Workflow 
Design the complete model lifecycle workflow using a model registry.

Registry: {{registry_tool}} (MLflow / SageMaker Model Registry / Vertex AI Model Registry)

1. Model registration (triggered after successful training run):
 - Register model only if performance gate passes
 - Required metadata at registration:
 - model_version (auto-incremented)
 - training_run_id (link to experiment tracker)
 - git_commit_hash (reproducibility)
 - dataset_version (which data was used)
 - evaluation_metrics (all performance metrics on holdout set)
 - model_signature (input/output schema)
 - dependencies (requirements.txt snapshot)
 - tags: model_family, use_case, owner_team

2. Stage transitions:
 - None → Staging: automatic after registration + gate pass
 - Staging → Production: requires human approval + integration test pass in staging
 - Production → Archived: when replaced by a newer version
 - Never delete versions — only archive

3. Approval workflow for Staging → Production:
 - Approver must be a senior ML engineer or ML team lead (not the model's author)
 - Approval checklist: performance gate results, canary test results, monitoring setup verified, runbook updated
 - Approval is recorded in the registry with approver identity and timestamp
 - Approval expires after {{approval_expiry}} hours — stale approvals require re-approval

4. Model loading at serving time:
 - Always load by stage ('Production'), never by version number
 - Cache the loaded model in memory, poll the registry every {{poll_interval}} seconds for version changes
 - On version change: load new model in parallel, switch traffic only after new model is warmed up
 - Graceful switch: in-flight requests complete on the old model, new requests go to the new model

5. Audit and compliance:
 - All stage transitions logged with: who, when, why, and from/to version
 - Monthly audit report: models promoted, models rolled back, approval SLA compliance

Return: registration code, stage transition automation, approval workflow, and serving-side model loader with polling. Copy prompt View page Show more ↓ 
## Production Incident Response 
6 prompt s Production Incident Response Intermediate Prompt 01 
### Emergency Rollback Procedure 
Design and implement a fast, reliable emergency rollback procedure for production ML models.

Target: complete rollback in < 5 minutes from decision to previous version serving traffic.

1. Pre-conditions for rollback:
 - Rollback is appropriate when: model is causing user-facing errors, model is producing obviously wrong predictions, or model is degrading a critical business metric
 - Rollback is NOT appropriate when: drift is detected but predictions are technically correct, a gradual performance decline is ongoing (investigate first)

2. Rollback implementation options (fastest to slowest):

 Option A — Model registry rollback (< 2 minutes):
 - Demote the current Production model version to Archived
 - Promote the previous version back to Production
 - Serving pods detect the version change via polling and hot-swap the model
 - No pod restart required
 ```
 mlflow_client.transition_model_version_stage(name='{{model_name}}', version='{{current_version}}', stage='Archived')
 mlflow_client.transition_model_version_stage(name='{{model_name}}', version='{{previous_version}}', stage='Production')
 ```

 Option B — Kubernetes deployment rollback (< 3 minutes):
 - kubectl rollout undo deployment/{{deployment_name}} -n {{namespace}}
 - Verify: kubectl rollout status deployment/{{deployment_name}}

 Option C — Traffic routing rollback (< 1 minute):
 - If A/B deployment is active: set challenger traffic weight to 0%
 - Only works if champion model is still deployed and healthy

3. Rollback verification checklist:
 - [ ] Error rate returned to pre-incident baseline
 - [ ] Latency p99 returned to pre-incident baseline
 - [ ] Prediction distribution matches pre-incident baseline
 - [ ] Confirm which model version is now serving
 - [ ] Downstream systems have recovered

4. Post-rollback actions:
 - Create a post-mortem ticket with: incident timeline, rollback trigger, business impact
 - Lock the rolled-back version to prevent automatic re-deployment
 - Do not re-deploy the same version without fixing the root cause

5. Rollback drill:
 - Conduct a rollback drill quarterly in staging to verify the procedure works and engineers are familiar with it

Return: rollback scripts for all three options, verification checklist, post-rollback action template, and drill procedure. Copy prompt View page Show more ↓ Production Incident Response Beginner Prompt 02 
### Incident Classification Matrix 
Define an ML model incident classification matrix and response procedures for each severity level.

1. Severity levels and definitions:

 P0 — Critical (page immediately, all hands):
 - Model is returning errors for > 5% of requests (hard failures)
 - Model is completely unresponsive (serving down)
 - Model predictions are obviously wrong across the board (e.g. classifier predicting all-one-class)
 - Downstream system failure caused by model output
 Response SLA: acknowledge in 5 minutes, update in 15 minutes, resolve or mitigate in 60 minutes

 P1 — High (page on-call engineer):
 - Model latency p99 > 2× SLA for > 10 minutes
 - Error rate > 1% and rising
 - Significant prediction distribution shift detected (PSI > 0.5)
 - Silent accuracy degradation confirmed (performance drop > 10% vs baseline)
 Response SLA: acknowledge in 15 minutes, resolve or mitigate in 4 hours

 P2 — Medium (notify ML team via Slack):
 - Model latency p99 between 1× and 2× SLA
 - Moderate drift detected (PSI 0.2–0.5)
 - Performance drop 5–10% vs baseline
 - Label rate dropped below expected (feedback loop issue)
 Response SLA: acknowledge in 1 hour, resolve in 24 hours

 P3 — Low (create ticket, handle next business day):
 - Minor drift (PSI 0.1–0.2)
 - Performance drop < 5%
 - Monitoring data quality issues (missing logs, delayed metrics)
 Response SLA: acknowledge in 4 hours, resolve in 1 week

2. Incident declaration criteria:
 - Any automated alert at P0 or P1 automatically creates an incident
 - P2 and P3: engineer uses judgment based on business context

3. Incident communication template:
 - Status page update: 'Investigating reports of [issue] affecting [model]. Engineers are engaged.'
 - Internal Slack: 'P[X] incident declared for [model_name]. Owner: [name]. Bridge: [link]'

Return: classification matrix table, SLA definitions, alert-to-incident mapping, and communication templates. Copy prompt View page Show more ↓ Production Incident Response Intermediate Prompt 03 
### Incident Post-Mortem 
Write a blameless post-mortem for this ML model incident.

Incident summary: {{incident_summary}}
Model affected: {{model_name}}
Incident duration: {{duration}}
Business impact: {{business_impact}}

Blameless post-mortem principles:
- The goal is to learn and prevent recurrence, not to assign blame
- People acted with good intentions given the information they had at the time
- Focus on system and process failures, not individual failures

1. Incident summary:
 - What happened? (2–3 sentences, suitable for a non-technical audience)
 - When did it start? When was it detected? When was it resolved?
 - Who was involved in the response?

2. Timeline (chronological):
 - [timestamp] — Event description
 - Include: first symptom, alert triggered, incident declared, triage started, root cause identified, mitigation applied, full resolution

3. Root cause analysis:
 - What was the immediate cause? (What triggered the incident?)
 - What were the contributing causes? (Five Whys or similar)
 - What allowed this to happen? (System design, monitoring gap, process gap)

4. Impact assessment:
 - User impact: how many users or requests were affected?
 - Business impact: estimated revenue impact, SLA violations, customer complaints
 - Data impact: any data corruption or loss?

5. What went well:
 - What detection, response, or mitigation actions worked effectively?

6. What went wrong:
 - What slowed detection, diagnosis, or resolution?

7. Action items (the most important section):
 - For each: what will be done, who owns it, and by when
 - Categorize: immediate fix, monitoring improvement, process improvement, systemic fix
 - All action items must be in a tracking system within 24 hours of the post-mortem

Return: complete blameless post-mortem document. Copy prompt View page Show more ↓ Production Incident Response Advanced Chain 04 
### Incident Response Chain 
Step 1: Detection — describe the detection mechanism that triggered this incident. Was it an automated alert, a user report, or proactive monitoring? Note the detection time and any delay between incident start and detection.
Step 2: Triage — work through the triage runbook. Is this a model issue, an infrastructure issue, or a data pipeline issue? What is the initial severity classification (P0/P1/P2/P3)?
Step 3: Immediate mitigation — what can be done in the next 15 minutes to reduce user impact? Options: rollback to previous model, route traffic to a fallback, disable the feature using this model, apply a threshold adjustment.
Step 4: Root cause investigation — with the immediate mitigation in place, investigate the root cause. Use the diagnostic tools: serving logs, feature pipeline logs, model performance metrics, drift dashboard. Apply Five Whys.
Step 5: Permanent fix — design and implement the fix for the root cause. This may take hours or days. It must be tested in staging before re-deployment to production.
Step 6: Recovery and verification — re-deploy the fixed model. Monitor closely for 24 hours: serving metrics, prediction distribution, business metrics. Confirm full recovery.
Step 7: Post-mortem — within 48 hours, write and publish the blameless post-mortem. All action items entered into tracking. Schedule a follow-up review in 2 weeks to verify action items are being completed. Copy prompt View page Show more ↓ Production Incident Response Advanced Prompt 05 
### Silent Failure Detection 
Design a system to detect silent model failures — cases where the model is technically healthy (no errors, normal latency) but is producing systematically wrong predictions.

Silent failures are the hardest ML incidents to catch because all serving metrics look normal.

1. Common silent failure patterns:
 - Feature pipeline regression: an upstream data change causes features to be systematically wrong (e.g. revenue column now in USD instead of thousands)
 - Stale model: model has not been retrained and concept drift has made it unreliable
 - Encoding mismatch: categorical encoder mapping changed but old encoder artifact is still loaded
 - Timestamp bug: features computed at wrong time (e.g. using future data that is not available at prediction time)
 - Default value injection: null handling changed upstream, high-null rate filling in default values

2. Detection signals:

 a. Business metric correlation:
 - Track the correlation between model scores and business outcomes (click rate, conversion, fraud rate)
 - A sudden drop in score-outcome correlation indicates silent failure
 - Requires labels but this correlation is often visible sooner than accuracy metrics

 b. Model score vs business outcome divergence:
 - If the model predicts high fraud probability but actual fraud rate is not rising: model may be crying wolf
 - If the model predicts low churn but actual churn rises: model may be failing silently

 c. Feature sanity checks:
 - For each key feature: compare the real-time mean to the expected mean from training
 - Flag if any feature mean shifts by > 3σ from the expected mean — possible upstream bug

 d. Prediction sanity rules:
 - Hard rules from domain knowledge: 'no customer with account age < 30 days should have a premium churn risk score'
 - Rule violation rate: track the % of predictions that violate domain rules daily

3. Canary evaluation:
 - Maintain a small set of labeled 'canary' examples with known correct predictions
 - Score canary examples daily and alert if any canary prediction changes
 - Canary examples should cover a range of prediction scores and edge cases

4. Regular prediction audits:
 - Weekly: sample 50 predictions randomly and manually inspect inputs + outputs
 - Monthly: have a domain expert review a larger sample and flag any suspicious patterns

Return: business metric correlation monitor, feature sanity check implementation, domain rule violation tracker, and canary evaluation system. Copy prompt View page Show more ↓ Production Incident Response Intermediate Prompt 06 
### Triage Runbook 
Write a model incident triage runbook for on-call engineers who may not be deeply familiar with the specific model.

Model: {{model_name}}
Serving infrastructure: {{infrastructure}}

The runbook must be executable by any on-call engineer within 15 minutes of being paged.

1. Initial triage (first 5 minutes):
 - Is this a model issue or an infrastructure issue?
 Check 1: Are the Kubernetes pods healthy? (kubectl get pods -n {{namespace}})
 Check 2: Is the serving endpoint returning any responses? (curl -X POST {{health_endpoint}})
 Check 3: Are the upstream feature pipelines healthy? (link to pipeline dashboard)
 Check 4: Was there a recent deployment? (check deployment log at {{deploy_log_link}})

2. Model-specific diagnostics (minutes 5–10):
 - Check serving dashboard: error rate, latency, prediction distribution (link: {{dashboard_link}})
 - Check feature drift dashboard: any features showing high PSI? (link: {{drift_dashboard_link}})
 - Check model version currently serving: what model version is in production? Expected: {{expected_version}}
 - Sample 10 recent predictions: do the inputs and outputs look sane? (query: {{sample_query}})

3. Common failure modes and immediate actions:
 - High error rate → Check logs for error type. If OOM: restart pods. If model file missing: check object storage.
 - High latency → Check GPU utilization. If GPU saturated: scale up pods. If CPU-bound: check for preprocessing bottleneck.
 - Wrong predictions → Check model version. If unexpected version: trigger rollback. Check feature pipeline for data quality issues.
 - All predictions same class → Model likely receiving all-null or all-default features. Check feature pipeline.

4. Rollback procedure:
 - Command: {{rollback_command}}
 - Expected output: {{expected_rollback_output}}
 - Verification: wait 2 minutes, then confirm error rate has returned to baseline

5. Escalation:
 - If unresolved in 30 minutes: page {{escalation_contact}}
 - If data pipeline issue: page {{data_team_contact}}
 - If model quality issue: page {{ml_team_contact}}

Return: complete triage runbook formatted as a step-by-step guide. Copy prompt View page Show more ↓ 
## Model Governance and Compliance 
3 prompt s Model Governance and Compliance Intermediate Prompt 01 
### Fairness Monitoring 
Implement ongoing fairness monitoring for this production model.

Model: {{model_name}}
Sensitive attributes to monitor: {{sensitive_attributes}} (e.g. age_group, gender, region)
Fairness metric: {{fairness_metric}}

1. Fairness metrics — implement all of the following:

 a. Demographic parity (statistical parity):
 - Positive prediction rate should be equal across groups
 - Disparity = |P(ŷ=1 | group=A) - P(ŷ=1 | group=B)|
 - Alert threshold: disparity > {{dp_threshold}} (e.g. 0.05 = 5 percentage points)

 b. Equal opportunity:
 - True positive rate (recall) should be equal across groups
 - Requires ground truth labels
 - Disparity = |TPR_A - TPR_B|

 c. Predictive parity:
 - Precision (positive predictive value) should be equal across groups
 - Disparity = |Precision_A - Precision_B|

 d. Calibration by group:
 - Among predictions with score ~0.7, 70% should actually be positive, in every group
 - Plot calibration curves separately for each group

2. Monitoring implementation:
 - Compute all fairness metrics weekly on the last 4 weeks of labeled predictions
 - Track trends: is any metric getting worse over time?
 - Statistical significance: use bootstrap confidence intervals to determine if disparities are significant

3. Alerting:
 - Demographic parity disparity > {{dp_alert_threshold}}: Slack alert to model owner and legal/compliance team
 - Equal opportunity disparity > {{eo_alert_threshold}}: same alert
 - Fairness degradation trend: if any metric worsens for 3 consecutive weeks: escalate

4. Fairness-performance tradeoff:
 - Document the explicit tradeoff between overall performance and fairness
 - If improving fairness requires accepting a performance hit: this is a product and legal decision, not just a technical one

5. Regulatory context:
 - Flag which regulations apply to this model (ECOA, FCRA, EU AI Act, GDPR)
 - Document compliance status per regulation

Return: fairness metrics implementation, monitoring pipeline, alerting configuration, and regulatory compliance checklist. Copy prompt View page Show more ↓ Model Governance and Compliance Advanced Chain 02 
### ML Audit Trail Chain 
Step 1: Define audit requirements — identify the regulatory and business requirements driving the need for an ML audit trail. What questions must the audit trail be able to answer? (e.g. 'Which model version made this prediction on this date?' 'What data was this model trained on?' 'Who approved this model for production?')
Step 2: Prediction-level traceability — ensure every production prediction is logged with: request_id, model_version, model_artifact_hash, feature_values, prediction, timestamp, serving_node. Verify the prediction log is immutable and tamper-proof.
Step 3: Model lineage — for every model version in the registry, record: training dataset version and hash, git commit of training code, hyperparameters, evaluation metrics, training job ID, and who triggered the training run.
Step 4: Deployment audit log — record every stage transition in the model registry: from stage, to stage, performed by, timestamp, reason, and approval reference. This log must be immutable.
Step 5: Data lineage — trace the training data back to its source systems. Document: which source tables were used, which date ranges, what transformations were applied, and whether any data was excluded and why.
Step 6: Access audit — log every access to the model registry, prediction logs, and training data: who accessed what, when, and from where. Alert on unusual access patterns.
Step 7: Audit report generation — implement an automated audit report generator that, given a request_id, produces a complete audit trail: source data → training data → model training → model approval → deployment → prediction. This report should be producible within 1 hour for regulatory or legal inquiries. Copy prompt View page Show more ↓ Model Governance and Compliance Beginner Prompt 03 
### Model Card Writer 
Write a comprehensive model card for this production ML model.

Model cards are documentation artifacts that describe a model's intended use, performance characteristics, limitations, and ethical considerations.

Model: {{model_name}}
Owner: {{owner_team}}

1. Model overview:
 - Model name and version
 - Model type: {{model_type}} (e.g. gradient boosted classifier)
 - Purpose: what task does this model solve? One paragraph.
 - Intended users: who uses this model and in what context?
 - Out-of-scope uses: what should this model NOT be used for?

2. Training data:
 - Data sources: where did the training data come from?
 - Time range: what period does the training data cover?
 - Dataset size: number of examples and features
 - Known biases or limitations in the training data
 - Data preprocessing and feature engineering summary

3. Performance:
 - Primary metric and its value on the test set
 - All secondary metrics
 - Performance broken down by key subgroups (age, region, device, etc.)
 - Performance comparison to baseline
 - Confidence: how reliable are these estimates?

4. Limitations and risks:
 - Known failure modes: when does this model perform poorly?
 - Distribution shift sensitivity: how sensitive is performance to input changes?
 - Uncertainty: what does the model not know it does not know?
 - Potential for harm: could this model produce unfair or harmful outcomes for any group?

5. Ethical considerations:
 - Fairness assessment: performance disparity across demographic groups
 - Privacy: does the model encode or memorize sensitive information?
 - Explainability: can individual predictions be explained?

6. Operations:
 - Model version and registry location
 - Serving infrastructure
 - Monitoring in place
 - Retraining frequency and trigger conditions
 - Owner and escalation path

Return: complete model card document in Markdown format. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
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
