# Anonymization and Pseudonymization Assessment *AI Prompt *

Assess whether this data is truly anonymized or only pseudonymized, and evaluate the re-identification risk. Dataset: {{dataset_description}} Claimed status: {{claimed_status}}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Assess whether this data is truly anonymized or only pseudonymized, and evaluate the re-identification risk.

Dataset: {{dataset_description}}
Claimed status: {{claimed_status}} (anonymized / pseudonymized / de-identified)
Intended use: {{intended_use}}

This distinction is critical: anonymized data falls outside GDPR's scope. Pseudonymized data is still personal data.

1. Definitions and legal significance:

 Anonymization (GDPR Recital 26):
 - Data that 'cannot be attributed to an identified or identifiable natural person'
 - The key test: is re-identification reasonably likely, taking into account all means reasonably likely to be used?
 - If truly anonymous: GDPR does not apply → can be used freely, shared openly, retained indefinitely
 - Caveat: near-impossible to prove true anonymization for complex datasets

 Pseudonymization (GDPR Art. 4(5)):
 - Data that 'can no longer be attributed to a specific data subject without the use of additional information'
 - Additional information (e.g. key linking pseudonym to identity) must be kept separately
 - Still personal data under GDPR — but reduces risk and is encouraged as a security measure
 - Examples: replacing name with a hash or random token, while retaining age and zip code

2. Re-identification risk evaluation:

 Apply the ICO's three-part test for anonymization:
 - Singling out: can you isolate one or more records that identify an individual?
 - Linkability: can you link records relating to the same individual or group?
 - Inference: can you deduce information about an individual with high probability?

 Specific techniques to assess:

 k-Anonymity:
 - For each combination of quasi-identifiers, at least k records share the same values
 - k = 1: not anonymous (individual is unique in the dataset)
 - Minimum acceptable k: typically 5 for general use, 10+ for sensitive data
 - Compute k for this dataset across the most identifying quasi-identifier combinations

 l-Diversity:
 - Extension of k-anonymity: within each equivalence class, the sensitive attribute has at least l distinct values
 - Protects against homogeneity attacks (all k records in a group share the same sensitive value)

 t-Closeness:
 - The distribution of the sensitive attribute in each group is close (within threshold t) to the distribution in the full dataset
 - Prevents skewness attacks

 Differential Privacy:
 - Mathematical guarantee: adding or removing one individual's record changes the output by at most a factor of e^ε
 - ε (epsilon): privacy budget. Lower ε = stronger privacy, less utility.
 - Ask: has differential privacy noise been applied? What is the epsilon value?

3. Common pseudo-anonymization mistakes:
 - Hashing without salting: SHA-256 of 'john.doe@email.com' is easily reversed by dictionary attack
 - Truncating postal codes: 5-digit zip may still be unique for small populations
 - Aggregation without k-anonymity: 'CEO of Company X, age 52, female' is identifiable
 - Releasing multiple 'anonymized' datasets that can be joined to re-identify
 - Unique record counts: if only 3 people in the dataset have a given combination, they are identifiable

4. Assessment verdict:
 - Is this data anonymized (GDPR does not apply) or pseudonymized (GDPR applies)?
 - If claimed to be anonymized: what is the re-identification risk level? (Negligible / Low / Medium / High)
 - What additional steps would be needed to achieve a defensible anonymization claim?

Return: anonymization vs pseudonymization classification, k-anonymity calculation, re-identification risk rating, specific vulnerabilities identified, and recommended additional protections. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin privacy impact and risk work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Privacy Impact and Risk or the wider Compliance & Privacy Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Definitions and legal significance:, Data that 'cannot be attributed to an identified or identifiable natural person', The key test: is re-identification reasonably likely, taking into account all means reasonably likely to be used?. The final answer should stay clear, actionable, and easy to review inside a privacy impact and risk workflow for compliance & privacy analyst work. 

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

Once you have the first result, continue deeper with related prompts in Privacy Impact and Risk.
