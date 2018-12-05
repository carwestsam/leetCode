from unittest import TestCase

from p26.Solution import Solution


class TestSolution(TestCase):
    def test_removeDuplicates_origin_length_less_than_2(self):
        sol = Solution()

        self.assertEqual(1, sol.removeDuplicates([1]))
        self.assertEqual(0, sol.removeDuplicates([]))
