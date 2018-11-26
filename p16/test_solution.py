from unittest import TestCase

from p16.Solution import Solution


class TestSolution(TestCase):
    def test_threeSumClosest(self):
        sol = Solution()

        self.assertEqual([0, 0, 0], sol.threeSumClosest([0, 0, 0], 1))
