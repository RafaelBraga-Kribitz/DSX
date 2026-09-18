# Training-Serving Skew Detection *AI Prompt *

This prompt detects training-serving skew, which is a deployment bug caused by inconsistent preprocessing or feature logic rather than natural distribution drift. It is valuable for launch validation and for diagnosing surprising production failures after deployment. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Detect and diagnose training-serving skew — when the feature distributions at serving time differ from those at training time due to preprocessing inconsistencies.

Training-serving skew is distinct from drift. It is a bug, not a statistical phenomenon. It means the model is receiving different data at serving time than it was trained on, even when the underlying reality has not changed.

1. Common causes:
 - Different preprocessing code paths for training and serving
 - Feature computation at different points in time (training uses future data, serving uses only past)
 - Different handling of nulls (training fills with 0, serving fills with mean)
 - Different categorical encoding mappings stored in different places
 - Unit differences (training in km, serving in miles)
 - Different normalization parameters (training uses training set stats, serving uses different stats)

2. Detection method:
 - Log the exact feature vector received by the model at serving time
 - At regular intervals: take a sample of serving feature vectors and compare their distribution to the corresponding training feature vectors
 - Compare: mean, std, min, max, and null rate for every feature
 - Flag any feature where the serving distribution differs from training distribution AND this difference appeared at launch (not gradually — that would be drift, not skew)

3. Automated skew scan (run at every new model deployment):
 - Deploy model in shadow mode for 24 hours
 - Compare shadow period feature distributions to training feature distributions
 - Block promotion to production if any feature has PSI > 0.1 at deployment time

4. Prevention:
 - Use a shared feature transformation library for both training and serving
 - Store fitted preprocessing artifacts (scalers, encoders, imputers) in the model artifact
 - Apply the same artifact at both training evaluation and serving
 - Integration test: run the serving preprocessing code on a training sample and compare outputs

Return: skew detection implementation, automated deployment scan, prevention checklist, and diagnosis guide. 
```

## When to use this prompt 
Use case 01 
when production features may not match training-time features 
Use case 02 
when you suspect a preprocessing mismatch between training and serving 
Use case 03 
when new deployments need an automated skew gate before promotion 
Use case 04 
when you need guidance on prevention as well as detection 

## What the AI should return 

A training-serving skew solution with comparison logic, deployment-time scans, prevention checklist, and diagnosis guidance. 

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

Once you have the first result, continue deeper with related prompts in Drift Detection.
