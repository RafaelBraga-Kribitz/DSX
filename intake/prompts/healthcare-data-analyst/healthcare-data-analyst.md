# Healthcare Data Analyst *AI Prompts *

Healthcare Data Analyst AI prompt library with 25 prompts in 6 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 6 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Healthcare Data Analyst prompt categories 
6 categories 
### Clinical Outcomes Analysis 

AI prompts for clinical outcomes analysis, treatment comparison, intervention evaluation, and healthcare performance measurement. 
5 prompts Complication Rate Tracking Length of Stay Analysis → 
### Patient Data Exploration 

AI prompts for patient data exploration, healthcare datasets, distributions, data completeness, and clinical record analysis. 
5 prompts Demographics Profile Diagnosis Code Analysis → 
### Cohort Analysis 

AI prompts for cohort analysis, retention tracking, user segmentation, longitudinal analysis, and population comparison. 
4 prompts Chronic Disease Cohort Comorbidity Burden Analysis → 
### Data Quality and Compliance 

AI prompts for data quality with compliance, including privacy, governance, regulatory requirements, and audit-ready data workflows. 
4 prompts Clinical Data Quality Audit Coding Accuracy Analysis → 
### Operational Analytics 

AI prompts for operational analytics, efficiency analysis, resource utilization, throughput, and performance optimization. 
4 prompts Bed Utilization and Capacity Discharge Timing Analysis → 
### Reporting and Communication 

AI prompts for healthcare reporting, stakeholder communication, narrative summaries, and clear presentation of insights. 
3 prompts Clinical Executive Summary Population Health Report Chain → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 25 Clinical Outcomes Analysis 5 Patient Data Exploration 5 Cohort Analysis 4 Data Quality and Compliance 4 Operational Analytics 4 Reporting and Communication 3 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **25 **of 25 prompts 
## Clinical Outcomes Analysis 
5 prompt s Clinical Outcomes Analysis Intermediate Prompt 01 
### Complication Rate Tracking 
Identify and analyze hospital-acquired complications (HACs) and adverse events in this dataset.

1. Identify the following HAC categories using ICD-10 codes:
 - Hospital-acquired pressure injuries (POA flag = N for HAPI codes)
 - Catheter-associated urinary tract infections (CAUTI)
 - Central line-associated bloodstream infections (CLABSI)
 - Surgical site infections (SSI)
 - Falls with injury
 - Venous thromboembolism (DVT/PE) with POA = N
2. Calculate HAC rate per 1,000 patient days for each category
3. Compare to CMS national rates and flag any HAC above the 75th percentile nationally
4. Analyze HACs by:
 - Unit or department
 - Shift (if time data is available)
 - Patient risk factors (age, LOS, comorbidities)
5. Calculate the estimated financial impact: average CMS HAC payment reduction × number of HAC cases

Return a HAC dashboard table with rates, benchmarks, and estimated financial impact per category. Copy prompt View page Show more ↓ Clinical Outcomes Analysis Intermediate Prompt 02 
### Length of Stay Analysis 
Analyze inpatient length of stay (LOS) in this dataset.

1. Calculate overall LOS statistics: mean, median, std, 25th, 75th, 90th, 95th percentiles
2. Use median rather than mean as the primary metric — LOS is right-skewed and mean is sensitive to outliers
3. Break down median LOS by:
 - Primary diagnosis (top 15 conditions)
 - Service line or unit
 - Discharge disposition (home, SNF, rehab, AMA, death)
 - Payer type
 - ICU vs non-ICU stay
4. Identify geometric mean LOS per DRG and compare to CMS national geometric mean LOS benchmarks
5. Flag outlier stays: admissions with LOS > 3× the condition-specific median
6. Analyze LOS trends over time: is average LOS increasing or decreasing by quarter?
7. Estimate excess days: for outlier stays, how many total bed-days were consumed beyond the expected LOS?

