from unittest import TestCase
from p215.Solution import Solution

class TestSolution(TestCase):
  def test_get_Kth_largest_number(self):
    sol = Solution()
    self.assertEqual(sol.findKthLargest([1],1), [1])

