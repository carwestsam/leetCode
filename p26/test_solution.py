from unittest import TestCase

from p26.Solution import Solution


class TestSolution(TestCase):
    def test_removeDuplicates(self):
        sol = Solution()

        self.assertEqual(1, sol.removeDuplicates([1]))
