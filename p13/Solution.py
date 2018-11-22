class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        i = 0
        s = s + "##"

        while s[i] == 'M':
            ans += 1000
            i += 1

        if s[i] == 'D':
            ans += 500
            i += 1

        if s[i] == 'C':
            ans += 100
            i += 1

        if s[i] == 'L':
            ans += 50
            i += 1

        if s[i] == 'X':
            ans += 10
            i += 1

        if s[i] == 'V':
            ans += 5
            i += 1

        if s[i] == 'I':
            ans += 1
            i += 1

        return ans
