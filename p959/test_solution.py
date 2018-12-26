from unittest import TestCase

from p959.Solution import Solution


class TestSolution(TestCase):
    def test_regionsBySlashes(self):
        sol = Solution()
        self.assertEqual(2, sol.regionsBySlashes([" /", "/  "]))
