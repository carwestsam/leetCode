class Heap:
    def __init__(self, max_size):
        self.heap = [0] * (max_size + 2)
        self.size = 0
        self.current_quality = 0.0

    def add(self, q):
        self.size += 1
        self.heap[self.size] = q
        self.current_quality += q
        i = self.size
        while i > 1 and self.heap[i] > self.heap[i // 2]:
            t = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = t
            i = i // 2

    def pop(self):
        self.current_quality -= self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1

        if self.size == 0:
            return

        i = 1
        while i * 2 <= self.size:
            j = i * 2
            if j + 1 <= self.size and self.heap[j + 1] > self.heap[j]:
                j = j + 1

            if self.heap[j] > self.heap[i]:
                t = self.heap[i]
                self.heap[i] = self.heap[j]
                self.heap[j] = t

            i = j

    def first(self):
        if self.size == 0:
            return 0.0
        else:
            return self.heap[1]


class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """

        N = len(quality)

        ratio = [(w / q, q, w) for q, w in zip(quality, wage)]
        ratio.sort()
        # print(ratio)

        heap = Heap(N)
        result = ratio[-1][0] * K * 10000

        for r, q, w in ratio:
            if heap.size < K:
                heap.add(q)

            elif heap.first() > q and heap.size == K:
                heap.pop()
                heap.add(q)

            if heap.size == K:
                current_result = heap.current_quality * r
                if current_result < result:
                    result = current_result

        return result
