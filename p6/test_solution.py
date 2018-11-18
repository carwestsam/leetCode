from unittest import TestCase

from p6.Solution import Solution


class TestSolution(TestCase):
    def test_convert(self):
        sol = Solution()

        self.assertEqual("a", sol.convert("a", 1))
        self.assertEqual("", sol.convert("", 1))

    def test_should_given_origin_when_numRow_equals_one(self):
        sol = Solution()

        self.assertEqual("abcdefg", sol.convert("abcdefg", 1))

    def test_should_given_origin_when_numRow_equals_two(self):
        sol = Solution()

        self.assertEqual("acegbdf", sol.convert("abcdefg", 2))
        self.assertEqual("a", sol.convert("a", 2))
        self.assertEqual("acbd", sol.convert("abcd", 2))
