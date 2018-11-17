class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        return self.longestMatch(s, s[::-1])

    def longestMatch(self, origin, pattern):
        longest = 0
        longestIdx = -1
        lo = len(origin)
        lp = len(pattern)
        init = [-1] * (lp+1)

        for j in range(lp - 1):
            self.kmpInit(pattern, j-1, init)

            k = j-1
            i = 0

            while i < lo:
                while k != j-1 and k+1 < lp and origin[i] != pattern[k+1]:
                    k = init[k]

                if k+1 < lp and origin[i] == pattern[k + 1]:
                    k += 1

                if k - j + 1 > longest and j + i + 1 == lp:
                    longest = k - j + 1

                    longestIdx = i - longest + 1


                if k+1 == lp:
                    k = init[k]

                i += 1

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
