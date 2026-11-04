"""Error-reporting contracts of the CLI (2026-09-30 audit items M6, M11, M12, M17).

- `--json` reports go to stdout whether or not they block; the exit code is
  the verdict (M17).
- An invalid-input ValueError keeps its message and exit 2, and shows the
  traceback under DSX_DEBUG=1 or --verbose (M11).
- `dsx explain` / `dsx stats` still exit 0 on an unreadable trail, but say so
  on stderr and in their JSON (M12).
- `dsx stats` dispatches its report through a selector table; the paradigm
  split is the default report (M6).

Run:  python3 -m unittest tests.test_cli_error_reporting -v
"""

from __future__ import annotations

import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dsx import cli
from dsx.decisions import DecisionRecord, InvocationHeader, append

ROOT = Path(__file__).resolve().parent.parent
GOOD = ROOT / "examples" / "good-ANALYSIS-SPEC.yaml"
BAD = ROOT / "examples" / "bad-ANALYSIS-SPEC.yaml"


def _run(argv: list[str]) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        code = cli.main(argv)
    return code, out.getvalue(), err.getvalue()


def _seed(path: Path, digest: str = "frame-1", paradigm: str = "frequentist") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    append(
        path,
        InvocationHeader(
            invocation_id="INV-0001", gate_point="plan", dsx_version="test",
            frame_digest=digest,
        ),
    )
    append(
        path,
        DecisionRecord(
            id="DEC-001", invocation_id="INV-0001", layer="deterministic",
            choice=f"paradigm={paradigm}",
        ),
    )


def _unreadable():
    """Make every trail read fail the way an unreadable file does. Patched on
    dsx.cli (the name the readers call) so the test does not depend on which
    on-disk states dsx.decisions.read_all chooses to raise for."""
    return mock.patch.object(cli, "read_all", side_effect=PermissionError("boom"))


class TestJsonOnStdout(unittest.TestCase):
    def test_blocking_audit_json_goes_to_stdout(self):
        code, out, err = _run(["audit", "--spec", str(BAD), "--json"])
        self.assertEqual(code, 1)
        self.assertEqual(err, "")
        payload = json.loads(out)
        self.assertTrue(payload["block"])

    def test_passing_audit_json_goes_to_stdout(self):
        code, out, _ = _run(["validate", "--spec", str(GOOD), "--json"])
        self.assertEqual(code, 0)
        self.assertFalse(json.loads(out)["block"])

    def test_blocking_gate_json_goes_to_stdout(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, out, _ = _run(
                ["gate", "plan", "--spec", str(BAD), "--phase-dir", tmp, "--json"]
            )
        self.assertEqual(code, 1)
        self.assertTrue(json.loads(out)["block"])

    def test_blocking_text_still_goes_to_stderr(self):
        code, out, err = _run(["audit", "--spec", str(BAD)])
        self.assertEqual(code, 1)
        self.assertEqual(out, "")
        self.assertIn("BLOCK", err)


class TestInvalidInputTraceback(unittest.TestCase):
    ARGV = ("validate", "--spec", str(GOOD), "--block-on", "bogus")

    def test_message_and_exit_2_without_traceback_by_default(self):
        with mock.patch.dict(os.environ, {cli.DEBUG_ENV: ""}):
            code, _, err = _run(list(self.ARGV))
        self.assertEqual(code, 2)
        self.assertIn("invalid input", err)
        self.assertNotIn("Traceback", err)
        self.assertIn(cli.DEBUG_ENV, err)

    def test_traceback_under_debug_env(self):
        with mock.patch.dict(os.environ, {cli.DEBUG_ENV: "1"}):
            code, _, err = _run(list(self.ARGV))
        self.assertEqual(code, 2)
        self.assertIn("invalid input", err)
        self.assertIn("Traceback", err)

    def test_traceback_under_verbose(self):
        with mock.patch.dict(os.environ, {cli.DEBUG_ENV: ""}):
            code, _, err = _run([*self.ARGV, "--verbose"])
        self.assertEqual(code, 2)
        self.assertIn("Traceback", err)

    def test_help_epilog_names_the_env_var(self):
        buf = io.StringIO()
        with redirect_stdout(buf), self.assertRaises(SystemExit):
            cli.main(["--help"])
        self.assertIn(cli.DEBUG_ENV, buf.getvalue())


class TestExplainUnreadable(unittest.TestCase):
    def test_no_trail_is_an_empty_array(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, out, err = _run(["explain", "--phase-dir", tmp, "--json"])
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out), [])
        self.assertEqual(err, "")

    def test_unreadable_trail_exits_0_but_reports_status_and_stderr(self):
        with tempfile.TemporaryDirectory() as tmp:
            _seed(Path(tmp) / "DECISIONS.jsonl")
            with _unreadable():
                code, out, err = _run(["explain", "--phase-dir", tmp, "--json"])
            self.assertEqual(code, 0)
            payload = json.loads(out)
            self.assertEqual(payload["status"], "unreadable")
            self.assertEqual(payload["error"], "PermissionError: boom")
            self.assertIn("could not read the decision trail", err)

            with _unreadable():
                code, out, err = _run(["explain", "--phase-dir", tmp])
            self.assertEqual(code, 0)
            self.assertIn("no readable decision trail", out)
            self.assertIn("PermissionError: boom", err)


class TestStatsStatus(unittest.TestCase):
    def test_status_distinguishes_ok_empty_and_unreadable(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, out, err = _run(["stats", "--root", tmp, "--json"])
            self.assertEqual(code, 0)
            self.assertEqual(json.loads(out)["status"], "no_history")
            self.assertEqual(err, "")

            trail = Path(tmp) / "p" / "DECISIONS.jsonl"
            _seed(trail)
            data = json.loads(_run(["stats", "--root", tmp, "--json"])[1])
            self.assertEqual(data["status"], "ok")
            self.assertEqual(data["paradigm_split"]["frequentist"], 1)

            with _unreadable():
                code, out, err = _run(["stats", "--root", tmp, "--json"])
            self.assertEqual(code, 0)
            data = json.loads(out)
            self.assertEqual(data["status"], "unreadable")
            self.assertEqual(data["error"], "PermissionError: boom")
            self.assertNotIn("shares", data)
            self.assertIn("could not read operator decision trails", err)

            with _unreadable():
                code, out, err = _run(["stats", "--root", tmp])
            self.assertEqual(code, 0)
            self.assertIn("could not be read", out)
            self.assertNotIn("no operator history", out)


class TestStatsSelectorDispatch(unittest.TestCase):
    def test_paradigm_is_the_default_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            _seed(Path(tmp) / "p" / "DECISIONS.jsonl")
            bare = _run(["stats", "--root", tmp, "--json"])
            flagged = _run(["stats", "--paradigm", "--root", tmp, "--json"])
        self.assertEqual(bare, flagged)

    def test_dispatch_goes_through_the_selector_table(self):
        calls: list[str] = []
        table = {"paradigm": lambda args: calls.append("paradigm")}
        with mock.patch.object(cli, "_STATS_REPORTS", table):
            self.assertEqual(_run(["stats", "--paradigm"])[0], 0)
            self.assertEqual(_run(["stats"])[0], 0)
        self.assertEqual(calls, ["paradigm", "paradigm"])


if __name__ == "__main__":
    unittest.main()
