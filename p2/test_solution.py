from unittest import TestCase

from p2.Solution import Solution, ListNode


class TestSolution(TestCase):
    def test_addTwoZeros(self):
        sol = Solution()
        l1 = ListNode(0)
        l2 = ListNode(0)
        self.assertEqual(0, sol.addTwoNumbers(l1, l2).val)

    def test_add_two_single_number(self):
        sol = Solution()
        l1 = ListNode(2)
        l2 = ListNode(4)
        self.assertEqual(6, sol.addTwoNumbers(l1, l2).val)

    def test_add_without_push_forwad(self):
        sol = Solution()
        l11 = ListNode(2)
        l12 = ListNode(3)
        l11.next = l12

        l21 = ListNode(3)
        l22 = ListNode(4)
        l21.next = l22

        self.assertEqual(5, sol.addTwoNumbers(l11, l21).val)
        self.assertEqual(7, sol.addTwoNumbers(l11, l21).next.val)
