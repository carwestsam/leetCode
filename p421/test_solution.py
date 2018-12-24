from unittest import TestCase

from p421.Solution import Solution


class TestSolution(TestCase):
    def test_findMaximumXOR(self):
        sol = Solution()
        # self.assertEqual(28, sol.findMaximumXOR([5, 25]))
        self.assertEqual(28, sol.findMaximumXOR([3, 10, 5, 25, 2, 8]))
