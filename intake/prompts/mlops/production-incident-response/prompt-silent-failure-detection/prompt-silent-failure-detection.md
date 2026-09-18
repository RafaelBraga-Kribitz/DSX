# Silent Failure Detection *AI Prompt *

This prompt designs detection for silent model failures where infrastructure metrics look healthy but prediction quality has collapsed or become unreliable. It is especially useful for catching subtle but high-impact failures that standard uptime dashboards miss. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: business metric correlation monitor, feature sanity check implementation, domain rule violation tracker, and canary evaluation system. 
```

## When to use this prompt 
Use case 01 
when a model may be failing even though latency and error rate look normal 
Use case 02 
when upstream feature bugs can silently corrupt prediction quality 
Use case 03 
when domain rules or canary cases should validate prediction sanity 
Use case 04 
when business metrics may reveal problems before model metrics do 

## What the AI should return 

A silent-failure detection system including business-outcome correlation checks, feature sanity rules, canary evaluations, and manual audit procedures. 

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

Once you have the first result, continue deeper with related prompts in Production Incident Response.
