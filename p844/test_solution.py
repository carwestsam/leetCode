from unittest import TestCase

from p844.Solution import Solution


class TestSolution(TestCase):
    def test_backspaceCompare(self):
        sol = Solution()
        self.assertEqual(True, sol.backspaceCompare("ab#c", "ad#c"))
        self.assertEqual(True, sol.backspaceCompare("ab##", "c#d#"))
        self.assertEqual(True, sol.backspaceCompare("a##c", "#a#c"))
        self.assertEqual(False, sol.backspaceCompare("a#c", "b"))
        self.assertEqual(True, sol.backspaceCompare("nzp#o#g", "b#nzp#o#g"))


