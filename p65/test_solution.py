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

  def test_is_integer_true(self):
    self.assertTrue(self.sol.isNumber("12321"))
    self.assertTrue(self.sol.isNumber("-321312"))
    self.assertTrue(self.sol.isNumber("0"))
    self.assertTrue(self.sol.isNumber("12321371283721937821937281937"))
    self.assertTrue(self.sol.isNumber("-321893212321371283721937821937281937"))

    self.assertFalse(self.sol.isNumber("-0"))
    self.assertFalse(self.sol.isNumber("--1"))
    self.assertFalse(self.sol.isNumber("-12fs21"))
    self.assertFalse(self.sol.isNumber("x12fs"))

  def test_trim_spaces(self):
    self.assertTrue(self.sol.isNumber(" 0 "))

    self.assertFalse(self.sol.isNumber(" 1 23"))

