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

    def test_find_two_in_random_array(self):
        sol = Solution()
        self.assertEqual([0, 3], sol.twoSum([5, 3, 2, 1], 6))
        self.assertEqual([1, 7], sol.twoSum([32, 23, 512, 522, 123, 412, 512, 64, 1, 67, 124], 87))

    def test_if_have_same_number(self):
        sol = Solution()
        self.assertEqual([2, 3], sol.twoSum([12, 12, 64, 64, 33, 33], 128))
