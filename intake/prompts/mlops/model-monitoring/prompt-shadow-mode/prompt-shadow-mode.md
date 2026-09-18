# Shadow Mode Evaluation *AI Prompt *

This prompt sets up shadow mode so a challenger model can be evaluated in production without affecting user-facing responses. It is most useful when validating a new model safely before canary or full rollout. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: shadow mode routing implementation, comparison analysis script, and promotion decision criteria. 
```

## When to use this prompt 
Use case 01 
when you want to compare champion and challenger models in live traffic 
Use case 02 
when challenger inference must not block or affect the user response 
Use case 03 
when you need daily comparison analysis for shadow predictions 
Use case 04 
when promotion criteria should be based on production-like evidence without exposure 

## What the AI should return 

A shadow mode design including asynchronous request duplication, paired prediction logging, comparison analytics, and promotion criteria. 

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
