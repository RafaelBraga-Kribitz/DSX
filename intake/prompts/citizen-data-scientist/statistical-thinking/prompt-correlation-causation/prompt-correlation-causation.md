# Correlation vs Causation *AI Prompt *

I found a relationship between two things in my data. Help me figure out whether one causes the other or whether they just happen to move together. Relationship found: {{relatio... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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
 - How should I accurately describe this finding without overclaiming? Give me the exact phrasing to use. 
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

The AI should return a structured result that covers the main requested outputs, such as Explain the difference — with an example that makes it stick:, Correlation: two things move together, Causation: one thing makes the other happen. The final answer should stay clear, actionable, and easy to review inside a statistical thinking workflow for citizen data scientist work. 

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
