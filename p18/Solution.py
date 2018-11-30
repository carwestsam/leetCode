class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ln = len(nums)
        valueDict = {}
        ans = []

        for i in range(ln):
            for j in range(i):
                s = nums[i] + nums[j]
                if valueDict.get(s) is None:
                    valueDict[s] = []

                if valueDict.get(target-s) is not None:
                    for pair in valueDict[target - s]:
                        if pair[1] < j:
                            current = [nums[pair[0]], nums[pair[1]], nums[i], nums[j]]
                            ans.append(current)

                valueDict[s].append([j, i])
        ans.sort()

        if len(ans) == 0:
            return []

        fans = [ans[0]]
        for a in ans:
            if a != fans[-1]:
                fans.append(a)

        return fans