Return a LOS breakdown table and a trend chart by month or quarter. Copy prompt View page Show more ↓ Clinical Outcomes Analysis Intermediate Prompt 03 
### Mortality Analysis 
Analyze inpatient mortality in this dataset.

1. Calculate crude in-hospital mortality rate: deaths / total admissions
2. Break down mortality rate by:
 - Primary diagnosis category
 - Age group (especially 65+, 75+, 85+)
 - ICU vs non-ICU admission
 - Elective vs emergency admission
 - Day of week of admission (weekend effect on mortality is well-documented)
3. Compute case mix index (CMI) adjusted mortality if DRG data is available
4. Compare condition-specific mortality rates to national benchmarks:
 - Sepsis: national mortality ~15–20%
 - AMI: national in-hospital mortality ~5–6%
 - Stroke: national in-hospital mortality ~5–8%
5. Analyze time to death distribution: what % of deaths occur within 24 hours, 48 hours, 7 days, and 30 days of admission?
6. Identify the top 5 conditions with mortality rates significantly above benchmark

Return a mortality summary table with benchmark comparisons and flag any rate that exceeds 1.5× the national benchmark. Copy prompt View page Show more ↓ Clinical Outcomes Analysis Advanced Chain 04 
### Outcomes Benchmarking Chain 
Step 1: Calculate observed rates for the top 5 clinical outcome metrics: 30-day readmission, in-hospital mortality, LOS, HAC rate, and discharge to home rate.
Step 2: Risk-adjust each metric using available patient demographics and comorbidities (age, sex, Elixhauser or Charlson comorbidity index, admission type, payer). Calculate expected rates.
Step 3: Compute the observed-to-expected (O/E) ratio for each metric. O/E > 1 indicates worse than expected performance; O/E < 1 indicates better.
Step 4: Compare O/E ratios to CMS national benchmarks and rank the facility's performance percentile for each metric.
Step 5: Identify the 3 metrics with the worst O/E ratios. For each, drill down to the top 3 contributing patient segments or conditions.
Step 6: Write a performance summary report: overall standing, top achievements, priority improvement areas, and recommended next analytical steps. Copy prompt View page Show more ↓ Clinical Outcomes Analysis Beginner Prompt 05 
### Readmission Rate Analysis 
Analyze 30-day hospital readmission rates in this dataset.

1. Define readmission: any inpatient admission within 30 days of a prior discharge for the same patient
2. Calculate:
 - Overall 30-day readmission rate
 - 7-day and 90-day readmission rates for comparison
3. Break down readmission rates by:
 - Primary diagnosis category (top 10 conditions)
 - Service line or department
 - Payer type
 - Age group (10-year bands)
 - Day of week of original discharge (are Friday/weekend discharges more likely to readmit?)
4. Identify the top 10 diagnosis pairs: original admission diagnosis vs readmission diagnosis
5. Compare your readmission rate to CMS national benchmarks for the top conditions (AMI, heart failure, pneumonia, COPD, hip/knee replacement, CABG)

Flag any condition or patient segment with a readmission rate more than 2× the overall average. Copy prompt View page Show more ↓ 
## Patient Data Exploration 
5 prompt s Patient Data Exploration Beginner Prompt 01 
### Demographics Profile 
Create a comprehensive demographic profile of the patient population in this dataset.

1. Age distribution: histogram with 10-year age bands, mean, median, and IQR
2. Sex/gender breakdown: count and percentage
3. Race and ethnicity breakdown if available: count, percentage, and flag if >10% are recorded as 'Unknown' or 'Other'
4. Insurance/payer mix: breakdown by payer type (Medicare, Medicaid, Commercial, Self-pay, Other)
5. Geographic distribution: by zip code, county, or state if available — identify top 10 areas by patient volume
6. Socioeconomic indicators if present: area deprivation index, social determinants of health flags

Compare this population to national or regional benchmarks where possible.
Flag any demographic group that is underrepresented and may affect generalizability of findings. Copy prompt View page Show more ↓ Patient Data Exploration Intermediate Prompt 02 
### Diagnosis Code Analysis 
Analyze the diagnosis codes (ICD-10-CM) in this dataset.

