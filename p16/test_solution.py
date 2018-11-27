from unittest import TestCase

from p16.Solution import Solution


class TestSolution(TestCase):
    def test_threeSumClosest(self):
        sol = Solution()

        self.assertEqual(0, sol.threeSumClosest([0, 0, 0], 1))
        self.assertEqual(-4, sol.threeSumClosest([-1, 2, 1, -4], -5))
        self.assertEqual(2, sol.threeSumClosest([-1, 2, 1, -4], 3))
        self.assertEqual(2, sol.threeSumClosest([-1, 2, 1, -4], 3))
        self.assertEqual(2, sol.threeSumClosest([-1, 2, 1, -4], 1))
        # self.assertEqual(0, sol.threeSumClosest([0, 2, 1, -3], 1))
