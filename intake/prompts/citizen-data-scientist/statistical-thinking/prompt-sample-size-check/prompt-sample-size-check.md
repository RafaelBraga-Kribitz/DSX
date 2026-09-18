# Sample Size Sanity Check *AI Prompt *

Help me understand whether I have enough data to trust my findings and make decisions. My analysis: {{analysis_description}} My sample size: {{sample_size}} The difference or ef... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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
 Which option makes most sense for my situation? 
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

The AI should return a structured result that covers the main requested outputs, such as Why sample size matters — in plain English:, Explain using a coin flip analogy: with 10 flips you might get 7 heads and think the coin is biased. With 1,000 flips, you get a much more reliable answer., Apply this to my specific analysis: why does my sample size matter here?. The final answer should stay clear, actionable, and easy to review inside a statistical thinking workflow for citizen data scientist work. 

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
