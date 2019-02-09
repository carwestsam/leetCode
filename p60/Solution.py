class Solution:
    def getPermutation(self, n: 'int', k: 'int') -> 'str':
        # print('---')
        self.flag = [False for _ in range(n + 1)]
        self.A = [0] * 10000
        self.A[0] = 1
        for i in range(1, 10000):
            self.A[i] = self.A[i - 1] * i
        return self.__recurse_generator(n, n, k)

    def __recurse_generator(self, n, left, k):
        current = ''
        pt = 1
        while self.flag[pt] is True:
            pt += 1
        subsum = self.A[left - 1]

        if left == 1:
            return str(pt)

        if subsum > k:
            # print('case 1')
            self.flag[pt] = True
            current += str(pt) + self.__recurse_generator(n, left - 1, k)
        else:
            # print('case 2', left, k)
            while k > subsum:
                k -= subsum
                # print('cut', k, subsum)
                pt += 1
                while self.flag[pt] is True:
                    pt += 1
            self.flag[pt] = True
            current += str(pt) + self.__recurse_generator(n, left - 1, k)

        return current


import unittest


class TestSol(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual('1', sol.getPermutation(1, 1))
        self.assertEqual('12', sol.getPermutation(2, 1))
        self.assertEqual('21', sol.getPermutation(2, 2))
        self.assertEqual('213', sol.getPermutation(3, 3))
        self.assertEqual('2314', sol.getPermutation(4, 9))
        self.assertEqual('2314', sol.getPermutation(8, 8590))


if __name__ == '__main__':
    unittest.main()