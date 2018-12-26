from unittest import TestCase

from p958.Solution import Solution


class T:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class TestSolution(TestCase):
    def test_isCompleteTree(self):
        sol = Solution()
        t = T(1, T(2, T(4), T(5)), T(3, None, T(7)))
        self.assertEqual(False, sol.isCompleteTree(t))
        t = T(1, T(2, T(4), T(5)), T(3, T(6), T(7)))
        self.assertEqual(True, sol.isCompleteTree(t))
