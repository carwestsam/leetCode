from unittest import TestCase
from p65a.Solution import Solution


class TestSolution(TestCase):
  def test(self):
    self.assertTrue(True)

  def test_integer(self):
    solution = Solution()
    self.assertEqual(solution.isNumber(""), False)

    self.assertTrue(solution.isNumber("0"), True)
    self.assertTrue(solution.isNumber("12"), True)
    self.assertTrue(solution.isNumber("-321"), True)
    self.assertTrue(solution.isNumber("+321"), True)

    self.assertFalse(solution.isNumber("+0321"))
    self.assertFalse(solution.isNumber("-0321"))

  def test_float_without_e(self):
    sol = Solution()

    self.assertTrue(sol.isNumber("1.0"))
    self.assertTrue(sol.isNumber("1.38247932"))
    self.assertTrue(sol.isNumber("+1.38247932"))
    self.assertTrue(sol.isNumber("-1.38247932"))

    self.assertTrue(sol.isNumber(".123321"))
    self.assertTrue(sol.isNumber("123321."))

  def test_float_with_e(self):
    sol = Solution()

    self.assertTrue(sol.isNumber("32e10"))

    self.assertTrue(sol.isNumber("34322.432e10432"))
    self.assertTrue(sol.isNumber("34322.432e+10432"))
    self.assertTrue(sol.isNumber("34322.432e-10432"))

  def test_special_case(self):
    sol = Solution()

    self.assertFalse(sol.isNumber("feafea"))
    self.assertTrue(sol.isNumber(" 1"))


