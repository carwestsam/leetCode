# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swap(self, lists, a, b):
        t = lists[a]
        lists[a] = lists[b]
        lists[b] = t

    def down(self, lists, idx):
        size = len(lists)
        l = (idx+1) * 2 - 1
        r = l + 1
        if l < size:
            t = l
            if r < size and lists[l].val > lists[r].val:
                t = r

            if lists[t].val < lists[idx].val:
                self.swap(lists, t, idx)
                self.down(lists, t)

    def mergeKLists(self, olists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        lists = []

        for node in olists:
            if node != None:
                lists.append(node)

        if len(lists) == 0:
            return None

        for x in range(len(lists)//2, -1, -1):
            self.down(lists, x)

        ans = []

        while len(lists) > 0:
            ans.append(lists[0])

            if lists[0].next == None:
                if len(lists) > 1:
                    lists[0] = lists[len(lists) - 1]
                    del lists[len(lists)-1]
                    self.down(lists, 0)
                else :
                    del lists[0]

            else :
                lists[0] = lists[0].next
                self.down(lists, 0)

        for x in range(len(ans) - 1):
            ans[x].next = ans[x+1]

        ans[len(ans) -1].next = None

        return ans[0]
