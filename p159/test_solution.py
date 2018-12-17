from unittest import TestCase

from p159.Solution import Solution


class TestSolution(TestCase):
    def test_lengthOfLongestSubstringTwoDistinct(self):
        sol = Solution()
        self.assertEqual(3, sol.lengthOfLongestSubstringTwoDistinct("eceba"))
        self.assertEqual(5, sol.lengthOfLongestSubstringTwoDistinct("ccaabbb"))
