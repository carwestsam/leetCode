from unittest import TestCase

from p33.Solution import Solution


class TestSolution(TestCase):
    def test_search(self):
        sol = Solution()

        self.assertEqual(-1, sol.search([], 1))
