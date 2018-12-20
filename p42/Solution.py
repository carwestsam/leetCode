class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) == 0:
            return 0

        left_max = [0] * len(height)
        right_max = [0] * len(height)

        left_max[0] = height[0]
        for i in range(1, len(height)):
            if height[i] < left_max[i - 1]:
                left_max[i] = left_max[i - 1]
            else:
                left_max[i] = height[i]

        right_max[-1] = height[-1]
        for i in reversed(range(0, len(height) - 1)):
            if height[i] < right_max[i + 1]:
                right_max[i] = right_max[i + 1]
            else:
                right_max[i] = height[i]

        result = 0
        for i in range(1, len(height) - 1):
            left = left_max[i - 1]
            right = right_max[i + 1]
            if left > height[i] and right > height[i]:
                result += min(left, right) - height[i]

        return result
