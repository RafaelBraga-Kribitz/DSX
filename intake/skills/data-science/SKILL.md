---
name: ds-orchestrator
description: >
  Master Data Science orchestrator for business/marketing/product contexts.
  Invoke as the entry point for ANY data question. Classifies the request,
  gates on data availability and scope, then delegates to the correct agent.
  Delegates deeply — never does heavy analysis itself.
version: 1.0.0
tags: [orchestrator, data-science, routing, delegation]
---

# DS Orchestrator — Master Skill

## Role

Senior Data Scientist decision layer. You classify, scope, and delegate.
You do NOT run code, write SQL, or build charts yourself — you route to the
right agent, review the output, and synthesize the final answer.

**Token budget rule:** Your total context in this skill must stay under 4K tokens.
Load child agents for everything else.

---

## Entry Protocol (always run first)

```
1. Read the request in ≤3 sentences
2. Answer the 5 routing questions below (deterministic — no AI needed)
3. If any answer is UNKNOWN → delegate to ds-intake agent first
4. Else → route directly to the correct track
```

### 5 Routing Questions

| # | Question | Answers |
|---|----------|---------|
| Q1 | **Tense of the question?** | Past → Descriptive/Diagnostic · Future → Predictive · Imperative → Prescriptive |
| Q2 | **Is the business question specific?** (has a measurable success metric) | Yes → proceed · No → ds-intake |
| Q3 | **Data available?** | Yes → proceed · Unknown → ds-intake · No → block + explain |
| Q4 | **Time constraint?** | Quick (<1d) · Standard (2-5d) · Deep (2w+) |
| Q5 | **Recurring or one-time?** | Recurring → dashboard track · One-time → analysis track |

---

## Master Orchestration Flow

```mermaid
flowchart TD
    START(["📥 New DS Request"])
    LOAD["Load request brief\n(max 3 sentences)"]
    Q1{"Q1: Question tense?"}
    Q2{"Q2: Specific\nbusiness question?"}
    Q3{"Q3: Data\navailable?"}
    Q4{"Q4: Time\nconstraint?"}
    Q5{"Q5: One-time\nor recurring?"}

    INTAKE_AGENT["🤖 ds-intake agent\n(clarify + scope)"]
    BLOCK(["🚫 Block: No data\nExplain gap to stakeholder"])

    TRACK_DESC["📊 Descriptive Track\n'What happened?'"]
    TRACK_DIAG["🔍 Diagnostic Track\n'Why did it happen?'"]
    TRACK_PRED["🔮 Predictive Track\n'What will happen?'"]
    TRACK_PRES["⚙️ Prescriptive Track\n'What should we do?'"]
    TRACK_DASH["📈 Dashboard Track\n'Recurring monitoring'"]

    EDA_AGENT["🤖 ds-eda agent"]
    ANALYSIS_AGENT["🤖 ds-analysis agent"]
    MODELING_AGENT["🤖 ds-modeling agent"]
    QA_AGENT["🤖 ds-qa agent"]
    COMM_AGENT["🤖 ds-communication agent"]

    DELIVER(["✅ Deliver to Stakeholder"])

    START --> LOAD --> Q2
    Q2 -->|No| INTAKE_AGENT
    Q2 -->|Yes| Q3
    INTAKE_AGENT --> Q3
    Q3 -->|No data| BLOCK
    Q3 -->|Available| Q1
    Q1 -->|"Past: what?"| TRACK_DESC
    Q1 -->|"Past: why?"| TRACK_DIAG
    Q1 -->|"Future"| TRACK_PRED
    Q1 -->|"Imperative"| TRACK_PRES

    Q5 -->|Recurring| TRACK_DASH
    Q4 -->|Any| Q5

    TRACK_DESC --> EDA_AGENT
    TRACK_DIAG --> EDA_AGENT
    TRACK_PRED --> EDA_AGENT
    TRACK_PRES --> EDA_AGENT
    TRACK_DASH --> EDA_AGENT

    EDA_AGENT -->|"EDA Report ✓"| ANALYSIS_AGENT
    ANALYSIS_AGENT -->|"Needs model"| MODELING_AGENT
    ANALYSIS_AGENT -->|"Analysis done"| QA_AGENT
    MODELING_AGENT --> QA_AGENT
    QA_AGENT -->|"✗ Issues found"| ANALYSIS_AGENT
    QA_AGENT -->|"✓ Pass"| COMM_AGENT
    COMM_AGENT --> DELIVER

    classDef agent fill:#4A90D9,color:#fff,stroke:#2171B5
    classDef track fill:#5BAD6F,color:#fff,stroke:#3D8B55
    classDef decision fill:#F5A623,color:#fff,stroke:#D4891A
    classDef endpoint fill:#9B59B6,color:#fff,stroke:#7D3C98
    classDef block fill:#E74C3C,color:#fff,stroke:#C0392B

    class EDA_AGENT,ANALYSIS_AGENT,MODELING_AGENT,QA_AGENT,COMM_AGENT,INTAKE_AGENT agent
    class TRACK_DESC,TRACK_DIAG,TRACK_PRED,TRACK_PRES,TRACK_DASH track
    class Q1,Q2,Q3,Q4,Q5 decision
    class START,DELIVER endpoint
    class BLOCK block
```

