class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = []
        n2 = n * 2

        def recuresiveGenerate(pt, left, right, seq):
            if pt == n2:
                ans.append(seq)
                return

            if right > 0:
                iseq = seq + '('
                recuresiveGenerate(pt + 1, left + 1, right - 1, iseq)
                if left > 0:
                    iseq = seq + ')'
                    recuresiveGenerate(pt + 1, left - 1, right, iseq)
            elif right == 0:
                iseq = seq + ')' * left
                ans.append(iseq)
                return

        if n == 0:
            return []
        elif n >= 1:
            recuresiveGenerate(0, 0, n, "")
            return ans
