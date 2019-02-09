class Solution:
    def jump(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        if n <= 1:
            return 0

        cnt = 0
        i, j = 0, 1
        for cnt in range(1, n):
            i, j = j, max([k + nums[k] + 1 for k in range(i, j)])
            if j >= n:
                return cnt


import unittest


class Test(unittest.TestCase):
    def test_should_return_0_when_only_one_element(self):
        sol = Solution()
        self.assertEqual(0, sol.jump([1]))

    def test_should_handle_1_jump_case(self):
        sol = Solution()
        self.assertEqual(1, sol.jump([2, 1, 1]))

    def xtest_should_have_segment_tree(self):
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