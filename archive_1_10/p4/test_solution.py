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

    def test_find_by_index_in_one_empty_list(self):
        sol = Solution()

        self.assertEqual(7, sol.findByIndex([], [1, 3, 5, 7], 4))
        self.assertEqual(4, sol.findMedianSortedArrays([], [1, 3, 5, 7]))
        self.assertEqual(7, sol.findByIndex([1, 3, 5, 7], [], 4))
        self.assertEqual(4, sol.findMedianSortedArrays([1, 3, 5, 7], []))

    def test_find_scope(self):
        sol = Solution()

        self.assertEqual((3, 4, 1), sol.findScope([1, 2, 3, 4, 5], 4, 0, 5))
        self.assertEqual((3, 4, 1), sol.findScope([1, 2, 4, 4, 5], 4, 0, 5))
        self.assertEqual((4, 5, 3), sol.findScope([1, 2, 4, 4, 5, 6, 7, 8], 5.5, 0, 8))
        self.assertEqual((4, 2, 2), sol.findScope([1, 2, 4, 4, 5, 6, 7, 8], 5.5, 3, 7))
        self.assertEqual((0, 0, 0), sol.findScope([1, 2, 3], 3, 2, 2))
        self.assertEqual((2, 0, 1), sol.findScope([1, 2, 3], 2, 2, 3))
        self.assertEqual((2, 3, 0), sol.findScope([2, 2, 2], 2, 0, 3))
        self.assertEqual((0, 0, 3), sol.findScope([2, 2, 2], 2, 0, 3, False))
        self.assertEqual((1, 2, 2), sol.findScope([1, 3, 5, 7], 4, 0, 4))
        self.assertEqual((2, 2, 2), sol.findScope([1, 3, 5, 7], 4, 0, 4, False))

    def test_find_by_index_in_two_array(self):
        sol = Solution()

        self.assertEqual(3, sol.findByIndex([1, 3, 5, 7], [2, 4, 6, 8], 3))
        self.assertEqual(4, sol.findByIndex([1, 3, 5, 7], [2, 4, 6, 8], 4))
        self.assertEqual(5, sol.findByIndex([1, 3, 5, 7], [2, 4, 6, 8], 5))
        self.assertEqual(1, sol.findByIndex([1, 1], [1, 1], 2))

    def test_find_median(self):
        sol = Solution()

        self.assertEqual(4.5, sol.findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6, 8]))
        self.assertEqual(4, sol.findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6]))

    def test_find_median2(self):
        sol = Solution()

        self.assertEqual(2, sol.findMedianSortedArrays([1, 3], [2]))
        self.assertEqual(2, sol.findMedianSortedArrays([1, 2, 3], []))
        self.assertEqual(2.5, sol.findMedianSortedArrays([1, 2, 3, 4], []))
        self.assertEqual(2.5, sol.findMedianSortedArrays([1, 2, 3, 4], []))
        self.assertEqual(4, sol.findMedianSortedArrays([1, 2, 3, 4], [2, 6, 7, 8, 9]))
        self.assertEqual(4.5, sol.findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6, 8]))
        self.assertEqual(1, sol.findMedianSortedArrays([1], []))
        self.assertEqual(1, sol.findMedianSortedArrays([], [1]))
        self.assertEqual(1, sol.findMedianSortedArrays([1], [1]))
        self.assertEqual(2.5, sol.findMedianSortedArrays([1], [4]))
        self.assertEqual(1, sol.findMedianSortedArrays([1, 1], [1, 1]))
        self.assertEqual(1, sol.findMedianSortedArrays([1, 1, 1], [1, 1]))
        self.assertEqual(2.5, sol.findMedianSortedArrays([2], [1, 3, 4]))
