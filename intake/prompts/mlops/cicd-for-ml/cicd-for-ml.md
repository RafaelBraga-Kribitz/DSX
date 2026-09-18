# CI/CD for ML *AI Prompts *

8 MLOps prompts in CI/CD for ML. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 7 single prompts · 1 chain. 

## AI prompts in CI/CD for ML 
8 prompts Intermediate Single prompt 01 
### Automated Retraining Pipeline 

This prompt builds an automated retraining pipeline that responds to monitoring triggers such as drift, performance decline, new labeled data, or schedules. It is intended for teams that want retraining to be systematic, rate-limited, and connected to model registry and deployment gates. 
Prompt text Build an automated model retraining pipeline triggered by monitoring signals.

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

Return: trigger detection script, pipeline orchestration code (Airflow DAG or Prefect flow), and gate integration. Copy prompt Open prompt details Intermediate Single prompt 02 
### Canary Deployment 

This prompt implements a canary rollout strategy for new model versions using staged traffic shifts, automated health checks, and rollback conditions. It is useful when production deployment risk must be reduced while still collecting live evidence about a challenger model. 
Prompt text Implement a canary deployment strategy for safely rolling out a new model version.

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

Return: traffic routing implementation, health check automation, progressive rollout logic, and canary analysis report generator. Copy prompt Open prompt details Advanced Chain 03 
### CI/CD Pipeline Design Chain 

This chain prompt designs the overall CI/CD architecture for an ML system, covering fast CI, extended checks, deployment automation, retraining, rollback, and documentation. It is useful when the goal is to define the full delivery lifecycle rather than a single pipeline job. 
Prompt text Step 1: Test inventory — catalog all existing tests (unit, integration, smoke). Identify untested code paths in the preprocessing, feature engineering, training, and serving layers. Prioritize which gaps to fill first based on risk.
Step 2: CI pipeline (on every PR) — define the fast CI pipeline: linting, type checking, unit tests, smoke training test, serving health check. Target: completes in < 10 minutes. Block merge on any failure.
Step 3: Extended CI (on merge to main) — define the extended pipeline: full integration tests, performance gate against holdout set, training-serving skew check, latency benchmark. Target: completes in < 30 minutes.
Step 4: CD pipeline (on model registry promotion) — define the deployment pipeline: staging deploy, integration tests in staging, canary deployment to production (1% → 5% → 20% → 100%), automated rollback on health check failure.
Step 5: Retraining pipeline — design the automated retraining trigger, training job, evaluation gate, and staging promotion. Define the human-in-the-loop gates for high-stakes models.
Step 6: Rollback procedure — document and automate the rollback: config repo revert, GitOps reconciliation, verification that the previous model is serving. Target: rollback executable by any on-call engineer in < 5 minutes.
Step 7: Pipeline documentation — write the CI/CD runbook: what each pipeline stage does, how to debug a failing stage, how to manually trigger or skip a stage, and who to escalate to when the pipeline is broken. Copy prompt Open prompt details Advanced Single prompt 04 
### ML GitOps Workflow 

This prompt designs a GitOps deployment workflow for ML systems where Git declares the desired production state and rollbacks happen through version-controlled changes. It is useful for teams standardizing deployment governance and auditability in Kubernetes environments. 
Prompt text Design a GitOps workflow for managing ML model deployments where Git is the single source of truth.

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

Return: repository structure, GitOps operator configuration (ArgoCD or Flux), PR workflow definition, and rollback procedure. Copy prompt Open prompt details Intermediate Single prompt 05 
### ML Pipeline Integration Tests 

This prompt writes integration tests that exercise the full ML workflow across feature generation, training, registry loading, serving, and rollback. It is useful when unit tests exist but system-level confidence is still missing before deployment. 
Prompt text Write integration tests for the end-to-end ML pipeline from feature ingestion to model serving.

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

Return: complete integration test suite, test data fixtures, CI/CD configuration to run tests on every PR and deployment. Copy prompt Open prompt details Beginner Single prompt 06 
### ML Unit Testing 

This prompt writes a comprehensive unit test suite for ML code, covering preprocessing, feature engineering, models, losses, metrics, and smoke tests. It is best for improving code reliability in projects where data and training logic are more complex than standard application code. 
Prompt text Write a comprehensive unit test suite for this ML codebase.

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

Return: test suite covering all categories, with fixtures for synthetic data and a pytest configuration. Copy prompt Open prompt details Beginner Single prompt 07 
### Model Performance Gate 

This prompt designs a deterministic model performance gate that decides whether a challenger can move forward based on holdout metrics, guardrails, fairness, and calibration. It is useful for reducing subjective promotion decisions in CI/CD workflows. 
Prompt text Implement a model performance gate that automatically approves or blocks model promotion based on predefined quality criteria.

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

Return: gate evaluation code, gate criteria configuration (YAML), pass/fail report generator, and CI/CD integration. Copy prompt Open prompt details Intermediate Single prompt 08 
### Model Registry Workflow 

This prompt designs a full model registry workflow including registration metadata, stage transitions, approvals, serving-time loading, and audit reporting. It is useful when the registry is the backbone of model lifecycle management across training and production. 
Prompt text Design the complete model lifecycle workflow using a model registry.

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

Return: registration code, stage transition automation, approval workflow, and serving-side model loader with polling. Copy prompt Open prompt details 
## Recommended CI/CD for ML workflow 
1 
### Automated Retraining Pipeline 

Start with a focused prompt in CI/CD for ML so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Canary Deployment 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### CI/CD Pipeline Design Chain 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### ML GitOps Workflow 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
