from unittest import TestCase

from p24.Solution import Solution
from utils import nodes_to_list, list_to_nodes


class TestSolution(TestCase):
    def test_swapPairs(self):
        sol = Solution()

        self.assertEqual(None, sol.swapPairs(None))
        self.assertEqual([2], nodes_to_list(sol.swapPairs(list_to_nodes([2]))))
        self.assertEqual([2, 1], nodes_to_list(sol.swapPairs(list_to_nodes([1, 2]))))
        self.assertEqual([2, 1, 3], nodes_to_list(sol.swapPairs(list_to_nodes([1, 2, 3]))))
        self.assertEqual([2, 1, 4, 3], nodes_to_list(sol.swapPairs(list_to_nodes([1, 2, 3, 4]))))
        self.assertEqual([2, 1, 4, 3, 5], nodes_to_list(sol.swapPairs(list_to_nodes([1, 2, 3, 4, 5]))))
        self.assertEqual([2, 1, 4, 3, 6, 5], nodes_to_list(sol.swapPairs(list_to_nodes([1, 2, 3, 4, 5, 6]))))
