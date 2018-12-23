class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        M = len(grid)
        if M == 0:
            return 0

        N = len(grid[0])

        def isLand(x, y):
            if 0 <= x < M and 0 <= y < N and grid[x][y] == 1:
                return True
            return False

        di = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    for d in di:
                        if not isLand(i + d[0], j + d[1]):
                            ans += 1

        return ans
