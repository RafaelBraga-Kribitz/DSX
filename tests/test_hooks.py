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
    for key in ("DSX_STOP_GATE", "DSX_BLOCK_ON", "DSX_PYTHON", "CURSOR_PLUGIN_ROOT", "COPILOT_CLI"):
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


# Everything stop-gate shells out to besides python. A PATH holding only
# symlinks to these simulates a machine with no interpreter installed.
_HOOK_TOOLS = ("cat", "dirname", "grep", "sed", "head", "find", "sort")


def python_free_path(tmp: str, extra: dict | None = None) -> str:
    """Build a bin dir with the hook's coreutils and nothing else; return it.

    ``extra`` maps a file name to script text, for planting a fake interpreter.
    """
    bindir = Path(tmp) / "bin"
    bindir.mkdir()
    for tool in _HOOK_TOOLS:
        real = shutil.which(tool)
        if real is None:
            raise unittest.SkipTest(f"{tool} not on PATH")
        (bindir / tool).symlink_to(real)
    for name, text in (extra or {}).items():
        target = bindir / name
        target.write_text(text, encoding="utf-8")
        target.chmod(0o755)
    return str(bindir)


# Stands in for a Python 2 `python`: it fails the >= 3.9 probe (and anything else).
_FAKE_PY2 = "#!/bin/sh\necho 'Python 2.7.18' >&2\nexit 1\n"


@unittest.skipIf(BASH is None, "bash not available")
@unittest.skipIf(os.name == "nt", "symlinked PATH simulation is POSIX-only")
class TestStopGateWithoutPython(unittest.TestCase):
    """H2: a missing interpreter must not block a stop it has no business blocking."""

    def _spec_dir(self, tmp: str) -> Path:
        d = Path(tmp) / "work"
        d.mkdir()
        (d / "ANALYSIS-SPEC.yaml").write_text("spec_version: 1\n", encoding="utf-8")
        return d

    def test_no_spec_exits_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp) / "empty"
            work.mkdir()
            env = {"PATH": python_free_path(tmp)}
            proc = run_hook("stop-gate", stdin=payload(work), cwd=work, env=env)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(proc.stderr, "")

    def test_stop_hook_active_breaks_the_loop(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = self._spec_dir(tmp)
            env = {"PATH": python_free_path(tmp)}
            proc = run_hook("stop-gate", stdin=payload(work, active=True), cwd=work, env=env)
        self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_compact_json_stop_hook_active_breaks_the_loop(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = self._spec_dir(tmp)
            env = {"PATH": python_free_path(tmp)}
            stdin = json.dumps({"cwd": str(work), "stop_hook_active": True}, separators=(",", ":"))
            proc = run_hook("stop-gate", stdin=stdin, cwd=work, env=env)
        self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_escaped_key_in_a_string_does_not_break_the_loop(self):
        # The literal key quoted inside another field's text is not the flag.
        with tempfile.TemporaryDirectory() as tmp:
            work = self._spec_dir(tmp)
            env = {"PATH": python_free_path(tmp)}
            stdin = json.dumps({"cwd": str(work), "stop_hook_active": False,
                                "note": '{"stop_hook_active": true}'})
            proc = run_hook("stop-gate", stdin=stdin, cwd=work, env=env)
        self.assertEqual(proc.returncode, 2, proc.stderr)

    def test_spec_without_python_blocks_with_a_clear_reason(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = self._spec_dir(tmp)
            env = {"PATH": python_free_path(tmp)}
            proc = run_hook("stop-gate", stdin=payload(work), cwd=work, env=env)
        self.assertEqual(proc.returncode, 2, proc.stdout)
        self.assertIn("no Python 3.9+", proc.stderr)
        self.assertIn("Nothing was verified", proc.stderr)
        self.assertIn("ANALYSIS-SPEC.yaml", proc.stderr)

    def test_payload_cwd_is_honoured_without_python(self):
        # Process cwd has no spec; the payload's cwd does. The sed fallback must
        # read the payload, not quietly search the wrong directory and pass.
        with tempfile.TemporaryDirectory() as tmp:
            work = self._spec_dir(tmp)
            elsewhere = Path(tmp) / "elsewhere"
            elsewhere.mkdir()
            env = {"PATH": python_free_path(tmp)}
            proc = run_hook("stop-gate", stdin=payload(work), cwd=elsewhere, env=env)
            self.assertEqual(proc.returncode, 2, proc.stdout)
            proc = run_hook("stop-gate", stdin=payload(elsewhere), cwd=work, env=env)
            self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_python2_does_not_satisfy_the_probe(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = self._spec_dir(tmp)
            env = {"PATH": python_free_path(tmp, {"python": _FAKE_PY2, "python3": _FAKE_PY2})}
            proc = run_hook("stop-gate", stdin=payload(work), cwd=work, env=env)
        self.assertEqual(proc.returncode, 2, proc.stdout)
        self.assertIn("no Python 3.9+", proc.stderr)

    def test_bad_dsx_python_falls_back_to_a_real_one(self):
        # DSX_PYTHON pointing at a Python 2 is skipped, like install.mjs findPython().
        with tempfile.TemporaryDirectory() as tmp:
            fake = Path(tmp) / "python2"
            fake.write_text(_FAKE_PY2, encoding="utf-8")
            fake.chmod(0o755)
            analysis_dir(tmp, "good")
            proc = run_hook("stop-gate", stdin=payload(Path(tmp)), cwd=Path(tmp),
                            env={"DSX_PYTHON": str(fake)})
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("1 ANALYSIS-SPEC(s) pass", proc.stdout)


if __name__ == "__main__":
    unittest.main()
