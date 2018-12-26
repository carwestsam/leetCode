class Solution:
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """

        d = {}
        k = {}

        start = 0
        step = 0
        for i in range(8):
            start = start | (cells[i] << i)

        d[start] = step
        k[step] = start

        nn = 0
        while nn < N:
            nn += 1
            step += 1
            start = (~ ((start ^ (start << 2)) >> 1)) & (0x7e)
            if start in d:
                # print('hit', nn, d[start])
                T = nn - d[start]
                t_ = d[start] + ((N - d[start]) % T)
                # print('converted', t_)
                start = k[t_]
                break
            d[start] = step
            k[step] = start
            # print(nn)

        ans = [0] * 8
        for i in range(8):
            ans[i] = (start >> i) & 1

        return ans

    def raw(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """

        d = {}
        k = {}

        start = 0
        step = 0
        for i in range(8):
            start = start | (cells[i] << i)

        d[start] = step
        k[step] = start

        nn = 0
        while nn < N:
            step += 1
            start = (~ ((start ^ (start << 2)) >> 1)) & (0x7e)
            d[start] = step
            k[step] = start
            nn += 1
            # print(nn, start)

        ans = [0] * 8
        for i in range(8):
            ans[i] = (start >> i) & 1

        return ans
