# Pre-Mortem Analysis *AI Prompt *

Conduct a pre-mortem analysis of my planned study — assume the study has failed and work backwards to identify what went wrong. Study plan: {{study_plan}} A pre-mortem is a pros... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Conduct a pre-mortem analysis of my planned study — assume the study has failed and work backwards to identify what went wrong.

Study plan: {{study_plan}}

A pre-mortem is a prospective failure analysis. Instead of optimistically planning for success, you assume the study produced null or uninterpretable results and identify the most likely causes.

1. The failure scenarios:

 Scenario A — Null results (no effect found):
 - Was the effect truly absent? Or was the study underpowered to detect it?
 - Was the treatment inadequately implemented (low treatment fidelity)?
 - Was the outcome measured too soon (insufficient follow-up)?
 - Were participants not the right population (wrong target group, too heterogeneous)?
 - Was there contamination between conditions?

 Scenario B — Uninterpretable results (effect found but meaning is unclear):
 - Did the manipulation check fail? (We do not know if the treatment changed the intended mechanism)
 - Did demand characteristics drive results? (Participants responded as they thought we wanted)
 - Was there differential attrition? (The groups who remained are systematically different)
 - Did an unmeasured third variable explain the result?

 Scenario C — Methodological failure:
 - Recruitment shortfall: could not enroll enough participants
 - Protocol deviations: participants or experimenters did not follow the protocol
 - Instrument problems: scale showed poor psychometric properties in this sample
 - Data loss: technical failures, missing data beyond acceptable thresholds

 Scenario D — External invalidity:
 - Results replicate in the lab but not in field settings
 - Results hold for the study sample but not for the target population
 - Results are highly context-specific and do not generalize

2. For each failure scenario:
 - Probability: how likely is this scenario to occur?
 - Impact: if this happens, can the study be salvaged or must it be abandoned?
 - Prevention: what can be done NOW, before data collection, to prevent or detect this?
 - Detection: how would you know during or after the study that this scenario occurred?

3. Protocol modifications from the pre-mortem:
 - List the specific changes to the study protocol that the pre-mortem analysis suggests
 - Include: manipulation checks, fidelity monitoring, attrition tracking, pilot testing

Return: failure scenario analysis, prevention and detection measures, and a revised protocol checklist. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin experimental design and methodology work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Experimental Design and Methodology or the wider Research Scientist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as The failure scenarios:, Was the effect truly absent? Or was the study underpowered to detect it?, Was the treatment inadequately implemented (low treatment fidelity)?. The final answer should stay clear, actionable, and easy to review inside a experimental design and methodology workflow for research scientist work. 

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

Once you have the first result, continue deeper with related prompts in Experimental Design and Methodology.
