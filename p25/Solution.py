# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        if k == 1:
            return head

        begin = head
        end = head
        pt = None

        def reversable(h, k):
            p = h
            for _ in range(k - 1):
                p = p.next
                if p is None:
                    return False
            return p is not None

        if not reversable(head, k):
            return head

        for i in range(k):
            tmp = end
            end = end.next

            if i != k - 1 and end is None:
                return head

            if pt is None:
                pt = tmp
            else:
                tmp.next = pt
                pt = tmp

        head = pt
        begin.next = end

        while end is not None:
            prehead = begin
            begin = end
            pt = None
            if not reversable(begin, k):
                return head
            for i in range(k):
                tmp = end
                end = end.next

                if i != k - 1 and end is None:
                    return head

                if pt is None:
                    pt = tmp
                else:
                    tmp.next = pt
                    pt = tmp

            prehead.next = pt
            begin.next = end

        return head
