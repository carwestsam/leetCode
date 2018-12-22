from unittest import TestCase

from p7.Solution import Solution


class TestSolution(TestCase):
    def test_reverse(self):
        sol = Solution()

        self.assertEqual(1, sol.reverse(1))
        self.assertEqual(0, sol.reverse(0))
        self.assertEqual(321, sol.reverse(123))
        self.assertEqual(321, sol.reverse(12300))
        self.assertEqual(-321, sol.reverse(-123))

    def test_reverse_should_return_zero_if_exceed(self):
        sol = Solution()

        self.assertEqual(0, sol.reverse(2147483649))
        self.assertEqual(0, sol.reverse(-2147483649))
