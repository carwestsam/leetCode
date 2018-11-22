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
