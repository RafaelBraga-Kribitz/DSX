# MLOps and CI/CD *AI Prompts *

7 ML Engineer prompts in MLOps and CI/CD. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 6 single prompts · 1 chain. 

## AI prompts in MLOps and CI/CD 
7 prompts Intermediate Single prompt 01 
### Automated Retraining Trigger 

This prompt designs an automated retraining system driven by monitored signals such as accuracy degradation, drift, new data volume, or time-based schedules. It focuses on reliable trigger detection, retraining execution, and safe promotion gates. 
Prompt text Design an automated model retraining system that triggers based on monitored signals.

1. Retraining trigger conditions (any one is sufficient):
 - Performance degradation: model accuracy on recent data drops below {{performance_threshold}}
 - Data drift: PSI > 0.2 for any top-10 feature by importance
 - Prediction drift: KS test p-value < 0.05 on prediction distribution vs baseline
 - Scheduled: time-based trigger every {{retrain_schedule}} (e.g. weekly, monthly)
 - New data volume: {{new_data_threshold}} new labeled samples available since last training

2. Trigger detection pipeline:
 - Run drift checks daily as a scheduled job
 - Log trigger signals to a monitoring database
 - When a trigger fires: log which signal, the metric value, and the threshold exceeded

3. Retraining execution:
 - Submit training job to compute cluster (Kubernetes Job, Airflow DAG, or SageMaker Pipeline)
 - Use the latest full dataset (not just new data) with a sliding window if dataset grows unbounded
 - Run with the same config as the current production model to enable fair comparison

4. Model promotion gate:
 - New model must beat current production model on a fixed evaluation set by > {{min_improvement}}%
 - If gate passes: automatically promote to staging, trigger deployment pipeline
 - If gate fails: alert the ML team, do not auto-promote

5. Human-in-the-loop option:
 - For high-stakes models: require human approval before any promotion, even if gate passes

Return: drift detection script, trigger condition implementation, retraining job submission code, and promotion gate logic. Copy prompt Open prompt details Intermediate Single prompt 02 
### CI/CD for ML Pipeline 

This prompt designs a GitHub Actions-based CI/CD workflow for an ML project, from fast PR checks to post-merge validation and deployment gates. It is aimed at preventing broken training code, silent leakage, poor model quality, and unsafe releases. 
Prompt text Design and implement a CI/CD pipeline for this ML project using GitHub Actions.

1. On every pull request — fast checks (< 5 minutes):
 - Code quality: ruff lint, black format check, mypy type checking
 - Unit tests: test data preprocessing, loss functions, metrics, and model architecture
 - Smoke test: train for 2 epochs on 100 samples, assert loss decreases and model saves
 - No data leakage check: run automated leakage detection tests

2. On merge to main — extended checks (< 30 minutes):
 - Integration test: full training run on a small held-out dataset
 - Model performance gate: assert validation metric > {{min_metric_threshold}}
 - Inference test: run the exported model through the serving stack
 - Benchmark: run throughput/latency benchmark and compare to baseline

3. On new model registration — deployment checks:
 - Champion vs challenger comparison on fixed holdout set
 - Deploy to staging if challenger beats champion by > {{improvement_threshold}}%
 - Run smoke test in staging environment
 - Manual approval gate before production deployment

4. GitHub Actions workflow structure:
 - Separate workflow files for each stage
 - Cache: pip dependencies, pre-downloaded datasets for tests
 - Secrets: model registry credentials, cloud storage keys via GitHub Secrets

5. Failure handling:
 - Notify Slack channel on pipeline failure with the failing step and logs link
 - Auto-revert deployment if post-deployment canary metrics degrade

Return: GitHub Actions YAML files for each pipeline stage and a workflow diagram. Copy prompt Open prompt details Advanced Single prompt 03 
### Data Versioning with DVC 

This prompt introduces DVC-based data versioning and pipeline tracking for an ML project. It covers remote storage, tracked datasets, stage definitions, experiments, metrics, and CI integration so data and pipeline state remain reproducible over time. 
Prompt text Set up data versioning and pipeline tracking for this ML project using DVC.

1. DVC initialization:
 - dvc init in the Git repository
 - Configure remote storage: S3, GCS, or Azure Blob
 - .dvcignore file for files to exclude

