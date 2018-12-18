class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        size = len(flowers)
        tree = [0] * (size + 1)

        def lbs(x):
            return x & (-x)

        def sum(i):
            if i < 0:
                return -10
            if i > size:
                i = size
            s = 0
            while i > 0:
                s += tree[i]
                i -= lbs(i)
            return s

        def update(i):
            while i <= size:
                tree[i] += 1
                i += lbs(i)

        for day in range(size):
            pos = flowers[day]
            left_ahead = sum(pos - k - 2)
            left = sum(pos - k - 1)
            mid = sum(pos)
            right_ahead = sum(pos + k)
            right = sum(pos + k + 1)

            if left - left_ahead == 1 and mid - left == 0:
                return day + 1
            if right - right_ahead == 1 and right_ahead - mid == 0:
                return day + 1

            update(pos)
        return -1
