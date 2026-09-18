# Citizen Data Scientist *AI Prompts *

Citizen Data Scientist AI prompt library with 24 prompts in 5 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 5 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Citizen Data Scientist prompt categories 
5 categories 
### No-Code and Low-Code ML 

AI prompts for no-code and low-code machine learning workflows, enabling practical model building and analysis without heavy coding overhead. 
6 prompts AutoML Results Interpreter Clustering Results Explainer → 
### Exploratory Analysis 

AI prompts for exploratory analysis to understand dataset structure, distributions, relationships, anomalies, and initial analytical directions. 
5 prompts Data Quality Red Flags Find the Patterns → 
### Insight Communication 

AI prompts for communicating analytical insights clearly to stakeholders through concise narratives, recommendations, and business-ready outputs. 
5 prompts Chart Caption Writer Data Story Builder → 
### Statistical Thinking 

AI prompts for statistical thinking, including uncertainty awareness, hypothesis discipline, and defensible interpretation of data evidence. 
5 prompts Avoiding Common Analysis Mistakes Correlation vs Causation → 
### Self-Service Analytics 

AI prompts for self-service analytics workflows that help non-specialists answer business questions through guided analysis and reusable patterns. 
3 prompts Automate My Recurring Report Reusable Analysis Template → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 24 No-Code and Low-Code ML 6 Exploratory Analysis 5 Insight Communication 5 Statistical Thinking 5 Self-Service Analytics 3 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **24 **of 24 prompts 
## No-Code and Low-Code ML 
6 prompt s No-Code and Low-Code ML Beginner Prompt 01 
### AutoML Results Interpreter 
I ran an AutoML tool on my dataset and got a results report. Help me understand what it means in plain English.

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
 - Based on this report, what is the one thing I should do next? (deploy it, get more data, investigate a specific feature, try a different approach) Copy prompt View page Show more ↓ No-Code and Low-Code ML Intermediate Prompt 02 
### Clustering Results Explainer 
I ran a clustering analysis on my data and got groups back. Help me understand and name each cluster in business terms.

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
 - Under what circumstances might these clusters not be stable or reliable? Copy prompt View page Show more ↓ No-Code and Low-Code ML Advanced Prompt 03 
### Feature Importance in Plain English 
My model gave me a feature importance chart. Help me understand what it means and what to do with it.

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
 - What does this feature importance tell us about the business problem — independent of the model? Copy prompt View page Show more ↓ No-Code and Low-Code ML Intermediate Prompt 04 
### Model Prediction Explainer 
My model made a prediction for a specific case. Help me explain to a business stakeholder why the model predicted what it did.

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
 - Write a 2-sentence explanation of this prediction that a sales manager or account manager could understand and use to take action Copy prompt View page Show more ↓ No-Code and Low-Code ML Intermediate Prompt 05 
### Prediction Model Setup Guide 
Guide me through setting up a prediction model for my problem using a low-code or AutoML tool.

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
 - What are my options? (more data, better features, different model type, different problem framing) Copy prompt View page Show more ↓ No-Code and Low-Code ML Beginner Prompt 06 
### Should I Use ML Here? 
Help me decide whether machine learning is the right tool for my problem, or whether a simpler approach would work better.

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
 Tell me directly: based on my problem, would you start with ML or a simpler approach, and why? Copy prompt View page Show more ↓ 
## Exploratory Analysis 
5 prompt s Exploratory Analysis Intermediate Prompt 01 
### Data Quality Red Flags 
Review this dataset for data quality issues that could lead me to wrong conclusions if I do not address them first.

I am not a data engineer — I need you to explain each issue in plain terms and tell me what to do about it.

1. Completeness problems:
 - Which columns are missing data, and how many rows are affected?
 - For each column with significant missing data (more than 5%): could the missing values be a problem, or is it normal for that field to be blank?
 - Is there a pattern to what is missing? (e.g. missing values are concentrated in one region or time period — that is more concerning than random gaps)

2. Accuracy problems:
 - Are there values that look impossible? (negative quantities, prices of $0 on paid products, ages of 150, dates in the future)
 - Are there values that are technically possible but suspiciously unlikely? (every sale is exactly $100, all customer ages are round numbers)
 - Are there columns where the same thing is written in different ways? ('New York', 'new york', 'NY', 'N.Y.' — these are all the same but will be counted separately)

