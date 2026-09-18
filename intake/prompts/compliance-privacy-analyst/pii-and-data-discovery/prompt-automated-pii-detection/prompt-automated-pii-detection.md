# Automated PII Detection Prompt *AI Prompt *

Design a prompt and validation framework for using LLMs to detect PII in unstructured text at scale. Data type: {{data_type}} (customer emails, support tickets, free-text form f... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a prompt and validation framework for using LLMs to detect PII in unstructured text at scale.

Data type: {{data_type}} (customer emails, support tickets, free-text form fields, documents)
Volume: {{volume}}
Acceptable false negative rate: {{fnr}} (missed PII — lower is better for compliance)

1. The detection prompt (to be applied to each text sample):

 System instruction:
 'You are a privacy compliance assistant. Identify all personally identifiable information (PII) in the following text. Be conservative — when in doubt, flag it.'

 Task instruction:
 'Scan this text and identify every instance of PII. For each instance found:
 - Quote the exact text
 - Classify the PII type: name / email / phone / address / SSN / date-of-birth / financial / health / government-ID / IP-address / username / other
 - Confidence: High (clearly PII) / Medium (likely PII, context-dependent) / Low (possible PII, may be fictional or generic)

 If no PII is found, return: {"pii_found": false}

 Return ONLY a JSON object matching this schema:
 {
 "pii_found": true,
 "instances": [
 {"text": "...", "type": "...", "confidence": "High|Medium|Low", "start_char": N, "end_char": N}
 ]
 }'

2. Sensitivity settings by use case:
 - For compliance scanning (minimize false negatives): flag all Medium and Low confidence instances
 - For redaction workflows (minimize false positives): flag only High confidence instances
 - For audit sampling: flag High + Medium; review Low manually

3. Validation framework:
 - Create a golden test set of 200 labeled text samples (100 with PII, 100 without)
 - Measure: precision, recall, F1 at each confidence threshold
 - Acceptable recall for compliance: ≥ 95% (missing < 5% of true PII)
 - Measure false positive rate: flag non-PII flagged as PII (acceptable up to 15% for initial triage)

4. Known failure modes to test:
 - Fictional PII (novel character names, example data) — should not be flagged
 - Partial PII (first name only with no other context) — judgment call, document the policy
 - PII in non-English text — test language coverage
 - Obfuscated PII (john[at]email[dot]com) — should be flagged
 - PII in code or SQL queries embedded in text

5. Redaction approach (after detection):
 - Replace detected PII with: [REDACTED-{type}] (e.g. [REDACTED-EMAIL])
 - Log: original text hash, PII types found, redaction timestamp, operator ID
 - Never log the actual PII values in the audit log

Return: the detection prompt, JSON schema, validation framework, golden test set design, and redaction specification. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin pii and data discovery work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in PII and Data Discovery or the wider Compliance & Privacy Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as The detection prompt (to be applied to each text sample):, Quote the exact text, Classify the PII type: name / email / phone / address / SSN / date-of-birth / financial / health / government-ID / IP-address / username / other. The final answer should stay clear, actionable, and easy to review inside a pii and data discovery workflow for compliance & privacy analyst work. 

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

Once you have the first result, continue deeper with related prompts in PII and Data Discovery.