1. Count the total number of unique ICD-10 codes present
2. Show the top 20 most frequent primary diagnoses with code, description, count, and % of encounters
3. Group diagnoses by ICD-10 chapter (first 3 characters) — what are the top 5 disease categories?
4. Check coding quality:
 - What % of diagnoses use unspecified codes (codes ending in '9' or containing 'unspecified')? High rates suggest poor coding specificity.
 - Are there any invalid or non-existent ICD-10 codes?
 - Is there a mix of ICD-9 and ICD-10 codes?
5. Identify the top 10 comorbidity pairs — which two diagnoses most frequently appear together for the same patient?
6. Flag any patients with an unusually high number of diagnosis codes per encounter (>15 codes may indicate upcoding) Copy prompt View page Show more ↓ Patient Data Exploration Intermediate Prompt 03 
### Lab Values Distribution 
Analyze the distribution of laboratory values in this dataset.

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

Return a lab profile table and flag any lab with more than 30% critical or implausible values. Copy prompt View page Show more ↓ Patient Data Exploration Beginner Prompt 04 
### Patient Dataset Overview 
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
- Date inconsistencies (discharge before admission, future dates) Copy prompt View page Show more ↓ Patient Data Exploration Intermediate Prompt 05 
### Vital Signs Exploration 
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

Return a vital signs summary table with a clinical interpretation note for any metric where more than 10% of readings fall outside normal range. Copy prompt View page Show more ↓ 
## Cohort Analysis 
4 prompt s Cohort Analysis Beginner Prompt 01 
### Chronic Disease Cohort 
Build and profile a chronic disease patient cohort from this dataset.

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

Return a cohort definition table and a summary profile comparing cohort vs non-cohort patients. Copy prompt View page Show more ↓ Cohort Analysis Intermediate Prompt 02 
### Comorbidity Burden Analysis 
Calculate and analyze the comorbidity burden of patients in this dataset.

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

Return a comorbidity burden table, CCI distribution chart, and outcomes by CCI category. Copy prompt View page Show more ↓ Cohort Analysis Intermediate Prompt 03 
### High Utilizer Identification 
Identify and profile high utilizer patients — those consuming a disproportionate share of healthcare resources.

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

Return a high utilizer profile and the potential savings if average utilization were reduced by 20% for this group. Copy prompt View page Show more ↓ Cohort Analysis Advanced Chain 04 
### Readmission Risk Cohort Chain 
Step 1: Define the index admission cohort — all inpatient discharges in the study period, excluding deaths, AMA discharges, and transfers to other acute facilities.
Step 2: Calculate the LACE score for each patient (Length of stay, Acuity of admission, Charlson Comorbidity Index, ED visits in past 6 months). Classify: low risk (0–4), moderate (5–9), high (≥10).
Step 3: Validate LACE score performance against actual 30-day readmissions in the dataset: compute AUC-ROC, sensitivity, and specificity at each risk threshold.
Step 4: Profile the high-risk cohort (LACE ≥10): size, top diagnoses, demographics, payer mix, and social risk factors.
Step 5: Identify which high-risk patients were not readmitted — what interventions or patient factors may have protected them?
Step 6: Prioritize the top 50 patients by readmission risk for care management outreach. Return a ranked list with LACE score, primary diagnosis, payer, and suggested intervention type. Copy prompt View page Show more ↓ 
## Data Quality and Compliance 
4 prompt s Data Quality and Compliance Beginner Prompt 01 
### Clinical Data Quality Audit 
Audit the quality of this clinical dataset and return a structured quality report.

Check each of the following dimensions:

1. Completeness: which required clinical fields are missing?
 - Critical fields (flag if >5% missing): patient_id, admission_date, discharge_date, primary_diagnosis, discharge_disposition
 - Important fields (flag if >15% missing): attending_physician, procedure_codes, payer, age, sex

