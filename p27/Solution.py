class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ans = 0
        for v in nums:
            if v != val:
                nums[ans] = v
                ans += 1
        return ans