3. Consistency problems:
 - If the same information appears in multiple columns, do they agree with each other?
 - Are there rows where related columns contradict each other? (an order with a delivery date before the order date)

4. Duplicates:
 - Are there exact duplicate rows that should not exist?
 - Are there near-duplicates — the same customer or order appearing twice with slightly different details?

5. What to do:
 For each issue found, tell me:
 - How serious it is: will this issue mislead my analysis (serious) or is it minor (cosmetic)?
 - What I should do before I analyze: fix it, exclude affected rows, note it as a caveat, or ignore it safely
 - How to describe this limitation honestly when I share my findings Copy prompt View page Show more ↓ Exploratory Analysis Intermediate Prompt 02 
### Find the Patterns 
Look through this dataset and find the most interesting patterns, trends, and relationships.

I am not looking for a list of statistics. I want to understand what story the data is telling.

1. Trends over time (if this data has dates):
 - Is the main metric going up, down, or staying flat over time?
 - Are there any seasonal patterns — does it spike at certain times of year or week?
 - Was there a turning point where things changed significantly?

2. Differences across groups:
 - When you split the data by the most important categories (region, product, customer type, etc.), which group performs best? Which performs worst?
 - Is the gap between the best and worst groups large or small?
 - Is there any group that behaves very differently from all the others?

3. Relationships between columns:
 - Which two numeric columns tend to move together — when one goes up, does the other also go up?
 - Is there a column that seems to predict or explain the main outcome?
 - Is there anything that seems like it should be related but is not?

4. Outliers and exceptions:
 - Are there any rows that are dramatically different from the rest? What makes them unusual?
 - Are there any gaps, zeros, or plateaus that seem like they should not be there?

5. The most important pattern:
 - Out of everything above, which single pattern is most important for the business to know about?
 - Describe it in one sentence that a non-analyst could repeat accurately to their manager. Copy prompt View page Show more ↓ Exploratory Analysis Beginner Prompt 03 
### My First Dataset Exploration 
I just received a new dataset and I am not sure where to start. Help me explore it step by step.

1. Tell me the basics:
 - How many rows and columns does this dataset have?
 - What does each column appear to represent based on its name and values?
 - What time period does the data cover, if it has dates?
 - What does one row in this dataset represent? (e.g. one customer, one order, one day)

2. What is the data quality like?
 - Which columns have missing values, and how many?
 - Are there any columns where the values look wrong or impossible? (negative ages, future dates, prices of zero)
 - Are there any duplicate rows?

3. What are the most interesting things in this data?
 - Which numeric columns have the widest range of values?
 - Which categories appear most and least frequently in the text columns?
 - Is there anything in this data that immediately looks unusual or surprising?

4. What questions can this data answer?
 - Based on what you can see, list 5 business questions this dataset could help answer.

5. What should I look at first?
 - Given everything above, what is the single most interesting thing to explore next and why?

Write your response in plain English. Avoid technical jargon. Explain any terms you do use. Copy prompt View page Show more ↓ Exploratory Analysis Beginner Prompt 04 
### Plain English Data Summary 
Summarize this dataset in plain English for someone who has never seen it before.

Write the summary as if you are explaining it to a colleague in a 5-minute conversation — not a technical report.

Cover:
1. What this dataset is about — one sentence that a non-technical person would understand
2. The scale — how much data is here? Put it in relatable terms (e.g. '12,000 rows — roughly one row for every customer who visited last year')
3. The time range — what period does this cover and is that enough to spot trends?
4. The key columns — the 4–5 most important columns and what they tell us
5. The data quality in plain terms — not statistics, but a verdict: 'mostly complete', 'some gaps in a few areas', or 'significant holes that need fixing'
6. The headline finding — is there one thing that immediately stands out as interesting or concerning?
7. What you would do first if this were your dataset — one specific next step

