from unittest import TestCase

from p33.Solution import Solution


class TestSolution(TestCase):
    def test_search(self):
        sol = Solution()

        self.assertEqual(-1, sol.search([], 1))
        self.assertEqual(4, sol.search([4, 5, 6, 7, 0, 1, 2], 0))
        self.assertEqual(-1, sol.search([4, 5, 6, 7, 0, 1, 2], 3))
        self.assertEqual(1, sol.search([4, 5, 6, 7, 0, 1, 2], 5))
        self.assertEqual(-1, sol.search([4], 5))
        self.assertEqual(0, sol.search([4], 4))
        self.assertEqual(-1, sol.search([1, 3], 0))
