from unittest import TestCase

from p681.Solution import Solution


class TestSolution(TestCase):
    def test_nextClosestTime(self):
        sol = Solution()
        self.assertEqual("19:39", sol.nextClosestTime("19:34"))
        self.assertEqual("22:22", sol.nextClosestTime("23:59"))
