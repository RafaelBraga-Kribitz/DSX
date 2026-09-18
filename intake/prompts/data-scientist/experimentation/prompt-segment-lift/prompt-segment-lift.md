# Segment Lift Analysis *AI Prompt *

This prompt examines whether treatment effects vary meaningfully across user segments. It is useful when average lift may hide strong winners, losers, or targeting opportunities. The forest-plot format also makes heterogeneous effects easier to communicate. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze treatment lift across different user segments in this experiment.

1. Compute the overall lift: (treatment metric - control metric) / control metric
2. Compute lift separately for each segment defined by the available dimension columns (age group, region, device, acquisition channel, etc.)
3. Plot lift per segment as a forest plot (point estimate ± 95% CI for each segment)
4. Test for heterogeneous treatment effects: is the lift significantly different across segments? (interaction test)
5. Identify the segments with the highest and lowest lift
6. Flag any segment where the treatment caused a statistically significant negative effect
7. Recommend: should the feature be shipped to all users, or only to the highest-lift segments?

Return: segment lift table, forest plot, and a targeting recommendation. 
```

## When to use this prompt 
Use case 01 
The overall experiment result may not apply equally to all users. 
Use case 02 
You suspect device, region, channel, or demographic segments respond differently. 
Use case 03 
A targeted rollout is under consideration. 
Use case 04 
You need to detect and avoid segments harmed by treatment. 

## What the AI should return 

Overall and per-segment lift estimates, confidence intervals, forest plot, heterogeneity test result, and a recommendation on broad rollout versus targeted deployment. 

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
