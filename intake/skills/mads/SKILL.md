---
name: mads
description: BMADS-MKT framework for Marketing Data Science, BI, and Analytics. Activates the agent roster (Carla, Diego, Eva, Marco, Petra, Otto) for end-to-end marketing DS projects. Use when working on marketing analytics, attribution, churn, CLV, A/B testing, MMM, segmentation, dashboards, insight delivery, or MLOps for marketing models.
when_to_use: marketing analytics, marketing data science, churn model, attribution modeling, MMM, media mix model, A/B test, experiment design, CLV, customer lifetime value, segmentation, clustering, propensity model, data audit, insight report, dashboard spec, model card, mlops, deploy monitor, marketing brief, mads-help, hey carla, hey diego, hey eva, hey marco, hey petra, hey otto
allowed-tools: Read Write Edit Bash Glob Grep
argument-hint: [agent name or skill name, e.g. "carla", "diego", "mads-help"]
---

# BMADS-MKT: Breakthrough Marketing Analytics & Data Science Method

> AI-native framework for end-to-end Marketing Data Science projects.
> Designed for Claude Code. Modeled after the BMAD-METHOD architecture.
> Version: 2.0.0 — with Book-to-Skill, Recursive Improvement, and Storytelling Viz integrations.

---

## How to Use This Framework

**Activate an agent:**
```
Hey Carla, I need to frame a churn prediction problem.
Hey Diego, let's audit the events table for the MMM project.
Hey Eva, design an A/B test for the new email subject line.
Hey Marco, build the CLV model pipeline.
Hey Petra, create the attribution dashboard brief.
Hey Otto, spec the monitoring setup for the propensity model.
```

**Call a skill directly:**
```
/mads-problem-frame
/mads-data-audit
/mads-experiment-design
/mads-model-spec
/mads-insight-delivery
/mads-deploy-monitor
/mads-help
```

**Meta-skills (deeply integrated into all agents):**
```
/book-to-skill <path>     → Convert any PDF/EPUB book into a reusable skill
/recursive-improve        → Analyze agent traces and recursively improve agents
/ratchet                  → Autonomous overnight improvement loop
/benchmark                → Measure agent performance before/after changes
/storytelling-viz         → Produce polished, story-first data visualizations
```

---

## Agent Roster

| Agent | Emoji | Role | Phase | Activation |
|-------|-------|------|-------|------------|
| **Carla** | 🎯 | Marketing Strategist | Business Framing | `Hey Carla` or `/mads-problem-frame` |
| **Diego** | 🔍 | Data Steward | Data Scoping | `Hey Diego` or `/mads-data-audit` |
| **Eva** | ⚗️ | Experiment Designer | Methodology Design | `Hey Eva` or `/mads-experiment-design` |
| **Marco** | 🧠 | DS/ML Engineer | Build & Engineer | `Hey Marco` or `/mads-build` |
| **Petra** | 📊 | Insights Lead | Insight Delivery | `Hey Petra` or `/mads-insight-delivery` |
| **Otto** | ⚙️ | MLOps Engineer | Deploy & Monitor | `Hey Otto` or `/mads-deploy-monitor` |

Agent definitions: `~/.claude/skills/mads/agents/`

---

## Workflow Phases

```
Phase 1: Business Framing      → Marketing Analytics Brief (MAB)
Phase 2: Data Scoping          → Data Audit Report (DAR)
Phase 3: Methodology Design    → Experiment Plan or Model Spec Doc (MSD)
Phase 4: Build & Engineer      → Model Card + Pipeline code + Tests
Phase 5: Insight Delivery      → Insight Report + Dashboard Spec + Visualizations
Phase 6: Deploy & Monitor      → Monitoring Spec + Runbook
```

Each phase produces a named artifact. Artifacts gate the next phase.

---

## Integrated Meta-Skills

