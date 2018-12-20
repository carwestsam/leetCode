from unittest import TestCase

from p200.Solution import Solution


class TestSolution(TestCase):
    def test_numIslands(self):
        sol = Solution()
        self.assertEqual(3, sol.numIslands([
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "0", "1", "0", "0"],
            ["0", "0", "0", "0", "1"]
        ]))
        self.assertEqual(0, sol.numIslands([]))
