class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ld = len(digits)
        if ld == 0:
            return []
        if ld == 1 and digits[0] == '1':
            return []

        num2char = {
            '1': '',
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        lnc = {}

        for k in num2char:
            lnc[k] = num2char[k].__len__()

        ans = []

        stack = [0] * (ld + 1)
        stackStr = [""] * (ld + 1)
        top = 0

        while top >= 0:
            if top == ld:
                if stackStr[top - 1] != '':
                    ans.append(stackStr[top - 1])
                top -= 1
                stack[top] += 1
                continue

            if top == 0:
                if digits[top] == '1' and stack[top] == 0:
                    stackStr[0] = ''
                    top += 1
                    stack[top] = 0
                elif stack[top] >= lnc[digits[0]]:
                    top -= 1
                    stack[top] += 1
                else:
                    # print(top, digits[0], stack[top])
                    stackStr[0] = num2char[digits[0]][stack[top]]
                    top += 1
                    stack[top] = 0
                continue

            if digits[top] == '1' and stack[top] == 0:
                stackStr[top] = stackStr[top - 1]
                top += 1
                stack[top] = 0
            elif stack[top] >= lnc[digits[top]]:
                top -= 1
                stack[top] += 1
            else:
                stackStr[top] = stackStr[top-1] + num2char[digits[top]][stack[top]]
                top += 1
                stack[top] = 0

        return ans
