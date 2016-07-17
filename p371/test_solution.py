from unittest import TestCase
from p371.Solution import Solution


class TestSolution(TestCase):

  def test_plus(self):
    solution = Solution()
    self.assertEqual(solution.getSum(1,2), 3)