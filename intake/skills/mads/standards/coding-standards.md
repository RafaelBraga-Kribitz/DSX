# BMADS-MKT Coding Standards

> Enforced by all agents. Violations trigger automatic refactoring and explanation.

---

## Global Rules (All Languages)

1. **Reproducibility over convenience.** Set seeds. Pin versions. Use lockfiles. Use relative paths.
2. **Explicitness over magic.** No magic numbers. No hidden state. No implicit casts.
3. **Separation of concerns.** Notebooks are for exploration and explanation only. Business logic lives in `src/`.
4. **Clarity over cleverness.** A junior analyst must be able to read and modify this code in 6 months without asking anyone.
5. **Fail loudly.** Validate inputs. Raise informative errors. Never suppress warnings without explanation.
6. **Test the non-obvious.** Unit tests for transformations, leakage assertions, schema checks. Skip tests for trivial getters.

---

## Python Standards

### Naming

| Construct | Convention | Example |
|-----------|-----------|---------|
| Variables | snake_case | `feature_window_days` |
| Functions | snake_case | `compute_rfm_features` |
| Methods | snake_case | `fit_pipeline` |
| Modules | snake_case | `feature_pipeline` |
| Packages | snake_case | `churn_model` |
| Classes | PascalCase | `FeatureConfig` |
| Constants | SCREAMING_SNAKE_CASE | `RANDOM_SEED` |
| Type aliases | PascalCase | `FeatureMatrix` |

**Never use:**
- camelCase (not even for dicts or config keys)
- Single-letter names except trivial loop indices (`i`, `j`) in very small scope
- Abbreviated names that obscure meaning (`df2`, `tmp`, `res`)

### Structure

- Max function length: 40 lines. If longer, decompose.
- Max file length: 300 lines. If longer, split into modules.
- Max nesting depth: 3 levels. Prefer early returns.
- No star imports (`from module import *`)
- No unused imports

### Type Hints

Required for:
- All public functions in `src/`
- All class attributes
- Return types, always

```python
# Correct
def compute_psi(
    reference_distribution: pd.Series,
    current_distribution: pd.Series,
    n_bins: int = 10,
) -> float:
    ...

# Wrong
def compute_psi(ref, curr, bins=10):
    ...
```

### Docstrings

Use Google style for all public functions, methods, and classes:

```python
def build_label(
    events_df: pd.DataFrame,
    reference_date: str,
    label_window_days: int,
) -> pd.DataFrame:
    """
    Construct binary churn label for each user relative to reference_date.

    Args:
        events_df: Raw events DataFrame with columns [user_id, event_date].
        reference_date: ISO date string. Label window starts from this date.
        label_window_days: Number of days after reference_date defining the label window.

    Returns:
        DataFrame with columns [user_id, is_churned] where is_churned is 1 if the
        user made zero purchases in the label window, 0 otherwise.

    Raises:
        ValueError: If reference_date is not a valid ISO date string.
        KeyError: If required columns are missing from events_df.

    Notes:
        Only users active in the 90 days prior to reference_date are included.
        Users with no prior activity are excluded (not labeled as churned).
    """
```

### Constants and Configuration

```python
# Correct: named constant
RANDOM_SEED = 42
LABEL_WINDOW_DAYS = 90
FEATURE_WINDOW_DAYS = 180

# Correct: dataclass for config groups
from dataclasses import dataclass

@dataclass
class TrainingConfig:
    random_seed: int = RANDOM_SEED
    test_size: float = 0.20
    n_cv_folds: int = 5
    label_window_days: int = LABEL_WINDOW_DAYS

# Wrong: magic number embedded in function
model = GradientBoostingClassifier(random_state=42, n_estimators=100)
```

### Leakage Prevention (enforced by Marco)

```python
# The split always comes first
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=RANDOM_SEED, stratify=y
)

# Scaler and imputer fit on training data only
pipeline = Pipeline([("scaler", StandardScaler()), ("model", LogisticRegression())])
pipeline.fit(X_train, y_train)  # correct

# Wrong: fit on full data, then split
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # leakage! test data seen by scaler
```

### Seeds

