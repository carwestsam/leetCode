from unittest import TestCase

from p135.Solution import Solution


class TestSolution(TestCase):
    def test_candy(self):
        sol = Solution()
        self.assertEqual(5, sol.candy([1, 0, 2]))
