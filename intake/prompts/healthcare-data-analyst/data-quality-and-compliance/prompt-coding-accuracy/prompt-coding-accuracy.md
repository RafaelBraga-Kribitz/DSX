# Coding Accuracy Analysis *AI Prompt *

This prompt evaluates clinical coding quality from both a documentation specificity and revenue optimization perspective. It looks at CC/MCC capture, unspecified coding, DRG intensity, and sequencing concerns that can materially affect case mix and reimbursement. It is best used when reviewing coding performance, CDI program impact, or suspected undercoding opportunities. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: coding quality scorecard, estimated revenue impact of undercoding, and top 5 coding improvement opportunities. 
```

## When to use this prompt 
Use case 01 
when coding leaders want to review documentation specificity and revenue capture 
Use case 02 
when low CMI or low CC/MCC rates suggest possible undercoding 
Use case 03 
when unspecified diagnoses are being overused 
Use case 04 
when you need a prioritized list of coding improvement opportunities with financial impact 

## What the AI should return 

A coding accuracy scorecard with CC/MCC capture, specificity analysis, DRG/CMI review, suspected sequencing issues, revenue impact estimate, and the top coding improvement opportunities. 

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
