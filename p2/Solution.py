# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        ans = None
        last = None

        while p1 is not None and p2 is not None:

            if p1 is not None:
                v1 = p1.val
                p1 = p1.next
            else:
                v1 = 0
            if p2 is not None:
                v2 = p2.val
                p2 = p2.next
            else:
                v2 = 0

            if ans is None:
                ans = ListNode(v1 + v2)
                last = ans
            else:
                node = ListNode(v1 + v2)
                last.next = node
                last = node

        return ans
