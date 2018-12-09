from unittest import TestCase

from p31.Solution import Solution


class TestSolution(TestCase):
    def test_nextPermutation(self):
        sol = Solution()
        nums = [1]
        self.assertEqual([1], sol.nextPermutation(nums))
