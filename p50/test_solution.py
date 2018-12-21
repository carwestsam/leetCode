from unittest import TestCase

from p50.Solution import Solution


class TestSolution(TestCase):
    def test_myPow(self):
        sol = Solution()

        self.assertAlmostEqual(1024.0, sol.myPow(2.0, 10), 0.001)
        self.assertAlmostEqual(0.125, sol.myPow(2.0, -3), 0.001)
