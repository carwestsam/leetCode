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

    def test_handle_double_or_more_numbers(self):
        sol = Solution()

        self.assertEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], sol.letterCombinations("23"))
        tmp1 = ["adg", "aeg", "afg", "bdg", "beg", "bfg", "cdg", "ceg", "cfg",
                "adh", "aeh", "afh", "bdh", "beh", "bfh", "cdh", "ceh", "cfh",
                "adi", "aei", "afi", "bdi", "bei", "bfi", "cdi", "cei", "cfi"]
        print(tmp1.sort())
        self.assertEqual(tmp1, sol.letterCombinations("234"))

    def test_should_handle_key_1(self):
        sol = Solution()
        self.assertEqual([], sol.letterCombinations("1"))
        self.assertEqual([], sol.letterCombinations("111"))
        self.assertEqual(['a', 'b', 'c'], sol.letterCombinations("12"))
        self.assertEqual(['a', 'b', 'c'], sol.letterCombinations("21"))
        self.assertEqual(['a', 'b', 'c'], sol.letterCombinations("11211"))
        self.assertEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], sol.letterCombinations("11211311"))
