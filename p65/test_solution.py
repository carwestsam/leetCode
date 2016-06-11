from unittest import TestCase
from p65.Solution import Solution
__author__ = 'tcsong'


class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_isNumber(self):
    self.assertFalse(self.sol.isNumber(""))
