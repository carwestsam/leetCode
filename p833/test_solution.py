from unittest import TestCase

from p833.Solution import Solution


class TestSolution(TestCase):
    def test_findReplaceString(self):
        sol = Solution()
        self.assertEqual("eeebffff", sol.findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]))
