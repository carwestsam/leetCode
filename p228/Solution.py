class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ln = len(nums)
        if ln == 0:
            return []

        i = 0
        j = 0

        ans = []

        while i < ln:
            j = i + 1
            while j < ln and nums[j] == nums[j - 1] + 1:
                j += 1

            if i == j - 1:
                ans.append(str(nums[i]))
            else:
                ans.append(str(nums[i]) + '->' + str(nums[j - 1]))

            i = j

        return ans