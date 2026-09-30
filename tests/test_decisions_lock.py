"""DECISIONS.jsonl writer serialisation (SEED-004 CL-01) and the unreadable-trail
contract of ``read_all`` (audit L36), plus decision-layer validation (audit L65).

SEED-004's three test obligations, each made real rather than simulated:

1. Concurrent ``dsx gate`` subprocesses against one root get distinct
   invocation ids and ``dsx explain`` groups each run under exactly one header.
2. A writer killed while holding the lock does not wedge the next run.
3. When the lock cannot be taken, the trail is not written and the gate still
   exits on its findings.

Run:  python3 -m unittest tests.test_decisions_lock -v
"""

from __future__ import annotations

import contextlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

from dsx import decisions as d
from dsx.findings import CheckError

ROOT = Path(__file__).resolve().parent.parent
GOOD_SPEC = ROOT / "examples" / "good-ANALYSIS-SPEC.yaml"
ENV = {**os.environ, "PYTHONPATH": str(ROOT)}

# A child that takes the trail lock, reports it, then sleeps until killed.
_HOLDER = """
import sys, time
from dsx.decisions import trail_lock
with trail_lock(sys.argv[1], timeout=5):
    print("locked", flush=True)
    time.sleep(60)
"""


# A real `dsx gate` run whose id derivation is slowed, widening the window
# between counting headers and appending one from microseconds to 300 ms, so
# the race is certain without the lock instead of merely possible.
_SLOW_GATE = """
import sys, time
import dsx.cli as cli
_real = cli.next_invocation_id
def _slow(path):
    inv = _real(path)
    time.sleep(0.3)
    return inv
cli.next_invocation_id = _slow
sys.exit(cli.main(["gate", "plan", "--phase-dir", sys.argv[1]]))
"""


def _spawn_holder(trail: Path) -> subprocess.Popen:
    proc = subprocess.Popen(
        [sys.executable, "-c", _HOLDER, str(trail)],
        stdout=subprocess.PIPE,
        text=True,
        env=ENV,
    )
    line = proc.stdout.readline().strip()
    if line != "locked":
        proc.kill()
        proc.wait()
        raise AssertionError(f"lock holder did not start: {line!r}")
    return proc


def _kill(proc: subprocess.Popen) -> None:
    if proc.poll() is None:
        proc.kill()
    proc.wait()
    proc.stdout.close()


class TestConcurrentGateRuns(unittest.TestCase):
    RUNS = 4

    def test_parallel_gates_get_distinct_ids_and_unbroken_grouping(self):
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copy(GOOD_SPEC, Path(tmp) / "ANALYSIS-SPEC.yaml")
            procs = [
                subprocess.Popen(
                    [sys.executable, "-c", _SLOW_GATE, tmp],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.PIPE,
                    text=True,
                    env=ENV,
                )
                for _ in range(self.RUNS)
            ]
            for proc in procs:
                _, err = proc.communicate(timeout=120)
                self.assertEqual(0, proc.returncode, err)

            records = d.read_all(Path(tmp) / "DECISIONS.jsonl")
            headers = [r for r in records if r.get("record_type") == "invocation"]
            ids = [h["invocation_id"] for h in headers]
            self.assertEqual(
                sorted(ids), [f"INV-{n:04d}" for n in range(1, self.RUNS + 1)]
            )

            # Each run's records are contiguous after its own header.
            current = None
            for record in records:
                if record.get("record_type") == "invocation":
                    current = record["invocation_id"]
                else:
                    self.assertEqual(current, record["invocation_id"])

            # And `dsx explain` renders each run under exactly one header.
            for inv in ids:
                out = subprocess.run(
                    [sys.executable, "-m", "dsx", "explain", "--phase-dir", tmp,
                     "--invocation", inv, "--json"],
                    capture_output=True, text=True, env=ENV, check=True,
                ).stdout
                shown = json.loads(out)
                self.assertEqual(
                    1, sum(1 for r in shown if r.get("record_type") == "invocation")
                )
                self.assertTrue(all(r["invocation_id"] == inv for r in shown))


