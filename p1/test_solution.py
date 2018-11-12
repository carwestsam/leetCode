from unittest import TestCase

from p1.Solution import Solution


class TestSolution(TestCase):
    def test_twoSum(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([1,2], 3), [0,1])
