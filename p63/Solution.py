class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if len(obstacleGrid) == 0:
            return 0

        if obstacleGrid[0][0] == 1:
            return 0

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        f = []

        for i in range(row):
            f.append([0] * col)

        f[0][0] = 1

        for i in range(1, row):
            if obstacleGrid[i][0] == 0:
                f[i][0] = 1
            else:
                break

        for j in range(1, col):
            if obstacleGrid[0][j] == 0:
                f[0][j] = 1
            else:
                break

        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 0:
                    f[i][j] = f[i - 1][j] + f[i][j - 1]

        return f[row - 1][col - 1]
