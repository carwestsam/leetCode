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