### 📚 Book-to-Skill (`/book-to-skill`)
Every agent can learn from books. When a relevant domain book (PDF or EPUB) is available:
- Say `"Hey [Agent], convert this book to a skill"` and provide the path
- Or call `/book-to-skill /path/to/book.pdf [skill-name]` directly
- Extracted frameworks become persistent skills usable across all future sessions
- Especially powerful for: marketing strategy books, causal inference texts, statistics references, attribution methodology papers

### 🔄 Recursive Improvement (`/recursive-improve`)
Every agent can improve itself. After completing project phases:
- Run `/recursive-improve` to analyze execution traces and apply targeted fixes
- Run `/ratchet` for an autonomous overnight improvement loop
- Run `/benchmark` to measure metric deltas before/after changes
- All agents embed instructions to generate traces via `ri.patch()` + `ri.session()`

### 📈 Storytelling Viz (`/storytelling-viz`)
**Petra, Diego, and Marco automatically invoke this skill for every visualization.**
- No chart is produced in this framework without a one-sentence takeaway
- Petra: all insight charts, dashboard previews, executive comms
- Diego: all EDA plots (distributions, correlations, target variable analysis)
- Marco: all model evaluation plots (ROC curves, calibration, feature importance)
- Invocation is mandatory — not optional — for any visual output

---

## Artifact Flow

```
[Business Question]
        ↓
  /mads-problem-frame → MAB.md
        ↓
  /mads-data-audit    → DAR.md
        ↓
  /mads-experiment-design or /mads-model-spec → EP.md or MSD.md
        ↓
  /mads-build         → Model Card + src/ + tests/
        ↓
  /mads-insight-delivery → Insight Report + Dashboard Spec + Visualizations
        ↓
  /mads-deploy-monitor   → Monitoring Spec + Runbook
```

---

## Core Principles

1. Business question first. No model without a signed-off MAB.
2. Data before modeling. A DAR must precede any feature engineering.
3. No leakage, ever. Train/test splits before any transformation is fitted.
4. Metrics defined upfront. Locked in the MAB, not discovered post-hoc.
5. Stakeholder alignment is a deliverable. Insight reports are written artifacts.
6. Models have owners and expiry dates. Every deployed model has monitoring.
7. Reproducibility is non-negotiable. Seeds, versions, lockfiles, relative paths.
8. Visualizations are arguments. Every chart needs a one-sentence thesis (storytelling-viz).
9. Agents learn continuously. Books → skills, traces → improvements (/book-to-skill, /recursive-improve).

---

## Tech Stack Defaults

| Layer | Tools |
|-------|-------|
| Languages | Python 3.11+, SQL (DuckDB, BigQuery, Postgres) |
| Data | pandas, polars, pyarrow, duckdb |
| Modeling | scikit-learn, xgboost, lightgbm, statsmodels, pymc |
| Attribution / Causal | pymc-marketing, DoWhy, CausalImpact |
| Experimentation | scipy.stats, pingouin, pymc |
| Viz & BI | plotly (storytelling-viz), matplotlib, seaborn, Looker Studio / Power BI |
| MLOps | MLflow, Prefect/Airflow, Docker |
| Agent Improvement | recursive-improve (ri.patch, ri.session) |
| Env | uv / poetry, venv |
| Quality | Black, Ruff, pytest, pyright |

---

## Agent Files

- `~/.claude/skills/mads/agents/carla.md`
- `~/.claude/skills/mads/agents/diego.md`
- `~/.claude/skills/mads/agents/eva.md`
- `~/.claude/skills/mads/agents/marco.md`
- `~/.claude/skills/mads/agents/petra.md`
- `~/.claude/skills/mads/agents/otto.md`

## Supporting Files

- `~/.claude/skills/mads/standards/coding-standards.md`
- `~/.claude/skills/mads/standards/repo-structure.md`
- `~/.claude/skills/mads/workflows/mads-help.md`
- `~/.claude/skills/mads/templates/` (MAB, DAR, EP, MSD, IR, MonSpec)
