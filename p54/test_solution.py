from unittest import TestCase

from p54.Solution import Solution


class TestSolution(TestCase):
    def test_spiralOrder(self):
        sol = Solution()
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
