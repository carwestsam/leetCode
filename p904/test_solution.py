from unittest import TestCase

from p904.Solution import Solution


class TestSolution(TestCase):
    def test_totalFruit(self):
        sol = Solution()
        self.assertEqual(3, sol.totalFruit([1, 2, 1]))
        self.assertEqual(3, sol.totalFruit([0, 1, 2, 2]))
        self.assertEqual(4, sol.totalFruit([1, 2, 3, 2, 2]))
        self.assertEqual(5, sol.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
