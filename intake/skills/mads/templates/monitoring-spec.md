# Monitoring Specification (MonSpec)

> Document owner: Otto
> Status: DRAFT | APPROVED | ACTIVE | DEPRECATED
> Version: 1.0
> Date:
> References Model Card version:
> References MAB version:

---

## 1. Model Identity

| Field | Value |
|-------|-------|
| Model name | |
| Model version | |
| Model owner | |
| Backup owner | |
| Deployment date | |
| Review / expiry date | |
| Serving mode | Batch / Real-time API / Embedded |
| Scoring frequency | |
| Output location | |
| Downstream consumers | |

---

## 2. Data Pipeline Monitoring

### Input Data Checks

| Check | Expected | Alert threshold | Alert channel | Owner |
|-------|---------|----------------|--------------|-------|
| Daily row count | {min} – {max} | Outside range | Slack: #data-alerts | |
| Null rate: {column} | < {pct}% | > {pct}% | Slack: #data-alerts | |
| Schema match | Per data contract | Any mismatch | PagerDuty | |
| Data freshness | Within {N} hours | Older than {N} hours | Slack: #data-alerts | |
| Duplicate rate | < 0.1% | > 0.1% on primary key | Slack: #data-alerts | |

### Data Contract Reference

```
.mads/contracts/{dataset_name}_contract.yaml
```

---

## 3. Feature Distribution Monitoring (Data Drift)

**Method:** Population Stability Index (PSI) per feature
**Reference distribution:** Training period ({start_date} to {end_date})
**Monitoring window:** Rolling 30-day vs. reference

| Feature | PSI threshold: investigate | PSI threshold: retrain | Current PSI |
|---------|--------------------------|----------------------|-------------|
| {feature_1} | 0.10 | 0.20 | — |
| {feature_2} | 0.10 | 0.20 | — |
| {feature_3} | 0.10 | 0.20 | — |

**PSI alert flow:**
- PSI 0.10–0.20: Notify model owner. Diego investigates data source.
- PSI > 0.20: Trigger retraining protocol automatically.

---

## 4. Model Output Distribution Monitoring (Concept Drift)

**Output metric:** {e.g., daily mean prediction score, % scored above threshold}

| Statistic | Baseline (training) | Alert threshold |
|-----------|--------------------|-|
| Daily mean score | {value} | Outside baseline ± 2.5 std for 3 consecutive days |
| Daily std score | {value} | Increase > 50% vs. baseline |
| % scored > 0.7 | {value}% | Outside baseline ± 5pp for 7-day rolling |

**Method:** KS test daily distribution vs. reference distribution (p < 0.01 triggers review)

---

## 5. Business Metric Performance

*For models where labels arrive with a lag, schedule periodic evaluation on labeled cohorts.*

| Metric | Minimum to stay deployed | Evaluation frequency | Data source |
|--------|------------------------|---------------------|-------------|
| {primary metric, e.g., ROC-AUC} | {value} | Monthly | {table or process} |

**Alert:** If primary metric falls below minimum for {N} consecutive evaluation periods,
automatically trigger retraining protocol.

---

## 6. Retraining Protocol

### Triggers

| Trigger type | Condition | Priority |
|-------------|----------|---------|
| Performance degradation | Primary metric < {threshold} for {N} periods | HIGH |
| Feature drift | PSI > 0.20 on any top-5 feature | HIGH |
| Scheduled | Every {quarter / 6 months} | MEDIUM |
| Data event | Major campaign, product change, or market disruption | HIGH |

### Retraining Steps

1. Diego runs DAR refresh on new data window (confirm data quality)
2. Marco runs feature pipeline on new training window
3. Marco trains new model version using MSD configuration
4. Marco compares new vs. current model on holdout set
5. If new model performance >= current - {tolerance}: promote to staging
6. Run deployment plan: shadow mode → partial → full
7. New Model Card version produced
8. MonSpec updated with new baseline distributions
9. Version logged in `models/CHANGELOG.md`

### Retraining validation gate

*New model must pass all of these before replacing current:*

- [ ] Test set primary metric >= current model - {tolerance}
- [ ] No guardrail metric regression
- [ ] Integration tests pass
- [ ] Shadow mode comparison: output distributions within {tolerance}

---

## 7. Alert Configuration

| Alert | Method | Channel | On-call owner | Response SLA |
|-------|--------|---------|--------------|-------------|
| Data pipeline failure | Airflow / Prefect | Slack: #data-alerts | Data engineer | 2 hours |
| Schema mismatch | Pipeline check | PagerDuty | Data engineer | 1 hour |
| PSI > 0.20 | Scheduled job | Slack: #model-alerts | Model owner | 24 hours |
| Business metric below threshold | Scheduled job | Slack: #model-alerts + Email | Model owner | 48 hours |
| Scoring pipeline failure | Airflow / Prefect | PagerDuty | ML engineer | 1 hour |

---

## 8. Runbook Reference

Full operational runbook: `reports/runbook_{model_name}.md`

Quick reference:

| Situation | First action |
|-----------|-------------|
| Scoring pipeline fails | Check Airflow DAG logs → escalate to data engineering if source delay |
| PSI alert fires | Diego investigates upstream source → retraining if drift is real |
| Business metric alert | Confirm labels are complete → check for product/campaign changes → retrain |
| Rollback required | Repoint to previous model version → notify Slack → log incident |

---

## 9. Monitoring Dashboard

**Dashboard name:**
**Location:** {Looker Studio / Power BI URL}
**Refresh cadence:** {real-time / hourly / daily}
**Primary audience:** {Model owner, Data team, Marketing team}

**Key panels:**
- Daily prediction score distribution (time series with ±2std band)
- PSI per feature (bar chart, last 30 days vs. reference)
- Business metric performance (trend vs. deployment threshold)
- Data pipeline status (last successful run, row count, freshness)

---

## 10. Model Expiry and Retirement

| Event | Action |
|-------|--------|
| Review date reached ({date}) | Otto and Marco conduct model health review |
| Business context fundamentally changed | Carla initiates new MAB; model retired |
| New model version promoted | Current version deprecated; kept for 90 days for rollback |
| Model retired | Remove from scoring pipeline; archive artifact; notify all consumers |

---

## Otto's Quality Gate

- [ ] All four monitoring layers defined (pipeline, input drift, output drift, business metric)
- [ ] PSI thresholds set per feature
- [ ] Retraining triggers defined (performance, drift, scheduled, event)
- [ ] Alert channels and owners assigned for every alert type
- [ ] Response SLAs defined
- [ ] Runbook written and shared
- [ ] Monitoring dashboard specified
- [ ] Review / expiry date set in calendar
- [ ] Model owner and backup owner named
