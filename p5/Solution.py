class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s

    def longestMatch(self, origin, pattern):
        longest = 0
        longestIdx = -1
        lo = len(origin)
        lp = len(pattern)
        for j in range(lp):
            for i in range(lo):
                tmp = 0
                for k in range(lp - j):
                    if i+k < lo and pattern[j+k] == origin[i+k]:
                        tmp += 1
                    else:
                        break
                if tmp > longest:
                    longest = tmp
                    longestIdx = i

        print(longestIdx, longest)
        return origin[longestIdx:longestIdx+longest]
