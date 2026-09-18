---
name: storytelling-viz
description: Story-first Plotly workflow for turning a dataset into a polished interactive visualization with local review artifacts. Use this skill when producing any data visualization in BMADS-MKT projects, or when the user wants a concise, intuitive chart with a clear takeaway, plus final `index.html` and `preview.html`. Deeply integrated into Petra (all insight charts), Diego (all EDA plots), and Marco (all model evaluation plots).
when_to_use: data visualization, chart, plot, histogram, scatter plot, bar chart, line chart, time series, EDA chart, insight chart, model evaluation, feature importance, ROC curve, dashboard chart, executive chart, data story, plotly, interactive chart, visualization, viz
allowed-tools: Read Write Edit Bash Glob Grep
argument-hint: [dataset path or description, optional: chart type preference]
---

# Storytelling Viz

Use this skill when the task is about choosing, building, and refining a data visualization.

## MADS Integration

This skill is mandatory for all BMADS-MKT visualizations:

- **Petra** (Insights Lead): ALL charts in insight reports, dashboards, executive comms
- **Diego** (Data Steward): ALL EDA plots in data audit reports
- **Marco** (DS/ML Engineer): ALL model evaluation charts in model cards

When invoked from within a MADS agent context, the skill automatically:
1. Applies the MADS color palette and branding defaults
2. Uses the agent's current dataset and business context
3. Writes the one-sentence takeaway first (aligned with the MAB primary metric)
4. Produces `reports/viz/{chart-slug}/index.html` and `preview.html`

## Skill Promise

Unless the user explicitly asks otherwise, optimize for:

- one chart, not a dashboard
- one main takeaway, not a bundle of loosely related points
- comprehension without hover
- minimal interaction that adds value
- concise copy and restrained styling

## Non-Negotiable Tests

Before moving from one stage to the next, apply these tests:

- `Story test`: the main takeaway can be stated in one sentence
- `Intuition test`: a first-time viewer can understand the main claim quickly without hover
- `Concision test`: if an element can be removed without hurting meaning, remove it
- `Honesty test`: the framing still matches the actual data, scope, and caveats

If the visualization fails one of these tests, simplify the chart, the copy, or both.

## Fast Path

1. Identify the data source and inspect the dataset shape.
2. Check comparability and chart logic.
3. Write the one-sentence story the viewer should remember.
4. Recommend one default chart and one fallback.
5. Ask the user to confirm the recommended direction before building.
6. Build the first draft in `Plotly.js`.
7. Run rendered visual QA on desktop and, when needed, a narrower layout.
8. Deliver the local artifacts, insight bullets, and any material caveats.

## Dataset Review

Before proposing a chart:

- confirm the dataset source and citation
- identify row count, column names, and data types
- classify each quantitative field: cost, income, rate, stock, flow, share, index, or timepoint
- check whether compared values are actually comparable
- flag concept mismatches early

## Recommendation Format

Always provide:

- `Recommended chart`: the default choice
- `Why it fits`: the structural reason
- `Why not the obvious alternative`: the main reason a nearby chart is weaker
- `Interaction`: the minimum useful interaction, or `none`
- `Fallback`: one credible alternative
- `Draft title`: a concise title candidate
- `Draft takeaway`: the one-sentence message
- `Comparability note`: any caveat that materially affects interpretation

End with: `If you want, I'll proceed with the recommended chart. If you'd rather use the fallback, say so before I build.`

## Plotly Rules

Use `Plotly.js` by default. Prefer a single polished chart over a multi-panel dashboard.

Prioritize:
- clear ranking or comparison
- readable labels
- restrained color
- titles and subtitles that carry the narrative
- hover that adds detail, not essential meaning
- stable layouts across desktop and mobile

Avoid:
- unnecessary animation
- pie charts or donut charts
- default Plotly styling left unrefined
- dense dashboards with no visual hierarchy

## Story Framing

Choose the chart only after identifying the sentence the viewer should remember.

For MADS deliverables:
- The takeaway must connect to the MAB primary metric
- "Churn risk is up" is not enough. "Churn risk in paid-social cohort is up 12pp vs. baseline, exceeding the 8pp guardrail threshold" is a takeaway.

## Framing Modes

- `Analytic clean`: restrained, minimal, mostly neutral framing
- `Editorial`: stronger hierarchy, topic-shaped palette, and direct annotations (default for MADS)
- `Atmospheric`: editorial plus scene-like background or surface treatment

Default to `Editorial` for all MADS work.

## Output Contract

The final deliverable includes:

- `index.html` — the visualization artifact
- `preview.html` — local review wrapper
- A short title
- 2-3 insight bullets
- Any assumptions or caveats that affect interpretation
- An explicit linked data source

Output path for MADS projects:
```
reports/viz/{chart-slug}/index.html
reports/viz/{chart-slug}/preview.html
```

## Heuristics

- time series: line chart or area chart
- ranking: sorted horizontal bar chart or dot plot
- distribution: histogram, box plot, or violin plot
- relationship: scatter plot with optional trend line
- composition: stacked bars only when category count stays readable
- model evaluation (ROC, PR): use Plotly line with AUC annotation
- feature importance: horizontal bar chart, sorted by importance

## Visual QA

Before delivery:

- review the final `index.html` in a rendered state
- check at least one desktop-width view
- look for clipped text, overlapping annotations, truncated labels
- explicitly state which QA was performed

## Style Guide

Load `~/.claude/skills/storytelling-viz/references/style-guide.md` for detailed style rules.
Load `~/.claude/skills/storytelling-viz/references/plotly-patterns.md` for Plotly defaults.
