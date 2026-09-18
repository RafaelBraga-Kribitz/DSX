# DS Skill System — Complete Folder Tree & Architecture

Senior Data Scientist emulation for business/marketing/product/industry contexts.
One master orchestrator, six agents, atomic skills per sub-routine.

---

## Invocation

```
/data-science   ← invoke the master orchestrator (SKILL.md)
```

The orchestrator reads your request, classifies it in <20 words,
and routes to the right agent. You never call agents or skills directly
unless you know exactly which sub-routine you need.

---

## Folder Tree

```
data-science/
│
├── SKILL.md                         ← MASTER ORCHESTRATOR (entry point)
├── README.md                        ← This file
│
├── reference/
│   └── decision-trees.md            ← All 7 Mermaid decision trees
│
├── agents/                          ← Autonomous Claude sub-agents
│   │                                   (each handles a full phase)
│   ├── ds-intake/
│   │   └── SKILL.md                 ← Clarify ambiguous requests
│   ├── ds-eda/
│   │   └── SKILL.md                 ← Data quality + EDA gate
│   ├── ds-analysis/
│   │   └── SKILL.md                 ← Descriptive/diagnostic/prescriptive
│   ├── ds-modeling/
│   │   └── SKILL.md                 ← Predictive + ML models
│   ├── ds-qa/
│   │   └── SKILL.md                 ← Validation + confidence assignment
│   └── ds-communication/
│       └── SKILL.md                 ← Narrative + format + visualization
│
└── skills/                          ← Atomic sub-routines (invoked by agents)
    │
    ├── 01-intake/
    │   ├── problem-framing/         ← Workshop unclear questions
    │   ├── requirements/            ← Structured requirements gathering
    │   └── scope-definition/        ← Document final scope
    │
    ├── 02-data/
    │   ├── data-discovery/          ← Find data sources for a question
    │   ├── data-quality-audit/ ★    ← 5-dimension quality scorecard
    │   ├── sql-extraction/          ← Write + validate SQL for analysis
    │   └── data-catalog/            ← Document dataset metadata
    │
    ├── 03-eda/
    │   ├── profiling/               ← Shape, types, basic stats (fast)
    │   ├── anomaly-detection/       ← Outlier identification + classification
    │   └── distribution-check/      ← Normality, skewness, parametric gate
    │
    ├── 04-analysis/
    │   │
    │   ├── descriptive/
    │   │   ├── metrics-snapshot/ ★  ← Quick KPI status with verdict
    │   │   ├── cohort-analysis/     ← Retention/behavior over time
    │   │   ├── funnel-analysis/     ← Conversion step analysis
    │   │   └── time-series-descriptive/ ← Trend + seasonality description
    │   │
    │   ├── diagnostic/
    │   │   ├── root-cause/ ★        ← 4-step decomposition + attribution
    │   │   ├── segmentation/        ← Segment the change by dimension
    │   │   ├── drill-down/          ← Time-point + filter investigation
    │   │   └── causal-check/        ← Ladder from correlation to causation
    │   │
    │   ├── predictive/
    │   │   ├── forecasting/         ← Time series forecast (Prophet/ARIMA)
    │   │   ├── churn-prediction/    ← Binary classifier for churn
    │   │   └── regression-modeling/ ← Feature engineering + model selection
    │   │
    │   └── prescriptive/
    │       ├── ab-test-design/ ★    ← Hypothesis + power + stop rules
    │       ├── ab-test-analysis/    ← SRM + significance + ship/rollback
    │       └── optimization-framing/ ← When RCT not possible
    │
    ├── 05-validation/
    │   ├── qa-checklist/            ← Systematic pre-delivery checklist
    │   ├── assumptions-log/         ← Document violated assumptions
    │   ├── sanity-check/            ← Smell test + simple explanation
    │   └── peer-review/             ← High-stakes second review
    │
    └── 06-communication/
        ├── data-narrative/          ← Write the analysis story
        ├── visualization-spec/      ← Chart selection + design rules
        ├── presentation-builder/    ← BLUF structure for executives
        └── dashboard-spec/          ← Recurring monitoring spec

★ = most commonly invoked, highest ROI to read first
```

---

## Delegation Flow

```
Request
  └─→ ORCHESTRATOR (classify + route)
        ├─→ ds-intake agent          (if ambiguous)
        │     └─→ skills/01-intake/*
        ├─→ ds-eda agent             (always, gates analysis)
        │     └─→ skills/02-data/* + skills/03-eda/*
        ├─→ ds-analysis agent        (descriptive/diagnostic/prescriptive)
        │     └─→ skills/04-analysis/{track}/*
        ├─→ ds-modeling agent        (predictive track only)
        │     └─→ skills/04-analysis/predictive/*
        ├─→ ds-qa agent              (always, before communication)
        │     └─→ skills/05-validation/*
        └─→ ds-communication agent   (final delivery)
              └─→ skills/06-communication/*
```

---

## Decision Trees (reference/decision-trees.md)

| DT | Name | Run when |
|----|------|----------|
| DT-1 | Intake & Problem Framing | Question is ambiguous |
| DT-2 | EDA & Data Quality | Always (before analysis) |
| DT-3 | Analysis Track Selection | After EDA passes |
| DT-4 | Validation & QA | Before any stakeholder delivery |
| DT-5 | Communication & Delivery | Formatting final output |
| DT-6 | Predictive / Modeling | Forecasting or ML requested |
| DT-7 | A/B Test Design & Analysis | Experiment work |

---

## Token Efficiency Rules

1. **Orchestrator stays light** — classifies in ≤20 words, never analyzes
2. **One agent per phase** — no two agents run simultaneously
3. **Skills are atomic** — each skill has a single output format, ≤2K tokens
4. **EDA report is the handoff** — agents don't re-read raw data, only EDA report
5. **Quick-look mode** — if time_constraint=quick, skip full EDA, acknowledge caveat
6. **Context packages** — structured YAML passed between agents, not free text

---

## Existing Skills Integration

These skills from `~/.claude/skills/` are plug-in compatible with this system:

| This system calls | Existing skill |
|------------------|---------------|
| `skills/04-analysis/descriptive/cohort-analysis/` | `cohort-analysis` |
| `skills/04-analysis/prescriptive/ab-test-analysis/` | `ab-test-analysis` |
| `skills/04-analysis/descriptive/funnel-analysis/` | `funnel-analysis` |
| `skills/06-communication/visualization-spec/` | `visualization-builder` |
| `skills/06-communication/data-narrative/` | `data-narrative-builder` |
| `skills/06-communication/dashboard-spec/` | `dashboard-specification` |
| `skills/02-data/data-quality-audit/` | `data-quality-audit` |
| `skills/04-analysis/diagnostic/segmentation/` | `segmentation-analysis` |
| `skills/05-validation/assumptions-log/` | `analysis-assumptions-log` |
| `skills/05-validation/qa-checklist/` | `analysis-qa-checklist` |
