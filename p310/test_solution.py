from unittest import TestCase
from p310.Solution import Solution

__author__ = 'tcsong'


class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()
  def test_true(self):
    self.assertEqual(1,1)
