# Data Quality and Compliance *AI Prompts *

4 Healthcare Data Analyst prompts in Data Quality and Compliance. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 4 single prompts. 

## AI prompts in Data Quality and Compliance 
4 prompts Beginner Single prompt 01 
### Clinical Data Quality Audit 

This prompt is a broad clinical data quality audit tailored to common healthcare data failure modes rather than generic spreadsheet issues. It checks missingness, coding validity, temporal logic, and cross-field consistency in ways that directly affect quality measurement, claims logic, and clinical interpretation. It is most useful before reporting, modeling, or submitting data for operational decision-making. 
Prompt text Audit the quality of this clinical dataset and return a structured quality report.

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

Return: quality scorecard with pass/fail per dimension, top 10 specific issues, and estimated % of records affected by each issue. Copy prompt Open prompt details Advanced Single prompt 02 
### Coding Accuracy Analysis 

This prompt evaluates clinical coding quality from both a documentation specificity and revenue optimization perspective. It looks at CC/MCC capture, unspecified coding, DRG intensity, and sequencing concerns that can materially affect case mix and reimbursement. It is best used when reviewing coding performance, CDI program impact, or suspected undercoding opportunities. 
Prompt text Analyze the accuracy and completeness of clinical coding in this dataset.

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

Return: coding quality scorecard, estimated revenue impact of undercoding, and top 5 coding improvement opportunities. Copy prompt Open prompt details Intermediate Single prompt 03 
### De-identification Verification 

This prompt verifies whether a dataset is sufficiently de-identified for compliant secondary use, sharing, or analysis. It scans for direct HIPAA identifiers as well as combinations of quasi-identifiers that could still create re-identification risk. It is especially useful before data leaves a protected clinical environment or is used in research, analytics sandboxes, or external reporting. 
Prompt text Verify that this dataset has been properly de-identified in compliance with HIPAA Safe Harbor or Expert Determination standards.

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

Return a de-identification gap report with recommended remediation for each finding. Copy prompt Open prompt details Intermediate Single prompt 04 
### POA Flag Validation 

This prompt is designed to validate present-on-admission coding, which is essential for distinguishing pre-existing conditions from complications that occurred during the hospitalization. It helps analysts detect documentation gaps, coding inconsistencies, and HAC-related payment exposure. It is particularly valuable in inpatient quality, coding compliance, and CMS-focused reimbursement reviews. 
Prompt text Validate the Present on Admission (POA) flags in this dataset.

POA flags indicate whether a diagnosis existed before the hospital admission. Correct POA coding is critical for quality reporting and HAC identification.

1. Check completeness: what % of secondary diagnoses have a POA flag? CMS requires POA for all diagnoses on inpatient claims.
2. Check value distribution: what % are Y (yes), N (no), U (unknown), W (clinically undetermined), 1 (exempt)?
 - Flag if >10% are U or W — this indicates documentation gaps
3. Validate HAC-relevant codes: for conditions that are CMS Hospital-Acquired Conditions (e.g. CAUTI, CLABSI, pressure injuries, DVT), verify that POA = N or W is correctly assigned
4. Check for impossible POA assignments:
 - Chronic diseases like diabetes, COPD, hypertension should almost never have POA = N
 - Flag any case where a common chronic condition has POA = N (likely a coding error)
5. Calculate the financial impact: how many cases have HAC conditions with POA = N, triggering potential CMS payment reductions?

Return a POA validation report with error rates per condition category and estimated payment impact. Copy prompt Open prompt details 
## Recommended Data Quality and Compliance workflow 
1 
### Clinical Data Quality Audit 

Start with a focused prompt in Data Quality and Compliance so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Coding Accuracy Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### De-identification Verification 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### POA Flag Validation 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
