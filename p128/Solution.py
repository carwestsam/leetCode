class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_set = {}
        v = [False] * len(nums)
        for i in range(len(nums)):
            num_set[nums[i]] = i

        result = 0
        for n in nums:
            if v[num_set[n]] is False:
                v[num_set[n]] = True
                c = 1
                pt = n
                while pt - 1 in num_set and v[num_set[pt - 1]] is False:
                    pt = pt - 1
                    c += 1
                    v[num_set[pt]] = True
                pt = n
                while pt + 1 in num_set and v[num_set[pt + 1]] is False:
                    pt = pt + 1
                    v[num_set[pt]] = True
                    c += 1

                if c > result:
                    result = c

        return result
