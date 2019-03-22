import heapq


class Heap:
    def headsort(self, array):
        heapq.heapify(array)

        ln = len(array)
        return [heapq.heappop(array) for _ in range(ln)]
