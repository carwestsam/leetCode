from unittest import TestCase

from p64.Solution import Solution


class TestSolution(TestCase):
    def test_minPathSum(self):
        sol = Solution()
        self.assertEqual(7, sol.minPathSum([
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]))
