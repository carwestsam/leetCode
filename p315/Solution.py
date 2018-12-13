# Tree Node: (val, height, count, left, right)
# 0: val
# 1: power
# 2: count
# 3: left
# 4: right

from random import random


class Node:
    def __init__(self, val, power, weight, left, right):
        self.val = val
        self.power = power
        self.weight = weight
        self.left = left
        self.right = right


class Solution:
    VAL = 0
    POWER = 1
    WEIGHT = 2
    LEFT = 3
    RIGHT = 4

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) == 0:
            return nums
        elif len(nums) == 1:
            return [0]

        ans = [0] * len(nums)
        head = None

        for i in reversed(range(len(nums))):
            num = nums[i]
            ans[i] = self.count_smaller(num, head)
            head = self.insert(num, head)
            if Solution.valid(head) is not True:
                print("Crashed", i)

        return ans

    def raw(self, nums):
        stop = len(nums)
        ans = [0] * stop
        for i in range(stop):
            for j in range(i + 1, stop):
                if nums[j] < nums[i]:
                    ans[i] += 1
        return ans

    def insert(self, num, head):
        if head is None:
            return Node(num, random(), 1, None, None)

        # print('insert', head.val, num)
        if num < head.val:
            head.left = self.insert(num, head.left)
        else:
            head.right = self.insert(num, head.right)

        left = head.left
        right = head.right
        head.weight = Solution.weight(head)

        if left is not None and left.power < head.power:
            head = self.rotate_right(head)
        elif right is not None and right.power < head.power:
            head = self.rotate_left(head)
        return head

    @staticmethod
    def valid(head):
        if head is None:
            return True

        if Solution.weight(head) != head.weight:
            print('weight crash')
            return False

        if head.left is not None:
            if head.left.power < head.power:
                print('power crash')
                return False
            if head.left.val > head.val:
                print('val crash', head.left.val, head.val)
                return False

        if head.right is not None:
            if head.power < head.power:
                print('power crash')
                return False
            if head.right.val < head.val:
                print('val crash', head.val, head.right.val)
                return False

        return Solution.valid(head.left) and Solution.valid(head.right)

    @staticmethod
    def weight(head):
        if head is None:
            return 0
        w = 1
        if head.left is not None:
            w += head.left.weight
        if head.right is not None:
            w += head.right.weight
        return w

    @staticmethod
    def rotate_right(head):
        # print('rotate_right')
        left = head.left
        head.left = left.right
        left.right = head

        head.weight = Solution.weight(head)
        left.weight = Solution.weight(left)

        return left

    @staticmethod
    def rotate_left(head):
        # print('rotate_left')
        right = head.right
        head.right = right.left
        right.left = head

        head.weight = Solution.weight(head)
        right.weight = Solution.weight(right)

        return right

    @staticmethod
    def count_smaller(target_val, head):
        if head is None:
            return 0

        if head.val < target_val:
            return Solution.weight(head.left) + 1 + Solution.count_smaller(target_val, head.right)

        else:
            return Solution.count_smaller(target_val, head.left)
