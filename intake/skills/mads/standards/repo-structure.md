# Repository Structure & Project Type Registry

---

## Standard Repository Layout

```
{project_name}/
│
├── CLAUDE.md                    ← Claude Code instructions (copy from framework)
├── README.md                    ← Setup, reproducibility, folder map, run commands
├── pyproject.toml               ← Dependencies (pinned), tool config (Black, Ruff, pytest)
├── .pre-commit-config.yaml      ← Black, Ruff, nbstripout
├── Makefile                     ← make setup | make lint | make test | make train | make score
│
├── .mads/                       ← Framework files (agents, workflows, templates, standards)
│   ├── agents/
│   ├── workflows/
│   ├── templates/
│   └── standards/
│
├── configs/                     ← YAML configs (no secrets; no hardcoded values)
│   ├── training_config.yaml
│   ├── feature_config.yaml
│   └── monitoring_config.yaml
│
├── data/
│   ├── raw/                     ← Immutable. Never modified after download.
│   ├── interim/                 ← Intermediate outputs (merged, cleaned)
│   └── processed/               ← Model-ready features. Reproducible from src/ + configs/
│
├── models/                      ← Serialized model artifacts
│   ├── CHANGELOG.md             ← Version log: version, date, performance, changes
│   └── {model_name}_v{n}.pkl
│
├── notebooks/                   ← Exploratory/explanatory only. Stripped outputs.
│   ├── 01_eda_{description}.ipynb
│   ├── 02_feature_engineering_{description}.ipynb
│   ├── 03_model_selection_{description}.ipynb
│   └── 04_evaluation_{description}.ipynb
│
├── reports/                     ← Final artifacts (MAB, DAR, MSD, EP, Model Card, IR, MonSpec)
│   ├── MAB.md
│   ├── DAR.md
│   ├── MSD.md
│   ├── EP.md                    ← If experimentation track
│   ├── model_card_{name}_v{n}.md
│   ├── IR.md
│   └── MonSpec.md
│
├── src/
│   └── {project_name}/
│       ├── __init__.py
│       ├── data/
│       │   ├── __init__.py
│       │   ├── loaders.py       ← Functions to load raw data
│       │   └── validators.py    ← Schema validation, null checks, contract checks
│       ├── features/
│       │   ├── __init__.py
│       │   └── feature_pipeline.py  ← Feature engineering functions
│       ├── models/
│       │   ├── __init__.py
│       │   ├── train.py         ← Training loop
│       │   └── predict.py       ← Inference / scoring
│       ├── evaluation/
│       │   ├── __init__.py
│       │   └── metrics.py       ← Metric computation, baseline comparison
│       ├── visualization/
│       │   ├── __init__.py
│       │   └── charts.py        ← Reusable chart functions
│       ├── monitoring/
│       │   ├── __init__.py
│       │   └── drift_detector.py ← PSI, KS test, alert logic
│       └── utils/
│           ├── __init__.py
│           └── helpers.py       ← Shared utilities
│
└── tests/
    ├── conftest.py
    ├── test_validators.py
    ├── test_feature_pipeline.py
    ├── test_train.py
    └── test_predict.py
```

---

## Mandatory README Sections

```markdown
# {Project Name}

## Overview
One paragraph: business question, methodology, output.

## Setup

### Prerequisites
- Python 3.11+
- uv (package manager): `pip install uv`

### Installation
```bash
git clone {repo_url}
cd {project_name}
uv sync                          # installs all pinned dependencies
pre-commit install                # installs hooks
```

## Reproducing Results

```bash
# 1. Download raw data (requires credentials in .env)
make download-data

# 2. Run feature pipeline
make features

# 3. Train model
make train

# 4. Score population
make score
```

## Project Structure
[copied from above]

## Reports
- MAB: reports/MAB.md
- Model Card: reports/model_card_{name}.md
- Insight Report: reports/IR.md

## Data Sources
[list with owner, type, refresh cadence]
```

---

## Makefile Template

