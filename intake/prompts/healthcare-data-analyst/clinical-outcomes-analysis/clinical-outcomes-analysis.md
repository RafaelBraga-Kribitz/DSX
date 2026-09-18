# Clinical Outcomes Analysis *AI Prompts *

5 Healthcare Data Analyst prompts in Clinical Outcomes Analysis. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 4 single prompts · 1 chain. 

## AI prompts in Clinical Outcomes Analysis 
5 prompts Intermediate Single prompt 01 
### Complication Rate Tracking 

This prompt focuses on hospital-acquired complications and other adverse events that have both patient safety and reimbursement implications. It combines coding-based identification, rate calculation, benchmark comparison, and financial impact estimation to make the results useful for both quality and operational leaders. It is well suited for monitoring CMS-sensitive safety events and prioritizing prevention work by unit or service. 
Prompt text Identify and analyze hospital-acquired complications (HACs) and adverse events in this dataset.

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

Return a HAC dashboard table with rates, benchmarks, and estimated financial impact per category. Copy prompt Open prompt details Intermediate Single prompt 02 
### Length of Stay Analysis 

This prompt evaluates inpatient length of stay using methods appropriate for heavily right-skewed hospital utilization data. It emphasizes median and geometric mean comparisons, highlights outlier stays, and quantifies excess bed-day consumption beyond expected norms. It is useful for throughput improvement, case management reviews, and benchmarking against national LOS expectations. 
Prompt text Analyze inpatient length of stay (LOS) in this dataset.

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

Return a LOS breakdown table and a trend chart by month or quarter. Copy prompt Open prompt details Intermediate Single prompt 03 
### Mortality Analysis 

This prompt analyzes inpatient mortality in a way that supports both internal performance review and benchmarking. It highlights crude and stratified mortality patterns, time-to-death distributions, and high-risk diagnosis groups that may require deeper case review. It is especially useful when leadership needs to understand whether mortality differences reflect case mix, care processes, or potential quality concerns. 
Prompt text Analyze inpatient mortality in this dataset.

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

Return a mortality summary table with benchmark comparisons and flag any rate that exceeds 1.5× the national benchmark. Copy prompt Open prompt details Advanced Chain 04 
### Outcomes Benchmarking Chain 

This chain prompt provides a structured framework for benchmarking multiple core outcomes rather than examining one metric at a time. It introduces risk adjustment, observed-to-expected comparisons, and percentile-style benchmarking so the analyst can separate raw performance from patient mix effects. It is best used when an organization wants a broad outcomes scorecard with clear priorities for deeper follow-up. 
Prompt text Step 1: Calculate observed rates for the top 5 clinical outcome metrics: 30-day readmission, in-hospital mortality, LOS, HAC rate, and discharge to home rate.
Step 2: Risk-adjust each metric using available patient demographics and comorbidities (age, sex, Elixhauser or Charlson comorbidity index, admission type, payer). Calculate expected rates.
Step 3: Compute the observed-to-expected (O/E) ratio for each metric. O/E > 1 indicates worse than expected performance; O/E < 1 indicates better.
Step 4: Compare O/E ratios to CMS national benchmarks and rank the facility's performance percentile for each metric.
Step 5: Identify the 3 metrics with the worst O/E ratios. For each, drill down to the top 3 contributing patient segments or conditions.
Step 6: Write a performance summary report: overall standing, top achievements, priority improvement areas, and recommended next analytical steps. Copy prompt Open prompt details Beginner Single prompt 05 
### Readmission Rate Analysis 

This prompt is designed to quantify short-term readmissions and identify where readmission risk is concentrated across diagnoses, demographics, and discharge patterns. It supports quality improvement, utilization management, and external benchmarking by comparing internal rates with national references where relevant. It is particularly useful for identifying conditions or care pathways that may benefit from transitional care interventions. 
Prompt text Analyze 30-day hospital readmission rates in this dataset.

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

Flag any condition or patient segment with a readmission rate more than 2× the overall average. Copy prompt Open prompt details 
## Recommended Clinical Outcomes Analysis workflow 
1 
### Complication Rate Tracking 

Start with a focused prompt in Clinical Outcomes Analysis so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Length of Stay Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Mortality Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Outcomes Benchmarking Chain 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
