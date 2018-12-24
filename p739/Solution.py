class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ln = len(T)
        ans = [0] * ln
        stack = []
        for i in range(ln - 1, -1, -1):
            while len(stack) > 0 and stack[-1][0] <= T[i]:
                stack.pop()

            if len(stack) > 0:
                ans[i] = stack[-1][1] - i
            else:
                ans[i] = 0

            stack.append([T[i], i])

        return ans
