# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2

        head = None
        pt = None
        next = None

        while not ( (p1 == None ) and ( p2 == None)):
            if p2 == None:
                next = p1
                p1 = p1.next
            elif p1 == None:
                next = p2
                p2 = p2.next
            else:
                if p1.val <= p2.val:
                    next = p1
                    p1 = p1.next
                else:
                    next = p2
                    p2 = p2.next

            if head == None:
                head = pt = next
            else:
                pt.next = next
                pt = next

        return head
