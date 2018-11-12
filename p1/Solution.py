class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        N = len(nums)

        advanced_list = []

        for i in range(N):
            advanced_list.append([nums[i], i])

        advanced_list.sort(key=lambda x: x[0])

        for i in range(N - 1):
            l = i + 1
            r = N - 1
            m = (l + r) // 2

            while l <= r:
                if advanced_list[i][0] + advanced_list[m][0] == target:
                    ans = [advanced_list[i][1], advanced_list[m][1]]
                    ans.sort()
                    return ans
                if advanced_list[i][0] + advanced_list[m][0] > target:
                    r = m - 1
                elif advanced_list[i][0] + advanced_list[m][0] < target:
                    l = m + 1
                m = (l + r) // 2

        return None
