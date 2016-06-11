from unittest import TestCase
from p65.Solution import Solution
__author__ = 'tcsong'


class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_is_empty_false(self):
    self.assertFalse(self.sol.isNumber(""))

  def test_is_zero_true(self):
    self.assertTrue(self.sol.isNumber("0"))
