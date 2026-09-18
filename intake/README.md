# Intake — bringing your own skills, agents and prompts into DSX

This folder is the landing zone for material written elsewhere: a personal
library, another plugin, a colleague's repository. Nothing here is installed or
loaded. It is a staging area with a checker.

## Drop things in

One kind per folder. The layout is what the checker reads:

```text
intake/
  skills/<name>/SKILL.md     ->  skills/<name>/      declared in the manifest
  agents/<name>.md           ->  agents/<name>.md    declared in the manifest
  prompts/<name>.md          ->  prompts/<name>.md   reference material
```

Skills and agents need YAML frontmatter with at least `name` and `description`,
and the `name` must match the folder or file name. **A prompt needs neither** —
prompts are usually written without frontmatter, so the checker falls back to
the file's first heading as its description.

`<name>` uses letters, digits and hyphens only, in every kind.

## Check what you dropped

```bash
python3 scripts/intake.py            # table: name, kind, status, words, notes
python3 scripts/intake.py --json     # the same, machine-readable
```

Status is one of:

| Status | Meaning |
|---|---|
| `ok` | Valid, no name collision. Can be promoted. |
| `collision` | That name is already used by a shipped skill, agent, prompt or a manifest entry. Rename it. |
| `invalid` | Malformed frontmatter, a `name` that does not match the path, or a skill folder with no `SKILL.md`. |
| `unrecognised` | Nothing claims this file or folder. See below. |

The notes column flags **possible overlap**: an item whose description shares
enough vocabulary with a shipped `dsx-*` skill or agent that you should read
both before promoting. Overlap is a hint, not a verdict — two skills can
legitimately cover the same ground from different angles. It is most useful on
prompts, where a one-shot prompt often turns out to be an earlier draft of a
skill that now exists.

### Nothing is skipped in silence

Any folder under `intake/` that is not `skills/`, `agents/` or `prompts/` is
reported as `unrecognised`, with a count of the files inside it. A loose file
directly under `intake/`, a non-markdown file in a flat-file kind folder, and a
skill folder missing its `SKILL.md` are all reported too.

This is deliberate. A checker that ignores what it does not understand is the
same defect class as a gate that passes what it cannot read — and an
`unrecognised` row is a decision waiting for you, not an error.

## Promote

```bash
python3 scripts/intake.py --promote <name> [<name>...]
```

Each name moves to its destination; skills and agents are also declared in
`capabilities/dsx/capability.json`, so both install paths — the Claude Code
plugin and the GSD Core overlay — pick them up. Prompts are **not** declared:
nothing loads them, and a manifest entry would be a claim the project does not
honour. A name that is not `ok` is refused and reported; the rest of the batch
still moves. Then:

```bash
python3 scripts/validate-capability.py   # manifest still conformant
./scripts/check.sh                        # everything still green
```

Promoted skills load on demand through the `Skill` tool. Nothing is ever added
to the always-on text automatically; `skills/using-dsx/SKILL.md` is the only
text paid for on every session, and it stays short by hand. If a promoted skill
should be reachable from its routing table, add a row there yourself.

## Which kind is it?

The question that decides placement is *who chooses to run this*:

| The file… | Kind |
|---|---|
| encodes a repeatable workflow an agent should follow when it recognises the situation | skill |
| is an adversarial brief for one narrow review, run in its own context | agent |
| is a good opening move **you** send | prompt |

A prompt that turns out to be the first kind is worth converting: give it
frontmatter whose `description` says *when to use it*, move it into `skills/`,
declare it, and route to it. See [`prompts/README.md`](../prompts/README.md).

## Conventions worth matching

The shipped `dsx-*` skills share a shape the checks rely on. A skill you
promote does not have to match it, but the closer it is, the less the routing
table and the agents have to explain:

- `description` starts with what the work *is* and when to use it, in the third
  person. It does not summarise the steps.
- `argument-hint` lists the flags, if any.
- `allowed-tools` is explicit.
- The body opens with an `<objective>` block: one paragraph, what the skill
  produces.
- Where a step can be checked by code, the skill names the `dsx` command that
  checks it rather than describing the check in prose.

Agents are adversarial by default. The six shipped agents each open with a
`<role>` block stating the hypothesis the agent is trying to break.
