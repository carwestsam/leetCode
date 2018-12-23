class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ln = len(nums)
        i = 0

        def abs(x):
            if x < 0:
                return -x
            return x

        while i < ln:
            v = abs(nums[i]) - 1
            nums[v] = - abs(nums[v])
            i += 1

        ans = []

        for i in range(ln):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans

