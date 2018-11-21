class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        pairs = []
        for i in range(len(height)):
            pairs.append((height[i], i + 1))

        def getKey(elem):
            return elem[0] * 100000000 + elem[1]

        pairs.sort(key=getKey, reverse=True)

        min_idx = pairs[0][1]
        max_idx = pairs[0][1]
        maximum = 0
        for i in range(1, len(height)):
            value, idx = pairs[i]
            # left
            if min_idx < idx:
                v = (idx - min_idx) * value
                if v > maximum:
                    maximum = v
            else:
                min_idx = idx

            # right
            if max_idx > idx:
                v = (max_idx - idx) * value

                if v > maximum:
                    maximum = v
            else:
                max_idx = idx
        return maximum
