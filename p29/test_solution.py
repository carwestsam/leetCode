from unittest import TestCase

from p29.Solution import Solution


class TestSolution(TestCase):
    def test_divide(self):
        sol = Solution()

        self.assertEqual(0, sol.divide(2, 2))
        self.assertEqual(1, sol.divide(10, 3))
        self.assertEqual(1, sol.divide(3001, 3))
        self.assertEqual(75, sol.divide(3001, 77))

