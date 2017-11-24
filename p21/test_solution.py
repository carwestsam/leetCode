from unittest import TestCase
from p21.Solution import Solution

class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()
  def test_should_return_empty_list(self):
    result = self.sol.mergeTwoLists([], [])
    self.assertEqual(result, [])