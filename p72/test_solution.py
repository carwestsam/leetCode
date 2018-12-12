from unittest import TestCase

from p72.Solution import Solution


class TestSolution(TestCase):
    def test_minDistance(self):
        sol = Solution()

        self.assertEqual(3, sol.minDistance("horse", "ros"))
        self.assertEqual(5, sol.minDistance("intention", "execution"))
        self.assertEqual(0, sol.minDistance("", ""))
        self.assertEqual(1, sol.minDistance("", "a"))
        self.assertEqual(2, sol.minDistance("abc", "a"))
        self.assertEqual(3, sol.minDistance("abc", ""))
