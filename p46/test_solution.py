from unittest import TestCase

from p46.Solution import Solution


class TestSolution(TestCase):
    def test_permute(self):
        sol = Solution()
        self.assertEqual([], sol.permute([]))
