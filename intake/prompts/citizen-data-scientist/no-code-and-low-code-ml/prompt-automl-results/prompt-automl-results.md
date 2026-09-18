# AutoML Results Interpreter *AI Prompt *

I ran an AutoML tool on my dataset and got a results report. Help me understand what it means in plain English. AutoML output: {{automl_output}} 1. What model was selected and w... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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
 - Based on this report, what is the one thing I should do next? (deploy it, get more data, investigate a specific feature, try a different approach) 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin no-code and low-code ml work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in No-Code and Low-Code ML or the wider Citizen Data Scientist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as What model was selected and why:, What is the winning model type? (e.g. gradient boosting, random forest, neural network), Explain what this type of model does in one sentence without jargon. The final answer should stay clear, actionable, and easy to review inside a no-code and low-code ml workflow for citizen data scientist work. 

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

Once you have the first result, continue deeper with related prompts in No-Code and Low-Code ML.
