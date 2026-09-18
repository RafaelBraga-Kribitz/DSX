# Full Experiment Design Chain *AI Prompt *

This prompt designs an experiment from first principles before any users are exposed. It is useful for pre-registration, alignment with product and business stakeholders, and avoiding weak experiment setups. The chain covers hypothesis, sample size, randomization, guardrails, and decision rules. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Define the experiment — what hypothesis are we testing, what is the primary metric, what is the minimum detectable effect, and what is the business rationale?
Step 2: Calculate sample size — given baseline metric, MDE, α=0.05, power=0.80. Calculate required experiment duration based on available traffic.
Step 3: Design the assignment — define unit of randomization (user, session, device). Check for network effects or contamination risks. Define the holdout strategy.
Step 4: Define guardrail metrics — list 3–5 metrics that must not degrade. Define the threshold for each guardrail.
Step 5: Design the analysis plan — specify the primary statistical test, multiple testing correction method, and pre-registration of hypotheses.
Step 6: Write the experiment brief: hypothesis, primary metric, guardrail metrics, sample size, duration, assignment method, analysis plan, decision criteria for ship/no-ship. 
```

## When to use this prompt 
Use case 01 
A new experiment is being designed and needs a rigorous brief. 
Use case 02 
You want the statistical plan agreed before launch. 
Use case 03 
Guardrails and assignment risks must be defined up front. 
Use case 04 
You need a reusable experiment design template for the team. 

## What the AI should return 

A complete experiment brief covering hypothesis, metrics, MDE, sample size, duration, assignment method, guardrails, analysis plan, and ship/no-ship decision criteria. 

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

Once you have the first result, continue deeper with related prompts in Experimentation.
