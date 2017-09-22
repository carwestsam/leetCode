class Solution(object):
    def __init__(self):
        self.solutions = 0
        self.transDict = {}

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        pass

    def recursiveNQueens(self, level, left, straight, right, n):
        if level == n:
            self.solutions += 1
            return

        for i in range(n):
            pos = 1<<i
            if left & pos == 0 and straight & pos == 0 and right & pos == 0:
                self.recursiveNQueens(level+1, (left | pos)<<1, straight | pos, (right | pos) >> 1, n )

    def raw_solveNQueens(self, n):
        self.solutions = 0
        self.recursiveNQueens(0, 0, 0, 0, n)
        return self.solutions

    def pre_trans(self, n):
        pos = 1

        for i in range(n):

            queenString = "." * (n - i - 1)  + 'Q' + "." * i

            self.transDict[pos] = queenString
            pos <<= 1

    def trans(self, pos):
        return self.transDict[pos]
