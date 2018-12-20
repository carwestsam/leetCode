from unittest import TestCase

from p777.Solution import Solution


class TestSolution(TestCase):
    def test_canTransform(self):
        sol = Solution()
        self.assertEqual(False, sol.canTransform("L", "R"))
        self.assertEqual(True, sol.canTransform("LXRX", "LXXR"))
        self.assertEqual(False, sol.canTransform("RLXX", "XXRL"))
        self.assertEqual(True, sol.canTransform("RXXLRXRXL", "XRLXXRRLX"))
        self.assertEqual(True, sol.canTransform("XXXXRXXXLX", "XXXXRLXXXX"))
