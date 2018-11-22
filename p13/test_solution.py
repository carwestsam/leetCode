from unittest import TestCase

from p13.Solution import Solution


class TestSolution(TestCase):
    def test_romanToInt(self):
        sol = Solution()

        self.assertEqual(1, sol.romanToInt("I"))
