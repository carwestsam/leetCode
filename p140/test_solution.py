from unittest import TestCase

from p140.Solution import Solution


class TestSolution(TestCase):
    def test_wordBreak(self):
        sol = Solution()
        self.assertEqual(["a b c"], sol.wordBreak("abc", ["a", "b", "c"]))
        self.assertEqual(["cat sand dog", "cats and dog"],
                         sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))

        self.assertEqual([], sol.wordBreak(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", \
            ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
