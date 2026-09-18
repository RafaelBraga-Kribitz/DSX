# Canary Deployment *AI Prompt *

This prompt implements a canary rollout strategy for new model versions using staged traffic shifts, automated health checks, and rollback conditions. It is useful when production deployment risk must be reduced while still collecting live evidence about a challenger model. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: traffic routing implementation, health check automation, progressive rollout logic, and canary analysis report generator. 
```

## When to use this prompt 
Use case 01 
when rolling out a new model gradually is safer than a full switch 
Use case 02 
when champion and challenger health must be compared at each traffic stage 
Use case 03 
when rollout progression should be automatic but overrideable 
Use case 04 
when you need routing logic plus stage-by-stage analysis reports 

## What the AI should return 

A canary deployment framework with traffic routing, staged progression, health checks, rollback logic, and canary analysis reporting. 

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

Once you have the first result, continue deeper with related prompts in CI/CD for ML.
