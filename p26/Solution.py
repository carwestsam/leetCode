class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = len(nums)

        if ln < 2:
            return ln

        ans = 1
        last = nums[0]
        for i in range(ln):
            if nums[i] != last:
                nums[ans] = nums[i]
                ans += 1
                last = nums[i]
        return ans
