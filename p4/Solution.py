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
        else :
            return self.findByIndex(nums1, nums2, idx1)


    def findByIndex(self, nums1, nums2, idx):
        l1 = len(nums1)
        l2 = len(nums2)

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
