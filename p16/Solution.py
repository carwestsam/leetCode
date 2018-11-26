class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        print(nums)

        left = 0
        right = len(nums) - 1

        if target <= nums[left]:
            return [nums[0], nums[1], nums[2]]
        elif target >= nums[right]:
            return [nums[-3], nums[-2], nums[-1]]

        return [0, 0, 0]
