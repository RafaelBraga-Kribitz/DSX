# Fractal Claude harness (progressive disclosure)

**Goal:** Save tokens, keep flexibility, preserve quality by loading only what the task needs.

## Layer stack (top → bottom)

```
settings.json          ← global toggles, env, budgets (no workflows)
    ↓
CLAUDE.md (root)       ← universal heuristics + routing table (~150–400 words target)
    ↓
CLAUDE.md (domain)     ← area/use-case rules + small decision trees (~300–800 words)
    ↓
CLAUDE.md (project)    ← project contracts, naming extensions, interfaces (~400–1200 words)
    ↓
SKILL.md / AGENT.md    ← dense procedures, templates, checklists (unbounded but load on demand)
```

## Size targets (soft caps)

| Layer | Target | MUST NOT contain |
|-------|--------|------------------|
| `settings.json` | small JSON | Markdown, decision trees, LifeOS prose |
| Root `CLAUDE.md` | ≤ ~400 words | Step-by-step playbooks, API examples |
| Domain `CLAUDE.md` | ≤ ~800 words | Full task playbooks |
| Project `CLAUDE.md` | ≤ ~1200 words | Global governance duplicates |
| `SKILL.md` | lean body; split heavy refs | Duplicated root policies |

## Routing table template (paste into root `CLAUDE.md`)

```markdown
## Routing
- LifeOS architecture / autonomy / SoT → `lifeos-fractal-architect/SKILL.md`
- Naming / JD / PARA detail → `<path>/CLAUDE.md` for that vault area
- Single-tool formatting only → local formatter; do NOT load LifeOS architect skill
```

## Anti-patterns

- Duplicating the same MUST/NEVER in `settings.json`, root `CLAUDE.md`, and a skill.
- Putting long workflows at root to “help the model” — it hides the real router and burns context.
- More than **two** hops of “see X see Y” without an index note listing children.
- Child file **contradicts** parent MUST/NEVER — forbidden; child may only narrow or add scoped rules.

## UUID minting (harness-adjacent)

- **GitHub** mints `task_id` / execution IDs for issues and milestones.
- **Obsidian** mints `note_id` for knowledge objects at note creation.
- **Google Calendar** mints `event_id` for events.
- Mirrors **reference** IDs; they never remint a canonical ID for the same object facet.
