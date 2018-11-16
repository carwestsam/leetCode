from unittest import TestCase

from p5.Solution import Solution


class TestSolution(TestCase):
    def test_longestPalindrome(self):
        sol = Solution()
        sol.longestPalindrome("a")
