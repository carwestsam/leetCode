from unittest import TestCase

from p27.Solution import Solution


class TestSolution(TestCase):
    def test_removeElement(self):
        sol = Solution()

        self.assertEqual(0, sol.removeElement([3], 3))
        self.assertEqual(0, sol.removeElement([], 3))
        self.assertEqual(1, sol.removeElement([1, 3], 3))
        self.assertEqual(2, sol.removeElement([3, 2, 2, 3], 3))
        self.assertEqual(5, sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
        l = [0, 1, 2, 2, 3, 0, 4, 2]
        ret = sol.removeElement(l, 2)
        self.assertEqual(5, ret)
        self.assertEqual([0, 1, 3, 0, 4], l[:ret])
