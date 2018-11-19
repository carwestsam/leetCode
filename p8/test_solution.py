from unittest import TestCase

from p8.Solution import Solution


class TestSolution(TestCase):
    def test_myAtoi(self):
        sol = Solution()

        self.assertEqual(0, sol.myAtoi("0"))

    def test_positive_number_without_white_space(self):
        sol = Solution()

        self.assertEqual(1, sol.myAtoi("1"))
        self.assertEqual(12, sol.myAtoi("12"))
        self.assertEqual(2147483647, sol.myAtoi("2147483647"))
        self.assertEqual(2147483647, sol.myAtoi("2147483647"))

    def test_negative_number_without_white_space(self):
        sol = Solution()

        self.assertEqual(-2, sol.myAtoi("-2"))
        self.assertEqual(-22, sol.myAtoi("-22"))
        self.assertEqual(-232, sol.myAtoi("-232"))

    def test_ignore_whitespace_and_chars(self):
        sol = Solution()

        self.assertEqual(-42, sol.myAtoi("   -42"))
        self.assertEqual(4193, sol.myAtoi("4193 with words"))