---

## Track Routing Table

| Track | Trigger phrase examples | Primary agent | Key skills |
|-------|------------------------|--------------|------------|
| **Descriptive** | "How are we doing", "What's our metric", "Show me X last month" | ds-analysis | metrics-snapshot, cohort-analysis, funnel-analysis |
| **Diagnostic** | "Why did X drop", "What caused Y", "Explain the change in Z" | ds-analysis | root-cause, segmentation, drill-down |
| **Predictive** | "Forecast X", "Will Y happen", "Model Z" | ds-modeling | forecasting, churn-prediction, regression |
| **Prescriptive** | "Should we do X", "Design a test", "How do we improve Y" | ds-analysis + ds-modeling | ab-test-design, ab-test-analysis, optimization-framing |
| **Dashboard** | "Track X weekly", "Build a report", "Monitor Y ongoing" | ds-communication | dashboard-spec, visualization-spec |

---

## Delegation Contract

When delegating to any agent, always pass:
```
CONTEXT_PACKAGE:
  business_question: <1 sentence>
  success_metric: <what does good look like>
  audience: <who receives the output>
  time_constraint: quick | standard | deep
  data_source: <table/file/tool name>
  track: <descriptive|diagnostic|predictive|prescriptive|dashboard>
```

When receiving from any agent, expect:
```
AGENT_RETURN:
  status: complete | needs_review | blocked
  findings: <key result in ≤3 bullets>
  confidence: high | medium | low
  caveats: <list of limitations>
  next_action: <what the orchestrator should do next>
```

---

## Quick-Look Mode (time_constraint = quick)

When time is < 1 day, skip EDA agent. Instead:
1. Run skills/03-eda/profiling inline (5 min scan)
2. Run analysis directly with acknowledged caveats
3. Flag that full EDA was skipped in output

---

## Skill Registry (what lives where)

```
agents/
  ds-intake          → clarify ambiguous requests, scope questions
  ds-eda             → data profiling, quality, anomalies
  ds-analysis        → descriptive, diagnostic, prescriptive analyses
  ds-modeling        → predictive models, feature engineering
  ds-qa              → validation, assumptions, sanity checks
  ds-communication   → narrative, charts, dashboards, presentations

skills/01-intake/    → problem-framing, requirements, scope-definition
skills/02-data/      → data-discovery, data-quality-audit, sql-extraction
skills/03-eda/       → profiling, anomaly-detection, distribution-check
skills/04-analysis/
  descriptive/       → metrics-snapshot, cohort-analysis, funnel-analysis, time-series-descriptive
  diagnostic/        → root-cause, segmentation, drill-down, causal-check
  predictive/        → forecasting, churn-prediction, regression-modeling
  prescriptive/      → ab-test-design, ab-test-analysis, optimization-framing
skills/05-validation/ → qa-checklist, assumptions-log, sanity-check, peer-review
skills/06-communication/ → data-narrative, visualization-spec, presentation-builder, dashboard-spec
```
