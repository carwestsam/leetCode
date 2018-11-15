from unittest import TestCase

from p4.Solution import Solution


class TestSolution(TestCase):
    def test_findMedianSortedArrays(self):
        self.assertTrue(True)

    def test_find_median_of_no_overlap_arrays(self):
        sol = Solution()
        self.assertEqual(2, sol.findMedianSortedArrays([1], [2, 3]))
        self.assertEqual(8, sol.findMedianSortedArrays([1, 2], [7, 8, 9, 10, 11]))
        self.assertEqual(8, sol.findMedianSortedArrays([7, 8, 9, 10, 11], [1, 2]))
        self.assertEqual(8.5, sol.findMedianSortedArrays([7, 8, 9, 10, 11, 12], [1, 2]))