2. Data versioning:
 - Track large data files and directories: dvc add data/raw/
 - Commit .dvc files to Git, push data to remote: dvc push
 - Retrieve a specific data version: git checkout {commit} && dvc pull
 - List data versions and their Git commits for audit trail

3. DVC pipeline definition (dvc.yaml):
 - Define pipeline stages: preprocess → train → evaluate
 - For each stage: deps (inputs), outs (outputs), params (config values), metrics (metrics.json)
 - Cache: DVC caches stage outputs — skips re-running unchanged stages
 - Run the pipeline: dvc repro

4. Experiment tracking:
 - dvc exp run for tracking experiments with different params
 - dvc exp show to compare experiments in a table
 - dvc exp branch to create a Git branch from a promising experiment

5. Metrics and params tracking:
 - Save metrics as JSON: accuracy, loss, etc.
 - dvc metrics show, dvc metrics diff to compare across commits
 - dvc params diff to see which params changed between runs

6. CI/CD integration:
 - dvc pull in CI before running tests
 - dvc repro in CI to re-run the pipeline if deps changed
 - dvc push in CI to save new data artifacts after processing

Return: dvc.yaml pipeline definition, Git workflow for data versioning, and CI/CD integration. Copy prompt Open prompt details Advanced Chain 04 
### MLOps Platform Chain 

This chain designs an MLOps platform from current-state assessment through tool selection, lifecycle definition, golden-path implementation, runbooks, and success metrics. It is intended for teams building shared ML infrastructure rather than solving only one project. 
Prompt text Step 1: Assess current state — inventory existing tools for: experiment tracking, model registry, data versioning, serving, and monitoring. Identify the biggest gaps causing friction for the ML team.
Step 2: Define the platform requirements — number of ML engineers, models in production, deployment frequency, latency requirements, on-prem vs cloud. These drive the tool selection.
Step 3: Design the stack — select and justify tools for each layer: orchestration (Airflow/Kubeflow/Prefect), experiment tracking (MLflow/W&B), model registry (MLflow/SageMaker), serving (TorchServe/Triton/BentoML), monitoring (Evidently/WhyLabs).
Step 4: Define the ML lifecycle workflow — document the exact steps from idea to production: experiment → training run → model registration → evaluation → staging → production → monitoring → retraining trigger.
Step 5: Implement the golden path — build a template project that uses all platform components. An engineer starting a new project should be able to use this template and have full MLOps support from day one.
Step 6: Write the runbook — document how to: deploy a new model, roll back a model, investigate a prediction incident, and trigger retraining. Each runbook should be executable by an on-call engineer without ML expertise.
Step 7: Define success metrics for the platform: deployment frequency, time-from-experiment-to-production, MTTR (mean time to recover from a model incident), and % of models with active drift monitoring. Copy prompt Open prompt details Advanced Single prompt 05 
### Model Incident Response 

This prompt creates a production model incident response playbook with severity levels, alerting chains, triage steps, rollback criteria, and post-mortem structure. It is designed to help teams respond quickly and consistently when a deployed model misbehaves. 
Prompt text Write a model incident response playbook for production ML systems.

1. Incident classification:
 - P0 (Critical): model returning errors for >5% of requests, or predictions are completely wrong (e.g. all same class)
 - P1 (High): model latency > 2× SLA, silent accuracy degradation detected, feature drift alarm
 - P2 (Medium): single-segment performance degradation, prediction distribution shift detected
 - P3 (Low): data freshness lag, minor accuracy regression within acceptable bounds

2. Detection and alerting:
 - Define the monitoring signals that trigger each severity level
 - Alerting chain: PagerDuty → on-call ML engineer → ML team lead → CTO (for P0 only)
 - Initial acknowledgment SLA: P0=5 min, P1=15 min, P2=1 hour, P3=next business day

3. Immediate triage checklist (first 15 minutes for P0/P1):
 - Is this a model issue or an infrastructure issue? (Check serving logs, Kubernetes pod status)
 - Did a deployment happen recently? (Check deployment log)
 - Is the input data correct? (Check feature store freshness, pipeline health)
 - Is the error rate growing or stable?

