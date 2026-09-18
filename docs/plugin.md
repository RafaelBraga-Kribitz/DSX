# Plugin, hooks and continuous integration

How DSX runs without GSD: the Claude Code plugin, the two hooks it wires, the
continuous-integration gate, and the environment variables that tune them. The
engine is the same `dsx` command in every path; only the point of enforcement
moves.

## What the plugin installs

```text
/plugin marketplace add RafaelBraga-Kribitz/DSX
/plugin install dsx@dsx
```

The repository was renamed from `gsd-dsx` to `DSX`. GitHub redirects the old
path, so a command that still names `GSD-DSX` keeps working.

Three things, and nothing else:

- **One always-on rule.** A SessionStart hook injects
  [`skills/using-dsx/SKILL.md`](../skills/using-dsx/SKILL.md) — about 70 lines —
  into every session: no data before a spec, no claim before `dsx audit`, and
  which skill to invoke for which work. That is the entire per-session cost.
- **Fourteen skills, loaded on demand.** `dsx-scope-analysis`,
  `dsx-explore-data`, `dsx-design-experiment` and the rest load through the
  Skill tool only when the work calls for them.
- **A Stop hook that will not let the session end on a failing audit.** Before
  the turn closes, [`hooks/stop-gate`](../hooks/stop-gate) finds every
  `ANALYSIS-SPEC.{yaml,yml,json}` under the working directory and runs
  `dsx audit` on each.

Requires Python 3.9+ on PATH and no third-party packages.

## The Stop hook

| `dsx audit` exit | Hook exit | Effect |
|---|---|---|
| 0 | 0 | The session ends. One line on stdout names how many specs passed. |
| 1 | 2 | The stop is refused; the findings go back to the model on stderr. |
| 2 | 2 | The stop is refused; a gate that could not run has verified nothing. |

- A directory with **no spec passes through silently**, so the plugin is safe
  in a repository that is not analytics.
- When the hook has already blocked one stop, Claude Code sets
  `stop_hook_active` on the retry and the hook lets it through — it blocks
  once, shows the reason, and cannot loop.
- The search skips `.git`, `node_modules`, `.venv` and `__pycache__`.

## Environment variables

| Variable | Default | Effect |
|---|---|---|
| `DSX_STOP_GATE` | `on` | `off` disables the end-of-session gate for one shell |
| `DSX_BLOCK_ON` | `HIGH` | Minimum severity that blocks: `CRITICAL` · `HIGH` · `MEDIUM` · `LOW` |
| `DSX_SEARCH_DEPTH` | `4` | How deep under the working directory the Stop hook looks for specs |
| `DSX_PYTHON` | `python3` | Interpreter override |

## Continuous integration

Copy [`templates/github-workflow-dsx-gate.yml`](../templates/github-workflow-dsx-gate.yml)
to `.github/workflows/dsx-gate.yml` in any repository that holds analyses. On
every push and pull request it audits every `ANALYSIS-SPEC` it finds; a finding
at or above `DSX_BLOCK_ON` fails the job and blocks the merge. This gate costs
no tokens and cannot be argued with. Pin `DSX_REF` to a tag for a reproducible
ruleset.

## Windows

The hooks run through Git Bash. [`hooks/run-hook.cmd`](../hooks/run-hook.cmd)
is a polyglot wrapper: `cmd.exe` runs its batch half and hands over to
`bash.exe`; on Unix the shell skips that half and runs the script directly.

If your checkout location is deep, clone with long paths enabled
(`git -c core.longpaths=true clone …`, or `git config --global core.longpaths true`):
the planning archives under `.planning/milestones/` carry paths up to ~135
characters below the repository root, and Windows refuses paths beyond 260
without it.

## The GSD capability path

`node install.mjs` installs the same engine as a GSD Core capability overlay
with blocking gates at `plan:post`, `execute:post`, `verify:post` and
`ship:pre`, plus prompt fragments injected into the planner, researcher,
checker, executor and verifier. It is the heaviest way to run DSX and the only
one that gates on phase boundaries rather than at the end of the turn. The
installer self-tests: the known-good fixture must pass every gate and the
known-bad fixture must be blocked by every gate, or the install aborts.
Rollout, ceremony tiers and per-project configuration are in the
[operating guide](operating-guide.md).
