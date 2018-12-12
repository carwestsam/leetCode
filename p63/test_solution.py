from unittest import TestCase

from p63.Solution import Solution


class TestSolution(TestCase):
    def test_uniquePathsWithObstacles(self):
        sol = Solution()
        self.assertEqual(0, sol.uniquePathsWithObstacles([
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]))
        self.assertEqual(6, sol.uniquePathsWithObstacles([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]))

        self.assertEqual(3, sol.uniquePathsWithObstacles([
            [0, 0, 0],
            [0, 0, 0]
        ]))

    def test_should_return_zero_when_no_grid(self):
        sol = Solution()
        self.assertEqual(0, sol.uniquePathsWithObstacles([]))

    def test_should_return_example_case(self):
        sol = Solution()
        self.assertEqual(2, sol.uniquePathsWithObstacles([
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]))

    def test_should_zero_if_start_point_is_obstacle(self):
        sol = Solution()
        self.assertEqual(0, sol.uniquePathsWithObstacles([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]))
