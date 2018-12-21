class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []

        M = len(matrix)
        N = len(matrix[0])
        visited = [[False] * N for _ in range(M)]
        nav = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        i = 0
        j = 0
        d = 0
        result = [matrix[0][0]]
        visited[0][0] = True

        def next(x, y, z):
            return x + nav[z][0], y + nav[z][1]

        def valid(x, y):
            if 0 <= x < M and 0 <= y < N and visited[x][y] is False:
                return True
            return False

        while True:
            ni, nj = next(i, j, d)
            if not valid(ni, nj):
                d = (d + 1) % 4
                ni, nj = next(i, j, d)
                if not valid(ni, nj):
                    break

            i = ni
            j = nj
            visited[i][j] = True
            result.append(matrix[i][j])

        return result
