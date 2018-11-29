from unittest import TestCase

from p17.Solution import Solution


class TestSolution(TestCase):
    def test_letterCombinations(self):
        sol = Solution()

        self.assertEqual(["a", "b", "c"], sol.letterCombinations("2"))
