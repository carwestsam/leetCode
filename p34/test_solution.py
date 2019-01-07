from unittest import TestCase

from p34.Solution import Solution


class TestSolution(TestCase):
    def test_searchRange(self):
        sol = Solution()
        self.assertEqual([-1, -1], sol.searchRange([5, 7, 7, 8, 8, 10], 6))
