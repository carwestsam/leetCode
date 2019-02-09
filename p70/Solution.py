class Solution:
    def mpow(self, ma, mb):
        x = len(ma)
        y = len(ma[0])
        z = len(mb[0])
        n = [[0] * z for _ in range(x)]
        # print(x, y, z)
        for i in range(x):
            for j in range(z):
                for k in range(y):
                    # print('-', i, j, k)
                    n[i][j] += ma[i][k] * mb[k][j]
        return n

    def qpow(self, m, p):
        if p == 1:
            return m

        x = self.qpow(m, p // 2)
        x = self.mpow(x, x)
        # print ('-', x)
        if p % 2 == 0:
            return x
        else:
            return self.mpow(x, m)

    def climbStairs(self, n: 'int') -> 'int':
        m = [[1, 1], [1, 0]]

        fm = self.qpow(m, n)

        return fm[0][0]


import unittest


class T(unittest.TestCase):
    def test_should_calculate(self):
        sol = Solution()
        self.assertEqual(1, sol.climbStairs(1))
        self.assertEqual(2, sol.climbStairs(2))
        self.assertEqual(3, sol.climbStairs(3))
        self.assertEqual(5, sol.climbStairs(4))
        self.assertEqual(8, sol.climbStairs(5))
        self.assertEqual(13, sol.climbStairs(6))
        self.assertEqual(21, sol.climbStairs(7))


if __name__ == '__main__':
    unittest.main()
