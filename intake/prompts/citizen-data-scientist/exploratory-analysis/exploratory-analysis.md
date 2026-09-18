# Exploratory Analysis *AI Prompts *

5 Citizen Data Scientist prompts in Exploratory Analysis. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → intermediate levels and 5 single prompts. 

## AI prompts in Exploratory Analysis 
5 prompts Intermediate Single prompt 01 
### Data Quality Red Flags 

Review this dataset for data quality issues that could lead me to wrong conclusions if I do not address them first. I am not a data engineer — I need you to explain each issue i... 
Prompt text Review this dataset for data quality issues that could lead me to wrong conclusions if I do not address them first.

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
 - How to describe this limitation honestly when I share my findings Copy prompt Open prompt details Intermediate Single prompt 02 
### Find the Patterns 

Look through this dataset and find the most interesting patterns, trends, and relationships. I am not looking for a list of statistics. I want to understand what story the data... 
Prompt text Look through this dataset and find the most interesting patterns, trends, and relationships.

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
 - Describe it in one sentence that a non-analyst could repeat accurately to their manager. Copy prompt Open prompt details Beginner Single prompt 03 
### My First Dataset Exploration 

I just received a new dataset and I am not sure where to start. Help me explore it step by step. 1. Tell me the basics: - How many rows and columns does this dataset have? - Wha... 
Prompt text I just received a new dataset and I am not sure where to start. Help me explore it step by step.

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

Write your response in plain English. Avoid technical jargon. Explain any terms you do use. Copy prompt Open prompt details Beginner Single prompt 04 
### Plain English Data Summary 

Summarize this dataset in plain English for someone who has never seen it before. Write the summary as if you are explaining it to a colleague in a 5-minute conversation — not a... 
Prompt text Summarize this dataset in plain English for someone who has never seen it before.

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
- End with a single sentence: 'The most important thing to know about this dataset is: [sentence].' Copy prompt Open prompt details Intermediate Single prompt 05 
### Segment Comparison Guide 

Help me compare different groups or segments in this dataset to understand what drives differences in performance. I want to understand which groups are performing differently a... 
Prompt text Help me compare different groups or segments in this dataset to understand what drives differences in performance.

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

Explain your findings in plain language. Avoid using terms like 'statistically significant' without explaining what that means. Copy prompt Open prompt details 
## Recommended Exploratory Analysis workflow 
1 
### Data Quality Red Flags 

Start with a focused prompt in Exploratory Analysis so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Find the Patterns 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### My First Dataset Exploration 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Plain English Data Summary 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