4. Rollback procedure:
 - Trigger: error rate > 5% AND confirmed model issue
 - Steps: promote previous Production model version in registry → trigger rolling restart → verify error rate drops
 - Target: rollback complete within 10 minutes of decision to rollback

5. Post-incident review:
 - Timeline of events
 - Root cause analysis
 - Customer or business impact
 - What monitoring would have detected this earlier?
 - Action items with owners and deadlines

Return: complete incident response playbook with classification matrix, triage checklist, rollback procedure, and post-mortem template. Copy prompt Open prompt details Intermediate Single prompt 06 
### Model Monitoring Setup 

This prompt sets up production model monitoring across service metrics, prediction logging, drift checks, confidence shifts, and delayed ground-truth evaluation. It is intended for teams that need ongoing visibility into both operational health and model quality after deployment. 
Prompt text Set up a comprehensive production model monitoring system.

1. Prediction logging:
 - Log every prediction to a structured store: timestamp, request_id, model_version, input_features, prediction, confidence, latency_ms
 - Use async logging to avoid adding latency to the serving path
 - Rotate logs daily and archive to object storage after 7 days

2. Service-level monitoring (Prometheus + Grafana):
 - Metrics to track: requests/sec, error rate (4xx, 5xx), p50/p95/p99 latency, queue depth
 - Alerts: error rate > 1%, p99 latency > {{latency_sla_ms}}, model load failure
 - Dashboard: request volume, latency percentiles, error rate, model version deployed

3. Model-level monitoring:
 - Prediction distribution: compare daily prediction distribution to training distribution (PSI)
 - Confidence distribution: alert if mean confidence drops significantly (model is uncertain)
 - Output drift: KS test on prediction scores between current week vs baseline week

4. Feature/data drift monitoring:
 - For each of the top 10 features: compute PSI weekly
 - PSI < 0.1: no significant change
 - PSI 0.1–0.2: moderate drift, investigate
 - PSI > 0.2: significant drift, trigger retraining evaluation

5. Ground truth feedback loop:
 - If labels become available with a delay (e.g. churn labels available after 30 days): join predictions to outcomes and compute actual model accuracy over time
 - Alert if rolling 30-day accuracy drops below {{accuracy_threshold}}

Return: prediction logging implementation, Prometheus metrics setup, drift monitoring scripts, and Grafana dashboard spec. Copy prompt Open prompt details Beginner Single prompt 07 
### Training Pipeline as Code 

This prompt refactors an ad-hoc training script into a reproducible pipeline with configuration management, stage separation, artifact versioning, and a CLI. It is useful when a one-off training file has grown into something that needs repeatable execution and maintenance. 
Prompt text Refactor this ad-hoc training script into a reproducible, configurable ML pipeline.

1. Configuration management:
 - Move all hyperparameters and paths to a config file (YAML or JSON)
 - Use OmegaConf or Hydra for hierarchical config with command-line overrides
 - Never hardcode paths — all paths are config variables with sensible defaults
 - Log the full resolved config at the start of every run

2. Pipeline stages as separate functions or classes:
 - data_preprocessing(): validate, clean, and split data
 - train(): train model with given config
 - evaluate(): evaluate on test set and return metrics dict
 - export(): save model in deployment format
 - Each stage is independently runnable and testable

3. Artifact management:
 - Every run saves to a versioned output directory: outputs/{run_id}/
 - Artifacts: model checkpoint, config copy, metrics JSON, training plots
 - Symlink outputs/latest → most recent run for convenience

4. CLI interface:
 - python train.py --config configs/base.yaml --overrides learning_rate=1e-4
 - Subcommands: train, evaluate, export, full (all stages)

5. Dependency management:
 - requirements.txt with pinned versions
 - Optional: pyproject.toml with extras for training vs inference

6. Entry point guard:
 - All DataLoader workers require if __name__ == '__main__': guard on Windows

Return: refactored pipeline structure, Hydra config setup, and CLI interface. Copy prompt Open prompt details 
## Recommended MLOps and CI/CD workflow 
1 
### Automated Retraining Trigger 

Start with a focused prompt in MLOps and CI/CD so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### CI/CD for ML Pipeline 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Data Versioning with DVC 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### MLOps Platform Chain 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
