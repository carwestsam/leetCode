from unittest import TestCase

from p139.Solution import Solution


class TestSolution(TestCase):
    def test_wordBreak(self):
        sol = Solution()
        self.assertEqual(True, sol.wordBreak('leetcode', ['leet', 'code']))
        self.assertEqual(True, sol.wordBreak("applepenapple", ["apple", "pen"]))
        self.assertEqual(False, sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
