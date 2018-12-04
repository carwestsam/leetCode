from unittest import TestCase

from p24.Solution import Solution


class TestSolution(TestCase):
    def test_swapPairs(self):
        sol = Solution()

        self.assertEqual(None, sol.swapPairs(None))
