from unittest import TestCase

from p279.Solution import Solution


class TestSolution(TestCase):
    def test_numSquares(self):
        sol = Solution()
        self.assertEqual(3, sol.numSquares(12))
        self.assertEqual(2, sol.numSquares(13))
        self.assertEqual(2, sol.numSquares(1025))
        self.assertEqual(3, sol.numSquares(22))
        self.assertEqual(3, sol.numSquares(48))
        self.assertEqual(3, sol.numSquares(88))
        # #
        # self.assertEqual(3, sol.numSquares(1232142))
        # self.assertEqual(3, sol.numSquares(123212342))
