class Solution:
    def numTrees(self, n: 'int') -> 'int':
        cache = {0: 1, 1: 1, 2: 2}
        return self.sub(n, cache)

    def sub(self, n, cache):
        if n in cache:
            return cache[n]
        else:
            total = 0
            for i in range(n):
                total += self.sub(n - i - 1, cache) * self.sub(i, cache)
                # print( i , total)
            cache[n] = total
            return total


import unittest


class T(unittest.TestCase):
    def test_all(self):
        sol = Solution()
        self.assertEqual(5, sol.numTrees(3))
        self.assertEqual(3, sol.numTrees(4))
        # self.assertEqual(3, sol.numTrees(3))


if __name__ == '__main__':
    unittest.main()
