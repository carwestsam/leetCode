from unittest import TestCase

from p25.Solution import Solution


class TestSolution(TestCase):
    def test_reverseKGroup(self):
        sol = Solution()

        self.assertEqual(None, sol.reverseKGroup(None, 2))
