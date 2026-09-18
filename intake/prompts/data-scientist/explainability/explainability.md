# Explainability *AI Prompts *

8 Data Scientist prompts in Explainability. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 7 single prompts · 1 chain. 

## AI prompts in Explainability 
8 prompts Intermediate Single prompt 01 
### Counterfactual Explanations 

This prompt generates actionable counterfactual explanations for unfavorable model outcomes. It is useful in domains where people need to understand what realistic changes could improve their predicted outcome. The focus is on minimal, feasible, and user-actionable changes rather than impossible edits. 
Prompt text Generate counterfactual explanations for rejected or unfavorable predictions from this model.

A counterfactual answers the question: 'What is the minimal change to the input that would flip the prediction?'

For the top 10 most impactful negative predictions (e.g. loan rejected, churn predicted, fraud flagged):
1. Find the nearest counterfactual: the smallest change to input features that would result in a positive prediction
2. Constraints: only change features that are actionable (not age, not historical data — only things the person can change)
3. For each counterfactual show: original values | counterfactual values | what changed | magnitude of change
4. Rank the required changes from easiest to hardest to achieve
5. Generate a plain-English 'what you could do differently' explanation for each case

Return: counterfactual table for each case and template text suitable for a customer-facing explanation. Copy prompt Open prompt details Beginner Single prompt 02 
### Decision Tree Proxy 

This prompt builds a shallow decision tree that approximates a complex model for interpretability. It is useful when the real model is hard to explain but stakeholders still want simplified rules of thumb. The key idea is fidelity: the tree should mimic the complex model as well as possible while staying readable. 
Prompt text Build a simple decision tree that approximates the behavior of this complex model.

1. Generate predictions from the complex model on the full training set
2. Train a decision tree on those predictions (use model outputs as the new target)
3. Limit the tree depth to 4 levels maximum for interpretability
4. Tune: find the depth (1–6) that maximizes fidelity (agreement with the complex model) while staying interpretable
5. Visualize the decision tree using graphviz or a text representation
6. Extract the top 5 decision rules as plain-English if-then statements
7. Report fidelity: what percentage of predictions does the proxy tree agree with the complex model?

Note: this is a surrogate model, not the real model. Flag where the proxy disagrees most with the original. Copy prompt Open prompt details Beginner Single prompt 03 
### Feature Importance 

This prompt provides a straightforward explanation of what features matter most and whether different importance methods agree. It is a practical first step in explainability for models that support built-in importances or can be probed with permutation tests. It also helps identify candidates for feature pruning. 
Prompt text Explain which features matter most to this model.

1. Extract built-in feature importances from the model (gain, split count, or permutation importance)
2. Plot a horizontal bar chart of the top 20 features, ranked by importance
3. Compute permutation importance on the validation set as a cross-check — compare to built-in importances
4. Flag any features where built-in and permutation importances disagree significantly
5. Identify features with near-zero importance in both methods — candidates for removal
6. Group features by type (original vs engineered) and show which group contributes more total importance

Return: importance table, bar chart, and a one-paragraph plain-English explanation of what the model is learning. Copy prompt Open prompt details Advanced Chain 04 
### Full XAI Chain 

This prompt runs a full explainable AI workflow from global importance to business translation. It is useful when you want one coherent interpretability package that can support both technical validation and stakeholder communication. It also explicitly flags potentially risky or counterintuitive model behavior. 
Prompt text Step 1: Global importance — compute and plot SHAP feature importances (beeswarm). Identify the top 5 features driving predictions.
Step 2: Effect direction — create SHAP dependence plots for the top 5 features. Describe the relationship between each feature and the prediction (linear, threshold, non-linear).
Step 3: Interaction analysis — compute SHAP interaction values. Identify the strongest pairwise interaction and plot it as a 2D PDP.
Step 4: Local explanation — generate waterfall plots for 3 representative predictions: high, low, and borderline.
Step 5: Business translation — write a 1-page non-technical explanation of how the model makes decisions, using analogies and avoiding all technical terms.
Step 6: Risk flagging — identify any feature effects that seem counterintuitive or potentially problematic from a fairness or business logic perspective. Copy prompt Open prompt details Intermediate Single prompt 05 
### LIME Explanation 

