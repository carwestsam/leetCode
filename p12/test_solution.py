from unittest import TestCase

from p12.Solution import Solution


class TestSolution(TestCase):
    def test_intToRoman(self):
        sol = Solution()

        self.assertEqual("I", sol.intToRoman(1))
