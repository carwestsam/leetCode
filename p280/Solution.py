class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        nums.sort(reverse=True)

        i = 0

        ln = len(nums)
        while i < ln:
            j = i + 1
            if j < ln:
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
            i += 2
