# Ground Truth Feedback Loop *AI Prompt *

This prompt creates a delayed-label feedback loop that joins production predictions to later-arriving ground truth so real performance can be measured over time. It is useful for churn, fraud, risk, and similar use cases where labels are not immediately available. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: prediction storage schema, label join pipeline, performance tracking queries, and retraining trigger logic. 
```

## When to use this prompt 
Use case 01 
when production labels arrive days or weeks after prediction 
Use case 02 
when you need ongoing real-world performance tracking by model version 
Use case 03 
when building retraining triggers from labeled production outcomes 
Use case 04 
when prediction storage, label joins, and rolling metrics must work together 

## What the AI should return 

A feedback loop design including prediction storage schema, delayed-label ingestion, join logic, rolling performance tracking, and retraining trigger rules. 

## How to use this prompt 
1 
### Open your data context 

Load your dataset, notebook, or working environment so the AI can operate on the actual project context. 
2 
### Copy the prompt text 

Use the copy button above and paste the prompt into the AI assistant or prompt input area. 
3 
### Review the output critically 

Check whether the result matches your data, assumptions, and desired format before moving on. 
4 
### Chain into the next prompt 

Once you have the first result, continue deeper with related prompts in Model Monitoring.
