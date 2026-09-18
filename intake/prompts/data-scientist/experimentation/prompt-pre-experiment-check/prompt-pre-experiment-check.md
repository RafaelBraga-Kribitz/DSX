# Pre-Experiment Sanity Check *AI Prompt *

This prompt checks whether an experiment is healthy before launch by validating assumptions that often break real tests. It is useful for avoiding wasted traffic due to bad randomization, unstable metrics, hidden seasonality, or broken instrumentation. The output acts like a launch readiness review for experimentation. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Run a pre-experiment sanity check before launching this A/B test.

1. AA test simulation: randomly split the existing data into two equal groups and test for significant differences on the primary metric — there should be none (p > 0.05). If there is a significant difference, the randomization is broken.
2. Check metric variance: compute the standard deviation of the primary metric per user over the past 4 weeks. High variance increases required sample size.
3. Check for seasonality: does the primary metric vary significantly by day of week or time of year? Adjust experiment timing accordingly.
4. Check for novelty effects: does the user base regularly respond to any UI changes with a short-term spike that fades? How long should the experiment run to see past this?
5. Verify logging: confirm the event tracking is firing correctly for both the primary metric and guardrail metrics by spot-checking recent data.

Return: AA test result, variance estimate, seasonality assessment, and recommended experiment start date and duration. 
```

## When to use this prompt 
Use case 01 
An A/B test is about to launch and you want a preflight check. 
Use case 02 
You want to verify randomization, variance, seasonality, and logging first. 
Use case 03 
The metric may have weekly cycles or novelty effects that affect duration. 
Use case 04 
You need a recommended launch timing and run length. 

## What the AI should return 

An AA test result, metric variance summary, seasonality and novelty assessment, instrumentation check guidance, and a recommendation for experiment start date and duration. 

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
