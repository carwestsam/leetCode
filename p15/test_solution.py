from unittest import TestCase

from p15.Solution import Solution


class TestSolution(TestCase):
    def test_threeSum(self):
        sol = Solution()
        self.assertEqual([[-1, -2, 3]], sol.threeSum([-1, -2, 3]))
