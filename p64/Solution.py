class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if len(grid) == 0:
            return 0

        f = []
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            f.append([0] * col)

        f[0][0] = grid[0][0]

        for i in range(1, row):
            f[i][0] = f[i-1][0] + grid[i][0]

        for j in range(1, col):
            f[0][j] = f[0][j-1] + grid[0][j]

        for i in range(1, row):
            for j in range(1, col):
                f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]

        return f[row-1][col-1]
