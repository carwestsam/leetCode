from unittest import TestCase

from p315.Solution import Solution


class TestSolution(TestCase):
    def test_countSmaller(self):
        sol = Solution()
        self.assertEqual([0], sol.countSmaller([1]))
        self.assertEqual([2, 1, 1, 0], sol.countSmaller([5, 2, 6, 1]))
        self.assertEqual([3, 0, 0, 0], sol.countSmaller([2, 1, 1, 1]))

        num_list = [26, 78, 27, 100, 33, 67, 90, 23, 66, 5, 38, 7, 35, 23, 52, 22, 83, 51, 98, 69, 81, 32, 78, 28, 94,
                    13, 2, 97, 3, 76, 99, 51, 9, 21, 84, 66, 65, 36, 100, 41]
        self.assertEqual(sol.raw(num_list), sol.countSmaller(num_list))
