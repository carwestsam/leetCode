from unittest import TestCase

from p46.Solution import Solution


class TestSolution(TestCase):
    def test_permute(self):
        sol = Solution()
        self.assertEqual([], sol.permute([]))
        self.assertEqual([[1]], sol.permute([1]))
        self.assertEqual([[1, 2], [2, 1]], sol.permute([1, 2]))
        self.assertEqual([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]], sol.permute([1, 2, 3]))
