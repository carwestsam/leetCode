from unittest import TestCase
from p310a.Solution import Solution

__author__ = 'tcsong'


class TestSolution(TestCase):
    def setUp(self):
      self.sol = Solution()

    def test_different_cases(self):
      self.assertEqual(len(self.sol.findMinHeightTrees(0, [])), 0)
      self.assertEqual(len(self.sol.findMinHeightTrees(1, [])), 1)
      self.assertEqual(len(self.sol.findMinHeightTrees(4, [[0,1],[1,2],[1,3]])), 1)
      self.assertEqual(len(self.sol.findMinHeightTrees(7, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]])), 2)
      self.assertEqual(len(self.sol.findMinHeightTrees(12, [[0,1],[0,2],[0,3],[3,4],[3,5],[1,6],[4,7],[2,8],[0,9],[0,10],[2,11]])), 2)