Rules:
- No bullet points that list statistics without meaning
- Every number must have context ('23% of rows have missing values in the discount column — that is nearly 1 in 4 rows')
- End with a single sentence: 'The most important thing to know about this dataset is: [sentence].' Copy prompt View page Show more ↓ Exploratory Analysis Intermediate Prompt 05 
### Segment Comparison Guide 
Help me compare different groups or segments in this dataset to understand what drives differences in performance.

I want to understand which groups are performing differently and why — not just that they are different.

1. Identify the segments:
 - What categories in this dataset naturally divide the data into groups? (region, product type, customer tier, age group, channel, etc.)
 - Which of these segmentations is likely to be most meaningful for the business?

2. Compare the groups on the key metric:
 - What is the average (and range) of the main metric for each group?
 - Rank the groups from best to worst
 - Which group is the biggest outlier — far above or far below the average?

3. Is the difference meaningful or just noise?
 - Is the gap between the best and worst group large enough to act on?
 - Are some groups so small that their results are unreliable? (if a group has fewer than 30 rows, its average can swing wildly by chance)
 - What would the result look like if the worst group performed as well as the average group?

4. What else is different about the groups?
 - Look beyond the main metric: do the high-performing groups share other characteristics? (different mix of products, longer customer tenure, different geography)
 - Could any of these characteristics explain why they perform better?

5. The actionable insight:
 - Based on this comparison, what is the one thing the business should investigate or act on?
 - Be specific: name the group, the gap, and the potential action.

Explain your findings in plain language. Avoid using terms like 'statistically significant' without explaining what that means. Copy prompt View page Show more ↓ 
## Insight Communication 
5 prompt s Insight Communication Beginner Prompt 01 
### Chart Caption Writer 
Write a clear, insightful caption for this data visualization that tells the audience what to notice and what it means.

Chart description: {{chart_description}}
Audience: {{audience}}
Key finding in the chart: {{key_finding}}

Most chart captions are bad because they describe what the chart shows rather than what it means. A good caption answers: 'So what?'

1. The headline caption (1 sentence, bold):
 - State the insight, not a description of the chart
 - Wrong: 'Monthly revenue from January to December 2024'
 - Right: 'Revenue peaked in March before falling steadily — Q4 is 23% below Q1'
 - The headline should be a complete sentence with a verb, not a label

2. The supporting caption (1–2 sentences):
 - Add the most important context or implication that the headline did not capture
 - Point the reader to something specific: 'Note the sharp drop in August, which coincides with the system outage'
 - If the finding is surprising: explain briefly why that matters

3. Data note (optional, smaller text):
 - Source of the data
 - Any important caveat about how to read the chart (e.g. 'revenue excludes refunds')

4. Write 3 alternative headline options:
 - Option A: factual and neutral
 - Option B: action-oriented (implies what should happen)
 - Option C: question-framing (poses the key question the chart raises)

For each option, explain in one sentence who it would be most appropriate for (analyst audience, executive audience, public-facing report). Copy prompt View page Show more ↓ Insight Communication Intermediate Prompt 02 
### Data Story Builder 
Help me build a data story that takes my audience from the current situation to a clear recommendation.

My data findings: {{findings}}
My audience: {{audience}}
The decision I want them to make: {{desired_decision}}

A data story is not a data dump. It is a narrative that uses data as evidence to make a persuasive case.

1. The opening hook (1–2 sentences):
 - Start with something that makes the audience care: a surprising number, a relatable scenario, or the cost of inaction
 - Do not start with 'The purpose of this analysis is...'

2. The context (2–3 sentences):
 - What is the situation? Why are we looking at this now?
 - What were we expecting or hoping for?

3. The finding (the heart of the story):
 - What does the data actually show?
 - Present the key insight with supporting evidence — not a list of all findings, just the most important one
 - Acknowledge any counterintuitive or surprising element — it builds credibility

4. The implication (so what?):
 - What does this finding mean for the business?
 - What happens if we ignore it?
 - Quantify the impact if possible: revenue at risk, cost savings available, customers affected

5. The recommendation (the ask):
 - State one clear, specific action
 - Say who should do it, by when, and what the expected outcome is
 - Acknowledge the main objection your audience might have and address it briefly

6. The narrative structure check:
 - Does each section naturally lead to the next?
 - Could someone who did not see the data repeat your key point accurately to a colleague?

