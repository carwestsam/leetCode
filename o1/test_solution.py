from unittest import TestCase
from o1.Solution import raw,sol1,sol2, set_ct, get_ct
import random
# import numpy as np


# class TestSolution(TestCase):
#     def get_random_arr(self, n):
#         return np.random.randint(1, 1000, n)
#
#     def cell_test(self, func):
#
#         n = 10
#         nums = self.get_random_arr(n)
#         na = list(nums)
#         nb = list(nums)
#
#         set_ct(0)
#         real_first, real_second = func(na)
#         self.assertLessEqual(get_ct(), 3 * (n//2))
#
#         raw_first, raw_second = raw(nb)
#
#         self.assertEqual(raw_first, real_first)
#         self.assertEqual(raw_second, real_second)
#
#     def xtest_raw(self):
#         for i in range(100):
#             self.cell_test(func=sol2)

