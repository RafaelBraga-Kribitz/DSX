# Vital Signs Exploration *AI Prompt *

This prompt explores vital sign data with both operational and clinical interpretation in mind. It summarizes distributions, identifies abnormal and impossible readings, and looks for expected physiologic patterns within diagnosis groups such as sepsis. It is especially valuable when vital signs are recorded repeatedly over time and may be used for acuity analysis, deterioration detection, or quality control. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Explore the vital signs data in this dataset.

For each vital sign (heart rate, blood pressure systolic/diastolic, respiratory rate, temperature, oxygen saturation, weight, BMI):

1. Distribution statistics: mean, median, std, 5th and 95th percentiles
2. Percentage of readings outside normal clinical range:
 - HR: normal 60–100 bpm
 - BP systolic: normal 90–140 mmHg
 - RR: normal 12–20 breaths/min
 - SpO2: normal ≥ 95%
 - Temp: normal 36.1–37.2°C (97–99°F)
3. Implausible values: HR = 0, SpO2 > 100%, negative values — flag as likely data errors
4. If multiple readings per patient exist: show the trend over time for the 5 most common vital signs
5. Correlate vital signs with diagnosis categories — do sepsis patients show expected patterns (high HR, high RR, low BP)?

Return a vital signs summary table with a clinical interpretation note for any metric where more than 10% of readings fall outside normal range. 
```

## When to use this prompt 
Use case 01 
when the dataset includes bedside vitals or repeated physiologic measurements 
Use case 02 
when you need to assess clinical plausibility of vital sign values 
Use case 03 
when you want to compare physiologic patterns across patient groups or diagnoses 
Use case 04 
when you are preparing features for an early warning or severity model 

## What the AI should return 

A vital signs summary with distribution metrics, out-of-range percentages, implausible-value checks, optional time trends, diagnosis-linked patterns, and concise clinical interpretation notes. 

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

Once you have the first result, continue deeper with related prompts in Patient Data Exploration.