```python
import random
import numpy as np

RANDOM_SEED = 42

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# For scikit-learn: pass random_state=RANDOM_SEED to every stochastic estimator
# For pandas sample: df.sample(frac=0.1, random_state=RANDOM_SEED)
```

---

## SQL Standards

### Naming
- Tables and columns: `snake_case`
- No reserved word collisions: don't name a column `date`, `value`, `key`, `order`

### Forbidden
- `SELECT *` in production queries
- Implicit JOINs (use explicit `JOIN ... ON ...`)
- Implicit casting
- Subqueries where CTEs are clearer

### Required
- Explicit `JOIN` conditions
- Table aliases that are meaningful abbreviations, not single letters
- CTEs for any query with more than 2 logical steps

```sql
-- Correct
WITH daily_sessions AS (
    SELECT
        user_id,
        DATE(event_timestamp) AS event_date,
        COUNT(*) AS session_count,
        SUM(revenue_usd) AS daily_revenue
    FROM raw.events
    WHERE event_date >= '2024-01-01'
    GROUP BY 1, 2
),

user_features AS (
    SELECT
        user_id,
        MAX(event_date) AS last_active_date,
        SUM(session_count) AS total_sessions,
        SUM(daily_revenue) AS total_revenue
    FROM daily_sessions
    GROUP BY 1
)

SELECT *
FROM user_features
WHERE total_sessions >= 3;

-- Wrong
SELECT u.*, o.* FROM users u, orders o WHERE u.id = o.user_id;
```

---

## Notebook Standards

### Naming Convention

```
{phase}_{sequence}_{description}.ipynb

Examples:
01_eda_user_events.ipynb
02_feature_engineering_rfm.ipynb
03_model_selection_gradient_boosting.ipynb
04_evaluation_test_set.ipynb
```

### Required Header Cell

Every notebook starts with:

```python
# =============================================================================
# Project: {project_name}
# Notebook: {notebook_name}
# Author: {author}
# Date: {YYYY-MM-DD}
# =============================================================================
# Objective:
#   {One sentence describing what this notebook explores or demonstrates.}
#
# Data sources:
#   - {source_name}: {brief description}
#
# Assumptions:
#   - {assumption 1}
#
# Outputs:
#   - {what this notebook produces, e.g., a saved feature file, a chart}
# =============================================================================

import random
import numpy as np

RANDOM_SEED = 42
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)
```

### Rules

1. Must execute linearly from top to bottom (no `Run All` failures)
2. No hidden state (no reliance on cells run out of order)
3. Cell outputs stripped before commit (use `nbstripout` or Jupytext)
4. Reusable functions moved to `src/` — notebooks import from `src/`
5. Every chart has a title, axis labels, and a one-sentence caption below it
6. No inline data definitions larger than a 5-row example

---

## Tooling Checklist (per project)

```
Formatting:     Black
Linting:        Ruff
Type checking:  pyright (or mypy)
Testing:        pytest
Env:            uv (preferred) or poetry
Notebook:       nbstripout (pre-commit hook)
Pre-commit:     pre-commit with Black, Ruff, nbstripout hooks
CI:             GitHub Actions (lint + test on push)
Experiment tracking: MLflow (track run, log params, log metrics, log artifact)
```

---

## Anti-Patterns (auto-flagged by any agent)

| Anti-pattern | Why it matters | Fix |
|-------------|---------------|-----|
| `scaler.fit(X)` before split | Leakage | Split first, fit on train only |
| `df = pd.read_csv("C:/Users/...")` | Non-reproducible path | Use `Path(__file__).parent / "data"` |
| `np.random.seed()` missing | Non-deterministic | Set seed at top of every script |
| `except: pass` | Silent failure | At minimum: `except Exception as error: logger.error(error); raise` |
| Column named `df2` | Ambiguity | Use descriptive name |
| Notebook with 200-line cells | Hidden state risk | Decompose; move to `src/` |
| `import *` | Namespace pollution | Explicit imports only |
| Credentials in code | Security | Load from environment variables |
| `model.predict(X_test)` before cross-validation | Over-optimistic evaluation | CV first, test set last |
