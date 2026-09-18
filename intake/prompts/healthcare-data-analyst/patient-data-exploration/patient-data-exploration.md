# Patient Data Exploration *AI Prompts *

5 Healthcare Data Analyst prompts in Patient Data Exploration. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → intermediate levels and 5 single prompts. 

## AI prompts in Patient Data Exploration 
5 prompts Beginner Single prompt 01 
### Demographics Profile 

This prompt is built to characterize who is represented in the dataset and whether the patient population reflects the intended care setting or study use case. It goes beyond simple counts by surfacing payer mix, geography, and social risk indicators that often shape utilization, outcomes, and equity analyses. It also helps identify whether the data may underrepresent certain demographic groups, which matters for benchmarking and generalizability. 
Prompt text Create a comprehensive demographic profile of the patient population in this dataset.

1. Age distribution: histogram with 10-year age bands, mean, median, and IQR
2. Sex/gender breakdown: count and percentage
3. Race and ethnicity breakdown if available: count, percentage, and flag if >10% are recorded as 'Unknown' or 'Other'
4. Insurance/payer mix: breakdown by payer type (Medicare, Medicaid, Commercial, Self-pay, Other)
5. Geographic distribution: by zip code, county, or state if available — identify top 10 areas by patient volume
6. Socioeconomic indicators if present: area deprivation index, social determinants of health flags

Compare this population to national or regional benchmarks where possible.
Flag any demographic group that is underrepresented and may affect generalizability of findings. Copy prompt Open prompt details Intermediate Single prompt 02 
### Diagnosis Code Analysis 

This prompt helps analysts understand how diagnosis coding is being used across encounters and whether the diagnosis data is analytically reliable. It surfaces coding frequency, major disease categories, specificity problems, invalid codes, and common comorbidity combinations that shape both quality reporting and risk stratification. It is useful for both clinical analytics and revenue-cycle oriented reviews of diagnosis documentation quality. 
Prompt text Analyze the diagnosis codes (ICD-10-CM) in this dataset.

1. Count the total number of unique ICD-10 codes present
2. Show the top 20 most frequent primary diagnoses with code, description, count, and % of encounters
3. Group diagnoses by ICD-10 chapter (first 3 characters) — what are the top 5 disease categories?
4. Check coding quality:
 - What % of diagnoses use unspecified codes (codes ending in '9' or containing 'unspecified')? High rates suggest poor coding specificity.
 - Are there any invalid or non-existent ICD-10 codes?
 - Is there a mix of ICD-9 and ICD-10 codes?
5. Identify the top 10 comorbidity pairs — which two diagnoses most frequently appear together for the same patient?
6. Flag any patients with an unusually high number of diagnosis codes per encounter (>15 codes may indicate upcoding) Copy prompt Open prompt details Intermediate Single prompt 03 
### Lab Values Distribution 

This prompt is intended for detailed review of laboratory result columns from both a statistical and clinical perspective. It combines descriptive distribution analysis with reference-range interpretation, critical value screening, and plausibility checks so the analyst can distinguish normal variation from dangerous values or likely data-entry errors. It is especially helpful when lab data will be used for cohort definitions, severity adjustment, or predictive modeling. 
Prompt text Analyze the distribution of laboratory values in this dataset.

For each lab test column:
1. Compute: mean, median, std, min, max, and key percentiles (5th, 25th, 75th, 95th)
2. Show the reference range for each lab (normal range) and calculate:
 - % of values below normal range
 - % of values within normal range
 - % of values above normal range
3. Flag clinically critical values (panic values) — values so extreme they require immediate clinical attention:
 - e.g. potassium < 2.5 or > 6.5 mEq/L, glucose < 40 or > 500 mg/dL, sodium < 120 or > 160 mEq/L
4. Check for implausible values that are likely data entry errors (e.g. hemoglobin of 0 or 500)
5. Show missingness rate per lab — high missingness may indicate the test is only ordered for specific patient types

Return a lab profile table and flag any lab with more than 30% critical or implausible values. Copy prompt Open prompt details Beginner Single prompt 04 
### Patient Dataset Overview 

This prompt is designed for a first-pass assessment of a patient-level healthcare dataset before any downstream analysis begins. It helps the analyst understand whether the file is organized at the patient, encounter, or admission level, what core clinical domains are available, and whether there are obvious data integrity issues that could bias later findings. It is especially useful because healthcare data often mixes repeated encounters, multiple identifiers, and clinically implausible values in ways that are not obvious from a simple schema review. 
Prompt text Give me a complete overview of this patient dataset. Include:
- Total number of patients and total number of records (are there multiple records per patient?)
- Key demographic columns: age distribution, sex breakdown, race/ethnicity if present
- Date range of the data and what time period it covers
- Clinical identifiers present: patient ID, encounter ID, admission ID
- Key clinical columns and their data types: diagnoses, procedures, medications, lab values, vitals
- Missing values per column (%)

Flag any immediate data quality concerns specific to healthcare data:
- Implausible clinical values (e.g. age > 120, heart rate = 0, negative lab values)
- Patients with unusually high record counts that may indicate data duplication
- Date inconsistencies (discharge before admission, future dates) Copy prompt Open prompt details Intermediate Single prompt 05 
### Vital Signs Exploration 

This prompt explores vital sign data with both operational and clinical interpretation in mind. It summarizes distributions, identifies abnormal and impossible readings, and looks for expected physiologic patterns within diagnosis groups such as sepsis. It is especially valuable when vital signs are recorded repeatedly over time and may be used for acuity analysis, deterioration detection, or quality control. 
Prompt text Explore the vital signs data in this dataset.

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

Return a vital signs summary table with a clinical interpretation note for any metric where more than 10% of readings fall outside normal range. Copy prompt Open prompt details 
## Recommended Patient Data Exploration workflow 
1 
### Demographics Profile 

Start with a focused prompt in Patient Data Exploration so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Diagnosis Code Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Lab Values Distribution 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Patient Dataset Overview 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