Write the complete data story following this structure. Copy prompt View page Show more ↓ Insight Communication Beginner Prompt 03 
### Findings to Executive Summary 
Turn my data findings into a clear executive summary that a non-technical leader can understand and act on.

My findings: {{findings}}
Audience: {{audience}} (e.g. VP of Sales, CFO, Operations Director)
Decision needed: {{decision_needed}}

1. Lead with the so-what — not the analysis:
 - The first sentence must state the business implication, not the data finding
 - Wrong: 'Revenue declined 14% in Q3 compared to Q2'
 - Right: 'We are at risk of missing the annual target by $2.3M if Q4 revenue does not recover — here is what drove Q3's decline'

2. Use the SCR structure (Situation, Complication, Resolution):
 - Situation (1–2 sentences): what is the context? What were we expecting or hoping for?
 - Complication (2–3 sentences): what did the data reveal that is different from expectations? Include the key numbers.
 - Resolution (2–3 sentences): what does this mean for the decision at hand? What do you recommend?

3. Make every number meaningful:
 - Every statistic must have context: '14% decline' should be '14% decline — the largest quarter-over-quarter drop in 3 years'
 - Translate percentages to absolute impact where possible: '14% decline = $1.8M less than the same period last year'
 - Replace 'significant' with the actual number

4. One clear ask:
 - End with a single, specific request: a decision, an action, or a resource
 - Do not list 5 options — give one recommendation with a brief rationale

5. Length and format:
 - Maximum 200 words for the summary
 - One supporting table or chart description if needed
 - No bullet lists of raw statistics — write in paragraphs

Write the executive summary now, following these principles. Copy prompt View page Show more ↓ Insight Communication Advanced Prompt 04 
### Handling Stakeholder Pushback 
A business stakeholder is pushing back on my data findings. Help me respond thoughtfully and maintain credibility.

My finding: {{my_finding}}
Stakeholder's objection: {{objection}}

1. First, take the objection seriously:
 Before preparing a rebuttal, ask: is the stakeholder raising a legitimate concern?
 - 'The data might be wrong' → Check: is there a reason the data quality could be an issue here?
 - 'This does not match what I see on the ground' → Check: is there a segment or time period the data is missing?
 - 'That cannot be right' → Check: have you double-checked the calculation?
 - 'The analysis method is wrong' → Check: is there a better method you should consider?

2. Classify the objection:
 - Factual objection (they dispute the data itself) → Respond with evidence and methodology
 - Interpretation objection (they agree on the data but disagree on the conclusion) → Explore the alternative interpretation together
 - Emotional objection (the finding is inconvenient or threatening) → Acknowledge the difficulty while holding the finding
 - Expertise objection (they know the domain better) → Listen carefully — they may be right

3. Prepare your response:
 For each objection type, draft a response that:
 - Acknowledges their perspective genuinely: 'That is a fair challenge to raise'
 - Addresses the substance of the concern with evidence
 - Does not become defensive or dismissive
 - Leaves the conversation open rather than closing it: 'What data would change your view?'

4. When to concede:
 - If the stakeholder raises a point that genuinely undermines the finding: concede it clearly and update your conclusion
 - Conceding when warranted builds far more credibility than defending a flawed finding

5. Draft the actual response:
 Write a 3–5 sentence response to the specific objection above that is confident but not combative. Copy prompt View page Show more ↓ Insight Communication Intermediate Prompt 05 
### Simplify Technical Findings 
I have technical analysis results that I need to explain to a non-technical business audience. Help me translate them into plain language without losing the key insights.

Technical findings: {{technical_findings}}
Audience: {{audience}} (their background: {{audience_background}})

1. Jargon replacement guide:
 For each technical term in my findings, provide the plain English replacement:
 - 'Statistically significant' → 'We can be confident this difference is real, not just random'
 - 'Correlation of 0.73' → 'When X goes up, Y tends to go up about 73% of the time'
 - 'Regression model' → 'A mathematical formula that calculates the predicted value based on other factors'
 - 'Confidence interval' → 'The range within which the true answer almost certainly falls'
 - 'Null hypothesis rejected' → 'The data shows a clear difference — it is not just chance'
 Apply this principle to every technical term in my specific findings.

