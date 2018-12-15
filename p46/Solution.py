class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ln = len(nums)
        if ln == 0:
            return []
        ans = []
        self.assemble(nums, 0, ln, ans)
        return ans

    def assemble(self, nums, idx, ln, ans):
        if idx == ln:
            tmp = [0] * ln
            for i in range(ln):
                tmp[i] = nums[i]
            ans.append(tmp)
            return

        for i in range(idx, ln):
            t = nums[i]
            nums[i] = nums[idx]
            nums[idx] = t
            self.assemble(nums, idx + 1, ln, ans)
            t = nums[i]
            nums[i] = nums[idx]
            nums[idx] = t
