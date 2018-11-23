from unittest import TestCase

from p14.Solution import Solution


class TestSolution(TestCase):
    def test_should_have_no_common_string(self):
        sol = Solution()

        self.assertEqual("", sol.longestCommonPrefix([]))
        self.assertEqual("", sol.longestCommonPrefix(["abc", "def"]))

    def test_should_have_longest_common_string(self):
        sol = Solution()

        self.assertEqual("fl", sol.longestCommonPrefix(["flower", "flpr"]))
        self.assertEqual("flower", sol.longestCommonPrefix(["flower"]))