2. Translate each finding:
 For each technical finding, write:
 - The plain English version (1–2 sentences, no jargon)
 - A concrete analogy or example that makes it tangible
 - The business implication in one sentence

3. What to leave out:
 - Methodological details your audience does not need to evaluate the conclusion
 - Intermediate results that do not change the recommendation
 - Caveats that are technically important but would not change the action taken
 (note separately: caveats that ARE important enough to share, and how to phrase them without undermining your findings)

4. The 'can they repeat it?' test:
 After writing the simplified version, check: could your audience repeat the key finding accurately in a conversation with their own colleagues?
 If no: simplify further. If yes: you are done.

Return: the translated findings, the jargon glossary, and a 3-bullet 'take-away' summary for the audience. Copy prompt View page Show more ↓ 
## Statistical Thinking 
5 prompt s Statistical Thinking Intermediate Prompt 01 
### Avoiding Common Analysis Mistakes 
Review my analysis for common mistakes that could lead to wrong conclusions — even when the math is correct.

My analysis: {{analysis_description}}
My conclusion: {{conclusion}}

Check for each of these traps and tell me honestly whether I have fallen into any of them:

1. Cherry-picking (looking only at data that supports your conclusion):
 - Did I look at the full dataset, or did I filter down to a subset where the pattern is clearest?
 - Did I try multiple time periods or segments and only report the one that shows the pattern?
 - The test: would the same conclusion hold if I looked at a different time period, different region, or different product?

2. Overfitting the narrative to the data:
 - Did I find a pattern and then construct an explanation for it after the fact?
 - Patterns found by looking at data often do not replicate in new data — this is the overfitting trap
 - The test: was this pattern something I predicted before looking at the data, or did I discover it by exploring?

3. Ignoring the base rate:
 - Example: '80% of our churned customers were contacted by support in their last month' sounds alarming — but if 80% of ALL customers contact support each month, this tells us nothing
 - Did I compare my finding to the base rate of the broader population?

4. Simpson's Paradox:
 - This is when a trend appears in the overall data but reverses within each subgroup
 - Example: overall conversion rate improved, but it declined in every individual region — because the mix shifted toward regions with naturally higher rates
 - Did I check whether my overall trend holds within the individual subgroups?

5. Availability bias in data selection:
 - Did I use this data because it was available, not because it is the right data?
 - Is there important data that I do not have that could change the conclusion?

For each trap: tell me if I fell into it, how serious the problem is, and what I should do to correct or acknowledge it. Copy prompt View page Show more ↓ Statistical Thinking Beginner Prompt 02 
### Correlation vs Causation 
I found a relationship between two things in my data. Help me figure out whether one causes the other or whether they just happen to move together.

Relationship found: {{relationship}} (e.g. 'Customers who receive more than 3 emails per month have 40% lower churn rates')

1. Explain the difference — with an example that makes it stick:
 - Correlation: two things move together
 - Causation: one thing makes the other happen
 - Classic example: ice cream sales and drowning rates both go up in summer. They are correlated. But ice cream does not cause drowning — hot weather causes both.
 - Now apply this logic to my specific relationship

2. The three possibilities for my relationship:
 - Option A: X causes Y directly (send more emails → customers stay longer)
 - Option B: Y causes X (customers who plan to stay engage with more emails — reverse causation)
 - Option C: Something else causes both (high-value customers both receive more targeted emails AND churn less — a third variable is driving both)
 For my specific relationship, which of these is most likely and why?

3. The self-selection problem (the most common trap in business data):
 - When we observe who receives treatment vs who does not, the groups are often not comparable
 - In my example: do all customers receive the same number of emails, or do certain types of customers get more? If engaged customers get more emails AND engaged customers churn less, we are confusing engagement for email effect.
 - Explain whether self-selection is a concern for my specific finding

4. How to test for causation:
 - The gold standard: a randomized experiment (A/B test) where some customers randomly get more emails and others do not
 - What a proper experiment would look like for my relationship
 - Without an experiment, what evidence would make me more confident the relationship is causal?

5. What to say to stakeholders:
 - How should I accurately describe this finding without overclaiming? Give me the exact phrasing to use. Copy prompt View page Show more ↓ Statistical Thinking Beginner Prompt 03 
