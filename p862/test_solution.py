from unittest import TestCase

from p862.Solution import Solution


class TestSolution(TestCase):
    def test_shortestSubarray(self):
        sol = Solution()
        self.assertEqual(3, sol.shortestSubarray([2, -1, 2], 3))
        self.assertEqual(1, sol.shortestSubarray([1], 1))
        self.assertEqual(-1, sol.shortestSubarray([1, 2], 4))
        # self.assertEqual(3, sol.shortestSubarray([84,-37,32,40,95], 167))
