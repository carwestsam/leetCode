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
        elif l1 == 1 and l2 == 1:
            return (nums1[0] + nums2[0]) / 2

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

        l = 0
        r = len(nums1)
        m = (l + r ) // 2
        while l < r:
            i1, left1, _ = self.findScope(nums2, nums1[m], 0, len(nums2))
            _, left2, _ = self.findScope(nums2, nums1[m], 0, len(nums2), False)

            result = left1 + m + 1
            if targetIdx == left1 + m + 1 or (left1 != left2 and targetIdx <= left1 + m + 1 and targetIdx >= left2 + m + 1 and nums2[i1] == nums1[m]):
                return nums1[m]
            elif result > targetIdx:
                r = m - 1
            elif result < targetIdx:
                l = m + 1

            m = (l + r ) // 2

        if l < len(nums1):
            m = l
            i1, left1, _ = self.findScope(nums2, nums1[m], 0, len(nums2))
            _, left2, _ = self.findScope(nums2, nums1[m], 0, len(nums2), False)

            if targetIdx == left1 + m + 1 or (left1 != left2 and targetIdx <= left1 + m + 1 and targetIdx >= left2 + m + 1 and nums2[i1] == nums1[m]):
                return nums1[m]

        return None

    # return ( max index of less or equal (include), left part size, right part size )
    def findScope(self, nums, target, left, right, eq = True):

        if left >= right or len(nums) == 0:
            return (0, 0, 0)

        if target < nums[left]:
            return (left, 0, right - left)
        elif target > nums[-1]:
            return (right - 1, right - left, 0)

        l = left
        r = right - 1
        m = (l + r) // 2
        while l < r:
            if eq == True:   # include target
                if nums[m] > target:
                    r = m - 1
                elif nums[m] <= target:
                    l = m
                m = (l + r + 1) // 2

            elif eq == False: # not include target
                if nums[m] >= target:
                    r = m
                elif nums[m] < target:
                    l = m+1
                m = (l+r)//2

        if eq == True:
            return (l, l - left + 1, right - l - 1)
        else:
            return (l, r - left, right - r)
