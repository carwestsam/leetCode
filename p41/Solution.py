class Solution:
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        N = len(nums)
        for i in range(N):
            # print(nums)
            if i != nums[i] - 1:
                self.fix(nums, i, N)

        for i in range(N):
            if i != nums[i] - 1:
                return i + 1

        return N + 1

    def fix(self, nums, pos, N):
        if pos != nums[pos] - 1 and 0 <= nums[pos] - 1 < N:
            pointer = nums[pos] - 1
            if nums[pointer] == nums[pos]:
                return
            tmp = nums[pointer]
            nums[pointer] = nums[pos]
            nums[pos] = tmp
            self.fix(nums, pos, N)


import unittest

class Test(unittest.TestCase):
    def test_should_handle_empty(self):
        sol = Solution()
        self.assertEqual(1, sol.firstMissingPositive([]))
        self.assertEqual(2, sol.firstMissingPositive([1]))
        self.assertEqual(4, sol.firstMissingPositive([1, 2, 3]))
        self.assertEqual(2, sol.firstMissingPositive([3, 0, 1]))
        self.assertEqual(2, sol.firstMissingPositive([3, 4, -1, 1]))
        self.assertEqual(1, sol.firstMissingPositive([7, 8, 9, 11, 12]))
        self.assertEqual(3, sol.firstMissingPositive([0, 2, 1]))
        self.assertEqual(2, sol.firstMissingPositive([1, 1]))


if __name__ == '__main__':
    unittest.main()
