from unittest import TestCase
from p310.Solution import Solution
MAX_NUM = 10000000000

__author__ = 'tcsong'


class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_construct_trees(self):
    N = 3
    E = [[0,1],[1,2]]
    tree = self.sol.createTree(N, E)
    self.assertEqual(len(tree[0]["edges"]), 1)
    self.assertEqual(len(tree[1]["edges"]), 2)

    self.assertEqual(tree[0]["conn"], 1)
    self.assertEqual(tree[1]["conn"], 2)

    self.assertEqual(tree[0]["height"], 1)
    self.assertEqual(tree[1]["height"], MAX_NUM)

  def test_get_conn_1_nodes(self):
    N = 3
    E = [[0,1],[1,2]]
    tree = self.sol.createTree(N, E)
    inHandNodes = self.sol.get_conn_nodes(tree)
    self.assertEqual(len(inHandNodes), 2)
    self.assertTrue(0 in [0,2])
    self.assertTrue(2 in [0,2])

    self.assertEqual(tree[0]["height"], 1)
    self.assertEqual(tree[1]["height"], MAX_NUM)

  def test_calc_minimum_height(self):
    N = 6
    E = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    tree = self.sol.createTree(N, E)
    self.sol.calc_minimum_height(tree)
    self.assertEqual(tree[3]['height'],2)
    self.assertEqual(tree[4]['height'],2)

  def test_get_Max_value_height_nodes(self):
    N = 6
    E = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    ans = self.sol.findMinHeightTrees(N, E)
    self.assertEqual(len(ans), 2)



