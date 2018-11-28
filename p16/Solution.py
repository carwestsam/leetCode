class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        # print(nums)

        def abs (x):
            if x > 0:
                return x
            else:
                return -x

        ln = len(nums)
        best = sum(nums[0:3])
        closest = abs(best - target)

        for i in range(ln-2):
            for j in range(i+1, ln-1):
                for k in range(j+1, ln):
                    s = nums[i] + nums[j] + nums[k]
                    if abs(s - target) < closest:
                        best = s
                        closest = abs(s - target)
                        # print(closest, best, nums[i], nums[j], nums[k])


        return best

