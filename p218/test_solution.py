from unittest import TestCase

from p218.Solution import Solution


class TestSolution(TestCase):
    def test_getSkyline(self):
        sol = Solution()
        self.assertEqual([[1, 10], [2, 0]], sol.getSkyline([[1, 2, 10]]))
        self.assertEqual([[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]],
                         sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
