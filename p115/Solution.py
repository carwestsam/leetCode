class Solution:
    def numDistinct(self, s: 'str', t: 'str') -> 'int':

        ls = len(s)
        lt = len(t)

        if s == t:
            return 1
        if s == 0 or ls < lt:
            return 0

        f = [[1] + [0] * lt, [1] + [0] * lt]
        side = 0
        for i in range(1, ls + 1):
            side = 1 - side
            for j in range(1, lt + 1):
                if s[i - 1] == t[j - 1]:
                    f[side][j] = f[1 - side][j] + f[1 - side][j - 1]
                else:
                    f[side][j] = f[1 - side][j]

        return f[side][lt]


import unittest


class Test(unittest.TestCase):
    def test_should_return_0_when_there_not_valid_answer(self):
        sol = Solution()
        self.assertEqual(0, sol.numDistinct('abcde', 'gde'))
        self.assertEqual(0, sol.numDistinct('gd', 'gde'))
        self.assertEqual(0, sol.numDistinct('', 'gde'))
        self.assertEqual(0, sol.numDistinct('', 'g'))

    def test_should_return_1_when_strings_are_same(self):
        sol = Solution()
        self.assertEqual(1, sol.numDistinct('a', 'a'))
        self.assertEqual(1, sol.numDistinct('abc', 'abc'))

    def test_should_match_and_return_distinct(self):
        sol = Solution()
        self.assertEqual(1, sol.numDistinct('abcd', 'abd'))
        self.assertEqual(3, sol.numDistinct('rabbbit', 'rabbit'))
        self.assertEqual(5, sol.numDistinct('babgbag', 'bag'))


if __name__ == '__main__':
    unittest.main()