# Multivariate Drift Detection *AI Prompt *

This prompt detects multivariate drift using classifier-based methods, MMD, and PCA-based monitoring so that joint-distribution changes are not missed. It is especially useful when univariate checks show stability but production behavior still looks suspicious. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement multivariate drift detection to catch drift patterns that are invisible in individual feature monitors.

Limitation of univariate drift detection: features A and B may individually look stable, but their joint distribution has shifted — a pattern that only multivariate detection catches.

1. Classifier-based drift detection (the most powerful general method):
 - Train a binary classifier to distinguish between reference data (label=0) and current data (label=1)
 - If the classifier achieves AUC significantly above 0.5, the distributions are distinguishable → drift detected
 - Use a lightweight classifier: LightGBM or Logistic Regression for speed
 - AUC interpretation:
 - AUC ≈ 0.5: no detectable drift
 - AUC 0.5–0.6: slight drift — monitor
 - AUC 0.6–0.7: moderate drift — investigate
 - AUC > 0.7: significant drift — alert
 - Bonus: the classifier's feature importances tell you WHICH features drive the drift

2. MMD (Maximum Mean Discrepancy):
 - Non-parametric test based on kernel embeddings
 - Works well for high-dimensional data
 - Use a Gaussian RBF kernel: MMD² = E[k(X,X')] - 2E[k(X,Y)] + E[k(Y,Y')]
 - Significance test: permutation test (shuffle reference/current labels and recompute MMD 1000 times)

3. PCA-based drift:
 - Fit PCA on the reference data (retain components explaining 95% of variance)
 - Project current data onto the reference PCA space
 - Monitor drift in the top 3–5 principal components using KS test
 - Advantage: reduces dimensionality, makes drift easier to visualize

4. When to use each method:
 - < 50 features: classifier-based (best explanability)
 - 50–500 features: PCA → KS test (scalable)
 - > 500 features or embeddings: MMD (handles high-dimensional spaces)

Return: classifier-based drift detector, MMD implementation, PCA-based drift, and a comparison of the three methods on synthetic drift scenarios. 
```

## When to use this prompt 
Use case 01 
when univariate drift monitors are not sufficient 
Use case 02 
when feature interactions may be shifting even if individual marginals look stable 
Use case 03 
when you need a more sensitive drift detector for higher-dimensional data 
Use case 04 
when comparing multivariate drift approaches on the same problem 

## What the AI should return 

A multivariate drift detection toolkit with classifier-based detection, MMD, PCA-based monitoring, and guidance on when to use each method. 

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
