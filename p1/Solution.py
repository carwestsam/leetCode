class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        N = len(nums)

        for i in range(N - 1):
            l = i+1
            r = N-1
            m = (l + r)/2

            while l <= r:
                if nums[i] + nums[m] == target:
                    return [i, m]
                if nums[i] + nums[m] > target:
                    r = m - 1
                elif nums[i] + nums[m] < target:
                    l = m + 1
                m = (l+r)/2

        return None