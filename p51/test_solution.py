from unittest import TestCase
from p51.Solution import Solution


class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_true(self):
    self.assertTrue(True)

  def test_n_queen_dictinct_solution(self):
    self.assertEqual(self.sol.raw_solveNQueens(2), 0)
    self.assertEqual(self.sol.raw_solveNQueens(4), 2)
    self.assertEqual(self.sol.raw_solveNQueens(8), 92)

  def test_translate_number_to_string(self):
    self.sol.pre_trans(2)
    self.assertEqual(self.sol.trans(1), "Q.")
    self.assertEqual(self.sol.trans(2), ".Q")

    self.sol.pre_trans(3)
    self.assertEqual(self.sol.trans(1), "Q..")
    self.assertEqual(self.sol.trans(4), "..Q")

  def test_solve_n_queen_problem(self):
    self.assertEqual(self.sol.solveNQueens(4),
      [
       [".Q..",
        "...Q",
        "Q...",
        "..Q."],
       ["..Q.",
        "Q...",
        "...Q",
        ".Q.."]
      ])
