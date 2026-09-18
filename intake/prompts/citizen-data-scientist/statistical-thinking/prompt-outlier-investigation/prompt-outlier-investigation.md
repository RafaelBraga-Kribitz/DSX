# Outlier Investigation Guide *AI Prompt *

I found outliers in my data. Help me figure out what to do with them. Outliers found: {{outlier_description}} Context: {{data_context}} 1. Not all outliers are the same — classi... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: classification of my specific outliers, investigation steps, recommended treatment, and the disclosure language to use. 
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

The AI should return a structured result that covers the main requested outputs, such as Not all outliers are the same — classify mine:, Data errors: the value is wrong due to a typo, system error, or import problem (e.g. a transaction amount of $10,000,000 when the max is normally $5,000), Genuine extreme values: the value is correct but unusually large or small (a real whale customer who spent 100× the average). The final answer should stay clear, actionable, and easy to review inside a statistical thinking workflow for citizen data scientist work. 

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
