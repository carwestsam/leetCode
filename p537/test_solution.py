from unittest import TestCase
from p537.Solution import Solution


class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_get_expected_a_b_of_complex_number(self):
    self.assertEqual(self.sol.parseComplex("12+3i"), (12,3))
    self.assertEqual(self.sol.parseComplex("12+-3i"), (12,-3))
    self.assertEqual(self.sol.parseComplex("0+1i"), (0,1))