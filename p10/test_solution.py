from unittest import TestCase

from p10.Solution import Solution


class TestSolution(TestCase):
    def test_isMatch(self):
        sol = Solution()

        self.assertEqual(True, sol.isMatch("a", "a"))
