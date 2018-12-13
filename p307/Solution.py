class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._length = len(nums)
        self._tree = [0] * (self._length * 2 + 20)
        self._nums = nums
        self._init_tree(0, self._length - 1, 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        pass

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sum_tree(i, j, 0, self._length - 1, 1)

    def _init_tree(self, left, right, idx):
        if left == right:
            self._tree[idx] = self._nums[left]
            return self._tree[idx]
        elif left > right:
            return 0
        else:
            mid = (left + right) // 2
            left_arm = self._init_tree(left, mid, idx * 2)
            right_arm = self._init_tree(mid + 1, right, idx * 2 + 1)
            self._tree[idx] = left_arm + right_arm
            return left_arm + right_arm

    def _sum_tree(self, target_left, target_right, left, right, idx):
        if left > right or right < target_left or target_right < left:
            return 0

        if target_left <= left and right <= target_right:
            return self._tree[idx]

        mid = (left + right) // 2
        left_arm = self._sum_tree(target_left, target_right, left, mid, idx * 2)
        right_arm = self._sum_tree(target_left, target_right, mid + 1, right, idx * 2 + 1)
        return left_arm + right_arm
