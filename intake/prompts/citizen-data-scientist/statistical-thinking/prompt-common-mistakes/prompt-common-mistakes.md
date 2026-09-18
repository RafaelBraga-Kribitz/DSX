# Avoiding Common Analysis Mistakes *AI Prompt *

Review my analysis for common mistakes that could lead to wrong conclusions — even when the math is correct. My analysis: {{analysis_description}} My conclusion: {{conclusion}}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

For each trap: tell me if I fell into it, how serious the problem is, and what I should do to correct or acknowledge it. 
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

The AI should return a structured result that covers the main requested outputs, such as Cherry-picking (looking only at data that supports your conclusion):, Did I look at the full dataset, or did I filter down to a subset where the pattern is clearest?, Did I try multiple time periods or segments and only report the one that shows the pattern?. The final answer should stay clear, actionable, and easy to review inside a statistical thinking workflow for citizen data scientist work. 

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
