class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        # print(nums)

        left = 0
        right = len(nums) - 1

        if target <= nums[left]:
            return sum([nums[0], nums[1], nums[2]])
        elif target >= nums[right]:
            return sum([nums[-3], nums[-2], nums[-1]])

        def abs(v):
            if v < 0:
                return -v
            else:
                return v

        while left + 2 < right:
            dl = abs(nums[left] - target)
            dr = abs(nums[right] - target)

            if dl >= dr:
                left = left + 1
            elif dr > dl:
                right = right - 1

        return sum(nums[left: right + 1])
