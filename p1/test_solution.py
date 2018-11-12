from unittest import TestCase

from p1.Solution import Solution


class TestSolution(TestCase):
    def test_twoSum(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([1, 2], 3), [0, 1])

    def test_find_two_in_sorted_array(self):
        sol = Solution()
        self.assertEqual(sol.twoSum([1, 2, 3], 4), [0, 2])
        self.assertEqual(sol.twoSum([3, 23, 435, 1234], 1237), [0, 3])
        self.assertEqual(sol.twoSum([1, 3, 4, 5, 6, 7, 8, 9, 15, 33], 24), [7, 8])
        self.assertEqual(sol.twoSum([1, 3, 4, 5, 6, 7, 8, 9, 15, 33], 23), [6, 8])
