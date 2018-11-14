from unittest import TestCase

from p3.Solution import Solution


class TestSolution(TestCase):
    def test_lengthOfLongestSubstring(self):
        self.assertTrue(True)

    def test_should_get_longest_substring_from_specific_position(self):
        sol = Solution()

        self.assertEqual(3, sol.lengthOfLongestSubstringIndex("abcabcbb", 0))
        self.assertEqual(1, sol.lengthOfLongestSubstringIndex("bbbbb", 2))
        self.assertEqual(3, sol.lengthOfLongestSubstringIndex("pwwkew", 2))

    def test_should_get_longest_substring_by_looping(self):
        sol = Solution()

        self.assertEqual(3, sol.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(1, sol.lengthOfLongestSubstring("bbbbb"))
        self.assertEqual(3, sol.lengthOfLongestSubstring("pwwkew"))
