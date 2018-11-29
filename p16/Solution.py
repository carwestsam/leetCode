class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        # print(nums)

        def abs(x):
            if x > 0:
                return x
            else:
                return -x

        ln = len(nums)
        best = abs(target - sum(nums[0:3]))
        ans = [0, 1, 2]

        for i in range(ln - 2):
            tempSum = nums[i] - target
            left = i + 1
            right = ln - 1

            while left < right:
                s = tempSum + nums[left] + nums[right]
                if best > abs(s):
                    best = abs(s)
                    ans = [i, left, right]
                if s == 0:
                    return target
                elif s > 0:
                    right = right - 1
                elif s < 0:
                    left = left + 1

        return nums[ans[0]] + nums[ans[1]] + nums[ans[2]]
