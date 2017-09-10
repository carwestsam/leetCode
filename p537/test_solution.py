from unittest import TestCase
from p537.Solution import Solution


class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_get_expected_a_b_of_complex_number(self):
    self.assertEqual(self.sol.parseComplex("12+3i"), (12,3))
    self.assertEqual(self.sol.parseComplex("12+-3i"), (12,-3))
    self.assertEqual(self.sol.parseComplex("0+1i"), (0,1))

  def test_calc_mulitply_of_complex_number(self):
    self.assertEqual(self.sol.multiply((1,1), (1,1)), (0,2))
    self.assertEqual(self.sol.multiply((1, -1),(1, -1)), (0, -2))
    self.assertEqual(self.sol.multiply((3, -1),(1, -2)), (1, -7))

  def test_print_complex(self):
    self.assertEqual(self.sol.convert((3,2)), "3+2i")
    self.assertEqual(self.sol.convert((0,-3)), "0+-3i")
