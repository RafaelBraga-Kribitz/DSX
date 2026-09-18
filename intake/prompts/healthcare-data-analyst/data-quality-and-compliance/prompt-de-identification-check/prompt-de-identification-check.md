# De-identification Verification *AI Prompt *

This prompt verifies whether a dataset is sufficiently de-identified for compliant secondary use, sharing, or analysis. It scans for direct HIPAA identifiers as well as combinations of quasi-identifiers that could still create re-identification risk. It is especially useful before data leaves a protected clinical environment or is used in research, analytics sandboxes, or external reporting. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return a de-identification gap report with recommended remediation for each finding. 
```

## When to use this prompt 
Use case 01 
when data is being prepared for research, analytics sharing, or sandbox access 
Use case 02 
when you need to verify HIPAA Safe Harbor style de-identification 
Use case 03 
when leadership wants a documented list of residual identifier risks 
Use case 04 
when quasi-identifier combinations may still permit re-identification 

## What the AI should return 

A de-identification gap report listing detected identifiers or quasi-identifiers by column, severity classification, row counts affected, and specific remediation recommendations. 

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

Once you have the first result, continue deeper with related prompts in Data Quality and Compliance.
