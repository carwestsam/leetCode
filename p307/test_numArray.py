from unittest import TestCase
import json
from itertools import zip_longest

from p307.Solution import NumArray


class TestNumArray(TestCase):
    def test_update(self):
        num_array = NumArray([1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(4, num_array.sumRange(2, 5))
        num_array.update(3, 2)
        self.assertEqual(5, num_array.sumRange(2, 5))

    def test_sumRange(self):
        num_array = NumArray([1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(6, num_array.sumRange(0, 2))
        self.assertEqual(10, num_array.sumRange(0, 3))
        self.assertEqual(18, num_array.sumRange(4, 6))

    def test_special1(self):
        num_array = NumArray([2])
        self.assertEqual(2, num_array.sumRange(0, 0))
        self.assertEqual(None, num_array.update(0, 1))
        self.assertEqual(1, num_array.sumRange(0, 0))

    def test_special2(self):
        num_array = NumArray([2, 3])
        self.assertEqual(5, num_array.sumRange(0, 1))
        self.assertEqual(None, num_array.update(0, 1))
        self.assertEqual(4, num_array.sumRange(0, 1))

    def test_special3(self):
        # print("hoo")
        with open('failed_case_1.txt', 'r') as file:
            actions = json.loads(file.readline())
            params = json.loads(file.readline())
            num_array = None
            for action, param in zip(actions, params):
                # print(action, param)
                if action == 'sumRange':
                    num_array.sumRange(param[0], param[1])
                elif action == 'update':
                    num_array.sumRange(param[0], param[1])
                elif action == 'NumArray':
                    num_array = NumArray(param[0])
                else:
                    print("Error!")
                    break
