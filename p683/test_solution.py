from unittest import TestCase

from p683.Solution import Solution


class TestSolution(TestCase):
    def test_kEmptySlots(self):
        sol = Solution()
        self.assertEqual(2, sol.kEmptySlots([1,3,2],1))
        self.assertEqual(-1, sol.kEmptySlots([1,2,3],1))

