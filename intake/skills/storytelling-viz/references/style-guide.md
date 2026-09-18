# Shared Style Guide

This style guide applies to all BMADS-MKT visualizations and storytelling-viz outputs.

## Core Principles

- Keep the look clean, story-led, and deliberate
- Prefer editorial hierarchy over chart-library defaults
- Use purposeful color, not decoration
- Keep the main takeaway visible without hover
- Use annotations sparingly and only when they clarify the story

## Editorial Standards

- When the user wants more creativity, redesign the whole frame, not just the marks
- Prefer one strong visual hook per chart over many small embellishments
- Use topic-shaped palettes, textures, or panel treatments when they reinforce the story
- Treat header cards, reading guides, and source framing as part of the visual system
- Vary composition across charts; do not reuse the same centered wrapper by reflex
- Use custom mark styling or geometry when it materially strengthens the message
- Keep creative choices subordinate to data honesty and mobile readability

## MADS-Specific Defaults

For BMADS-MKT projects:

### Color Palette
- Primary: `#2E4057` (dark navy) — for the main series or hero metric
- Accent: `#E84855` (alert red) — for metrics breaching guardrail thresholds
- Positive: `#3BB273` (teal green) — for metrics hitting targets
- Neutral: `#8D99AE` (slate grey) — for comparison/baseline series
- Background: `#FAFAFA` — clean white-grey

### Typography
- Chart title: 16px bold, sentence case
- Subtitle/takeaway: 13px regular, italic
- Axis labels: 11px regular
- Annotations: 11px, restrained use
- Source/date: 10px, grey

### Annotation Rule
- Maximum 2 in-chart annotations per visualization
- Annotations point to data evidence, never methodology
- If an annotation competes with a label, remove the annotation

### Marketing DS Conventions
- Always show confidence intervals on experiment results
- Always label baseline with a reference line
- For time series: use 7-day rolling average as default smoothing
- For model evaluation: include AUC value in chart title, not just in annotation
