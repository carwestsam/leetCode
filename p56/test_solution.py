from unittest import TestCase

from p56.Solution import Solution


class Intervel:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class TestSolution(TestCase):
    def test_merge(self):
        sol = Solution()
        result = sol.merge([Intervel(1, 4), Intervel(4, 5)])[0]
        self.assertEqual(1, result.start)
        self.assertEqual(5, result.end)
