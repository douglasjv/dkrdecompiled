#!/usr/bin/env python3

import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from find_residual_mechanisms import Instruction, role_pattern  # noqa: E402


class RolePatternTests(unittest.TestCase):
    def test_destructive_and_nondestructive_adds_are_distinct(self):
        destructive = role_pattern(
            [
                Instruction(0, "addu", "t3,t3,s2"),
                Instruction(4, "addu", "s1,t3,t5"),
            ]
        )
        nondestructive = role_pattern(
            [
                Instruction(0, "addu", "t4,t3,s2"),
                Instruction(4, "addu", "s1,t4,t5"),
            ]
        )
        self.assertNotEqual(destructive, nondestructive)
        self.assertEqual(nondestructive[0], "addu $g0,$g1,$g2")
        self.assertEqual(nondestructive[1], "addu $g3,$g0,$g4")

    def test_fpr_roles_survive_normalization(self):
        pattern = role_pattern(
            [
                Instruction(0, "neg.s", "f18,f12"),
                Instruction(4, "add.s", "f8,f12,f12"),
                Instruction(8, "add.s", "f16,f2,f2"),
            ]
        )
        self.assertEqual(
            pattern,
            (
                "neg.s $f0,$f1",
                "add.s $f2,$f1,$f1",
                "add.s $f3,$f4,$f4",
            ),
        )


if __name__ == "__main__":
    unittest.main()
