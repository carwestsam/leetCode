class Tree:
    def __init__(self, size):
        self.tree = [size * 10] * size * 4
        self.size = size

    def insert(self, target, value):
        self.__insert(target, value, 0, self.size, 1)

    def min(self, target_left, target_right):
        return self.__min(target_left, target_right, 0, self.size, 1)

    def __insert(self, target, value, left, right, idx):
        # print(target,value, left, right, idx)
        if left > right or target > right or target < left:
            return
        if left == right and right == target:
            self.tree[idx] = value
            return
        else:
            self.__insert(target, value, left, (left + right) // 2, idx * 2)
            self.__insert(target, value, (left + right) // 2 + 1, right, idx * 2 + 1)
            if value < self.tree[idx]:
                self.tree[idx] = value

    def __min(self, target_left, target_right, left, right, idx):
        # print('__min', left, right, idx)
        if left > right or target_left > right or target_right < left:
            return self.size * 10
        if target_left <= left <= right <= target_right:
            return self.tree[idx]
        else:
            return min(self.__min(target_left, target_right, left, (left + right) // 2, idx * 2),
                       self.__min(target_left, target_right, (left + right) // 2 + 1, right, idx * 2 + 1))


class Solution:
    def jump(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        if n <= 1:
            return 0

        tree = Tree(n + 1)

        for i in range(n - 1, -1, -1):
            if i + nums[i] >= n - 1:
                tree.insert(i, 1)
            else:
                # print ('check', i, i+nums[i], tree.min(i+1, i + nums[i]))
                tree.insert(i, tree.min(i + 1, i + nums[i]) + 1)

        return tree.min(0, 0)


import unittest


class Test(unittest.TestCase):
    def test_should_return_0_when_only_one_element(self):
        sol = Solution()
        self.assertEqual(0, sol.jump([1]))

    def test_should_handle_1_jump_case(self):
        sol = Solution()
        self.assertEqual(1, sol.jump([2, 1, 1]))

    def test_should_have_segment_tree(self):
        sol = Solution()
        tree = Tree(10)
        tree.insert(9, 10)
        tree.insert(8, 10)
        self.assertEqual(10, tree.min(8, 9))

    def test_should_handle_multi_jump_case(self):
        sol = Solution()
        self.assertEqual(2, sol.jump([1, 1, 1]))
        self.assertEqual(2, sol.jump([2, 3, 1, 1, 4]))


if __name__ == '__main__':
    unittest.main()