### Is This Difference Real? 
I see a difference in my data between two groups or time periods. Help me figure out whether this difference is meaningful or just random variation.

Observation: {{observation}} (e.g. 'Group A has a 12% conversion rate and Group B has a 14% conversion rate')
Sample sizes: {{sample_sizes}}

1. Explain the core problem in plain English:
 - Small samples are noisy: if you flip a coin 10 times and get 6 heads, that does not mean the coin is biased
 - The same applies to business data: a small difference on a small sample is often just luck
 - We need to know if the difference is large enough relative to the sample size to be trustworthy

2. The quick gut-check:
 - How large is the difference in percentage terms and in absolute terms?
 - How large is each group? Fewer than 30 in either group → the difference is probably unreliable. Fewer than 100 → be cautious.
 - Has this pattern held up over multiple time periods, or is this one observation?

3. The proper test (explained simply):
 - For comparing two rates or percentages between groups: use a proportion test
 - For comparing two averages: use a t-test
 - Explain what 'p-value' means without jargon: 'A p-value of 0.05 means that if there were truly no difference between the groups, we would only see a gap this large or larger by chance 5% of the time — so we can be reasonably confident the difference is real'
 - Run the appropriate test and tell me the result

4. Practical vs statistical significance:
 - Statistical significance just means the difference is real, not random
 - It does not mean the difference is large enough to matter for the business
 - A difference can be statistically significant but too small to act on (e.g. 3.1% vs 3.2% conversion rate on 100,000 users)
 - Is this difference both statistically significant AND large enough to care about?

5. Plain English verdict:
 - Give me a single sentence conclusion: is this difference real, probably real, probably not real, or impossible to tell with this data? Copy prompt View page Show more ↓ Statistical Thinking Advanced Prompt 04 
### Outlier Investigation Guide 
I found outliers in my data. Help me figure out what to do with them.

Outliers found: {{outlier_description}}
Context: {{data_context}}

1. Not all outliers are the same — classify mine:
 - Data errors: the value is wrong due to a typo, system error, or import problem (e.g. a transaction amount of $10,000,000 when the max is normally $5,000)
 - Genuine extreme values: the value is correct but unusually large or small (a real whale customer who spent 100× the average)
 - Rare events: the value represents a real but infrequent event (a bulk order, a promotional spike)
 - Different population: the row represents a different type of entity than the rest (a corporate account in a dataset of individual customers)
 Based on my specific outliers, which category do they most likely fall into?

2. How to investigate:
 - For suspected data errors: check the source system, check nearby records for context, look for patterns in the error
 - For genuine extreme values: look at other columns in the same row — do they also look extreme? Or is only one column anomalous?
 - Look at the timing: did the outlier occur at a time when something unusual happened (system migration, promotional event, data export issue)?

3. What to do with them:
 - Data errors → fix or remove them. Never include known errors in your analysis.
 - Genuine extremes that are relevant → include them, but report median alongside mean (outliers inflate the mean significantly)
 - Genuine extremes that are not relevant to your question → exclude and document the exclusion transparently
 - Different population → segment them separately rather than mixing with the main group

4. The transparency rule:
 - Whatever you decide to do with outliers: document it and disclose it
 - 'We excluded 3 transactions that appeared to be data errors; including them would change the average by X%'
 - Never silently remove outliers without noting it

5. A practical check:
 - Run your analysis both with and without the outliers
 - If the conclusion is the same either way: the outliers do not matter much, keep them
 - If the conclusion changes dramatically: the outliers are doing significant work and deserve careful investigation

Return: classification of my specific outliers, investigation steps, recommended treatment, and the disclosure language to use. Copy prompt View page Show more ↓ Statistical Thinking Intermediate Prompt 05 
### Sample Size Sanity Check 
Help me understand whether I have enough data to trust my findings and make decisions.

My analysis: {{analysis_description}}
My sample size: {{sample_size}}
The difference or effect I am measuring: {{effect_size}}

1. Why sample size matters — in plain English:
 - Explain using a coin flip analogy: with 10 flips you might get 7 heads and think the coin is biased. With 1,000 flips, you get a much more reliable answer.
 - Apply this to my specific analysis: why does my sample size matter here?

