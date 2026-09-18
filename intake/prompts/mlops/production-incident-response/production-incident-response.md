# Production Incident Response *AI Prompts *

6 MLOps prompts in Production Incident Response. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 5 single prompts · 1 chain. 

## AI prompts in Production Incident Response 
6 prompts Intermediate Single prompt 01 
### Emergency Rollback Procedure 

This prompt designs fast rollback options for model registry, Kubernetes deployments, and traffic-routing based releases, along with verification and drills. It is best when production rollback must be reliable, fast, and executable under pressure. 
Prompt text Design and implement a fast, reliable emergency rollback procedure for production ML models.

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

Return: rollback scripts for all three options, verification checklist, post-rollback action template, and drill procedure. Copy prompt Open prompt details Beginner Single prompt 02 
### Incident Classification Matrix 

This prompt defines severity levels, SLAs, declaration rules, and communication templates for ML production incidents. It is helpful when teams need a shared language for incident response before building detailed runbooks. 
Prompt text Define an ML model incident classification matrix and response procedures for each severity level.

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

Return: classification matrix table, SLA definitions, alert-to-incident mapping, and communication templates. Copy prompt Open prompt details Intermediate Single prompt 03 
### Incident Post-Mortem 

This prompt writes a blameless post-mortem for an ML incident, focusing on timeline, causes, impact, lessons, and tracked action items. It is useful for organizations that want learning-oriented incident reviews rather than one-off summaries. 
Prompt text Write a blameless post-mortem for this ML model incident.

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

Return: complete blameless post-mortem document. Copy prompt Open prompt details Advanced Chain 04 
### Incident Response Chain 

This chain prompt walks through the full lifecycle of incident response from detection and triage to mitigation, root-cause analysis, recovery verification, and post-mortem. It is useful as a guided template during live incidents and for training responders. 
Prompt text Step 1: Detection — describe the detection mechanism that triggered this incident. Was it an automated alert, a user report, or proactive monitoring? Note the detection time and any delay between incident start and detection.
Step 2: Triage — work through the triage runbook. Is this a model issue, an infrastructure issue, or a data pipeline issue? What is the initial severity classification (P0/P1/P2/P3)?
Step 3: Immediate mitigation — what can be done in the next 15 minutes to reduce user impact? Options: rollback to previous model, route traffic to a fallback, disable the feature using this model, apply a threshold adjustment.
Step 4: Root cause investigation — with the immediate mitigation in place, investigate the root cause. Use the diagnostic tools: serving logs, feature pipeline logs, model performance metrics, drift dashboard. Apply Five Whys.
Step 5: Permanent fix — design and implement the fix for the root cause. This may take hours or days. It must be tested in staging before re-deployment to production.
Step 6: Recovery and verification — re-deploy the fixed model. Monitor closely for 24 hours: serving metrics, prediction distribution, business metrics. Confirm full recovery.
Step 7: Post-mortem — within 48 hours, write and publish the blameless post-mortem. All action items entered into tracking. Schedule a follow-up review in 2 weeks to verify action items are being completed. Copy prompt Open prompt details Advanced Single prompt 05 
### Silent Failure Detection 

This prompt designs detection for silent model failures where infrastructure metrics look healthy but prediction quality has collapsed or become unreliable. It is especially useful for catching subtle but high-impact failures that standard uptime dashboards miss. 
Prompt text Design a system to detect silent model failures — cases where the model is technically healthy (no errors, normal latency) but is producing systematically wrong predictions.

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

Return: business metric correlation monitor, feature sanity check implementation, domain rule violation tracker, and canary evaluation system. Copy prompt Open prompt details Intermediate Single prompt 06 
### Triage Runbook 

This prompt writes a practical triage runbook that any on-call engineer can execute quickly, even without deep model context. It is useful for turning incident response from tribal knowledge into a repeatable first-response procedure. 
Prompt text Write a model incident triage runbook for on-call engineers who may not be deeply familiar with the specific model.

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

Return: complete triage runbook formatted as a step-by-step guide. Copy prompt Open prompt details 
## Recommended Production Incident Response workflow 
1 
### Emergency Rollback Procedure 

Start with a focused prompt in Production Incident Response so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Incident Classification Matrix 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Incident Post-Mortem 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Incident Response Chain 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