2. Validity: are clinical values within plausible ranges?
 - Negative LOS (discharge before admission)
 - Age > 120 or < 0
 - Invalid ICD-10 codes (not in official code list)
 - Discharge disposition codes that don't exist in standard NUBC taxonomy

3. Consistency: are related fields logically consistent?
 - Death as discharge disposition but no mortality flag
 - Pediatric patients with adult diagnoses (and vice versa)
 - Procedure dates outside the admission window

4. Timeliness: when was the data last updated? Are there records with suspiciously old last-modified dates?

Return: quality scorecard with pass/fail per dimension, top 10 specific issues, and estimated % of records affected by each issue. Copy prompt View page Show more ↓ Data Quality and Compliance Advanced Prompt 02 
### Coding Accuracy Analysis 
Analyze the accuracy and completeness of clinical coding in this dataset.

1. CC/MCC capture rate:
 - What % of cases have at least one Complication or Comorbidity (CC) or Major CC (MCC) coded?
 - Compare to expected national capture rates by DRG (most DRGs have 60–75% CC/MCC rates)
 - Low CC/MCC capture may indicate undercoding and lost revenue

2. Query rate analysis (if CDI query data is available):
 - What % of admissions triggered a Clinical Documentation Improvement query?
 - What is the agreement rate (physician accepted the suggested code)?

3. DRG optimization check:
 - For the top 20 DRGs by volume, calculate the case mix index (CMI)
 - Compare CMI to national geometric mean — significantly lower CMI may indicate undercoding

4. Specificity analysis:
 - What % of diagnoses use unspecified codes when a more specific code exists?
 - Flag the top 10 unspecified codes most frequently used and their more specific alternatives

5. Sequencing errors:
 - Identify cases where the principal diagnosis may be incorrectly sequenced (e.g. symptom coded as principal when the underlying condition is also coded)

Return: coding quality scorecard, estimated revenue impact of undercoding, and top 5 coding improvement opportunities. Copy prompt View page Show more ↓ Data Quality and Compliance Intermediate Prompt 03 
### De-identification Verification 
Verify that this dataset has been properly de-identified in compliance with HIPAA Safe Harbor or Expert Determination standards.

Check for the presence of the 18 HIPAA identifiers:

1. Direct identifiers to scan for:
 - Names: scan all text columns for patterns matching full names
 - Geographic data: zip codes with <20,000 population, full street addresses, city+state combinations that identify small areas
 - Dates: scan for specific dates of birth, death, admission, or discharge that could identify individuals (dates should be shifted or replaced with age/year only)
 - Phone numbers, fax numbers, email addresses
 - Social Security Numbers (pattern: XXX-XX-XXXX)
 - Medical record numbers, health plan numbers, account numbers
 - Certificate/license numbers, vehicle identifiers, device serial numbers
 - URLs and IP addresses
 - Biometric identifiers
 - Full-face photographs
2. Quasi-identifiers: flag any combination of age + zip + sex + rare diagnosis that could re-identify a patient
3. For each identifier found: column name, number of affected rows, severity (direct identifier vs quasi-identifier)

Return a de-identification gap report with recommended remediation for each finding. Copy prompt View page Show more ↓ Data Quality and Compliance Intermediate Prompt 04 
### POA Flag Validation 
Validate the Present on Admission (POA) flags in this dataset.

POA flags indicate whether a diagnosis existed before the hospital admission. Correct POA coding is critical for quality reporting and HAC identification.

1. Check completeness: what % of secondary diagnoses have a POA flag? CMS requires POA for all diagnoses on inpatient claims.
2. Check value distribution: what % are Y (yes), N (no), U (unknown), W (clinically undetermined), 1 (exempt)?
 - Flag if >10% are U or W — this indicates documentation gaps
