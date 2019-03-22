import unittest

from algorithms.divide_search.binary_search import max_pos_not_larger_than_K, max_pos_smaller_then_K, \
    min_pos_large_or_equal_K


class TestBinarySearch(unittest.TestCase):
    def test_max_pos_not_larger_than_K(self):
        self.assertEqual(max_pos_not_larger_than_K([1, 2, 3, 3, 3, 4, 5], 3), 4)
        self.assertEqual(max_pos_not_larger_than_K([1, 2, 3, 3, 4, 5], 3), 3)

    def test_max_pos_smaller_then_K(self):
        self.assertEqual(max_pos_smaller_then_K([1, 2, 3, 3, 3, 4, 5], 4), 4)
        self.assertEqual(max_pos_smaller_then_K([1, 2, 3, 3, 3, 4, 5], 5), 5)

    def test_min_pos_large_or_equal_K(self):
        self.assertEqual(min_pos_large_or_equal_K([1, 2, 3, 4, 4, 4, 4, 5], 4), 3)
        self.assertEqual(min_pos_large_or_equal_K([1, 2, 3, 4, 5, 6], 2), 1)
