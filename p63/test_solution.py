from unittest import TestCase

from p63.Solution import Solution


class TestSolution(TestCase):
    def test_uniquePathsWithObstacles(self):
        sol = Solution()
        self.assertEqual(0, sol.uniquePathsWithObstacles([
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]))
