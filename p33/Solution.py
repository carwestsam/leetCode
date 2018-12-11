class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(nums, 0, len(nums), target)

    def binary_search(self, nums, left, right, target):
        if left >= right:
            return -1
        if nums[left] == target:
            return left
        if nums[left] < nums[right-1]:
            mid = (left + right) // 2
            vm = nums[mid]
            if vm == target:
                return mid
            elif vm > target:
                return self.binary_search(nums, left + 1, mid, target)
            else:
                return self.binary_search(nums, mid + 1, right, target)

        elif nums[left] > nums[right-1]:
            mid = (left + right) // 2
            vm = nums[mid]
            if vm == target:
                return mid
            elif vm > nums[left]:
                if nums[left] <= target <= vm:
                    return self.binary_search(nums, left + 1, mid, target)
                else:
                    return self.binary_search(nums, mid + 1, right, target)
            elif vm < nums[left]:
                if vm <= target <= nums[right - 1]:
                    return self.binary_search(nums, mid + 1, right, target)
                else:
                    return self.binary_search(nums, left + 1, mid, target)
        else:
            return -1
