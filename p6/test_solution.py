from unittest import TestCase

from p6.Solution import Solution


class TestSolution(TestCase):
    def test_convert(self):
        sol = Solution()

        self.assertEqual("a", sol.convert("a", 1))