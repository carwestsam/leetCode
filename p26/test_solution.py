from unittest import TestCase

from p26.Solution import Solution


class TestSolution(TestCase):
    def test_removeDuplicates_origin_length_less_than_2(self):
        sol = Solution()

        self.assertEqual(1, sol.removeDuplicates([1]))
        self.assertEqual(0, sol.removeDuplicates([]))

    def test_remove_Duplicates(self):
        sol = Solution()

        self.assertEqual(2, sol.removeDuplicates([1, 1, 2]))

        l2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        result = sol.removeDuplicates(l2)

        self.assertEqual([0, 1, 2, 3, 4], l2[:result])
