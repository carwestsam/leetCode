from unittest import TestCase
from p310.Solution import Solution

__author__ = 'tcsong'


class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_construct_trees(self):
    N = 3
    E = [[1,2],[2,3]]
    tree = self.sol.createTree(N, E)
    self.assertEqual(len(tree[1]["edges"]), 1)
    self.assertEqual(len(tree[2]["edges"]), 2)

    self.assertEqual(tree[1]["conn"], 1)
    self.assertEqual(tree[2]["conn"], 2)

