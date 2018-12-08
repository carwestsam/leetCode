from unittest import TestCase

from p29.Solution import Solution


class TestSolution(TestCase):
    def test_divide(self):
        sol = Solution()

        self.assertEqual(1, sol.divide(2, 2))
        self.assertEqual(3, sol.divide(10, 3))
        self.assertEqual(38, sol.divide(3001, 77))

    def test_handle_negtive(self):
        sol = Solution()

        self.assertEqual(-2, sol.divide(7, -3))
        self.assertEqual(-7, sol.divide(21, -3))
        self.assertEqual(-8, sol.divide(-23, 3))
        self.assertEqual(-8, sol.divide(-24, 3))
        self.assertEqual(7, sol.divide(-23, -3))
        self.assertEqual(44574, sol.divide(-3432213, -77))

