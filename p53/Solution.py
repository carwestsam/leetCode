class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        if len(nums) == 0:
            return 0

        sum = 0
        max_sum = nums[0]
        min_sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            ans = sum - min_sum
            if ans > max_sum:
                max_sum = ans
            if sum < min_sum:
                min_sum = sum
            # print(i, sum, min_sum, max_sum, sum)

        return max_sum


import unittest


class Test(unittest.TestCase):
    def test_should_handle_empty_case(self):
        sol = Solution()
        self.assertEqual(0, sol.maxSubArray([]))

    def test_should_calculate_max_substr_sum(self):
        sol = Solution()
        self.assertEqual(7, sol.maxSubArray([1, 1, 2, 3]))
        self.assertEqual(5, sol.maxSubArray([0, 0, 2, 3]))
        self.assertEqual(6, sol.maxSubArray([0, 1, 2, 3, -1]))
        self.assertEqual(6, sol.maxSubArray([-1, 1, 2, 3, -1]))
        self.assertEqual(-1, sol.maxSubArray([-1]))
        self.assertEqual(-1, sol.maxSubArray([-3, -2, -1]))

    def test_should_pass_examples(self):
        sol = Solution()
        self.assertEqual(6, sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


if __name__ == '__main__':
    unittest.main()
    print('yes')