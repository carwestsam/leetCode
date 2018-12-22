from unittest import TestCase

from p128.Solution import Solution


class TestSolution(TestCase):
    def test_longestConsecutive(self):
        sol = Solution()
        self.assertEqual(4, sol.longestConsecutive([123, 233, 4, 1, 2, 3]))
