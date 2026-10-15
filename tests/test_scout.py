"""Tests for `dsx scout` — the multi-table schema scout (dsx/scout.py).

Fixtures under tests/fixtures/scout/ are three tiny tables with known defects:
orders fans out against payments (order 102 paid then refunded), customers fans
out against orders, order 106 references a customer that does not exist, the
two ``region`` columns share a name but not a code set, and ``amount`` is in
cents in orders and dollars in payments.

Run:  python -m unittest tests.test_scout -v
"""

from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dsx import cli
from dsx.findings import CheckError
from dsx.scout import check_expectations, scout

FIX = Path(__file__).resolve().parent / "fixtures" / "scout"
ALL = [FIX / "customers.csv", FIX / "orders.csv", FIX / "payments.csv"]


def _join(result: dict, left: str, right: str) -> dict:
    for j in result["joins"]:
        if (j["left"], j["right"]) in ((left, right), (right, left)):
            return j
    raise AssertionError(f"no join {left} = {right}")


def _kinds(result: dict) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for w in result["warnings"]:
        out.setdefault(w["kind"], []).append(w["join"])
    return out


class ScoutTest(unittest.TestCase):
    def setUp(self) -> None:
        self.result = scout(ALL)

    def test_grain_prefers_identifier_and_finds_composite(self):
        tables = self.result["tables"]
        self.assertEqual(tables["customers"]["grain"]["candidate_keys"][0], "customer_id")
        self.assertEqual(tables["orders"]["grain"]["candidate_keys"][0], "order_id")
        self.assertEqual(tables["payments"]["grain"]["candidate_keys"], ["order_id+status"])
        self.assertEqual(tables["payments"]["grain"]["verdict"], "composite_key")

    def test_float_column_is_never_a_grain_key(self):
        # payments.amount has duplicates anyway; build a table where a float is unique.
        with tempfile.TemporaryDirectory() as tmp:
            a = Path(tmp) / "a.csv"
            b = Path(tmp) / "b.csv"
            a.write_text("x,price\n1,1.5\n1,2.5\n", encoding="utf-8")
            b.write_text("x\n1\n", encoding="utf-8")
            res = scout([a, b])
            self.assertEqual(res["tables"]["a"]["grain"]["candidate_keys"], [])
            self.assertEqual(res["tables"]["a"]["grain"]["verdict"], "no_key_found")

    def test_fanout_matrix_matches_hand_count(self):
        j = _join(self.result, "orders.order_id", "payments.order_id")
        self.assertEqual(j["cardinality"], "one_to_many")
        self.assertEqual(j["left_join"]["rows_before"], 6)
        self.assertEqual(j["left_join"]["rows_after"], 7)
        self.assertAlmostEqual(j["left_join"]["fanout"], 7 / 6)
        self.assertAlmostEqual(j["left_join"]["match_rate"], 5 / 6)
        self.assertEqual(j["right_join"]["fanout"], 1.0)

    def test_orphan_rows_flag_low_match_rate_on_the_fact_side(self):
        j = _join(self.result, "customers.customer_id", "orders.customer_id")
        self.assertAlmostEqual(j["right_join"]["match_rate"], 5 / 6)
        details = [w["detail"] for w in self.result["warnings"] if w["kind"] == "low_match_rate"]
        self.assertTrue(any("of orders rows find a match in customers" in d for d in details))

    def test_name_collision_and_unit_mismatch(self):
        kinds = _kinds(self.result)
        self.assertIn("customers.region = orders.region", kinds["name_collision"])
        self.assertIn("orders.amount = payments.amount", kinds["possible_unit_mismatch"])
        # A unit mismatch is not also reported as a name collision.
        self.assertNotIn("orders.amount = payments.amount", kinds.get("name_collision", []))

    def test_flag_columns_are_not_join_candidates(self):
        with tempfile.TemporaryDirectory() as tmp:
            a = Path(tmp) / "a.csv"
            b = Path(tmp) / "b.csv"
            a.write_text("id,active\n1,1\n2,0\n3,1\n", encoding="utf-8")
            b.write_text("other,active\n7,1\n8,0\n9,0\n", encoding="utf-8")
            self.assertEqual(scout([a, b])["joins"], [])

    def test_null_keys_never_match(self):
        with tempfile.TemporaryDirectory() as tmp:
            a = Path(tmp) / "a.csv"
            b = Path(tmp) / "b.csv"
            a.write_text("k,v\n1,a\n2,b\n3,c\n,d\n", encoding="utf-8")
            b.write_text("k,w\n1,a\n2,b\n3,c\n,d\n", encoding="utf-8")
            j = _join(scout([a, b]), "a.k", "b.k")
            self.assertEqual(j["left_join"]["rows_after"], 4)
            self.assertEqual(j["left_join"]["fanout"], 1.0)
            self.assertAlmostEqual(j["left_join"]["null_key_rate"], 0.25)
            self.assertAlmostEqual(j["left_join"]["match_rate"], 0.75)

    def test_expectations(self):
        self.assertEqual(check_expectations(self.result, []), [])
        broken = check_expectations(self.result, ["orders.order_id=payments.order_id"])
        self.assertEqual(len(broken), 1)
        self.assertIn("fanout 1.1667", broken[0])
        # Order of the two sides does not matter.
        flipped = check_expectations(self.result, ["payments.order_id=orders.order_id"])
        self.assertEqual(len(flipped), 1)
        missing = check_expectations(self.result, ["orders.nope=payments.order_id"])
        self.assertIn("no such table column orders.nope", missing[0])
        with self.assertRaises(CheckError):
            check_expectations(self.result, ["orders.order_id"])

    def test_clean_one_to_one_expectation_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            a = Path(tmp) / "a.csv"
            b = Path(tmp) / "b.csv"
            a.write_text("id,v\n1,10\n2,20\n3,30\n", encoding="utf-8")
            b.write_text("id,w\n1,x\n2,y\n3,z\n", encoding="utf-8")
            res = scout([a, b])
            self.assertEqual(check_expectations(res, ["a.id=b.id"]), [])
            self.assertEqual(_join(res, "a.id", "b.id")["cardinality"], "one_to_one")

    def test_input_errors(self):
        with self.assertRaises(CheckError):
            scout([ALL[0]])
        with self.assertRaises(CheckError):
            scout([ALL[0], FIX / "absent.csv"])
        with tempfile.TemporaryDirectory() as tmp:
            dup = Path(tmp) / "orders.csv"
            dup.write_text("a\n1\n", encoding="utf-8")
            with self.assertRaises(CheckError):
                scout([ALL[1], dup])

    def test_deterministic(self):
        self.assertEqual(json.dumps(scout(ALL), sort_keys=True), json.dumps(self.result, sort_keys=True))
        self.assertEqual(
            json.dumps(scout(list(reversed(ALL)))["warnings"], sort_keys=True),
            json.dumps(scout(list(reversed(ALL)))["warnings"], sort_keys=True),
        )


class ScoutCliTest(unittest.TestCase):
    def _run(self, argv: list[str]) -> tuple[int, str]:
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = cli.main(argv)
        return code, out.getvalue()

    def test_exit_codes(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = str(Path(tmp) / "SCHEMA-SCOUT.yaml")
            files = [str(p) for p in ALL]
            code, _ = self._run(["scout", *files, "--out", out])
            self.assertEqual(code, 0)
            self.assertTrue(Path(out).read_text(encoding="utf-8").startswith("scout_version: 1"))
            code, text = self._run(
                ["scout", *files, "--out", out, "--json",
                 "--expect", "orders.order_id=payments.order_id"]
            )
            self.assertEqual(code, 1)
            self.assertEqual(len(json.loads(text)["expectation_failures"]), 1)
            code, _ = self._run(["scout", files[0], "--out", out])
            self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