class TestLockLifecycle(unittest.TestCase):
    def test_lock_released_when_holder_is_killed(self):
        with tempfile.TemporaryDirectory() as tmp:
            trail = Path(tmp) / "DECISIONS.jsonl"
            holder = _spawn_holder(trail)
            try:
                # Held: a short attempt must time out rather than hang.
                with self.assertRaises(d.TrailLockTimeout), d.trail_lock(trail, timeout=0.2):
                    pass
            finally:
                _kill(holder)  # SIGKILL on POSIX: no finally block runs in the child
            self.assertTrue(d.lock_path(trail).exists())  # existence never means "held"
            start = time.monotonic()
            with d.trail_lock(trail, timeout=5):
                pass
            self.assertLess(time.monotonic() - start, 5)

    def test_lock_is_reentrant_across_sequential_uses(self):
        with tempfile.TemporaryDirectory() as tmp:
            trail = Path(tmp) / "DECISIONS.jsonl"
            for _ in range(3):
                with d.trail_lock(trail, timeout=1):
                    d.append(
                        trail,
                        d.InvocationHeader(
                            invocation_id=d.next_invocation_id(trail),
                            gate_point="plan", dsx_version="x", frame_digest="y",
                        ),
                    )
            self.assertEqual("INV-0004", d.next_invocation_id(trail))

    def test_lock_timeout_is_a_check_error(self):
        self.assertTrue(issubclass(d.TrailLockTimeout, CheckError))


class TestGateWhenLockUnavailable(unittest.TestCase):
    def _gate(self, spec_name: str, tmp: str) -> int:
        from dsx.cli import main

        shutil.copy(ROOT / "examples" / spec_name, Path(tmp) / "ANALYSIS-SPEC.yaml")
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return main(["gate", "plan", "--phase-dir", tmp])

    def _gate_with_lock_held(self, spec_name: str) -> tuple[int, bool]:
        with tempfile.TemporaryDirectory() as tmp:
            trail = Path(tmp) / "DECISIONS.jsonl"
            holder = _spawn_holder(trail)
            try:
                with mock.patch.object(d, "LOCK_TIMEOUT_SECONDS", 0.2):
                    code = self._gate(spec_name, tmp)
            finally:
                _kill(holder)
            return code, trail.exists()

    def test_pass_exit_code_unchanged_and_trail_not_written(self):
        code, written = self._gate_with_lock_held("good-ANALYSIS-SPEC.yaml")
        self.assertEqual(0, code)
        self.assertFalse(written)

    def test_block_exit_code_unchanged_and_trail_not_written(self):
        code, written = self._gate_with_lock_held("bad-ANALYSIS-SPEC.yaml")
        self.assertEqual(1, code)
        self.assertFalse(written)


class TestReadAllUnreadableTrail(unittest.TestCase):
    def test_missing_trail_is_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual([], d.read_all(Path(tmp) / "DECISIONS.jsonl"))
            self.assertEqual("INV-0001", d.next_invocation_id(Path(tmp) / "DECISIONS.jsonl"))

    def test_unreadable_trail_raises_check_error_naming_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            trail = Path(tmp) / "DECISIONS.jsonl"
            trail.mkdir()  # exists but cannot be read as a file, on every platform
            with self.assertRaises(CheckError) as ctx:
                d.read_all(trail)
            self.assertIn(str(trail), str(ctx.exception))
            # ...so the id counter can no longer silently restart at INV-0001.
            with self.assertRaises(CheckError):
                d.next_invocation_id(trail)


class TestDecisionLayerValidation(unittest.TestCase):
    def test_known_layers_accepted(self):
        for layer in sorted(d.DECISION_LAYERS):
            with self.subTest(layer=layer):
                self.assertEqual(layer, d.DecisionRecord(id="D", invocation_id="I",
                                                         layer=layer, choice="c").layer)

    def test_unknown_layer_rejected(self):
        with self.assertRaisesRegex(ValueError, "layer 'heuristic'"):
            d.DecisionRecord(id="D", invocation_id="I", layer="heuristic", choice="c")


if __name__ == "__main__":
    unittest.main()
