from unittest import TestCase

from p345.Solution import Solution


class TestSolution(TestCase):
    def test_reverseVowels(self):
        sol = Solution()
        self.assertEqual('holle', sol.reverseVowels('hello'))