This prompt generates simple local explanations for selected individual predictions using LIME. It is most helpful when stakeholders care about case-by-case reasoning in language that is easy to communicate. The chosen set of examples covers typical, extreme, borderline, and wrong predictions. 
Prompt text Use LIME to explain individual predictions from this model in plain English.

Generate LIME explanations for 5 specific predictions:
1. One very high prediction (top 5% of predicted values)
2. One very low prediction (bottom 5% of predicted values)
3. One borderline prediction (near the decision threshold)
4. The single prediction the model got most wrong
5. A randomly selected typical prediction

For each explanation:
- Show the top 10 features that pushed the prediction up or down
- Display as a horizontal bar chart with green bars (positive contribution) and red bars (negative contribution)
- Write a 2-sentence plain-English explanation: 'The model predicted [value] primarily because [top driver]. This was offset by [top negative driver].'

Return all 5 explanations with plots and text summaries. Copy prompt Open prompt details Advanced Single prompt 06 
### Model Behavior Report 

This prompt writes a full technical behavior review of the model rather than isolated explainability charts. It is useful when a project needs a more formal narrative covering feature effects, decision patterns, interactions, and edge cases. The report is intended for technical stakeholders who still want business clarity. 
Prompt text Write a complete model behavior report suitable for a technical stakeholder review.

The report should cover:

1. What the model learned — top 10 features and their direction of effect, in plain English
2. Decision rules — extract the top 5 decision paths from the model using SHAP or tree rules
3. Edge cases — what input combinations lead to extreme predictions (very high and very low)?
4. Monotonicity check — for features where a directional relationship is expected (e.g. more experience → higher salary), does the model respect that direction?
5. Interaction effects — which two features interact the most strongly? How does their interaction affect predictions?
6. Sensitivity analysis — which single feature, if changed by 10%, has the largest average impact on predictions?

Format as a structured report with section headings, plots, and a non-technical executive summary at the top. Copy prompt Open prompt details Intermediate Single prompt 07 
### Partial Dependence Plots 

This prompt maps how changing a feature affects the model on average and across individual cases. It is useful for identifying monotonic, threshold, or highly heterogeneous feature effects. The combination of PDP and ICE helps distinguish average behavior from person-level variability. 
Prompt text Generate partial dependence plots (PDPs) and individual conditional expectation (ICE) plots for the top features in this model.

For each of the top 5 most important features:
1. Plot the PDP: how does the average model prediction change as this feature varies across its range?
2. Overlay 50 randomly sampled ICE curves to show individual variation around the average
3. Highlight the average ICE curve in bold
4. Mark the actual data distribution (rug plot) on the x-axis to show where data is sparse
5. Describe the relationship: monotonic increasing, monotonic decreasing, non-linear, threshold effect?

Also create one 2D PDP for the top pair of interacting features (identified from SHAP interaction values).

Return all plots and a table summarizing the relationship type for each feature. Copy prompt Open prompt details Intermediate Single prompt 08 
### SHAP Analysis 

This prompt uses SHAP to explain both global model behavior and individual predictions. It is useful when you need richer insight than a single importance ranking, including effect direction and case-level reasoning. It is one of the strongest all-around explainability prompts for tabular models. 
Prompt text Generate a complete SHAP-based model explanation.

1. Compute SHAP values for all predictions in the validation set
2. Global explanations:
 - Beeswarm plot: feature importance + direction of effect
 - Bar plot: mean absolute SHAP value per feature (top 20)
3. Dependence plots for the top 3 most important features:
 - SHAP value on y-axis, feature value on x-axis
 - Color by the most important interaction feature
4. Local explanations — waterfall plots for:
 - The most confidently correct prediction
 - The most confidently wrong prediction
 - One typical prediction near the decision boundary
5. Plain-English summary: what are the top 3 drivers of high predictions vs low predictions?

Return all plots and the plain-English summary. Copy prompt Open prompt details 
## Recommended Explainability workflow 
1 
### Counterfactual Explanations 

Start with a focused prompt in Explainability so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Decision Tree Proxy 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Feature Importance 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Full XAI Chain 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
