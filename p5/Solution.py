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
                    if i + k < lo and pattern[j + k] == origin[i + k]:
                        tmp += 1
                    else:
                        break
                if tmp > longest:
                    longest = tmp
                    longestIdx = i

        print(longestIdx, longest)
        return origin[longestIdx:longestIdx + longest]

    def kmpInit(self, pattern, left, init):
        lp = len(pattern)
        i = left
        init[left + 1] = left
        j = left + 2

        while j < lp:
            while i != left and pattern[j] != pattern[i + 1]:
                i = init[i]
            if pattern[j] == pattern[i + 1]:
                init[j] = i + 1
                i += 1
            else:
                init[j] = left

            j += 1

        return init
