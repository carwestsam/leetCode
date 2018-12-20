from unittest import TestCase

from p849.Solution import Solution


class TestSolution(TestCase):
    def test_maxDistToClosest(self):
        sol = Solution()

        self.assertEqual(3, sol.maxDistToClosest([1, 0, 0, 0]))
        self.assertEqual(2, sol.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
