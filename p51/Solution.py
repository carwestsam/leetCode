class Solution(object):
    def __init__(self):
        self.solutions = 0
        self.transDict = {}
        self.path = [0 for i in range(20)]
        self.answer = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.pre_trans(n)
        self.raw_solveNQueens(n)
        return self.answer

    def recursiveNQueens(self, level, left, straight, right, n):
        if level == n:
            self.solutions += 1
            oneAns = []
            for i in range(n):
                oneAns.append(self.trans(self.path[i]))
            self.answer.append(oneAns)
            return

        for i in range(n):
            pos = 1<<i
            if left & pos == 0 and straight & pos == 0 and right & pos == 0:
                self.path[level] = pos
                self.recursiveNQueens(level+1, (left | pos)<<1, straight | pos, (right | pos) >> 1, n )

    def raw_solveNQueens(self, n):
        self.solutions = 0
        self.recursiveNQueens(0, 0, 0, 0, n)
        return self.solutions

    def pre_trans(self, n):
        pos = 1

        for i in range(n):
            queenString = "." * i + 'Q' + "." * (n - i - 1)

            self.transDict[pos] = queenString
            pos <<= 1

    def trans(self, pos):
        return self.transDict[pos]
