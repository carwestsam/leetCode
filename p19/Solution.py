# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        return

    def getLength(self, head):
        if head is None:
            return 0

        pt = head
        length = 0
        while pt is not None:
            length += 1
            pt = pt.next

        return length
