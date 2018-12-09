from unittest import TestCase

from p31.Solution import Solution


class TestSolution(TestCase):
    def test_nextPermutation(self):
        sol = Solution()
        nums = [1]
        sol.nextPermutation(nums)
        self.assertEqual([1], nums)

        nums = [3, 2, 1]
        sol.nextPermutation(nums)
        self.assertEqual([1, 2, 3], nums)

        nums = [1, 2, 3]
        sol.nextPermutation(nums)
        self.assertEqual([1, 3, 2], nums)

        nums = [1, 3, 2]
        sol.nextPermutation(nums)
        self.assertEqual([2, 1, 3], nums)

        nums = [1, 1, 3, 2]
        sol.nextPermutation(nums)
        self.assertEqual([1, 2, 1, 3], nums)
        sol.nextPermutation(nums)
        self.assertEqual([1, 2, 3, 1], nums)

        nums = [1, 1, 1, 3, 1, 1]
        sol.nextPermutation(nums)
        self.assertEqual([1, 1, 3, 1, 1, 1], nums)

    def test_others(self):
        sol = Solution()

        nums = [1, 1, 5]
        sol.nextPermutation(nums)
        self.assertEqual([1, 5, 1], nums)
        sol.nextPermutation(nums)
        self.assertEqual([5, 1, 1], nums)

        nums = [1, 4, 2, 3]
        sol.nextPermutation(nums)
        self.assertEqual([1, 4, 3, 2], nums)
        sol.nextPermutation(nums)
        self.assertEqual([2, 1, 3, 4], nums)
