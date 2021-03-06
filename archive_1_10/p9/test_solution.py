from unittest import TestCase

from p9.Solution import Solution


class TestSolution(TestCase):
    def test_isPalindrome(self):
        sol = Solution()

        self.assertEqual(True, sol.isPalindrome(1))
        self.assertEqual(True, sol.isPalindrome(121))
        self.assertEqual(True, sol.isPalindrome(0))

        self.assertEqual(False, sol.isPalindrome(12))
        self.assertEqual(False, sol.isPalindrome(-121))
        self.assertEqual(False, sol.isPalindrome(10))
