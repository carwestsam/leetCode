class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        tokens = []
        len_s = len(s)
        i = 0
        ch0 = ord('0')
        ch9 = ord('9')

        while i < len_s:
            if s[i] == '+' or s[i] == '-' or s[i] == '(' or s[i] == ')':
                tokens.append(s[i])
                i += 1
            elif s[i] == ' ':
                i += 1
            elif ch0 <= ord(s[i]) <= ch9:
                v = 0
                while i < len_s and ch0 <= ord(s[i]) <= ch9:
                    v = v * 10 + ord(s[i]) - ch0
                    i += 1
                tokens.append(v)

        stack = [['+', 0]]
        pt = 0
        for token in tokens:
            [last_op, val] = stack[pt]
            if token == '(':
                stack.append(['+', 0])
                pt += 1
            elif token == ')':
                if stack[pt - 1][0] == '+':
                    stack[pt - 1][1] += val
                elif stack[pt - 1][0] == '-':
                    stack[pt - 1][1] -= val
                stack.pop()
                pt -= 1
            elif token == '+':
                stack[pt][0] = '+'
            elif token == '-':
                stack[pt][0] = '-'
            else:
                if last_op == '+':
                    stack[pt][1] = val + token
                elif last_op == '-':
                    stack[pt][1] = val - token

        return stack[0][1]
