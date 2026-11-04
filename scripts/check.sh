#!/usr/bin/env sh
# Full verification. Run before committing anything.
set -eu
cd "$(dirname "$0")/.."

# Skills, agents and prompts promoted from someone else's library are not held
# to this project's house style -- scripts/lint-scope.py says which those are
# and why. They are excluded here rather than in ruff.toml and
# .markdownlint-cli2.jsonc because neither config language can express "every
# promoted item, whatever it is called". Correctness is not excluded along with
# style: the second ruff pass below still runs the rules that catch a real
# error over exactly the material the first pass skipped.
ruff_promoted=$(python3 scripts/lint-scope.py --ruff)
md_promoted=$(python3 scripts/lint-scope.py --markdown)

echo "==> lint (ruff, per ruff.toml)"
if command -v ruff >/dev/null 2>&1; then
  # Promoted names are lower-case kebab (scripts/intake.py enforces it), so the
  # unquoted expansion below cannot split a path. `set -f` stops the shell from
  # expanding it either: these words are arguments for the linter, and
  # `skills/<name>/**` must reach markdownlint as a pattern, not as the list of
  # files that pattern happened to match here. `set --` carries the list into
  # the command; check.sh takes no arguments of its own.
  set -f
  set --
  for p in $ruff_promoted; do set -- "$@" "--extend-exclude=$p"; done
  set +f
  ruff check . "$@"
  if [ -n "$ruff_promoted" ]; then
    set -f
    set --
    for p in $ruff_promoted; do set -- "$@" "$p"; done
    # Broken beats untidy. E9 and F carry the rules that say the code cannot
    # work -- an undefined name, a redefinition, a bad format string, a file
    # that does not parse. The five ignored here are tidiness in disguise (an
    # unused import or variable, a star import, an f-string with nothing in
    # it): real in our own code, not worth failing someone else's on.
    set +f
    echo "    (promoted material: real errors only, not house style)"
    ruff check --select E9,F --ignore F401,F403,F405,F541,F841 "$@"
  fi
else
  echo "ruff not installed -- lint SKIPPED (pip install ruff)"
fi

echo "==> markdown lint (markdownlint-cli2, per .markdownlint-cli2.jsonc)"
if command -v markdownlint-cli2 >/dev/null 2>&1; then
  set -f
  set -- "**/*.md"
  for g in $md_promoted; do set -- "$@" "!$g"; done
  set +f
  markdownlint-cli2 "$@"
else
  echo "markdownlint-cli2 not installed -- markdown lint SKIPPED (npm install -g markdownlint-cli2)"
fi

echo "==> unit tests"
python3 -m unittest discover -s tests -q

echo "==> hook scripts parse and hooks.json is valid"
for h in hooks/session-start hooks/stop-gate hooks/run-hook.cmd; do
  bash -n "$h" || { echo "FAIL: $h does not parse"; exit 1; }
done
python3 -c "import json; json.load(open('hooks/hooks.json'))" \
  || { echo "FAIL: hooks/hooks.json is not valid JSON"; exit 1; }
python3 -c "import json; json.load(open('.claude-plugin/plugin.json')); json.load(open('.claude-plugin/marketplace.json'))" \
  || { echo "FAIL: plugin manifest is not valid JSON"; exit 1; }

echo "==> finding catalogue is current"
python3 scripts/gen-finding-catalogue.py --check

echo "==> capability manifest is valid JSON and internally consistent"
python3 scripts/validate-capability.py

echo "==> gate contract: good spec passes, bad spec blocks, missing spec errors"
# REQ-P11.2-05: run against isolated copies of examples/, not the committed
# tree directly, and never sharing one trail root between the good and bad
# specs. examples/DECISIONS.jsonl is a real, ever-growing, gitignored trail
# (already several distinct historical frame_digest values), and
# DSX-PRE-041's identity-free floor (dsx/frame/prereg.py) fires HIGH at
# verify/ship on any root recording more than one distinct frame_digest —
# an accepted, documented residual (T-11.2-07) whose deliberate cost is
# exactly this: a root shared across two different specs (even a fresh one,
# once both specs' own headers land in it) trips the floor as a false
# positive. Two separate copies, one per spec, is the isolation the floor's
# own design requires. Sibling artifacts (the good fixture's DATA-PROFILE,
# figures, evidence, narrative, entrypoint) still resolve, because each
# whole tree is copied, not just the one spec inside it.
gate_tmp="$(mktemp -d)"
trap 'rm -rf "$gate_tmp"' EXIT
cp -R examples "$gate_tmp/good"
cp -R examples "$gate_tmp/bad"
rm -f "$gate_tmp/good/DECISIONS.jsonl" "$gate_tmp/bad/DECISIONS.jsonl"
for point in plan execute verify ship; do
  ./bin/dsx gate "$point" --spec "$gate_tmp/good/good-ANALYSIS-SPEC.yaml" >/dev/null 2>&1 \
    || { echo "FAIL: good spec blocked at $point"; exit 1; }
  if ./bin/dsx gate "$point" --spec "$gate_tmp/bad/bad-ANALYSIS-SPEC.yaml" >/dev/null 2>&1; then
    echo "FAIL: bad spec passed at $point"; exit 1
  fi
done
rm -rf "$gate_tmp"
trap - EXIT
missing_code=0
./bin/dsx gate ship --spec /nonexistent.yaml >/dev/null 2>&1 || missing_code=$?
[ "$missing_code" -eq 2 ] || { echo "FAIL: missing spec exited $missing_code, expected 2"; exit 1; }

echo "==> determinism: identical input, identical output"
# The bad fixture exits 1 by design, so guard the assignment against `set -e`.
a=$(./bin/dsx audit --spec examples/bad-ANALYSIS-SPEC.yaml --json 2>&1) || true
b=$(./bin/dsx audit --spec examples/bad-ANALYSIS-SPEC.yaml --json 2>&1) || true
[ "$a" = "$b" ] || { echo "FAIL: non-deterministic output"; exit 1; }

echo
echo "all checks passed"
