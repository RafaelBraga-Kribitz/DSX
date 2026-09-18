# ML Pipeline Integration Tests *AI Prompt *

This prompt writes integration tests that exercise the full ML workflow across feature generation, training, registry loading, serving, and rollback. It is useful when unit tests exist but system-level confidence is still missing before deployment. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: complete integration test suite, test data fixtures, CI/CD configuration to run tests on every PR and deployment. 
```

## When to use this prompt 
Use case 01 
when end-to-end ML workflows need automated validation 
Use case 02 
when feature pipelines and model input contracts must be tested together 
Use case 03 
when serving behavior should be checked through the real HTTP path 
Use case 04 
when rollback procedures also need integration coverage 

## What the AI should return 

A complete ML integration test suite with fixtures, end-to-end assertions, and CI/CD configuration. 

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
