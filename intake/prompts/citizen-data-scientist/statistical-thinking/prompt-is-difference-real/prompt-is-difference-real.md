# Is This Difference Real? *AI Prompt *

I see a difference in my data between two groups or time periods. Help me figure out whether this difference is meaningful or just random variation. Observation: {{observation}}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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
 - Give me a single sentence conclusion: is this difference real, probably real, probably not real, or impossible to tell with this data? 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin statistical thinking work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Statistical Thinking or the wider Citizen Data Scientist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Explain the core problem in plain English:, Small samples are noisy: if you flip a coin 10 times and get 6 heads, that does not mean the coin is biased, The same applies to business data: a small difference on a small sample is often just luck. The final answer should stay clear, actionable, and easy to review inside a statistical thinking workflow for citizen data scientist work. 

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

Once you have the first result, continue deeper with related prompts in Statistical Thinking.
