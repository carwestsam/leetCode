from unittest import TestCase

from p7.Solution import Solution


class TestSolution(TestCase):
    def test_reverse(self):
        sol = Solution()

        self.assertEqual(1, sol.reverse(1))
        self.assertEqual(1, sol.reverse(1))


