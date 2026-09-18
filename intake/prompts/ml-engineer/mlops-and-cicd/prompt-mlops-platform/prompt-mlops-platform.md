# MLOps Platform Chain *AI Prompt *

This chain designs an MLOps platform from current-state assessment through tool selection, lifecycle definition, golden-path implementation, runbooks, and success metrics. It is intended for teams building shared ML infrastructure rather than solving only one project. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Assess current state — inventory existing tools for: experiment tracking, model registry, data versioning, serving, and monitoring. Identify the biggest gaps causing friction for the ML team.
Step 2: Define the platform requirements — number of ML engineers, models in production, deployment frequency, latency requirements, on-prem vs cloud. These drive the tool selection.
Step 3: Design the stack — select and justify tools for each layer: orchestration (Airflow/Kubeflow/Prefect), experiment tracking (MLflow/W&B), model registry (MLflow/SageMaker), serving (TorchServe/Triton/BentoML), monitoring (Evidently/WhyLabs).
Step 4: Define the ML lifecycle workflow — document the exact steps from idea to production: experiment → training run → model registration → evaluation → staging → production → monitoring → retraining trigger.
Step 5: Implement the golden path — build a template project that uses all platform components. An engineer starting a new project should be able to use this template and have full MLOps support from day one.
Step 6: Write the runbook — document how to: deploy a new model, roll back a model, investigate a prediction incident, and trigger retraining. Each runbook should be executable by an on-call engineer without ML expertise.
Step 7: Define success metrics for the platform: deployment frequency, time-from-experiment-to-production, MTTR (mean time to recover from a model incident), and % of models with active drift monitoring. 
```

## When to use this prompt 
Use case 01 
when an organization needs a coherent MLOps platform strategy 
Use case 02 
when selecting tools for experimentation, registry, serving, and monitoring 
Use case 03 
when creating a standardized project template for ML teams 
Use case 04 
when platform success should be measured by deployment speed, recovery, and coverage 

## What the AI should return 

An MLOps platform blueprint covering tool choices, lifecycle workflow, a golden-path project template, runbooks, and platform success metrics. 

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

Once you have the first result, continue deeper with related prompts in MLOps and CI/CD.
