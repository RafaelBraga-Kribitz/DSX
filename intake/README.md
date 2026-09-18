# Intake — bringing your own skills, agents and prompts into DSX

This folder is the landing zone for material written elsewhere: a personal
library, another plugin, a colleague's repository. Nothing here is installed or
loaded. It is a staging area with a checker.

## Drop things in

One kind per folder. Namespace subfolders are fine — organise however your
library already is:

```text
intake/
  skills/[ns/]<name>/SKILL.md  ->  skills/<name>/         declared in the manifest
  agents/[ns/]<name>.md        ->  agents/<ns-name>.md    declared in the manifest
  prompts/[ns/]<name>.md       ->  prompts/<ns-name>.md   reference material
```

**A skill keeps only its folder basename.** That basename is the skill's name in
every library measured — gsd-core 71/71, superpowers 14/14, the public skills
41/41, ECC 888/898 — and `install.mjs` copies `skills/<name>/` recursively, so a
skill's own `references/`, `scripts/` and `agents/` subfolders travel with it.

**Agents and prompts flatten**, joining their namespace segments with hyphens:
`agents/global/code-reviewer.md` becomes `global-code-reviewer`. This is forced,
not stylistic — `install.mjs` reads `agents/` with one non-recursive listing and
skips any entry that does not end in `.md`, so an agent in a subfolder would
never be installed.

A trailing `.prompt`, `.agent`, `.command` or `.skill` sub-extension is stripped,
so `brief.prompt.md` yields `brief`, not `brief.prompt` — the dot would fail the
name pattern.

Skills and agents need YAML frontmatter with at least `name` and `description`.
**A prompt needs neither** — prompts are usually written without frontmatter, so
the checker falls back to the file's first heading as its description.

The **derived** name must be lower-case kebab: `^[a-z0-9]+(-[a-z0-9]+)*$`. That
is the same pattern `scripts/validate-capability.py` enforces on every declared
name, and a test reads it out of that file so the two cannot drift apart. A
declared `name` in the frontmatter is held to no such rule, because promote
rewrites it — see below.

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
| `invalid` | Missing frontmatter where it is required, a derived name that is not lower-case kebab, or a folder under `skills/` with no `SKILL.md` anywhere below it. |
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

### The frontmatter name follows the destination

The folder or file name is what `install.mjs` projects, what `capability.json`
declares and what the harness loads the item under. So when a frontmatter `name`
disagrees with it, the frontmatter is the side that is wrong: the item still
reports `ok`, and promote rewrites that one line, printing the before and after.

```text
promoted skill forecasting -> skills/forecasting and declared in capabilities/dsx/capability.json
      frontmatter name: 'data-analytics-skills--forecasting' -> 'forecasting'
```

Nothing else in the file is touched — other frontmatter keys, the body, and a
literal `name:` inside the body all survive unchanged. A prompt with no
frontmatter is promoted byte-for-byte.

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

## House style stops at the border

A promoted skill is loaded exactly as its author wrote it, so it is not held to
this repository's line length, heading style or import order. `./scripts/check.sh`
excludes every promoted skill, agent and prompt from both linters and then runs
ruff back over them with the rules that mean the code cannot work — an undefined
name, a redefinition, a bad format string, a file that does not parse. Tidiness
rules (an unused import, an f-string with nothing in it) are not applied to
someone else's draft.

The border is the name, not a list anyone has to maintain: everything written
here is `dsx-*`, plus `using-dsx` and each folder's `README`. `scripts/lint-scope.py`
is where that rule lives, and `python3 scripts/lint-scope.py` prints what it
currently treats as promoted.

One consequence worth knowing: a bare `ruff check .` or `markdownlint-cli2
"**/*.md"` will report house-style findings on promoted material that the gate
does not. Run `./scripts/check.sh` — that is what CI runs.

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
