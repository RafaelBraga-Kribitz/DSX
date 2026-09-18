# Discharge Timing Analysis *AI Prompt *

This prompt examines when discharges actually happen and quantifies the operational consequences of late discharge patterns. It links discharge timing to occupancy pressure and ED boarding, making it useful for hospitals trying to improve patient flow without adding beds. It also highlights physicians or services with better discharge timing practices that may be reproducible elsewhere. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze discharge timing patterns and their operational impact.

1. Plot the distribution of actual discharge times by hour of day — when do most discharges happen?
2. Calculate the % of discharges that occur before noon vs after noon
 - Target: ≥30% of discharges before noon (industry best practice)
3. Analyze the relationship between discharge timing and:
 - ED boarding time (do early discharges reduce ED waits?)
 - Occupancy rate by hour (does morning discharge free capacity?)
4. Break down discharge timing by:
 - Service line / attending physician
 - Day of week
 - Discharge disposition (home discharges vs SNF vs other)
5. Identify which physicians or units have the best early discharge rates
6. Calculate the estimated impact: if early discharge rate improved from current to 30%, how many additional bed-hours would be freed per day?

Return: discharge timing histogram, early discharge rate by service and physician, and capacity impact estimate. 
```

## When to use this prompt 
Use case 01 
when hospital flow teams are trying to increase discharges before noon 
Use case 02 
when you want to quantify the capacity benefit of earlier discharge timing 
Use case 03 
when physician- or unit-level discharge behavior needs comparison 
Use case 04 
when late discharge patterns may be worsening ED boarding and occupancy 

## What the AI should return 

A discharge timing report with hourly discharge distribution, before-noon rate, subgroup comparisons, and an estimate of bed-hours that could be freed by earlier discharge performance. 

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

Once you have the first result, continue deeper with related prompts in Operational Analytics.
