# Cohort Analysis *AI Prompts *

4 Healthcare Data Analyst prompts in Cohort Analysis. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 3 single prompts · 1 chain. 

## AI prompts in Cohort Analysis 
4 prompts Beginner Single prompt 01 
### Chronic Disease Cohort 

This prompt is designed to define a chronic disease cohort in a defensible, repeatable way before downstream analysis begins. It includes longitudinal inclusion logic, exclusion of weak rule-out signals, and a comparison between cohort and non-cohort patients so the disease population can be understood in clinical and utilization terms. It is useful for registry creation, quality programs, and disease management reporting. 
Prompt text Build and profile a chronic disease patient cohort from this dataset.

Target disease: {{disease}} (e.g. Type 2 Diabetes, Heart Failure, COPD, CKD)

1. Identify cohort inclusion criteria using ICD-10 codes for {{disease}} — list the specific codes used
2. Apply inclusion and exclusion criteria:
 - Include: patients with ≥2 diagnoses of {{disease}} at least 30 days apart (to confirm chronic status)
 - Exclude: patients with only a rule-out or screening code
3. Profile the cohort:
 - Size: how many patients qualify?
 - Demographics: age, sex, payer mix
 - Top comorbidities and their prevalence rates
 - Average number of hospitalizations, ED visits, and outpatient encounters per year
4. Compute disease severity distribution if a severity classification exists (e.g. HbA1c ranges for diabetes, NYHA class for heart failure)
5. Compare cohort demographics and utilization to the non-{{disease}} patient population

Return a cohort definition table and a summary profile comparing cohort vs non-cohort patients. Copy prompt Open prompt details Intermediate Single prompt 02 
### Comorbidity Burden Analysis 

This prompt measures comorbidity burden using recognized clinical scoring systems and ties those scores to outcomes such as length of stay, readmissions, and mortality. It is useful for understanding how illness burden is distributed across the population and how strongly it relates to resource use and risk. It also supports risk adjustment and segmentation for quality or population health analyses. 
Prompt text Calculate and analyze the comorbidity burden of patients in this dataset.

1. Calculate the Charlson Comorbidity Index (CCI) for each patient using their ICD-10 diagnosis codes:
 - Map each ICD-10 code to its CCI weight
 - Sum weights per patient
 - Classify: CCI 0 (no comorbidity), 1–2 (low), 3–4 (moderate), ≥5 (severe)
2. Calculate the Elixhauser Comorbidity Score as an alternative measure
3. Show distribution of CCI scores across the patient population
4. Analyze relationship between CCI and outcomes:
 - Mean LOS by CCI category
 - 30-day readmission rate by CCI category
 - In-hospital mortality rate by CCI category
5. Identify the 10 most common comorbidity combinations (top comorbidity pairs and triples)
6. Map comorbidity burden by age group — show how CCI increases with age

Return a comorbidity burden table, CCI distribution chart, and outcomes by CCI category. Copy prompt Open prompt details Intermediate Single prompt 03 
### High Utilizer Identification 

This prompt identifies patients who drive disproportionate utilization and cost, then profiles what distinguishes them from the broader patient population. It is designed to support care management, population health, and cost-reduction programs by quantifying concentration of resource use and estimating savings scenarios. It is especially helpful when high utilization may be linked to behavioral health, social needs, or fragmented care. 
Prompt text Identify and profile high utilizer patients — those consuming a disproportionate share of healthcare resources.

1. Define high utilizers using these thresholds (adjust based on data):
 - ≥4 ED visits in the past 12 months, OR
 - ≥2 inpatient admissions in the past 12 months, OR
 - Top 5% of patients by total cost of care
2. Calculate what percentage of total visits, bed days, and costs are consumed by high utilizers
3. Profile high utilizers vs the general patient population:
 - Demographics (age, sex, payer mix)
 - Top 10 primary diagnoses
 - Prevalence of behavioral health diagnoses (depression, substance use disorder, anxiety)
 - Prevalence of social determinants of health flags (housing instability, food insecurity)
4. Calculate the average cost per high utilizer vs average patient
5. Identify the top 20 individual patients by total encounters — these are candidates for care management programs

Return a high utilizer profile and the potential savings if average utilization were reduced by 20% for this group. Copy prompt Open prompt details Advanced Chain 04 
### Readmission Risk Cohort Chain 

This chain prompt creates a full readmission-risk workflow centered on the LACE score and actual readmission outcomes. It moves from cohort definition to risk scoring, validation, profiling of high-risk patients, and practical prioritization for outreach. It is particularly helpful for organizations building or evaluating transitional care and readmission prevention programs. 
Prompt text Step 1: Define the index admission cohort — all inpatient discharges in the study period, excluding deaths, AMA discharges, and transfers to other acute facilities.
Step 2: Calculate the LACE score for each patient (Length of stay, Acuity of admission, Charlson Comorbidity Index, ED visits in past 6 months). Classify: low risk (0–4), moderate (5–9), high (≥10).
Step 3: Validate LACE score performance against actual 30-day readmissions in the dataset: compute AUC-ROC, sensitivity, and specificity at each risk threshold.
Step 4: Profile the high-risk cohort (LACE ≥10): size, top diagnoses, demographics, payer mix, and social risk factors.
Step 5: Identify which high-risk patients were not readmitted — what interventions or patient factors may have protected them?
Step 6: Prioritize the top 50 patients by readmission risk for care management outreach. Return a ranked list with LACE score, primary diagnosis, payer, and suggested intervention type. Copy prompt Open prompt details 
## Recommended Cohort Analysis workflow 
1 
### Chronic Disease Cohort 

Start with a focused prompt in Cohort Analysis so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Comorbidity Burden Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### High Utilizer Identification 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Readmission Risk Cohort Chain 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
