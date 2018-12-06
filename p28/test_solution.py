from unittest import TestCase

from p28.Solution import Solution


class TestSolution(TestCase):
    def test_strStr(self):
        sol = Solution()

        self.assertEqual(-1, sol.strStr("hello", "aa"))
