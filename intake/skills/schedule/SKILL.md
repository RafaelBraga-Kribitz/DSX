---
name: schedule
description: "Create a scheduled task that can be run on demand or automatically on an interval."
---

You are creating a reusable shortcut from the current session. Follow these steps:

## 1. Analyze the session

Review the session history to identify the core task the user performed or requested. Distill it into a single, repeatable objective.

## 2. Draft a prompt

The prompt will be used for future autonomous runs. It must be entirely self-contained. Include: objective, specific steps, file paths/URLs/tools, expected output, constraints.

Write in second-person imperative. Keep it concise but complete.

## 3. Choose a taskName

Short kebab-case name (e.g. "daily-inbox-summary", "weekly-dep-audit").

## 4. Determine scheduling

- Recurring -> cronExpression (user LOCAL timezone, not UTC)
- One-time -> fireAt as full ISO 8601 with offset, e.g. 2026-03-05T14:30:00-08:00
- Ad-hoc -> omit both
- Ambiguous -> propose and confirm first

Finally, call the create_scheduled_task tool.
