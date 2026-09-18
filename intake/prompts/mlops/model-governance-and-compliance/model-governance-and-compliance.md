# Model Governance and Compliance *AI Prompts *

3 MLOps prompts in Model Governance and Compliance. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 2 single prompts · 1 chain. 

## AI prompts in Model Governance and Compliance 
3 prompts Intermediate Single prompt 01 
### Fairness Monitoring 

This prompt implements production fairness monitoring with disparity metrics, trend tracking, significance testing, alerting, and regulatory context. It is useful when fairness must be treated as an ongoing operational responsibility rather than a one-time evaluation. 
Prompt text Implement ongoing fairness monitoring for this production model.

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

Return: fairness metrics implementation, monitoring pipeline, alerting configuration, and regulatory compliance checklist. Copy prompt Open prompt details Advanced Chain 02 
### ML Audit Trail Chain 

This chain prompt designs an ML audit trail spanning prediction logging, model lineage, deployment records, data lineage, access logs, and automated report generation. It is useful in regulated or high-accountability settings where every production prediction must be explainable and traceable. 
Prompt text Step 1: Define audit requirements — identify the regulatory and business requirements driving the need for an ML audit trail. What questions must the audit trail be able to answer? (e.g. 'Which model version made this prediction on this date?' 'What data was this model trained on?' 'Who approved this model for production?')
Step 2: Prediction-level traceability — ensure every production prediction is logged with: request_id, model_version, model_artifact_hash, feature_values, prediction, timestamp, serving_node. Verify the prediction log is immutable and tamper-proof.
Step 3: Model lineage — for every model version in the registry, record: training dataset version and hash, git commit of training code, hyperparameters, evaluation metrics, training job ID, and who triggered the training run.
Step 4: Deployment audit log — record every stage transition in the model registry: from stage, to stage, performed by, timestamp, reason, and approval reference. This log must be immutable.
Step 5: Data lineage — trace the training data back to its source systems. Document: which source tables were used, which date ranges, what transformations were applied, and whether any data was excluded and why.
Step 6: Access audit — log every access to the model registry, prediction logs, and training data: who accessed what, when, and from where. Alert on unusual access patterns.
Step 7: Audit report generation — implement an automated audit report generator that, given a request_id, produces a complete audit trail: source data → training data → model training → model approval → deployment → prediction. This report should be producible within 1 hour for regulatory or legal inquiries. Copy prompt Open prompt details Beginner Single prompt 03 
### Model Card Writer 

This prompt writes a model card that documents intended use, training data, performance, limitations, risks, and operational context. It is useful for internal governance, stakeholder communication, and responsible model release practices. 
Prompt text Write a comprehensive model card for this production ML model.

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

Return: complete model card document in Markdown format. Copy prompt Open prompt details 
## Recommended Model Governance and Compliance workflow 
1 
### Fairness Monitoring 

Start with a focused prompt in Model Governance and Compliance so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### ML Audit Trail Chain 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Model Card Writer 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
