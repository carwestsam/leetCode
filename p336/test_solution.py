from unittest import TestCase

from p336.Solution import Solution


class TestSolution(TestCase):
    def test_palindromePairs(self):
        sol = Solution()
        self.assertEqual([[0, 1], [1, 0]], sol.palindromePairs(["a", ""]))
        self.assertEqual([[0, 5], [5, 0], [3, 0], [4, 0], [1, 3], [2, 4]]
                         , sol.palindromePairs(["a", "b", "c", "ab", "ac", "aa"]))
