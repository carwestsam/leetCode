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

        def value(node):
            return node.val

        self.heapInit(lists, value)
        head = None
        pt = None
        while len(lists) > 0:
            current = self.heapPop(lists, value)

            if pt is not None:
                pt.next = current
            else:
                head = current
                pt = current

            if current.next is not None:
                self.heapInsert(lists, current.next, value)

        return head

    def heapSwap(self, left, right, heap):
        result = heap[left]
        heap[left] = heap[right]
        heap[right] = result

    def heapInit(self, heap, get_value = lambda x: x):
        lo = len(heap)
        for i in range(lo - 1, -1, -1):
            self.heapDown(i, heap, get_value)
        return heap

    def heapDown(self, x, heap, get_value):
        target = (x + 1) * 2 - 1

        lh = len(heap)

        if target >= lh:
            return

        if target + 1 < lh and get_value(heap[target + 1]) < get_value(heap[target]):
            target += 1

        if get_value(heap[target]) < get_value(heap[x]):
            self.heapSwap(x, target, heap)
            self.heapDown(target, heap, get_value)

    def heapPop(self, heap, get_value = lambda x: x):
        lo = len(heap)

        if lo == 0:
            return None

        result = heap[0]

        if lo == 1:
            heap.pop()
            return result

        v = heap.pop()
        heap[0] = v
        self.heapDown(0, heap, get_value)
        return result

    def heapInsert(self, heap, value, get_value = lambda x: x):
        heap.append(value)
        self.heapDown(self.heapUp(len(heap) - 1, heap, get_value), heap, get_value)

    def heapUp(self, pos, heap, get_value):
        if pos == 0:
            return 0

        while pos != 0:
            upper = (pos + 1) // 2 - 1
            if get_value(heap[upper]) > get_value(heap[pos]):
                self.heapSwap(upper, pos, heap)
                pos = upper
            else:
                break
        return pos
