from unittest import TestCase

from p857.Solution import Solution


class TestSolution(TestCase):
    def test_mincostToHireWorkers(self):
        sol = Solution()
        # self.assertAlmostEqual(105.0, sol.mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2))
        # self.assertAlmostEqual(30.66667, sol.mincostToHireWorkers([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3),
        #                        delta=0.00001)

        self.assertAlmostEqual(3.0, sol.mincostToHireWorkers([5, 4, 1, 3], [4, 3, 14, 9], 1),
                               delta=0.00001)
