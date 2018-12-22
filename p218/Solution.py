class RMQ:
    def __init__(self, l, r, value=0):
        self.left_idx = l
        self.right_idx = r
        self.value = value
        self.left = None
        self.right = None

    def paint(self, x, y, h):
        # print('paint', x, y, self.left_idx, self.right_idx)
        if self.right_idx < x or y < self.left_idx or self.right_idx < self.left_idx:
            return
        if self.value >= h:
            return

        if x <= self.left_idx <= self.right_idx <= y:
            if self.value != -1 and  self.value < h:
                self.value = h
                return

        if self.value != -1:
            mid = (self.left_idx + self.right_idx) // 2
            self.left = RMQ(self.left_idx, mid, self.value)
            self.right = RMQ(mid+1, self.right_idx, self.value)
            self.value = -1

        self.left.paint(x, y, h)
        self.right.paint(x, y, h)

    def travel(self, result):
        if self.left_idx > self.right_idx:
            return
        if self.value != -1:
            if self.value != result[-1][1]:
                result.append([self.left_idx, self.value])
            return
        self.left.travel(result)
        self.right.travel(result)


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        if len(buildings) == 0:
            return []

        points = set()

        for b in buildings:
            [x, y, _] = b
            points.add(x)
            points.add(y)

        rmq = RMQ(min(points), max(points) + 1)

        for b in buildings:
            [x, y, h] = b
            rmq.paint(x, y - 1, h)

        result = [[-1, 0]]

        rmq.travel(result)

        return result[1:]
