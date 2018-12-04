from unittest import TestCase

from p25.Solution import Solution
from utils import nodes_to_list, list_to_nodes


class TestSolution(TestCase):
    def test_reverseKGroup_when_given_None(self):
        sol = Solution()

        self.assertEqual(None, sol.reverseKGroup(None, 2))

    def test_should_return_origin_string_when_k_equals_1(self):
        sol = Solution()

        self.assertEqual([1, 2, 3, 4, 5], nodes_to_list(sol.reverseKGroup(list_to_nodes([1, 2, 3, 4, 5]), 1)))
        self.assertEqual([1, 2, 3], nodes_to_list(sol.reverseKGroup(list_to_nodes([1, 2, 3]), 1)))

    def test_should_return_K_reversed_nodes(self):
        sol = Solution()

        self.assertEqual([1], nodes_to_list(sol.reverseKGroup(list_to_nodes([1]), 2)))
        self.assertEqual([2, 1], nodes_to_list(sol.reverseKGroup(list_to_nodes([1, 2]), 2)))
        self.assertEqual([2, 1, 4, 3, 5], nodes_to_list(sol.reverseKGroup(list_to_nodes([1, 2, 3, 4, 5]), 2)))
        self.assertEqual([2, 1, 4, 3, 6, 5], nodes_to_list(sol.reverseKGroup(list_to_nodes([1, 2, 3, 4, 5, 6]), 2)))
        self.assertEqual([3, 2, 1, 4, 5], nodes_to_list(sol.reverseKGroup(list_to_nodes([1, 2, 3, 4, 5]), 3)))
        self.assertEqual([3, 2, 1, 6, 5, 4, 7],
                         nodes_to_list(sol.reverseKGroup(list_to_nodes([1, 2, 3, 4, 5, 6, 7]), 3)))

    def test_should_fix_error_case(self):
        sol = Solution()

        self.assertEqual([1, 2, 3], nodes_to_list(sol.reverseKGroup(list_to_nodes([1, 2, 3]), 4)))
        self.assertEqual([4, 3, 2, 1, 5, 6, 7],
                         nodes_to_list(sol.reverseKGroup(list_to_nodes([1, 2, 3, 4, 5, 6, 7]), 4)))
        self.assertEqual([4, 3, 2, 1, 8, 7, 6, 5, 9, 10],
                         nodes_to_list(sol.reverseKGroup(list_to_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 4)))