3. Validate HAC-relevant codes: for conditions that are CMS Hospital-Acquired Conditions (e.g. CAUTI, CLABSI, pressure injuries, DVT), verify that POA = N or W is correctly assigned
4. Check for impossible POA assignments:
 - Chronic diseases like diabetes, COPD, hypertension should almost never have POA = N
 - Flag any case where a common chronic condition has POA = N (likely a coding error)
5. Calculate the financial impact: how many cases have HAC conditions with POA = N, triggering potential CMS payment reductions?

Return a POA validation report with error rates per condition category and estimated payment impact. Copy prompt View page Show more ↓ 
## Operational Analytics 
4 prompt s Operational Analytics Intermediate Prompt 01 
### Bed Utilization and Capacity 
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

Return: occupancy dashboard by unit, peak demand heatmap, and capacity forecast chart. Copy prompt View page Show more ↓ Operational Analytics Intermediate Prompt 02 
### Discharge Timing Analysis 
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

Return: discharge timing histogram, early discharge rate by service and physician, and capacity impact estimate. Copy prompt View page Show more ↓ Operational Analytics Beginner Prompt 03 
### ED Throughput Analysis 
Analyze Emergency Department throughput and flow in this dataset.

1. Calculate key ED flow metrics:
 - Door-to-triage time: arrival to first nursing assessment
 - Door-to-physician time: arrival to first physician contact
 - Door-to-disposition time: arrival to admit/discharge decision
 - Door-to-departure time: total ED LOS
 - Left without being seen (LWBS) rate
 - Left against medical advice (AMA) rate
2. Show 50th, 75th, 90th, and 95th percentile for each time metric
3. Compare to CMS and Joint Commission benchmarks:
 - Door-to-physician: target ≤ 60 minutes (median)
 - Admitted patient ED LOS: target ≤ 360 minutes
4. Break down all metrics by:
 - Hour of day and day of week (heatmap format)
 - ESI triage level (1–5)
 - Admit vs discharge patients
5. Identify the top 3 bottlenecks in the ED flow based on where time is most lost

Return a throughput dashboard with benchmark comparisons and bottleneck analysis. Copy prompt View page Show more ↓ Operational Analytics Advanced Chain 04 
### Staffing Efficiency Chain 
Step 1: Calculate nursing hours per patient day (NHPPD) for each unit by dividing total nursing hours worked by total patient days. Compare to target NHPPD by unit type (ICU: 12–24, Med/Surg: 6–8, Telemetry: 8–10).
Step 2: Identify units with NHPPD significantly above or below target. Above target may indicate overstaffing or high patient acuity; below target may indicate understaffing risk.
Step 3: Analyze overtime usage: what % of total nursing hours are overtime? High overtime (>5%) increases cost and may indicate staffing shortages.
Step 4: Correlate staffing levels with patient outcomes: is there a statistically significant relationship between NHPPD and falls, pressure injuries, or 30-day readmissions on each unit?
Step 5: Identify peak demand hours where actual staffing consistently falls below target nurse-to-patient ratios.
Step 6: Model the cost impact: calculate the cost per patient day at current staffing vs optimized staffing, and the potential savings from better shift scheduling. Copy prompt View page Show more ↓ 
## Reporting and Communication 
3 prompt s Reporting and Communication Beginner Prompt 01 
### Clinical Executive Summary 
Write a clinical performance executive summary based on this dataset for a hospital leadership audience.

The summary should cover exactly 4 sections:

1. Patient Volume & Mix (2–3 sentences)
 - Total admissions, ED visits, and outpatient encounters for the period
 - Key payer mix highlights and any significant shifts vs prior period

2. Quality & Safety Performance (2–3 sentences)
 - 30-day readmission rate vs target and national benchmark
 - Mortality rate and HAC rate vs benchmark
 - Highlight one quality win and one quality concern

3. Operational Efficiency (2–3 sentences)
 - Average LOS vs geometric mean benchmark
 - ED throughput metrics and any capacity concerns
 - Case mix index vs prior period

4. Priority Actions (3 bullet points)
 - Three specific, data-driven recommendations based on the analysis
 - Each bullet: what to do, why (cite a specific number), and who should own it

