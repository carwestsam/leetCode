class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        ans = True

        if len(s) != len(p):
            return False

        for i in range(len(s)):
            if p[i] == ".":
                continue
            elif p[i] != s[i]:
                return False

        return True
