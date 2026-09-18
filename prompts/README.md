# Prompts

Reference material: one-shot prompts and prompt fragments worth keeping, either
because they were used to build part of this project or because they are a
useful starting point for analytical work.

**Nothing here loads automatically.** No hook injects it, no manifest declares
it, and the `Skill` tool cannot reach it. A file in this folder is read by a
person, or pasted by a person, and that is the whole contract.

## Why they are not skills

A skill is invoked by an agent because its `description` matched the work at
hand, and it then shapes what the agent does. A prompt here is text you chose
to send. The distinction decides where a file belongs:

| The file… | Belongs in |
|---|---|
| encodes a repeatable workflow an agent should follow when it recognises the situation | `skills/<name>/SKILL.md` |
| is an adversarial brief for one narrow review | `agents/<name>.md` |
| is a good opening move you want to send yourself | `prompts/<name>.md` |
| worked once and you want the wording remembered | `prompts/<name>.md` |

If a prompt here turns out to be the first kind, convert it: give it
frontmatter with a `name` and a `description` that says *when to use it*, move
it to `skills/`, declare it in `capabilities/dsx/capability.json`, and add a
row to `skills/using-dsx/SKILL.md` so it is routed to by name.

## Adding one

Drop it in `intake/prompts/<name>.md` and run `python3 scripts/intake.py`; the
report names collisions and any overlap with a shipped skill, and
`--promote <name>` moves it here. Adding a file directly is fine too — the
folder has no schema to satisfy.
