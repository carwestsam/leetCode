class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        return self.dp(s)

    def dp(self, s):
        A = s
        ls = len(s)

        f = []
        for i in range(ls + 1):
            arr = [-1] * (ls + 1)
            arr[i] = 1
            if i > 0:
                arr[i -1] = 0
            f.append(arr)

        mi = 1
        mj = 1
        longest = 1

        for k in range(2, ls + 1):
            for i in range(ls - k + 1):
                j = i + k - 1
                if s[i] == s[i + k - 1] and f[i+1][j-1] != -1:
                    f[i][j] = max(0, f[i+1][j-1]+2)
                    # print (k, i, j, s[i:j+1])
                    # print("%s from %s (%s, %s, %i, %i)" % (s[i:j+1], s[i+1:j], s[i], s[j], s[i]==s[j], f[i][j]))

                    if longest < f[i][j]:
                        longest = f[i][j]
                        mi = i
                        mj = j

        return s[mi:mj+1]

    def searching(self, s):
        left = 1
        right = len(s)
        mid = (left + right) // 2
        longest = 0
        longestIdx = -1

        while left < right:
            result = self.validate(s, mid)
            if result[0] is True:
                left = mid
                if mid > longest:
                    longest = mid
                    longestIdx = result[1]
            else:
                right = mid - 1

            mid = (left + right + 1) // 2

        # print(s, s[longestIdx:longest + longestIdx])
        return s[longestIdx:longest + longestIdx]
        # return self.longestMatch(s, s[::-1])

    def validate(self, s, l):
        for i in range(len(s) - l + 1):
            ii = i
            jj = i + l - 1
            success = True
            while ii < jj:
                if s[ii] != s[jj]:
                    success = False
                    break
                ii += 1
                jj -= 1
            if success is True:
                return True, i
        return False, -1


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
