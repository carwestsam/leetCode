class Solution:
    def sub_subset(self, ans, amount, nums, path):
        # print(amount, nums, path)

        if amount > len(nums):
            return

        if amount == 0:
            ans.append(path[:])
            return

        for i in range(len(nums)):
            tmp = path[:]
            tmp.append(nums[i])
            self.sub_subset(ans, amount-1, nums[i+1:], tmp)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        ans = [[]]

        for amount in range(1, len(nums)+1):
            self.sub_subset(ans, amount, nums, [])

        return ans
