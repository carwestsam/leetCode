# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.findFirstMatch(nums, target), self.findLastMatch(nums, target)]

    def findFirstMatch(self, nums, target):

        if len(nums) == 0:
            return -1

        left = 0
        right = len(nums)

        mid = (left + right + 1) // 2

        while left + 1 < right:
            if nums[mid] >= target:
                right = mid
            else:
                left = mid

            mid = (left + right) // 2

        if nums[left] == target:
            return left
        elif left + 1 < len(nums) and nums[left + 1] == target:
            return left + 1
        else:
            return -1

    def findLastMatch(self, nums, target):
        if len(nums) == 0:
            return -1

        left = 0
        right = len(nums)
        mid = (left + right + 1) // 2

        while left + 1 < right:
            if nums[mid] <= target:
                left = mid
            else:
                right = mid

            mid = (left + right + 1) // 2

        if nums[left] == target:
            return left
        else:
            return -1


def aq(actual, expect, message):
    if actual == expect:
        return

    print('expected: ', expect, '\nactual:', actual, '\n', message)
    # raise Exception('test failed')
    print('test fail')
    import sys
    sys.exit()


def should_match_all():
    sol = Solution()
    assert [0, 5] == sol.searchRange([2, 2, 2, 2, 2, 2], 2), 'should match all 1'
    assert [0, 4] == sol.searchRange([2, 2, 2, 2, 2], 2), 'should match all 2'


def should_find_first_pos():
    sol = Solution()
    aq(sol.findFirstMatch([1, 2, 3, 3, 3], 3), 2, 'should find first 1')
    aq(sol.findFirstMatch([1, 2, 3, 3, 3, 3, 2], 3), 2, 'should find first 2')
    aq(sol.findFirstMatch([1, 2, 3, 4, 5], 3), 2, 'should find first 3')
    aq(sol.findFirstMatch([1, 2, 2, 3, 4, 5], 3), 3, 'should find first 4')
    aq(sol.findFirstMatch([1, 1, 2, 3, 4, 5], 1), 0, 'should find first 5')
    aq(sol.findFirstMatch([1, 1, 2, 3, 4, 5], 1), 0, 'should find first 6')
    aq(sol.findFirstMatch([1, 1, 2, 3, 4, 5], 6), -1, 'should find first 6')
    aq(sol.findFirstMatch([1, 1, 2, 3, 4, 5], 0), -1, 'should find first 6')
    aq(sol.findFirstMatch([1, 1, 2, 3, 4, 5], 3.5), -1, 'should find first 6')


def should_find_last_pos():
    sol = Solution()
    aq(sol.findLastMatch([1, 2, 3, 3, 3], 3), 4, 'should find last 1')
    aq(sol.findLastMatch([1, 2, 3, 3, 3, 3, 7], 3), 5, 'should find last 2')
    aq(sol.findLastMatch([1, 2, 3, 4, 5], 3), 2, 'should find last 3')
    aq(sol.findLastMatch([1, 2, 2, 3, 4, 5], 3), 3, 'should find last 4')
    aq(sol.findLastMatch([1, 1, 2, 3, 4, 5], 1), 1, 'should find last 5')
    aq(sol.findLastMatch([1, 2, 3, 4, 5], 1), 0, 'should find last 6')
    aq(sol.findLastMatch([1, 2, 3, 4, 5], 3.3), -1, 'should find last 7')
    aq(sol.findLastMatch([1, 2, 2, 3, 3, 3, 3, 3, 4, 5], 3), 7, 'should find last 8')
    aq(sol.findLastMatch([1, 2, 3, 3, 3, 3, 3, 5], 3), 6, 'should find last 9')
    aq(sol.findLastMatch([1, 2, 2, 3, 3, 3, 3, 5], 3), 6, 'should find last 10')
    aq(sol.findLastMatch([1, 2, 3, 3, 3, 3, 4, 5], 3), 5, 'should find last 11')
    import json
    from utils import cpath
    with open(cpath(__file__, 'input1.txt'), 'r') as f:
        arr = json.loads(f.readline())
        aq(sol.findLastMatch(arr, 35), 2513, 'should find last 12')


def should_passall():
    sol = Solution()
    aq(sol.searchRange([1, 2, 3, 3, 3], 3), [2, 4], 'should pass 1')
    aq(sol.searchRange([1, 2, 3, 4, 5], 3), [2, 2], 'should pass 2')
    aq(sol.searchRange([3, 3, 3, 4, 5], 3), [0, 2], 'should pass 3')
    aq(sol.searchRange([1, 2, 3, 3, 5], 3), [2, 3], 'should pass 4')
    aq(sol.searchRange([], 3), [-1, -1], 'should pass 5')


if __name__ == "__main__":
    sol = Solution()
    should_match_all()
    # should_find_first_pos()
    should_find_last_pos()
    # should_passall()
    print('passed')
