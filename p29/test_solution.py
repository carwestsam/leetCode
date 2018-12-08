from unittest import TestCase

from p29.Solution import Solution


class TestSolution(TestCase):
    def test_divide(self):
        sol = Solution()

        self.assertEqual(0, sol.divide(2, 2))
