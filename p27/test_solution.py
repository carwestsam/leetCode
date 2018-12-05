from unittest import TestCase

from p27.Solution import Solution


class TestSolution(TestCase):
    def test_removeElement(self):
        sol = Solution()

        self.assertEqual(0, sol.removeElement([3], 3))
        self.assertEqual(0, sol.removeElement([], 3))
