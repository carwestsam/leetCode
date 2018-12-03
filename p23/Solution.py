# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]

    def heapSwap(self, left, right, heap):
        result = heap[left]
        heap[left] = heap[right]
        heap[right] = result

    def heapInit(self, heap):
        lo = len(heap)
        for i in range(lo - 1, -1, -1):
            self.heapDown(i, heap)
        return heap

    def heapDown(self, x, heap):
        target = (x + 1) * 2 - 1

        lh = len(heap)

        if target >= lh:
            return

        if target + 1 < lh and heap[target + 1] < heap[target]:
            target += 1

        if heap[target] < heap[x]:
            self.heapSwap(x, target, heap)
            self.heapDown(target, heap)

    def heapPop(self, heap):
        lo = len(heap)

        if lo == 0:
            return None

        result = heap[0]

        if lo == 1:
            heap.pop()
            return result

        v = heap.pop()
        heap[0] = v
        self.heapDown(0, heap)
        return result
