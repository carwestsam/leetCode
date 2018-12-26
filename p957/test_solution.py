from unittest import TestCase

from p957.Solution import Solution


class TestSolution(TestCase):
    def test_prisonAfterNDays(self):
        sol = Solution()
        self.assertEqual([0, 0, 1, 1, 0, 0, 0, 0], sol.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7))
        self.assertEqual([0, 0, 1, 1, 1, 1, 1, 0], sol.prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 1000000000))
        self.assertEqual(sol.raw([1, 0, 0, 1, 0, 1, 1, 0], 300),
                         sol.prisonAfterNDays([1, 0, 0, 1, 0, 1, 1, 0], 300))
