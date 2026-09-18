# ML Audit Trail Chain *AI Prompt *

This chain prompt designs an ML audit trail spanning prediction logging, model lineage, deployment records, data lineage, access logs, and automated report generation. It is useful in regulated or high-accountability settings where every production prediction must be explainable and traceable. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Define audit requirements — identify the regulatory and business requirements driving the need for an ML audit trail. What questions must the audit trail be able to answer? (e.g. 'Which model version made this prediction on this date?' 'What data was this model trained on?' 'Who approved this model for production?')
Step 2: Prediction-level traceability — ensure every production prediction is logged with: request_id, model_version, model_artifact_hash, feature_values, prediction, timestamp, serving_node. Verify the prediction log is immutable and tamper-proof.
Step 3: Model lineage — for every model version in the registry, record: training dataset version and hash, git commit of training code, hyperparameters, evaluation metrics, training job ID, and who triggered the training run.
Step 4: Deployment audit log — record every stage transition in the model registry: from stage, to stage, performed by, timestamp, reason, and approval reference. This log must be immutable.
Step 5: Data lineage — trace the training data back to its source systems. Document: which source tables were used, which date ranges, what transformations were applied, and whether any data was excluded and why.
Step 6: Access audit — log every access to the model registry, prediction logs, and training data: who accessed what, when, and from where. Alert on unusual access patterns.
Step 7: Audit report generation — implement an automated audit report generator that, given a request_id, produces a complete audit trail: source data → training data → model training → model approval → deployment → prediction. This report should be producible within 1 hour for regulatory or legal inquiries. 
```

## When to use this prompt 
Use case 01 
when regulatory, legal, or enterprise auditability is required for ML systems 
Use case 02 
when prediction-level traceability must connect back to data and code lineage 
Use case 03 
when deployment approvals and access patterns need immutable records 
Use case 04 
when an audit report must be generated quickly from a request or prediction ID 

## What the AI should return 

An end-to-end ML audit trail design covering prediction traceability, model and data lineage, deployment audit logs, access logging, and report generation. 

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

Once you have the first result, continue deeper with related prompts in Model Governance and Compliance.
