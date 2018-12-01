from unittest import TestCase

from p20.Solution import Solution


class TestSolution(TestCase):
    def test_isValid(self):
        sol = Solution()

        self.assertEqual(True, sol.isValid("()"))
        self.assertEqual(False, sol.isValid("{}}"))
        self.assertEqual(True, sol.isValid("()[]{}"))
        self.assertEqual(False, sol.isValid("(]"))
        self.assertEqual(False, sol.isValid("([)]"))
        self.assertEqual(True, sol.isValid("{[]}"))
