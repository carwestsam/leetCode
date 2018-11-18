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
