class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        ans = []
        # print('sorted', nums)

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                elif s > 0:
                    k -= 1

        if len(ans) < 2:
            return ans

        fans = [ans[0]]

        for i in range(1, len(ans)):
            if ans[i] != ans[i-1]:
                fans.append(ans[i])

        return fans
