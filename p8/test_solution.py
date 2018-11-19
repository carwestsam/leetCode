from unittest import TestCase

from p8.Solution import Solution


class TestSolution(TestCase):
    def test_myAtoi(self):
        sol = Solution()

        self.assertEqual(0, sol.myAtoi("0"))
