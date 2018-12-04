# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None
        elif head.next is None:
            return head

        pt1 = head
        pt2 = head.next

        pt1.next = pt2.next
        pt2.next = pt1
        head = pt2

        if head.next is None:
            return head

        ptpre = pt1
        pt1 = ptpre.next

        # ptpre -> ( pt1 <-> pt2 ) -> pt2.next

        while pt1 is not None:
            pt2 = pt1.next
            if pt2 is None:
                break

            # swap
            pt1.next = pt2.next
            pt2.next = pt1
            ptpre.next = pt2

            # forward

            ptpre = pt1
            pt1 = ptpre.next

        return head
