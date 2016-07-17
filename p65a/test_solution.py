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