Tone: concise, direct, evidence-based. No clinical jargon — write for a CFO and CMO audience. Maximum 300 words. Copy prompt View page Show more ↓ Reporting and Communication Advanced Chain 02 
### Population Health Report Chain 
Step 1: Define the population — total attributed patients, demographics breakdown, payer mix, and geographic distribution.
Step 2: Stratify by risk — use available risk scores (HCC RAF score, LACE, or a custom risk model) to classify patients into low, moderate, high, and very high risk tiers. Show size and cost of each tier.
Step 3: Analyze utilization patterns — ED visit rate, hospitalization rate, and preventable admission rate (ACSC conditions) per 1,000 patients for each risk tier.
Step 4: Identify care gaps — for chronic disease patients, what % are meeting evidence-based care standards? (e.g. HbA1c tested in last 12 months for diabetics, annual eye exam, statin prescribed for CAD patients)
Step 5: Calculate total cost of care — PMPM (per member per month) cost by risk tier, broken down by inpatient, ED, outpatient, pharmacy.
Step 6: Write a population health summary report: population profile, risk stratification results, top 5 care gaps with prevalence rates, cost drivers, and three priority interventions with estimated ROI. Copy prompt View page Show more ↓ Reporting and Communication Intermediate Template 03 
### Quality Measure Report 
Generate a quality measure performance report for {{measure_name}} for the period {{reporting_period}}.

The report must include:

1. Measure definition
 - Full measure name and steward (e.g. CMS, TJC, NQF)
 - Numerator definition: {{numerator_definition}}
 - Denominator definition: {{denominator_definition}}
 - Exclusions: {{exclusions}}

2. Performance results
 - Numerator count, denominator count, and measure rate
 - Performance vs target: {{target_rate}}
 - Performance vs national benchmark (50th and 90th percentile)
 - Trend: rate for the current period vs the prior 4 periods

3. Stratification
 - Rate broken down by: service line, payer, age group, and race/ethnicity (for health equity analysis)
 - Flag any subgroup performing more than 10 percentage points below the overall rate

4. Root cause and action plan
 - Top 3 contributing factors to any gap from target
 - Specific improvement actions with owner and due date

Format as a structured report suitable for submission to a quality committee. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
- Terms of Service 
- Privacy Policy 
- AI Policy 
- Licenses 
### AI Data Analysis Examples 

- LLM Benchmark on AI Data Analysis 
- Air Passengers Forecast 
- Iris Classification 
- Customer Churn Prediction 
- Energy Consumption Forecast 
### Resources 

- Example Python notebooks 
- Fix ModuleNotFoundError 
- Glossary 
- Brand 
- Answers 
- ML Algorithm Comparison 
- Research 
- Solutions 
### Products 

- MLJAR Studio 
- MLJAR AutoML 
- AI Data Analyst 
- AutoLab Experiments 
- Mercury 
### Tutorials 

- AutoML in Python: Beginner Tutorial with House Prices 
### Open Source 

- MLJAR AutoML 
- Mercury 
- More ... 
### AI Prompts 

- Prompts for Data Professionals 
- Data Analyst prompts 
- Business Analyst prompts 
- Data Scientist prompts 
- ML Engineer prompts 
- Data Engineer prompts 
- MLOps prompts 
### Compare 

- MLJAR Studio vs Julius 
- MLJAR Studio vs H2O 
- MLJAR Studio vs DataRobot 
- MLJAR Studio vs Jupyter 
- MLJAR Studio vs ChatGPT 
- MLJAR Studio vs Cursor 
### Company 

- Contact us 
- Services 
- About us 
- Blog Made by MLJAR. All rights reserved. Created in 🇵🇱 We ❤ you! 
We collect traffic information to improve the site. 

Data is collected in a privacy-friendly way (IP anonymization, no ads, no cross-site tracking). 
Analytics are only enabled if you accept. 
Read Privacy Policy Reject Accept
