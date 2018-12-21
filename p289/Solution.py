class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return


        M = len(board)
        N = len(board[0])

        old_board = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                old_board[i][j] = board[i][j]

        def get(x, y):
            if 0 <= x < M and 0 <= y < N and old_board[x][y] == 1:
                return 1
            else:
                return 0

        for i in range(M):
            for j in range(N):
                neighbors = get(i - 1, j) + get(i + 1, j) + get(i, j - 1) + get(i, j + 1) \
                            + get(i -1, j-1) + get(i+1, j-1) + get(i-1, j+1) + get(i+1, j+1)

                if old_board[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                    board[i][j] = 0
                elif old_board[i][j] == 0 and neighbors == 3:
                    board[i][j] = 1
                else:
                    board[i][j] = old_board[i][j]
