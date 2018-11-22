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

    def test_suffix_chain(self):
        sol = Solution()

        self.assertEqual(3, sol.romanToInt("III"))
        self.assertEqual(8, sol.romanToInt("VIII"))
        self.assertEqual(22, sol.romanToInt("XXII"))
        self.assertEqual(202, sol.romanToInt("CCII"))
        self.assertEqual(3002, sol.romanToInt("MMMII"))
        self.assertEqual(3383, sol.romanToInt("MMMCCCLXXXIII"))
