"""CLI coverage for `dsx charts`, `dsx init`, `dsx seal`, spec discovery, the
programmatic `cmd_gate` guard and the CHECKS registry (2026-09-30 audit items
M8, M10, L7, L9, L10, L12, L16).

Run:  python3 -m unittest tests.test_cli_charts_init -v
"""

from __future__ import annotations

import argparse
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dsx import cli
from dsx.findings import EXIT_ERROR, CheckError

ROOT = Path(__file__).resolve().parent.parent


def _run(argv: list[str]) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        code = cli.main(argv)
    return code, out.getvalue(), err.getvalue()


class TestCharts(unittest.TestCase):
    def test_list_text_names_every_inventory_item(self):
        code, out, _ = _run(["charts", "--list"])
        self.assertEqual(code, 0)
        self.assertIn("IT001", out)
        self.assertIn("IT040", out)
        self.assertIn("permitted:", out)

    def test_list_json_is_the_whole_catalogue(self):
        code, out, _ = _run(["charts", "--list", "--json"])
        self.assertEqual(code, 0)
        rows = json.loads(out)
        self.assertEqual(len(rows), 40)
        self.assertEqual(
            set(rows[0]), {"id", "name", "signature", "columns", "family", "admissible"}
        )

    def test_valid_it_id_prints_permitted_marks(self):
        from dsx.input_types import permitted

        code, out, _ = _run(["charts", "IT007"])
        self.assertEqual(code, 0)
        self.assertEqual(out.strip(), ", ".join(permitted("IT007")))

    def test_valid_shape_json(self):
        code, out, _ = _run(["charts", "it7", "--relationship", "comparison", "--json"])
        self.assertEqual(code, 0)
        payload = json.loads(out)
        self.assertEqual(payload["shape"], "it7")
        self.assertEqual(payload["relationship"], "comparison")
        self.assertTrue(payload["permitted"])

    def test_unknown_shape_is_a_usage_error_exit_2(self):
        code, out, err = _run(["charts", "IT999"])
        self.assertEqual(code, EXIT_ERROR)
        self.assertEqual(out, "")
        self.assertIn("unknown data shape", err)

    def test_missing_shape_is_a_usage_error_exit_2(self):
        code, _, err = _run(["charts"])
        self.assertEqual(code, EXIT_ERROR)
        self.assertIn("give a shape", err)


class TestInit(unittest.TestCase):
    def test_writes_template_to_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "ANALYSIS-SPEC.yaml"
            code, out, _ = _run(["init", "--output", str(target)])
            self.assertEqual(code, 0)
            self.assertIn("wrote", out)
            template = ROOT / "templates" / "ANALYSIS-SPEC.yaml"
            self.assertEqual(
                target.read_text(encoding="utf-8"), template.read_text(encoding="utf-8")
            )

    def test_refuses_to_overwrite_without_force(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "ANALYSIS-SPEC.yaml"
            target.write_text("mine\n", encoding="utf-8")
            code, _, err = _run(["init", "--output", str(target)])
            self.assertEqual(code, EXIT_ERROR)
            self.assertIn("--force", err)
            self.assertEqual(target.read_text(encoding="utf-8"), "mine\n")

    def test_force_overwrites(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "ANALYSIS-SPEC.yaml"
            target.write_text("mine\n", encoding="utf-8")
            code, _, _ = _run(["init", "--output", str(target), "--force"])
            self.assertEqual(code, 0)
            self.assertNotEqual(target.read_text(encoding="utf-8"), "mine\n")

    def test_missing_template_is_exit_2(self):
        with tempfile.TemporaryDirectory() as tmp:
            fake_module = Path(tmp) / "dsx" / "cli.py"
            target = Path(tmp) / "out.yaml"
            with mock.patch.object(cli, "__file__", str(fake_module)):
                code, _, err = _run(["init", "--output", str(target)])
            self.assertEqual(code, EXIT_ERROR)
            self.assertIn("template not found", err)
            self.assertFalse(target.exists())


class TestSeal(unittest.TestCase):
    def test_png_json_uses_the_svg_sha256_spec_field_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            png = Path(tmp) / "chart.png"
            png.write_bytes(b"\x89PNG\r\n\x1a\n")
            code, out, _ = _run(["seal", str(png), "--json"])
            self.assertEqual(code, 0)
            payload = json.loads(out)
            self.assertTrue(payload["svg_sha256"].startswith("sha256:"))

    def test_help_says_the_key_is_svg_sha256_for_every_format(self):
        buf = io.StringIO()
        with redirect_stdout(buf), self.assertRaises(SystemExit):
            cli.main(["seal", "--help"])
        text = " ".join(buf.getvalue().split())
        self.assertIn("svg_sha256 for every format", text)


class TestSpecDiscovery(unittest.TestCase):
    def test_lowercase_yml_and_json_are_discovered(self):
        for name in ("analysis-spec.yml", "analysis-spec.json"):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                (Path(tmp) / name).write_text("{}", encoding="utf-8")
                found = cli.find_spec(None, tmp)
                self.assertEqual(found.name.lower(), name)


class TestGateGuard(unittest.TestCase):
    """L7: argparse `choices` makes the unknown-point guard unreachable from the
    command line, so it is kept for programmatic callers and pinned here."""

    def test_cmd_gate_rejects_unknown_point_when_called_directly(self):
        args = argparse.Namespace(
            point="deploy", block_on=None, spec=None, phase_dir=None,
            allow_missing=False, report=None, json=False, verbose=False,
        )
        with self.assertRaises(CheckError) as cm:
            cli.cmd_gate(args)
        self.assertIn("unknown gate point", str(cm.exception))

    def test_cli_rejects_unknown_point_at_argparse(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as cm:
            cli.main(["gate", "deploy"])
        self.assertEqual(cm.exception.code, 2)


class TestChecksRegistry(unittest.TestCase):
    """L12/L16: CHECKS is the single source of truth, repro included."""

    def test_repro_is_registered(self):
        from dsx.checks import repro

        self.assertIs(cli.CHECKS["repro"].check, repro.check)

    def test_every_gate_profile_name_is_registered(self):
        for point, names in cli.GATE_PROFILES.items():
            for name in names:
                with self.subTest(point=point, name=name):
                    self.assertIn(name, cli.CHECKS)

    def test_check_help_lists_repro_once(self):
        buf = io.StringIO()
        with redirect_stdout(buf), self.assertRaises(SystemExit):
            cli.main(["check", "--help"])
        text = " ".join(buf.getvalue().split())
        self.assertEqual(text.count("repro"), 1)

    def test_unknown_check_name_is_exit_2_and_lists_repro(self):
        spec = ROOT / "examples" / "good-ANALYSIS-SPEC.yaml"
        code, _, err = _run(["check", "nosuchcheck", "--spec", str(spec)])
        self.assertEqual(code, EXIT_ERROR)
        self.assertIn("repro", err)

    def test_run_checks_dispatches_through_the_registry_adapter(self):
        from dsx.findings import Report

        seen = {}

        def fake(check, spec, ctx):
            seen["ctx"] = ctx
            return Report(check="repro")

        entry = cli.CheckEntry(cli.CHECKS["repro"].check, fake)
        with mock.patch.dict(cli.CHECKS, {"repro": entry}):
            cli.run_checks({}, ("repro",), "phase", gate_point="verify", resolve_root="root")
        ctx = seen["ctx"]
        self.assertEqual((ctx.phase_dir, ctx.root, ctx.strict), ("phase", "root", True))
        self.assertFalse(ctx.reconcile_trail)


if __name__ == "__main__":
    unittest.main()
