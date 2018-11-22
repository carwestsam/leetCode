from unittest import TestCase

from p13.Solution import Solution


class TestSolution(TestCase):
    def test_romanToInt(self):
        sol = Solution()

        self.assertEqual(1, sol.romanToInt("I"))

    def test_single_char(self):
        sol = Solution()

        self.assertEqual(5, sol.romanToInt("V"))
        self.assertEqual(10, sol.romanToInt("X"))
        self.assertEqual(50, sol.romanToInt("L"))
        self.assertEqual(100, sol.romanToInt("C"))
        self.assertEqual(500, sol.romanToInt("D"))
        self.assertEqual(1000, sol.romanToInt("M"))
