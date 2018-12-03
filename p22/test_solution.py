from unittest import TestCase

from p22.Solution import Solution


class TestSolution(TestCase):
    def test_generateParenthesis(self):
        sol = Solution()

        self.assertEqual([], sol.generateParenthesis(0))
        self.assertEqual(["()"], sol.generateParenthesis(1))
        self.assertEqual(["(())", "()()"], sol.generateParenthesis(2))
        self.assertEqual(["((()))", "(()())", "(())()", "()(())", "()()()"], sol.generateParenthesis(3))
