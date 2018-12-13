from unittest import TestCase

from p315.Solution import Solution


class TestSolution(TestCase):
    def test_countSmaller(self):
        sol = Solution()
        self.assertEqual([0], sol.countSmaller([1]))
