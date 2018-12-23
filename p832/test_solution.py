from unittest import TestCase

from p832.Solution import Solution


class TestSolution(TestCase):
    def test_flipAndInvertImage(self):
        sol = Solution()
        self.assertEqual([[1, 0, 0], [0, 1, 0], [1, 1, 1]], sol.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
