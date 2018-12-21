from unittest import TestCase

from p253.Solution import Solution


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class TestSolution(TestCase):
    def test_minMeetingRooms(self):
        sol = Solution()
        self.assertEqual(2, sol.minMeetingRooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))
