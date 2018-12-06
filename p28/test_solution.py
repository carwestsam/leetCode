from unittest import TestCase

from p28.Solution import Solution


class TestSolution(TestCase):
    def test_strStr(self):
        sol = Solution()

        self.assertEqual(-1, sol.strStr("hello", "aa"))

    def test_should_return_zero_when_needle_is_empty(self):
        sol = Solution()
        self.assertEqual(0, sol.strStr("hello", ""))

    def test_should_return_zero_when_plant_is_true(self):
        sol = Solution()
        self.assertEqual(1, sol.strStr("aabababa", "abababa"))
        self.assertEqual(2, sol.strStr("Hello", "ll"))
        self.assertEqual(-1, sol.strStr("aaaaa", "bba"))
        self.assertEqual(1, sol.strStr("Hello", "ello"))

    def test_wrong_case(self):
        sol = Solution()

        self.assertEqual(4, sol.strStr("mississippi", "issip"))
        self.assertEqual(0, sol.strStr("a", "a"))
