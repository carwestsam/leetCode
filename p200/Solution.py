class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        M = len(grid)

        if M == 0:
            return 0

        N = len(grid[0])

        result = 0
        visited = [[False] * N for _ in range(M)]
        di = [[1, 0], [0, -1], [-1, 0], [0, 1]]

        def bfs(x, y, v):
            queue = []
            queue.append((x, y))
            v[x][y] = True
            ii = 0
            while ii < len(queue):
                for d in range(4):
                    next_x = queue[ii][0] + di[d][0]
                    next_y = queue[ii][1] + di[d][1]
                    if 0 <= next_x < M and 0 <= next_y < N \
                            and grid[next_x][next_y] == '1' and v[next_x][next_y] is False:
                        v[next_x][next_y] = True
                        queue.append((next_x, next_y))
                ii += 1

        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1' and visited[i][j] is False:
                    result += 1
                    bfs(i, j, visited)

        return result