```makefile
.PHONY: setup lint test train score clean

setup:
	uv sync
	pre-commit install

lint:
	ruff check src/ tests/
	black --check src/ tests/

format:
	black src/ tests/
	ruff check --fix src/ tests/

test:
	pytest tests/ -v --tb=short

train:
	python -m {project_name}.models.train --config configs/training_config.yaml

score:
	python -m {project_name}.models.predict --config configs/training_config.yaml

features:
	python -m {project_name}.features.feature_pipeline --config configs/feature_config.yaml

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -name "*.pyc" -delete
```

---

## Project Type Registry

Reference this when Carla identifies the project type in the MAB.

### Type A: Propensity / Classification

Typical models: Churn, purchase propensity, lead scoring, lookalike
Key files: `feature_pipeline.py`, `train.py`, `predict.py`
Leakage risk: HIGH (temporal leakage; use strict cutoff dates)
Evaluation: ROC-AUC, Average Precision, lift at k%, expected value

### Type B: Demand Forecasting

Typical models: Marketing spend ROI forecast, demand planning, seasonality decomposition
Key files: `feature_pipeline.py`, `forecaster.py`
Leakage risk: CRITICAL (must use only past data to predict future; walk-forward validation)
Evaluation: MAPE, RMSE, sMAPE, bias, quantile coverage

### Type C: Customer Lifetime Value

Typical models: BG/NBD + Gamma-Gamma, survival models, regression on LTV
Key files: `ltv_pipeline.py`, `survival_model.py`
Leakage risk: HIGH (use transaction history up to reference date only)
Evaluation: Gini coefficient, decile-level accuracy, revenue lift vs. baseline targeting

### Type D: Marketing Mix Modeling (MMM)

Typical models: Bayesian MMM (pymc-marketing), Ridge regression, Robyn
Key files: `mmm_pipeline.py`, `adstock_transforms.py`
Leakage risk: MEDIUM (use properly lagged spend variables)
Evaluation: MAPE on holdout period, decomposition plausibility, contribution sanity check
Special: Requires business validation of channel contributions (Carla must sign off)

### Type E: Multi-Touch Attribution (MTA)

Typical models: Markov chain, Shapley value, data-driven attribution
Key files: `journey_builder.py`, `attribution_model.py`
Leakage risk: LOW (attribution is retrospective by definition)
Evaluation: Revenue weighted accuracy, channel contribution vs. MMM cross-check

### Type F: Customer Segmentation

Typical models: K-Means, hierarchical clustering, UMAP + HDBSCAN
Key files: `feature_pipeline.py`, `cluster_model.py`, `segment_profiler.py`
Leakage risk: LOW (unsupervised; but ensure test-period behavior not used in features)
Evaluation: Silhouette score, business interpretability, stability over time, activation rate per segment

### Type G: A/B Test / Causal Inference

Typical workflows: Eva's experiment design protocol, DiD, SCM, GeoLift
Key files: `power_analysis.py`, `experiment_analysis.py`, `causal_model.py`
Leakage risk: MEDIUM (pre-treatment covariates only for matching/weighting)
Evaluation: Pre-registered primary metric, ATE with CI, guardrail metric results

### Type H: Uplift / Causal ML

Typical models: T-learner, S-learner, X-learner, causal forests
Key files: `uplift_pipeline.py`, `uplift_model.py`
Leakage risk: HIGH (treatment assignment must be post-feature-computation)
Evaluation: Qini curve, AUUC, top-decile incremental lift, Placebo test

---

## Model Versioning Convention

```
models/CHANGELOG.md

| Version | Date | Trained by | Test ROC-AUC | Training window | Key changes |
|---------|------|-----------|-------------|-----------------|-------------|
| v1.0 | 2024-Q1 | Marco | 0.782 | 2022-01 to 2023-09 | Initial model |
| v1.1 | 2024-Q2 | Marco | 0.791 | 2022-01 to 2024-01 | Added recency features |
| v2.0 | 2024-Q4 | Marco | 0.801 | 2023-01 to 2024-09 | New label definition; retraining trigger |
```

Filenames: `{model_name}_v{major}.{minor}.pkl`
Breaking changes in label, features, or unit of prediction = major version bump.
