from unittest import TestCase

from p307.Solution import NumArray


class TestNumArray(TestCase):
    def test_update(self):
        # self.fail()
        pass

    def test_sumRange(self):
        num_array = NumArray([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(6, num_array.sumRange(0, 2))
