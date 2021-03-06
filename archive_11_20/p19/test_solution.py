from unittest import TestCase

from p19.Solution import Solution, ListNode


def nodesToList(head):
    l = []
    pt = head
    while pt != None:
        l.append(pt.val)
        pt = pt.next
    return l


def listToNodes(valList):
    head = ListNode(0)
    pt = head
    for v in valList:
        n = ListNode(v)
        pt.next = n
        pt = n

    return head.next


class TestSolution(TestCase):
    def test_removeNthFromEnd(self):
        sol = Solution()

        self.assertEqual([1], nodesToList(ListNode(1)))
        self.assertEqual(1, listToNodes([1]).val)
        self.assertEqual(2, listToNodes([1, 2]).next.val)

        self.assertEqual([], nodesToList(sol.removeNthFromEnd(listToNodes([1]), 1)))
        self.assertEqual([2], nodesToList(sol.removeNthFromEnd(listToNodes([1, 2]), 2)))
        self.assertEqual([1, 3], nodesToList(sol.removeNthFromEnd(listToNodes([1, 2, 3]), 2)))
        self.assertEqual([1, 2], nodesToList(sol.removeNthFromEnd(listToNodes([1, 2, 3]), 1)))
        self.assertEqual([2, 3], nodesToList(sol.removeNthFromEnd(listToNodes([1, 2, 3]), 3)))

    def test_shouldReturnListLength(self):
        sol = Solution()

        self.assertEqual(0, sol.getLength(listToNodes([])))
        self.assertEqual(4, sol.getLength(listToNodes([1, 2, 3, 4])))
        self.assertEqual(1, sol.getLength(listToNodes([2])))
