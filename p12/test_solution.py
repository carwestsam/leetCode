from unittest import TestCase

from p12.Solution import Solution


class TestSolution(TestCase):
    def test_intToRoman(self):
        sol = Solution()

        self.assertEqual("I", sol.intToRoman(1))

    def test_should_handle_one_char_digit(self):
        sol = Solution()

        self.assertEqual("I", sol.intToRoman(1))
        self.assertEqual("V", sol.intToRoman(5))
        self.assertEqual("X", sol.intToRoman(10))
        self.assertEqual("L", sol.intToRoman(50))
        self.assertEqual("C", sol.intToRoman(100))
        self.assertEqual("D", sol.intToRoman(500))
        self.assertEqual("M", sol.intToRoman(1000))

    def test_should_handle_chain(self):
        sol = Solution()

        self.assertEqual("III", sol.intToRoman(3))
        self.assertEqual("VIII", sol.intToRoman(8))
        self.assertEqual("XIII", sol.intToRoman(13))
        self.assertEqual("XVIII", sol.intToRoman(18))
        self.assertEqual("MDCLXVI", sol.intToRoman(1666))
        self.assertEqual("MXVIII", sol.intToRoman(1018))

    def test_should_handle_prefix_chain(self):
        sol = Solution()

        self.assertEqual("IV", sol.intToRoman(4))
        self.assertEqual("IX", sol.intToRoman(9))
        self.assertEqual("XLI", sol.intToRoman(41))
        self.assertEqual("XCII", sol.intToRoman(92))
        self.assertEqual("CDIII", sol.intToRoman(403))
        self.assertEqual("CMII", sol.intToRoman(902))

        self.assertEqual("MCMXCIV", sol.intToRoman(1994))
