from unittest import TestCase

from p32.Solution import Solution


class TestSolution(TestCase):
    def test_longestValidParentheses(self):
        sol = Solution()

        self.assertEqual(0, sol.longestValidParentheses(")("))
        self.assertEqual(2, sol.longestValidParentheses("())()"))
        self.assertEqual(4, sol.longestValidParentheses("()()"))
        self.assertEqual(4, sol.longestValidParentheses(")()()"))
        self.assertEqual(4, sol.longestValidParentheses(")()())"))
        self.assertEqual(4, sol.longestValidParentheses(")))(())(("))
        self.assertEqual(8, sol.longestValidParentheses("))((()))()"))
        self.assertEqual(22, sol.longestValidParentheses(")(((((()())()()))()(()))("))
        self.assertEqual(132, sol.longestValidParentheses(
            ")(()(()(((())(((((()()))((((()()(()()())())())()))()()()())(())()()(((()))))()((()))(((())()((()()())((())))(())))())((()())()()((()((())))))((()(((((()((()))(()()(())))((()))()))())"
            ))
