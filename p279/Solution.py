class Solution(object):
    def __init__(self):
        self.dict = {}
        self.best = 0

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # self.best = 10000000

        dict = set()
        path = [set() for _ in range(2)]
        side = 0
        last = 1
        i = 1
        ans = 1

        while i * i <= n:
            dict.add(i * i)
            path[side].add(i*i)
            i += 1

        while n not in path[side]:
            side = 1 - side
            last = 1 - last
            path[side] = set()
            ans += 1
            for x in path[last]:
                for y in dict:
                    # print('got', x+y)
                    if x + y < n:
                        path[side].add(x + y)
                    if x + y == n:
                        return ans

        return ans
