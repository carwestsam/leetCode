from unittest import TestCase

from p5.Solution import Solution


class TestSolution(TestCase):
    def test_longestPalindrome(self):
        sol = Solution()
        sol.longestPalindrome("a")

    def test_should_find_by_conbine_reverse_string(self):
        sol = Solution()
        self.assertEqual("aba", sol.longestMatch("abaa", "aaba"))
