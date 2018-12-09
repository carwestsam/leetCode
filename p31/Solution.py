class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)

        if ln <= 1:
            return

        def swap (x, y):
            t = nums[x]
            nums[x] = nums[y]
            nums[y] = t

        i = ln - 2
        while i >= 0:
            if nums[i] >= nums[i+1]:
                i = i - 1
            else:
                break

        if i == -1:
            l = 0
            r = ln -1
            while l < r:
                swap(l, r)
                l += 1
                r -= 1
        elif i == ln - 2:
            swap(i, i+1)
            return
        else:
            r = ln - 1
            while r > i and nums[i] >= nums[r]:
                r -= 1

            if r > i + 1:
                swap(r, i)
            else:
                swap(i, i+1)
            l = i + 1
            r = ln - 1
            while l < r:
                swap(l, r)
                l +=1
                r -= 1
            # nums[i+1:ln].sort()

