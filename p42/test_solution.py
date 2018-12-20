from unittest import TestCase

from p42.Solution import Solution


class TestSolution(TestCase):
    def test_trap(self):
        sol = Solution()
        self.assertEqual(6, sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
