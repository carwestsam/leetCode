from unittest import TestCase

from p5.Solution import Solution


class TestSolution(TestCase):
    def test_longestPalindrome(self):
        sol = Solution()
        sol.longestPalindrome("a")

    def test_should_find_by_conbine_reverse_string(self):
        sol = Solution()
        self.assertEqual("aba", sol.longestMatch("abaa", "aaba"))

    def test_should_calc_string_kmp_init_value(self):
        sol = Solution()
        init = [-1] * 20
        self.assertEqual([-1, -1, 0, 1, 2, 3, -1], sol.kmpInit("abababc", -1, init)[0:7])
        self.assertEqual([-1, -1, 0, 1, 2, 3, -1, 0, 1, 2, 3], sol.kmpInit("abababcabab", -1, init)[0:11])
        self.assertEqual([9, 9, 9, 10, 11, 12, 9], sol.kmpInit("aaaaaaaaaaabcabcd", 9, init)[10:17])
