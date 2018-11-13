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

    def numToList(self, number):
        last = None
        result = None
        while number != 0:
            node = ListNode(number % 10)
            if last is None:
                last = node
                result = last
            else:
                last.next = node
                last = node
            number = number // 10

        return result

    def test_add_without_push_forward(self):
        sol = Solution()
        l11 = self.numToList(32)
        l21 = self.numToList(43)

        self.assertEqual(5, sol.addTwoNumbers(l11, l21).val)
        self.assertEqual(7, sol.addTwoNumbers(l11, l21).next.val)

