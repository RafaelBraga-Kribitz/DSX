# Incident Response Chain *AI Prompt *

This chain prompt walks through the full lifecycle of incident response from detection and triage to mitigation, root-cause analysis, recovery verification, and post-mortem. It is useful as a guided template during live incidents and for training responders. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Detection — describe the detection mechanism that triggered this incident. Was it an automated alert, a user report, or proactive monitoring? Note the detection time and any delay between incident start and detection.
Step 2: Triage — work through the triage runbook. Is this a model issue, an infrastructure issue, or a data pipeline issue? What is the initial severity classification (P0/P1/P2/P3)?
Step 3: Immediate mitigation — what can be done in the next 15 minutes to reduce user impact? Options: rollback to previous model, route traffic to a fallback, disable the feature using this model, apply a threshold adjustment.
Step 4: Root cause investigation — with the immediate mitigation in place, investigate the root cause. Use the diagnostic tools: serving logs, feature pipeline logs, model performance metrics, drift dashboard. Apply Five Whys.
Step 5: Permanent fix — design and implement the fix for the root cause. This may take hours or days. It must be tested in staging before re-deployment to production.
Step 6: Recovery and verification — re-deploy the fixed model. Monitor closely for 24 hours: serving metrics, prediction distribution, business metrics. Confirm full recovery.
Step 7: Post-mortem — within 48 hours, write and publish the blameless post-mortem. All action items entered into tracking. Schedule a follow-up review in 2 weeks to verify action items are being completed. 
```

## When to use this prompt 
Use case 01 
when you need a structured response sequence during an ML incident 
Use case 02 
when mitigation and investigation should be separated clearly 
Use case 03 
when recovery must include monitored verification after redeployment 
Use case 04 
when post-mortem completion should be built into the process 

## What the AI should return 

An incident response workflow covering detection, triage, mitigation, investigation, permanent fix, recovery verification, and post-mortem follow-through. 

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
