# No-Code and Low-Code ML *AI Prompts *

6 Citizen Data Scientist prompts in No-Code and Low-Code ML. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 6 single prompts. 

## AI prompts in No-Code and Low-Code ML 
6 prompts Beginner Single prompt 01 
### AutoML Results Interpreter 

I ran an AutoML tool on my dataset and got a results report. Help me understand what it means in plain English. AutoML output: {{automl_output}} 1. What model was selected and w... 
Prompt text I ran an AutoML tool on my dataset and got a results report. Help me understand what it means in plain English.

AutoML output: {{automl_output}}

1. What model was selected and why:
 - What is the winning model type? (e.g. gradient boosting, random forest, neural network)
 - Explain what this type of model does in one sentence without jargon
 - Why did it win? What does it do that the other models did not?

2. How good is the model — in plain terms:
 - What does the accuracy metric mean? Translate it to business impact:
 - If accuracy is 85%, that means the model is wrong about 1 in 7 predictions
 - If AUC is 0.82, that means the model ranks a randomly chosen positive case above a randomly chosen negative case 82% of the time
 - Is this result good, okay, or poor? Give me context: what would random guessing score?
 - What is the most common type of mistake the model makes?

3. What does the model think matters most:
 - Which features (columns) did the model find most useful for making predictions?
 - Do these make intuitive sense? If a feature that should not matter ranks highly, that could indicate a data problem.
 - Is there any feature you are surprised is not on the list?

4. Should I trust this model:
 - Is there any sign of overfitting? (training accuracy much higher than validation accuracy)
 - Was the dataset large enough? As a rough guide: at least 1000 rows for simple problems, 10,000+ for complex ones
 - Are there any warnings in the AutoML report I should pay attention to?

5. Next step:
 - Based on this report, what is the one thing I should do next? (deploy it, get more data, investigate a specific feature, try a different approach) Copy prompt Open prompt details Intermediate Single prompt 02 
### Clustering Results Explainer 

I ran a clustering analysis on my data and got groups back. Help me understand and name each cluster in business terms. Clustering output: {{clustering_output}} Dataset context:... 
Prompt text I ran a clustering analysis on my data and got groups back. Help me understand and name each cluster in business terms.

Clustering output: {{clustering_output}}
Dataset context: {{dataset_context}}

1. What is clustering doing in plain English:
 - Explain to me what the algorithm did to create these groups — in one paragraph, no technical terms
 - How is this different from segments I define manually?
 - What does it mean that some customers are in the same cluster?

2. Describe each cluster:
 For each cluster, tell me:
 - Size: how many rows and what percentage of the total?
 - Key characteristics: which columns have the most distinctive values in this cluster compared to the rest?
 - In plain English: who or what are the members of this cluster? Describe them as if you were describing a person or type of product
 - Suggest a business-friendly name for this cluster (e.g. 'High-value loyalists', 'At-risk occasional buyers', 'New high-potential')

3. Are the clusters useful?
 - Are the clusters meaningfully different from each other? Or do they blend together?
 - Would a business colleague understand the difference between Cluster A and Cluster B if you described them?
 - Is there one cluster that deserves immediate business attention? Which one and why?

4. What I can do with these clusters:
 - Give me 2–3 specific actions I could take for each cluster
 - For example: 'Cluster 1 (high-value loyalists) → loyalty reward program', 'Cluster 3 (at-risk) → win-back campaign'

5. Limitations:
 - What should I be careful about when presenting these clusters to stakeholders?
 - Under what circumstances might these clusters not be stable or reliable? Copy prompt Open prompt details Advanced Single prompt 03 
### Feature Importance in Plain English 

