class Node:
    def __init__(self):
        self.links = []
        self.v = False

    def link(self, target):
        self.links.append(target)
        target.links.append(self)


class Solution:
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """

        if len(grid) == 0:
            return 0

        M = len(grid)
        N = len(grid[0])

        ### ' / '
        ### left : 0
        ### right : 1
        ### ' \\ '
        ### left : 0
        ### right: 1

        map = [[None] * N for _ in range(M)]

        for i in range(N):
            for j in range(M):
                map[i][j] = [Node(), Node(), Node(), Node()]
                if grid[i][j] == '/':
                    map[i][j][0].link(map[i][j][3])
                    map[i][j][1].link(map[i][j][2])
                elif grid[i][j] == '\\':
                    map[i][j][0].link(map[i][j][1])
                    map[i][j][2].link(map[i][j][3])
                elif grid[i][j] == ' ':
                    map[i][j][0].link(map[i][j][3])
                    map[i][j][1].link(map[i][j][2])
                    map[i][j][0].link(map[i][j][1])
                    map[i][j][2].link(map[i][j][3])

        for i in range(N):
            for j in range(M):
                if i > 0:  # up
                    map[i - 1][j][2].link(map[i][j][0])
                if j > 0:
                    map[i][j - 1][1].link(map[i][j][3])

        def travel(root):
            if root.v is True:
                return
            root.v = True
            for t in root.links:
                travel(t)

        ans = 0
        for i in range(N):
            for j in range(M):
                for k in range(4):
                    if map[i][j][k].v is False:
                        travel(map[i][j][k])
                        ans += 1

        return ans
