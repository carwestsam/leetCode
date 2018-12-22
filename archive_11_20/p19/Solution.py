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
        ln = self.getLength(head)
        target = ln - n

        if target == 0:
            return head.next

        pt = head
        cnt = 1
        while pt != None:
            if cnt == target:
                pt.next = pt.next.next
                break
            cnt += 1
            pt = pt.next
        return head

    def getLength(self, head):
        if head is None:
            return 0

        pt = head
        length = 0
        while pt != None:
            length += 1
            pt = pt.next

        return length