2. Is my sample size large enough for what I am trying to do?
 - For comparing two groups: explain how the required sample size depends on (a) how big the real difference is and (b) how variable the data is
 - For my specific numbers, would this analysis give a reliable answer?
 - Use round numbers and analogies — I do not need exact formulas, I need intuition

3. The margin of error:
 - If I report a number from my data (e.g. '42% of customers prefer X'), what is the realistic margin of error around that number given my sample size?
 - Explain what 'margin of error' means: 'This means the true answer is likely somewhere between [lower bound] and [upper bound]'
 - Is this range narrow enough to make a confident decision, or is it too wide?

4. When small samples are okay:
 - Not every decision needs a large sample
 - If the effect is very large, a small sample can still provide useful evidence
 - If the cost of being wrong is low, a rough answer from a small sample may be fine
 - Apply this to my situation: given the stakes of the decision, is my sample size acceptable?

5. What to do if I do not have enough data:
 - Collect more data before deciding
 - Make a provisional decision with explicit uncertainty
 - Combine this data with other evidence
 Which option makes most sense for my situation? Copy prompt View page Show more ↓ 
## Self-Service Analytics 
3 prompt s Self-Service Analytics Intermediate Prompt 01 
### Automate My Recurring Report 
Help me automate a report I currently produce manually so it runs itself and I can focus on analysis instead of assembly.

Report I produce manually: {{report_description}}
How long it takes me currently: {{time_spent}}
Tool I have access to: {{available_tools}}
Audience and delivery method: {{audience_and_delivery}}

1. Identify what can be automated vs what requires human judgment:
 Go through the report and classify each step:
 - Fully automatable: data pulling, number calculation, chart generation, formatting
 - Partially automatable: anomaly flagging (automate the detection, human writes the explanation)
 - Requires human judgment: context, implications, recommendations
 The goal is to automate the assembly so I can spend my time on interpretation.

2. Automation approach for my tools:

 If using Excel / Google Sheets:
 - Data connection: link directly to the data source so the file refreshes automatically
 - Scheduled refresh: configure the data connection to refresh on a schedule
 - Email distribution: use a simple script or Zapier to email the report automatically

 If using Python (low-code approach):
 - Use pandas to pull and process the data
 - Use openpyxl or xlsxwriter to generate a formatted Excel report
 - Schedule with cron (Mac/Linux) or Task Scheduler (Windows)
 - Send via smtplib or a Slack bot

 If using a BI tool (Tableau, Power BI, Looker, Metabase):
 - Set the data source to auto-refresh
 - Use the built-in subscription feature to email a PDF snapshot on a schedule

3. Build in quality checks:
 - Before the automated report sends: check that the data was refreshed (compare last update timestamp to expected update time)
 - Check that key metrics are within a plausible range (alert me if revenue is 0 or 10× normal — likely a data error)
 - If checks fail: send an alert to me instead of the report to the audience

4. The commentary problem:
 - Automated reports without commentary are just data dumps
 - Build a commentary template with fill-in-the-blank sections that I complete in 10 minutes
 - The template prompts me: 'Key trend this week:', 'Biggest deviation from expectations:', 'Recommended action:'

Return: automation approach for my specific tools, quality check implementation, commentary template, and estimated time savings. Copy prompt View page Show more ↓ Self-Service Analytics Beginner Prompt 02 
### Reusable Analysis Template 
Help me create a reusable analysis template so I can repeat this analysis quickly each week or month without starting from scratch.

Analysis I do repeatedly: {{analysis_description}}
Data source: {{data_source}}
Outputs needed: {{outputs}}

1. Template structure:
 Design a template that:
 - Has clearly labeled sections I fill in each time (date range, filter criteria, comparison period)
 - Has fixed sections that stay the same every time (the formulas, the chart types, the table structure)
 - Is easy to use for someone who did not create it (my colleague should be able to run this without asking me how)

2. What to parameterize (make easy to change):
 - Date range: make it a single cell reference that all other cells use — change it once, everything updates
 - Comparison period: prior period, same period last year, target
 - Filters: which region, product, or segment to include
 For each parameter: where to put it, how to label it, and what the default value should be

