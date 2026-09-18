# Patient Dataset Overview *AI Prompt *

This prompt is designed for a first-pass assessment of a patient-level healthcare dataset before any downstream analysis begins. It helps the analyst understand whether the file is organized at the patient, encounter, or admission level, what core clinical domains are available, and whether there are obvious data integrity issues that could bias later findings. It is especially useful because healthcare data often mixes repeated encounters, multiple identifiers, and clinically implausible values in ways that are not obvious from a simple schema review. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Give me a complete overview of this patient dataset. Include:
- Total number of patients and total number of records (are there multiple records per patient?)
- Key demographic columns: age distribution, sex breakdown, race/ethnicity if present
- Date range of the data and what time period it covers
- Clinical identifiers present: patient ID, encounter ID, admission ID
- Key clinical columns and their data types: diagnoses, procedures, medications, lab values, vitals
- Missing values per column (%)

Flag any immediate data quality concerns specific to healthcare data:
- Implausible clinical values (e.g. age > 120, heart rate = 0, negative lab values)
- Patients with unusually high record counts that may indicate data duplication
- Date inconsistencies (discharge before admission, future dates) 
```

## When to use this prompt 
Use case 01 
when you first receive a new patient-level extract and need to understand its structure 
Use case 02 
when you need to confirm whether records are unique by patient, encounter, or admission 
Use case 03 
when you want a healthcare-specific data quality screen before deeper analysis 
Use case 04 
when you are preparing a handoff note for analysts, clinicians, or data engineers 

## What the AI should return 

A structured dataset overview with patient and record counts, key identifiers, major clinical domains, date coverage, missingness profile, and a short list of immediate healthcare-specific data quality concerns. 

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
