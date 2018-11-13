from unittest import TestCase

from p2.Solution import Solution, ListNode


class TestSolution(TestCase):
    def test_addTwoNumbers(self):
        sol = Solution()
        l1 = ListNode(0)
        l2 = ListNode(0)
        self.assertEqual(0, sol.addTwoNumbers(l1, l2).val)
