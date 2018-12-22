class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ln = len(nums)
        if ln == 0:
            return 0
        elif ln == 1:
            return 0
        elif ln >= 2:
            if nums[0] > nums[1]:
                return 0
            if nums[-1] > nums[-2]:
                return len(nums) - 1

            for i in range(1, len(nums) - 1):
                if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                    return i
