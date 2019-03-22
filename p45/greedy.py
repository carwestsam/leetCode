from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        ln = len(nums)
        step = 0
        max_dist = nums[0]
        last_max_dist = 0
        pos = 1
        while pos < ln:
            last_max_dist = max_dist
            step += 1
            while pos <= last_max_dist and pos < ln:
                if nums[pos] + pos > max_dist:
                    max_dist = nums[pos] + pos
                pos += 1

            # print('last', pos, step)
            pos -= 1
            if pos == ln - 1:
                return step

        return step


sol = Solution()

# print('return', sol.jump([2, 3, 1, 1, 4]))
