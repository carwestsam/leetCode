class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        top = -1
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
                top += 1
            elif ch == ')':
                if top == -1 or stack[top] != '(':
                    return False
                top -= 1
                stack.pop()
            elif ch == '}':
                if top == -1 or stack[top] != '{':
                    return False
                top -= 1
                stack.pop()
            elif ch == ']':
                if top == -1 or stack[top] != '[':
                    return False
                top -= 1
                stack.pop()

        if top != -1:
            return False

        return True
