class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans = 0

        ls = len(s)

        f = [0] * (ls + 2)

        for i in range(ls):
            if s[i] == '(':
                f[i] = 0
            else:
                if i > 0 and s[i - 1] == '(':
                    pre = 0
                    if i > 1:
                        pre = f[i - 2]
                    f[i] = pre + 2
                elif i > 0 and s[i - 1] == ')':
                    if f[i - 1] == 0:
                        pass
                    else:
                        if i - f[i - 1] > 0 and s[i - f[i - 1] - 1] == '(':
                            f[i] = f[i - 1] + 2
                            left = i - f[i - 1] - 1
                            while left > 0:
                                if f[left - 1] == 0:
                                    break
                                else:
                                    f[i] += f[left - 1]
                                    left = left - f[left - 1]

            if f[i] > ans:
                ans = f[i]

        return ans
