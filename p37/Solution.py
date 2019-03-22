from typing import List


class Solution:
    def __init__(self):
        self.numbuff = {
            1: 1 << 1,
            2: 1 << 2,
            3: 1 << 3,
            4: 1 << 4,
            5: 1 << 5,
            6: 1 << 6,
            7: 1 << 7,
            8: 1 << 8,
            9: 1 << 9
        }
        self.gridNumber = [
            [1, 1, 1, 2, 2, 2, 3, 3, 3],
            [1, 1, 1, 2, 2, 2, 3, 3, 3],
            [1, 1, 1, 2, 2, 2, 3, 3, 3],
            [4, 4, 4, 5, 5, 5, 6, 6, 6],
            [4, 4, 4, 5, 5, 5, 6, 6, 6],
            [4, 4, 4, 5, 5, 5, 6, 6, 6],
            [7, 7, 7, 8, 8, 8, 9, 9, 9],
            [7, 7, 7, 8, 8, 8, 9, 9, 9],
            [7, 7, 7, 8, 8, 8, 9, 9, 9]
        ]
        self.denum = {}
        self.buff = ((1 << 10) - 2)
        for key in self.numbuff:
            self.denum[self.numbuff[key]] = key

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        avBoard = [[1 << 10 - 2] * 9 for _ in range(9)]

        self.initBoard(board, avBoard)
        while not self.isSolved(board):
            # print(avBoard)
            px, py, v = self.findUniqueOnBoard(board, avBoard)
            print(px, py, v)
            board[px][py] = v
            avBoard[px][py] = 0
            self.invalidate(px, py, v, board, avBoard)

    def isSolved(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return False
        return True

    def findUniqueOnBoard(self, board, avBoard):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.' and (avBoard[i][j] & (avBoard[i][j] - 1)) == 0:
                    return i, j, self.denum[avBoard[i][j]]
        raise Exception("could not find unique")

    def invalidate(self, px, py, v, board, avBoard):
        debuff = self.buff ^ self.numbuff[int(v)]
        # print('debuff', px, py, v, debuff)
        for i in range(9):
            if board[i][py] == '.':
                avBoard[i][py] &= debuff
            if board[px][i] == '.':
                avBoard[px][i] &= debuff
            if board[px][py] == '.':
                self.invalidateGrid(self.gridNumber[px][py], debuff, board, avBoard)

    def invalidateGrid(self, grid, debuff, board, avBoard):
        for i in range(9):
            for j in range(9):
                if self.gridNumber[i][j] == grid and board[i][j] == '.':
                    avBoard[i][j] &= debuff

    def initBoard(self, board, avBoard):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    avBoard[i][j] = (1 << 10) - 2
                else:
                    avBoard[i][j] = 0

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    self.invalidate(i, j, board[i][j], board, avBoard)
