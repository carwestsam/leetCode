from unittest import TestCase

from p1.Solution import Solution


class TestSolution(TestCase):
    def test_twoSum(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([1, 2], 3), [0, 1])

    def test_find_two_in_sorted_array(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([1, 2, 3], 4), [0, 2])
