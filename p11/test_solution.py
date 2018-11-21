from unittest import TestCase

from p11.Solution import Solution


class TestSolution(TestCase):
    def test_maxArea(self):
        sol = Solution()
        self.assertEqual(1, sol.maxArea([1, 1]))
