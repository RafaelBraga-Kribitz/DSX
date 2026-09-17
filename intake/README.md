# Intake — bringing your own skills and agents into DSX

This folder is the landing zone for skills and agents written elsewhere — a
personal library, another plugin, a colleague's repository. Nothing here is
installed or loaded. It is a staging area with a checker.

## Drop things in

```text
intake/
  skills/<name>/SKILL.md        one folder per skill, SKILL.md inside
  agents/<name>.md              one file per agent
```

Both need YAML frontmatter with at least `name` and `description`. The `name`
must match the folder or file name and use only letters, digits and hyphens.

## Check what you dropped

```bash
python3 scripts/intake.py            # table: name, kind, status, words, notes
python3 scripts/intake.py --json     # the same, machine-readable
```

Status is one of:

| Status | Meaning |
|---|---|
| `ok` | Valid frontmatter, no name collision. Can be promoted. |
| `collision` | A skill or agent with this name already exists in `skills/` or `agents/`. Rename it. |
| `invalid` | Missing or malformed frontmatter, or `name` does not match the path. |

The notes column flags **possible overlap**: an intake item whose description
shares enough vocabulary with an existing `dsx-*` skill or agent that you
should read both before promoting. Overlap is a hint, not a verdict — two
skills can legitimately cover the same ground from different angles.

## Promote

```bash
python3 scripts/intake.py --promote <name>
```

Moves the item into `skills/` or `agents/` and declares it in
`capabilities/dsx/capability.json`, so both install paths — the Claude Code
plugin and the GSD overlay — pick it up. Then:

```bash
python3 scripts/validate-capability.py   # manifest still conformant
./scripts/check.sh                        # everything still green
```

Promoted skills load on demand through the Skill tool. They are never
injected at session start; `skills/using-dsx/SKILL.md` is the only always-on
text, and it stays that way. If a promoted skill should be reachable from the
"Which skill, when" table, add a row there by hand — that table is the
routing, and it is deliberately short.

## Conventions worth matching

The existing `dsx-*` skills share a shape that the checks rely on. A skill
you promote does not have to match it, but the closer it is, the less the
routing table and the agents have to explain:

- `description` starts with what the work *is* and when to use it, in the
  third person. It does not summarise the steps.
- `argument-hint` lists the flags, if any.
- `allowed-tools` is explicit.
- The body opens with an `<objective>` block: one paragraph, what the skill
  produces.
- Where a step can be checked by code, the skill says which `dsx` command
  checks it, rather than describing the check in prose.

Agents are adversarial by default. The six shipped agents each open with a
`<role>` block that states the hypothesis the agent is trying to break.
