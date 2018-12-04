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
