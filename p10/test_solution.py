from unittest import TestCase

from p10.Solution import Solution


class TestSolution(TestCase):
    def test_isMatch(self):
        sol = Solution()

        self.assertEqual(True, sol.isMatch("a", "a"))

    def test_isMatch_if_no_special_chars(self):
        sol = Solution()

        self.assertEqual(True, sol.isMatch("abc", "abc"))
        self.assertEqual(True, sol.isMatch("def", "def"))

        self.assertEqual(False, sol.isMatch("abc", "bc"))
        self.assertEqual(False, sol.isMatch("aa", "a"))

    def test_isMatch_if_have_dot(self):
        sol = Solution()

        self.assertEqual(True, sol.isMatch("abc", "ab."))
        self.assertEqual(True, sol.isMatch("abc", "a.c"))
        self.assertEqual(True, sol.isMatch("xx", ".."))
        self.assertEqual(True, sol.isMatch("xxxxb", "....b"))
        self.assertEqual(True, sol.isMatch("x", "."))

        self.assertEqual(False, sol.isMatch("dd", "."))
        self.assertEqual(False, sol.isMatch("", "."))
        self.assertEqual(False, sol.isMatch("abc", "a.d"))
