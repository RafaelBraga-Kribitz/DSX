# Bed Utilization and Capacity *AI Prompt *

This prompt evaluates whether inpatient capacity is being used efficiently and whether certain units are operating in chronic scarcity or chronic underuse. It connects census, occupancy, turnover, and boarding into one operational view, then extends the analysis into forecasting and scenario modeling. It is useful for bed management, service line planning, and hospital operations leadership. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze inpatient bed utilization and capacity in this dataset.

1. Calculate daily census for each unit or service line: total occupied beds per day
2. Calculate occupancy rate: (occupied beds / staffed beds) × 100
 - Target range: 80–85% for most acute care units
 - Flag any unit consistently above 90% (capacity crisis) or below 70% (inefficiency)
3. Analyze bed turnover ratio: admissions / average daily census — higher is more efficient
4. Identify peak demand periods:
 - Hour of day with highest census
 - Day of week with highest occupancy
 - Seasonal patterns (flu season, summer vs winter)
5. Calculate boarding hours: time admitted patients spend in the ED waiting for an inpatient bed
6. Model: what occupancy rate reduction is needed to eliminate boarding waits of >4 hours?
7. Forecast: based on current admission trends, when will average occupancy exceed 90%?

Return: occupancy dashboard by unit, peak demand heatmap, and capacity forecast chart. 
```

## When to use this prompt 
Use case 01 
when hospital capacity pressure or boarding is a major concern 
Use case 02 
when you need a unit-by-unit occupancy and census view 
Use case 03 
when leadership wants to know whether bed supply matches demand patterns 
Use case 04 
when you need a forecast of when occupancy may move into crisis levels 

## What the AI should return 

A bed utilization report with daily census, occupancy and turnover by unit, peak demand patterns, boarding analysis, and a simple forward-looking capacity forecast. 

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
