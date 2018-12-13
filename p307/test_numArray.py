from unittest import TestCase

from p307.Solution import NumArray


class TestNumArray(TestCase):
    def test_update(self):
        num_array = NumArray([1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(4, num_array.sumRange(2, 5))
        num_array.update(3, 2)
        self.assertEqual(5, num_array.sumRange(2, 5))

    def test_sumRange(self):
        num_array = NumArray([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(6, num_array.sumRange(0, 2))
        self.assertEqual(10, num_array.sumRange(0, 3))
        self.assertEqual(18, num_array.sumRange(4, 6))