3. What to standardize (keep the same every time):
 - Column names and order
 - Chart types and formatting
 - Metric definitions — write them out once so future-me and colleagues use the same definition
 - The commentary structure (this forces you to answer the same questions every time, which makes period-over-period comparison easier)

4. Documentation to include in the template:
 - A brief description of what this template does
 - Where the data comes from and when it was last refreshed
 - Definitions of each metric
 - Known limitations or caveats
 - Who to contact if something looks wrong

5. The 'can a colleague use this?' test:
 - Could someone with similar skills use this template without any instructions from you?
 - What is the most likely point of confusion? Add a note there.

Return: a step-by-step template design with all the above elements. Copy prompt View page Show more ↓ Self-Service Analytics Intermediate Prompt 03 
### Team Dashboard Design 
Help me design a simple dashboard that my team can use independently to monitor performance without needing my help.

Team: {{team_description}}
Key questions they need to answer: {{team_questions}}
Tool I will build it in: {{tool}} (e.g. Google Sheets, Excel, Tableau, Power BI, Metabase, Looker Studio)

1. What the dashboard is NOT:
 - It is not a data dump — every chart and number must answer a specific question
 - It is not for the builder — design it for people who look at it once a week, not for people who built it
 - It is not a report — it is a decision-support tool. Every element should prompt an action or confirm that no action is needed.

2. Design the dashboard structure:
 For each of the team's key questions, specify:
 - The metric or chart that answers it
 - The time frame it should show
 - The comparison context (vs last week, vs target, vs same period last year)
 - What 'green' looks like (no action needed) and what 'red' looks like (action needed)

3. Layout principles:
 - Most important metric top left (where eyes go first)
 - Single number + trend arrow for quick scanning
 - Detailed breakdowns below for people who want to dig in
 - Maximum 6–8 metrics on the main view — if you need more, create a second level

4. Making it self-service:
 - Add filter controls that the team can use to slice by region, product, time period
 - Color code automatically: green above target, yellow within 10% of target, red below threshold
 - Add a 'last updated' timestamp so users know if the data is fresh
 - Include a glossary section that defines every metric

5. Adoption tips:
 - Walk the team through it once — show them how to answer their 3 most common questions using it
 - Set a recurring reminder for them to check it at the start of each week
 - Ask for feedback after 2 weeks: which parts do they use, which do they ignore?

Return: dashboard wireframe (described in text), metric definitions, color coding rules, and a 30-minute walkthrough plan for the team. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
- Terms of Service 
- Privacy Policy 
- AI Policy 
- Licenses 
### AI Data Analysis Examples 

- LLM Benchmark on AI Data Analysis 
- Air Passengers Forecast 
- Iris Classification 
- Customer Churn Prediction 
- Energy Consumption Forecast 
### Resources 

- Example Python notebooks 
- Fix ModuleNotFoundError 
- Glossary 
- Brand 
- Answers 
- ML Algorithm Comparison 
- Research 
- Solutions 
### Products 

- MLJAR Studio 
- MLJAR AutoML 
- AI Data Analyst 
- AutoLab Experiments 
- Mercury 
### Tutorials 

- AutoML in Python: Beginner Tutorial with House Prices 
### Open Source 

- MLJAR AutoML 
- Mercury 
- More ... 
### AI Prompts 

- Prompts for Data Professionals 
- Data Analyst prompts 
- Business Analyst prompts 
- Data Scientist prompts 
- ML Engineer prompts 
- Data Engineer prompts 
- MLOps prompts 
### Compare 

- MLJAR Studio vs Julius 
- MLJAR Studio vs H2O 
- MLJAR Studio vs DataRobot 
- MLJAR Studio vs Jupyter 
- MLJAR Studio vs ChatGPT 
- MLJAR Studio vs Cursor 
### Company 

- Contact us 
- Services 
- About us 
- Blog Made by MLJAR. All rights reserved. Created in 🇵🇱 We ❤ you! 
We collect traffic information to improve the site. 

Data is collected in a privacy-friendly way (IP anonymization, no ads, no cross-site tracking). 
Analytics are only enabled if you accept. 
Read Privacy Policy Reject Accept
