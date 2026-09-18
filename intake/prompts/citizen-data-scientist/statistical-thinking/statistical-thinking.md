# Statistical Thinking *AI Prompts *

5 Citizen Data Scientist prompts in Statistical Thinking. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 5 single prompts. 

## AI prompts in Statistical Thinking 
5 prompts Intermediate Single prompt 01 
### Avoiding Common Analysis Mistakes 

Review my analysis for common mistakes that could lead to wrong conclusions — even when the math is correct. My analysis: {{analysis_description}} My conclusion: {{conclusion}}... 
Prompt text Review my analysis for common mistakes that could lead to wrong conclusions — even when the math is correct.

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

For each trap: tell me if I fell into it, how serious the problem is, and what I should do to correct or acknowledge it. Copy prompt Open prompt details Beginner Single prompt 02 
### Correlation vs Causation 

I found a relationship between two things in my data. Help me figure out whether one causes the other or whether they just happen to move together. Relationship found: {{relatio... 
Prompt text I found a relationship between two things in my data. Help me figure out whether one causes the other or whether they just happen to move together.

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
 - How should I accurately describe this finding without overclaiming? Give me the exact phrasing to use. Copy prompt Open prompt details Beginner Single prompt 03 
### Is This Difference Real? 

I see a difference in my data between two groups or time periods. Help me figure out whether this difference is meaningful or just random variation. Observation: {{observation}}... 
Prompt text I see a difference in my data between two groups or time periods. Help me figure out whether this difference is meaningful or just random variation.

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
 - Give me a single sentence conclusion: is this difference real, probably real, probably not real, or impossible to tell with this data? Copy prompt Open prompt details Advanced Single prompt 04 
### Outlier Investigation Guide 

I found outliers in my data. Help me figure out what to do with them. Outliers found: {{outlier_description}} Context: {{data_context}} 1. Not all outliers are the same — classi... 
Prompt text I found outliers in my data. Help me figure out what to do with them.

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

Return: classification of my specific outliers, investigation steps, recommended treatment, and the disclosure language to use. Copy prompt Open prompt details Intermediate Single prompt 05 
### Sample Size Sanity Check 

Help me understand whether I have enough data to trust my findings and make decisions. My analysis: {{analysis_description}} My sample size: {{sample_size}} The difference or ef... 
Prompt text Help me understand whether I have enough data to trust my findings and make decisions.

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
 Which option makes most sense for my situation? Copy prompt Open prompt details 
## Recommended Statistical Thinking workflow 
1 
### Avoiding Common Analysis Mistakes 

Start with a focused prompt in Statistical Thinking so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Correlation vs Causation 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Is This Difference Real? 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Outlier Investigation Guide 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
