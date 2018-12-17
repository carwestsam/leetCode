from unittest import TestCase

from p399.Solution import Solution


class TestSolution(TestCase):
    def test_calcEquation(self):
        sol = Solution()

        self.assertEqual([6.0, 0.5, -1.0, 1.0, -1.0], sol.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                                                                       [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"],
                                                                        ["x", "x"]]))
