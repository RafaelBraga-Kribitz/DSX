# /mads-help

> Always available. Call at any time.
> Activation: `/mads-help` or "what should I do next?" or "where am I in the workflow?"

---

## Purpose

`mads-help` orients you in the BMADS-MKT workflow, tells you which agents and skills
are available for your current situation, and surfaces the right next step.

It reads the current project state by checking which report artifacts exist in `reports/`.

---

## State Detection Logic

```
If reports/MAB.md does not exist:
  → You are in Phase 0 (not started)
  → Next: Hey Carla / /mads-problem-frame

If reports/MAB.md exists AND reports/DAR.md does not exist:
  → You are in Phase 1 complete, Phase 2 not started
  → Next: Hey Diego / /mads-data-audit

If reports/DAR.md exists AND reports/MSD.md and reports/EP.md do not exist:
  → You are in Phase 2 complete, Phase 3 not started
  → Next: Check MAB project type
    → If Type A/B/C/D/E/F/H: Hey Marco / /mads-model-spec
    → If Type G (experiment): Hey Eva / /mads-experiment-design

If reports/MSD.md or reports/EP.md exists AND models/ is empty:
  → You are in Phase 3 complete, Phase 4 not started
  → Next: Hey Marco / /mads-build

If models/ has a trained model AND reports/IR.md does not exist:
  → You are in Phase 4 complete, Phase 5 not started
  → Next: Hey Petra / /mads-insight-delivery

If reports/IR.md exists AND reports/MonSpec.md does not exist:
  → You are in Phase 5 complete, Phase 6 not started
  → Next: Hey Otto / /mads-deploy-monitor

If reports/MonSpec.md exists:
  → Project is in production
  → Next options: monitor, retrain trigger, new project
```

---

## Full Agent & Skill Reference

| Agent | Activation | Primary skill | Phase |
|-------|-----------|--------------|-------|
| 🎯 Carla | "Hey Carla" | `/mads-problem-frame` | 1: Business Framing |
| 🔍 Diego | "Hey Diego" | `/mads-data-audit` | 2: Data Scoping |
| ⚗️ Eva | "Hey Eva" | `/mads-experiment-design` | 3: Methodology (Experiments) |
| 🧠 Marco | "Hey Marco" | `/mads-model-spec`, `/mads-build` | 3+4: Spec + Build |
| 📊 Petra | "Hey Petra" | `/mads-insight-delivery` | 5: Insight Delivery |
| ⚙️ Otto | "Hey Otto" | `/mads-deploy-monitor` | 6: Deploy & Monitor |

---

## Project Type Quick Reference

| Business question starts with... | Project Type | Lead agent for Phase 3 |
|----------------------------------|-------------|----------------------|
| "Does X cause Y?" | Causal inference | Eva (design) + Marco (build) |
| "Which treatment performs better?" | A/B test | Eva |
| "Who is most likely to do X?" | Propensity model | Marco |
| "How much will we sell?" | Demand forecasting | Marco |
| "Which customers are similar?" | Segmentation | Marco |
| "What does each channel drive?" | Attribution (MTA/MMM) | Marco |
| "What is each customer worth?" | CLV model | Marco |
| "Why did this metric change?" | Decomposition | Marco + Petra |
| "Who should we target to lift X?" | Uplift / causal ML | Eva (design) + Marco (build) |

---

## Common Mistakes

| Situation | What it means | What to do |
|-----------|-------------|-----------|
| Starting to explore data without a MAB | No defined business question | Stop. Go to Carla. |
| Building a model before a DAR | Data quality unknown | Stop. Go to Diego. |
| Splitting train/test after fitting a scaler | Leakage | Refactor immediately. Marco can help. |
| Reporting p < 0.05 without an effect size | Statistical theater | Eva needs to review the results. |
| Shipping a model without a Model Card | No ownership / monitoring | Marco must produce the card before Otto accepts it. |
| "We'll add monitoring later" | Models have no owners or expiry | Otto must be involved before deployment. |

---

## Useful Files to Know

| File | Purpose |
|------|---------|
| `.mads/agents/carla.md` | Carla's full persona, skills, and gate checklist |
| `.mads/agents/diego.md` | Diego's full persona, skills, and gate checklist |
| `.mads/agents/eva.md` | Eva's full persona, skills, and gate checklist |
| `.mads/agents/marco.md` | Marco's full persona, skills, and gate checklist |
| `.mads/agents/petra.md` | Petra's full persona, skills, and gate checklist |
| `.mads/agents/otto.md` | Otto's full persona, skills, and gate checklist |
| `.mads/templates/marketing-analytics-brief.md` | MAB template |
| `.mads/templates/model-spec-doc.md` | MSD template |
| `.mads/templates/experiment-plan.md` | EP template |
| `.mads/templates/insight-report.md` | IR template |
| `.mads/templates/monitoring-spec.md` | MonSpec template |
| `.mads/standards/coding-standards.md` | All coding rules |
| `.mads/standards/repo-structure.md` | Project layout + project type registry |
