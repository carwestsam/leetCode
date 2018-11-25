from unittest import TestCase

from p15.Solution import Solution


class TestSolution(TestCase):
    def test_threeSum(self):
        sol = Solution()
        self.assertEqual([[-2, -1, 3]], sol.threeSum([-1, -2, 3]))

        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], sol.threeSum([-1, 0, 1, 2, -1, -4]))
        self.assertEqual([[-2, 0, 2], [-1, 0, 1]], sol.threeSum([-2, -1, 0, 1, 2]))
        self.assertEqual([[-1, 0, 1]], sol.threeSum([-1, 0, 1, 0]))
        self.assertEqual([[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]],
                         sol.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
