from unittest import TestCase
from p44.Solution import Solution

__author__ = 'tcsong'


class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_isSimpleEqual(self):
    self.assertTrue(self.sol.isMatch("", ""))
    self.assertTrue(self.sol.isMatch("123", "123"))
    self.assertFalse(self.sol.isMatch("321", "123"))

  def test_question_mark(self):
    self.assertTrue(self.sol.isMatch("a","?"))
    self.assertFalse(self.sol.isMatch("?", "a"))
    self.assertFalse(self.sol.isMatch("", "?"))

  def test_star_mark(self):
    self.assertTrue(self.sol.isMatch("", "*"))
    self.assertTrue(self.sol.isMatch("aa", "*"))
    self.assertTrue(self.sol.isMatch("aa", "a*"))
    self.assertTrue(self.sol.isMatch("ab", "?*"))
    self.assertFalse(self.sol.isMatch("aab", "c*a*b"))

  def suit_tle(self):
    self.assertTrue(self.sol.isMatch("abbabbbaabaaabbbbbabbabbabbbabbaaabbbababbabaaabbab", "*aabb***aa**a******aa*"))