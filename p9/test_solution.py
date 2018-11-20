from unittest import TestCase

from p9.Solution import Solution


class TestSolution(TestCase):
    def test_isPalindrome(self):
        sol = Solution()

        self.assertEqual(True, sol.isPalindrome(1))