My model gave me a feature importance chart. Help me understand what it means and what to do with it. Feature importance output: {{feature_importance_output}} Model predicts: {{... 
Prompt text My model gave me a feature importance chart. Help me understand what it means and what to do with it.

Feature importance output: {{feature_importance_output}}
Model predicts: {{target_variable}}

1. What feature importance means — in plain English:
 - Explain what feature importance is measuring: not 'which columns correlate with the target', but 'which columns the model actually relies on most to make its predictions'
 - Why does this matter? Because it tells us what the model believes drives the outcome

2. Walk through the top features:
 For each of the top 5 most important features:
 - Name: what is this column and what does it measure?
 - Direction: when this column has a high value, does the model predict a higher or lower outcome?
 - Business interpretation: what does this mean in business terms?
 - Does this make intuitive sense? If a feature ranks highly but you cannot explain why it matters, that is a warning sign.

3. Red flags to look for:
 - Is any feature suspiciously important? (e.g. a unique identifier like customer_id should not be important — it means the model memorized the training data)
 - Is any feature important that could not realistically be known at prediction time?
 - Is any feature important because it is a proxy for something else you should be measuring directly?

4. What is missing:
 - Are there features you expected to be important that are near the bottom? Why might the model not be using them?
 - Could an important column be missing from the data entirely?

5. What to do with this information:
 - Which features could I collect or engineer more of to improve the model?
 - Is there a feature so dominant that the model might be 'cheating'?
 - What does this feature importance tell us about the business problem — independent of the model? Copy prompt Open prompt details Intermediate Single prompt 04 
### Model Prediction Explainer 

My model made a prediction for a specific case. Help me explain to a business stakeholder why the model predicted what it did. Case details: {{case_details}} Model prediction: {... 
Prompt text My model made a prediction for a specific case. Help me explain to a business stakeholder why the model predicted what it did.

Case details: {{case_details}}
Model prediction: {{prediction}}
Model explanation output (SHAP or similar): {{explanation_output}}

1. What did the model predict and how confident is it:
 - State the prediction in plain English: 'The model predicts that [outcome] with [confidence]%'
 - Put the confidence in context: is 72% confidence high or low for this type of problem?

2. Why did the model predict this:
 - Using the explanation data, describe in plain English the top 3 reasons the model made this prediction
 - Format each reason as: '[Feature name] = [value] pushed the prediction [up/down] because [plain English reason]'
 - Avoid technical terms. Say 'the customer has been inactive for 90 days which increased the churn risk' not 'the days_since_last_purchase feature had a positive SHAP value'

3. What would change the prediction:
 - If the business wants to change this outcome, which factors could realistically be changed?
 - Example: 'If the customer made one purchase in the next 30 days, the churn risk would likely drop from 78% to around 45%'

4. Should we trust this specific prediction:
 - Is this customer/case similar to the training data? Or is it an unusual case where the model may be less reliable?
 - Are any of the input values unusual or possibly wrong?

5. How to communicate this to the business:
 - Write a 2-sentence explanation of this prediction that a sales manager or account manager could understand and use to take action Copy prompt Open prompt details Intermediate Single prompt 05 
### Prediction Model Setup Guide 

Guide me through setting up a prediction model for my problem using a low-code or AutoML tool. I want to predict: {{target_variable}} Using data from: {{data_source}} Tool I am... 
Prompt text Guide me through setting up a prediction model for my problem using a low-code or AutoML tool.

I want to predict: {{target_variable}}
Using data from: {{data_source}}
Tool I am using: {{tool_name}} (e.g. MLJAR Studio, DataRobot, Google AutoML, H2O.ai)

1. Before I build the model — data preparation:
 - What does my data need to look like before I feed it to the model?
 - Which columns should I include as inputs and which should I exclude? (e.g. exclude columns that would not be available at prediction time, exclude columns that directly reveal the answer)
 - How many rows do I need? Is my current dataset large enough?
 - Does my target variable (the thing I want to predict) need any preparation?

2. Common mistakes to avoid before pressing 'build':
 - Data leakage: including a column that tells the model the answer directly (e.g. using 'was refunded' to predict 'will churn' — if someone was refunded they already churned)
 - Using the future to predict the past: make sure all your input columns only use information that was available at the time you would have made the prediction
 - Predicting something that does not actually need prediction: if 95% of cases are one class, always predicting that class will look accurate but is useless

3. Setting up the model in {{tool_name}}:
 - Walk me through the key settings I need to configure: target column, problem type, training/test split, and the main metric to optimize
 - Which metric should I use to evaluate this model given my business goal?

4. Interpreting the first results:
 - What should I look at first in the results?
 - What does 'good enough' look like for my use case?
 - What are the most common reasons a first model underperforms?

5. If the model is not good enough:
 - What are my options? (more data, better features, different model type, different problem framing) Copy prompt Open prompt details Beginner Single prompt 06 
### Should I Use ML Here? 

Help me decide whether machine learning is the right tool for my problem, or whether a simpler approach would work better. My problem: {{problem_description}} My data: {{data_de... 
Prompt text Help me decide whether machine learning is the right tool for my problem, or whether a simpler approach would work better.

My problem: {{problem_description}}
My data: {{data_description}}
My goal: {{goal}}

1. What am I actually trying to do?
 Help me categorize my goal:
 - Am I trying to predict a number? (e.g. forecast next month's sales, estimate customer lifetime value)
 - Am I trying to classify something into categories? (e.g. is this customer likely to churn: yes or no)
 - Am I trying to find groups in my data? (e.g. which customers are similar to each other)
 - Am I trying to understand what causes something? (e.g. what factors drive sales)

2. Do I actually need machine learning?
 For each goal, explain the simpler alternative first:
 - Prediction → Could a trend line or simple average work well enough?
 - Classification → Could a simple rule (IF revenue < $100 AND no purchase in 90 days THEN high churn risk) work?
 - Grouping → Could I just segment by an existing column I already have?
 - Understanding causes → Could a comparison of group averages answer this?

 ML is worth the complexity only when:
 - The patterns are too complex for simple rules
 - Accuracy materially matters (a wrong prediction has real consequences)
 - You have enough data (at least a few hundred labeled examples for prediction/classification)

3. If ML is the right choice:
 - What type of ML would apply here: supervised (you have labeled examples), unsupervised (you want to find structure), or a different approach?
 - What tool is appropriate for my skill level? (Excel add-in, Google Sheets ML, DataRobot, H2O AutoML, Python scikit-learn, MLJAR Studio)
 - What data do I need that I might not have yet?

4. The honest answer:
 Tell me directly: based on my problem, would you start with ML or a simpler approach, and why? Copy prompt Open prompt details 
## Recommended No-Code and Low-Code ML workflow 
1 
### AutoML Results Interpreter 

Start with a focused prompt in No-Code and Low-Code ML so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Clustering Results Explainer 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Feature Importance in Plain English 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Model Prediction Explainer 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
