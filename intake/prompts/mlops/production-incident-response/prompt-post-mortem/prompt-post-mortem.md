# Incident Post-Mortem *AI Prompt *

This prompt writes a blameless post-mortem for an ML incident, focusing on timeline, causes, impact, lessons, and tracked action items. It is useful for organizations that want learning-oriented incident reviews rather than one-off summaries. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write a blameless post-mortem for this ML model incident.

Incident summary: {{incident_summary}}
Model affected: {{model_name}}
Incident duration: {{duration}}
Business impact: {{business_impact}}

Blameless post-mortem principles:
- The goal is to learn and prevent recurrence, not to assign blame
- People acted with good intentions given the information they had at the time
- Focus on system and process failures, not individual failures

1. Incident summary:
 - What happened? (2–3 sentences, suitable for a non-technical audience)
 - When did it start? When was it detected? When was it resolved?
 - Who was involved in the response?

2. Timeline (chronological):
 - [timestamp] — Event description
 - Include: first symptom, alert triggered, incident declared, triage started, root cause identified, mitigation applied, full resolution

3. Root cause analysis:
 - What was the immediate cause? (What triggered the incident?)
 - What were the contributing causes? (Five Whys or similar)
 - What allowed this to happen? (System design, monitoring gap, process gap)

4. Impact assessment:
 - User impact: how many users or requests were affected?
 - Business impact: estimated revenue impact, SLA violations, customer complaints
 - Data impact: any data corruption or loss?

5. What went well:
 - What detection, response, or mitigation actions worked effectively?

6. What went wrong:
 - What slowed detection, diagnosis, or resolution?

7. Action items (the most important section):
 - For each: what will be done, who owns it, and by when
 - Categorize: immediate fix, monitoring improvement, process improvement, systemic fix
 - All action items must be in a tracking system within 24 hours of the post-mortem

Return: complete blameless post-mortem document. 
```

## When to use this prompt 
Use case 01 
when an ML incident needs formal retrospective documentation 
Use case 02 
when root cause and contributing factors should be recorded without blame 
Use case 03 
when action items need owners and deadlines 
Use case 04 
when post-incident communication should work for both technical and non-technical readers 

## What the AI should return 

A complete blameless ML incident post-mortem document with summary, timeline, root cause analysis, impact, lessons, and action items. 

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

Once you have the first result, continue deeper with related prompts in Production Incident Response.
