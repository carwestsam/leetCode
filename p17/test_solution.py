from unittest import TestCase

from p17.Solution import Solution


class TestSolution(TestCase):
    def test_letterCombinations(self):
        sol = Solution()

        self.assertEqual([], sol.letterCombinations(""))

        self.assertEqual(["a", "b", "c"], sol.letterCombinations("2"))
        self.assertEqual(["d", "e", "f"], sol.letterCombinations("3"))
        self.assertEqual(["g", "h", "i"], sol.letterCombinations("4"))
        self.assertEqual(["j", "k", "l"], sol.letterCombinations("5"))
        self.assertEqual(["m", "n", "o"], sol.letterCombinations("6"))
        self.assertEqual(["p", "q", "r", 's'], sol.letterCombinations("7"))
        self.assertEqual(["t", "u", "v"], sol.letterCombinations("8"))
        self.assertEqual(["w", "x", "y", "z"], sol.letterCombinations("9"))
