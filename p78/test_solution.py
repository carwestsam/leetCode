from unittest import TestCase
from p78.Solution import Solution

class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()
  def test_should_return_empty(self):
    self.assertEqual(self.sol.subsets([]), [[]])

  def test_should_return_empty_and_one_element_when_input_one_number(self):
    self.assertEqual(self.sol.subsets([1]), [[1],[]])

  def test_should_return_all_subsets(self):
    subsets = self.sol.subsets([1,2,3])
    self.assertEqual(len(subsets), 8)

  def test_should_return_all_subsets2(self):
    subsets = self.sol.subsets([1,2,3,4])
    self.assertEqual(len(subsets), 16)
