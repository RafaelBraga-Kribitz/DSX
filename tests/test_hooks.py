"""Hook contract tests. Stdlib unittest — no pytest dependency.

The hooks are bash; these tests run them the way a harness would and assert
on exit codes and output shape. Skipped when bash is not on PATH.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOOKS = ROOT / "hooks"
BASH = shutil.which("bash")


def run_hook(name: str, stdin: str = "", env: dict | None = None, cwd: Path | None = None):
    merged = {**os.environ, "CLAUDE_PLUGIN_ROOT": str(ROOT)}
    for key in ("DSX_STOP_GATE", "DSX_BLOCK_ON", "CURSOR_PLUGIN_ROOT", "COPILOT_CLI"):
        merged.pop(key, None)
    if env:
        merged.update(env)
    return subprocess.run(
        [BASH, str(HOOKS / name)],
        input=stdin, capture_output=True, text=True, env=merged, cwd=str(cwd or ROOT),
        check=False,
    )


def analysis_dir(tmp: str, which: str) -> Path:
    """Copy examples/ under tmp and rename one fixture to the discovered name.

    The fixtures declare sibling artefacts as repository-relative paths
    (``examples/good-REPRO-REPORT.md``), so the copy keeps the ``examples/`` name
    and the hook runs with ``tmp`` as its working directory, one level up — the
    same layout as the repository root. Returns the copied examples/ folder.
    """
    dst = Path(tmp) / "examples"
    shutil.copytree(ROOT / "examples", dst,
                    ignore=shutil.ignore_patterns("known-bad", "__pycache__", "DECISIONS.jsonl"))
    (dst / f"{which}-ANALYSIS-SPEC.yaml").rename(dst / "ANALYSIS-SPEC.yaml")
    return dst


def payload(cwd: Path, active: bool = False) -> str:
    return json.dumps({
        "session_id": "test", "transcript_path": "/dev/null",
        "cwd": str(cwd), "hook_event_name": "Stop", "stop_hook_active": active,
    })


@unittest.skipIf(BASH is None, "bash not available")
class TestHooksManifest(unittest.TestCase):
    def test_hooks_json_declares_both_hooks(self):
        data = json.loads((HOOKS / "hooks.json").read_text(encoding="utf-8"))
        events = data["hooks"]
        self.assertIn("SessionStart", events)
        self.assertIn("Stop", events)
        commands = [h["command"] for group in events.values() for entry in group for h in entry["hooks"]]
        self.assertTrue(any("session-start" in c for c in commands))
        self.assertTrue(any("stop-gate" in c for c in commands))

    def test_hook_scripts_parse(self):
        for name in ("session-start", "stop-gate", "run-hook.cmd"):
            proc = subprocess.run([BASH, "-n", str(HOOKS / name)], capture_output=True, text=True, check=False)
            self.assertEqual(proc.returncode, 0, f"{name}: {proc.stderr}")


@unittest.skipIf(BASH is None, "bash not available")
class TestSessionStart(unittest.TestCase):
    def test_claude_code_shape_carries_the_skill(self):
        proc = run_hook("session-start")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        out = data["hookSpecificOutput"]
        self.assertEqual(out["hookEventName"], "SessionStart")
        self.assertIn("ANALYSIS-SPEC.yaml", out["additionalContext"])
        self.assertIn("dsx audit", out["additionalContext"])
        self.assertIn("dsx-scope-analysis", out["additionalContext"])
        self.assertNotIn("additional_context", data)

    def test_cursor_shape(self):
        proc = run_hook("session-start", env={"CURSOR_PLUGIN_ROOT": str(ROOT)})
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertIn("additional_context", data)
        self.assertNotIn("hookSpecificOutput", data)

    def test_generic_shape_when_copilot(self):
        proc = run_hook("session-start", env={"COPILOT_CLI": "1"})
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertIn("additionalContext", data)
        self.assertNotIn("hookSpecificOutput", data)

    def test_wrapper_dispatches(self):
        proc = subprocess.run(
            [BASH, str(HOOKS / "run-hook.cmd"), "session-start"],
            capture_output=True, text=True, env={**os.environ, "CLAUDE_PLUGIN_ROOT": str(ROOT)},
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        json.loads(proc.stdout)

    def test_always_on_text_stays_small(self):
        # This is the only text paid for on every session. Keep it under a page.
        words = len((ROOT / "skills" / "using-dsx" / "SKILL.md").read_text(encoding="utf-8").split())
        self.assertLess(words, 900, f"using-dsx is {words} words; it is meant to stay short")


@unittest.skipIf(BASH is None, "bash not available")
class TestStopGate(unittest.TestCase):
    def test_no_spec_passes_silently(self):
        with tempfile.TemporaryDirectory() as tmp:
            proc = run_hook("stop-gate", stdin=payload(Path(tmp)), cwd=Path(tmp))
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(proc.stderr, "")

    def test_good_spec_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            analysis_dir(tmp, "good")
            proc = run_hook("stop-gate", stdin=payload(Path(tmp)), cwd=Path(tmp))
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("1 ANALYSIS-SPEC(s) pass", proc.stdout)

    def test_bad_spec_blocks_with_findings(self):
        with tempfile.TemporaryDirectory() as tmp:
            analysis_dir(tmp, "bad")
            proc = run_hook("stop-gate", stdin=payload(Path(tmp)), cwd=Path(tmp))
        self.assertEqual(proc.returncode, 2, proc.stdout)
        self.assertIn("BLOCKED", proc.stderr)
        self.assertIn("DSX-", proc.stderr)
        self.assertIn("Do not reword the claim", proc.stderr)

    def test_stop_hook_active_lets_through(self):
        # Blocking twice on the same stop would loop forever.
        with tempfile.TemporaryDirectory() as tmp:
            analysis_dir(tmp, "bad")
            proc = run_hook("stop-gate", stdin=payload(Path(tmp), active=True), cwd=Path(tmp))
        self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_off_switch(self):
        with tempfile.TemporaryDirectory() as tmp:
            analysis_dir(tmp, "bad")
            proc = run_hook("stop-gate", stdin=payload(Path(tmp)), cwd=Path(tmp), env={"DSX_STOP_GATE": "off"})
        self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_block_on_threshold_is_honoured(self):
        # The good fixture carries MEDIUM findings; raising sensitivity must block it.
        with tempfile.TemporaryDirectory() as tmp:
            analysis_dir(tmp, "good")
            proc = run_hook("stop-gate", stdin=payload(Path(tmp)), cwd=Path(tmp), env={"DSX_BLOCK_ON": "MEDIUM"})
        self.assertEqual(proc.returncode, 2, proc.stdout)

    def test_malformed_payload_falls_back_to_pwd(self):
        with tempfile.TemporaryDirectory() as tmp:
            analysis_dir(tmp, "bad")
            proc = run_hook("stop-gate", stdin="this is not json", cwd=Path(tmp))
        self.assertEqual(proc.returncode, 2, proc.stdout)

    def test_spec_found_below_cwd(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = analysis_dir(tmp, "bad")
            proc = run_hook("stop-gate", stdin=payload(Path(tmp)), cwd=Path(tmp))
        self.assertEqual(proc.returncode, 2, proc.stdout)
        self.assertIn(str(d / "ANALYSIS-SPEC.yaml"), proc.stderr)


if __name__ == "__main__":
    unittest.main()
