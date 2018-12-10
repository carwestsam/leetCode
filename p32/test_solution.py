from unittest import TestCase

from p32.Solution import Solution


class TestSolution(TestCase):
    def test_longestValidParentheses(self):
        sol = Solution()

        self.assertEqual(0, sol.longestValidParentheses(")("))
