# Prompts

This folder holds prompts promoted from `intake/`: one-shot prompts and prompt
fragments worth keeping as reference material. It is empty until the first one
is promoted.

**Nothing here loads automatically.** No hook injects it, no manifest declares
it, and the `Skill` tool cannot reach it. A file in this folder is read or
pasted by a person, and that is the whole contract. A prompt that describes a
workflow an agent should follow on its own belongs in `skills/` instead.

## Adding one

Drop it in `intake/prompts/<name>.md` and run `python3 scripts/intake.py`; the
report names collisions and any overlap with a shipped skill, and
`--promote <name>` moves it here. The rules for names and promotion are in
[intake/README.md](../intake/README.md).
