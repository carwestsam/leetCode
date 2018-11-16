class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)

        idx1 = (l1 + l2 + 1) // 2
        idx2 = (l1 + l2 + 2) // 2

        if idx1 != idx2:
            return (self.findByIndex(nums1, nums2, idx1) + self.findByIndex(nums1, nums2, idx2)) / 2
        else:
            return self.findByIndex(nums1, nums2, idx1)

    def findByIndex(self, nums1, nums2, idx):
        l1 = len(nums1)
        l2 = len(nums2)

        if l1 == 0:
            return nums2[idx - 1]
        elif l2 == 0:
            return nums1[idx - 1]

        if nums1[0] > nums2[-1] or nums1[-1] < nums2[0]:
            if nums1[0] > nums2[-1]:
                if idx > l2:
                    return nums1[idx - l2 - 1]
                else:
                    return nums2[idx - 1]

            if nums2[0] > nums1[-1]:
                if idx > l1:
                    return nums2[idx - l1 - 1]
                else:
                    return nums1[idx - 1]

        else:
            result = self.findSpecificIndex(nums1, nums2, idx)
            if result is None:
                result = self.findSpecificIndex(nums2, nums1, idx)
            return result

    def findSpecificIndex(self, nums1, nums2, targetIdx):
        for i in range(len(nums1)):
            ii, left, right = self.findScope(nums2, nums1[i], 0, len(nums2))
            # print(i, nums1[i], ii, left, right)
            if left + i == targetIdx - 1:
                return nums1[i]
            if left + i > targetIdx - 1:
                break

    # return ( max index of less or equal (include), left part size, right part size )
    def findScope(self, nums, target, left, right):
        l = left
        r = right
        m = (l + r + 1) // 2
        while l + 1 < r:
            if nums[m] > target:
                r = m
            elif nums[m] <= target:
                l = m

            m = (l + r + 1) // 2

        return (l, l - left + 1, right - l - 1)
