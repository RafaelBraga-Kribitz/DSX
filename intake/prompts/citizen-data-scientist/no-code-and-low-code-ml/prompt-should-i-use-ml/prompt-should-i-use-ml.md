# Should I Use ML Here? *AI Prompt *

Help me decide whether machine learning is the right tool for my problem, or whether a simpler approach would work better. My problem: {{problem_description}} My data: {{data_de... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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
 Tell me directly: based on my problem, would you start with ML or a simpler approach, and why? 
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

The AI should return a structured result that covers the main requested outputs, such as What am I actually trying to do?, Am I trying to predict a number? (e.g. forecast next month's sales, estimate customer lifetime value), Am I trying to classify something into categories? (e.g. is this customer likely to churn: yes or no). The final answer should stay clear, actionable, and easy to review inside a no-code and low-code ml workflow for citizen data scientist work. 

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
