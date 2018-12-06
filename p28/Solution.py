class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ln = len(needle)
        lh = len(haystack)

        if ln == 0:
            return 0

        prefix = [-1] * ln

        i = 1
        j = -1

        while i < ln:
            while j != -1  and needle[i] != needle[j + 1]:
                j = prefix[j]

            if j < ln - 1 and needle[i] == needle[j + 1]:
                prefix[i] = j + 1
                j += 1
            else:
                prefix[i] = -1

            i += 1

        # print(prefix)


        pn = -1

        for ph in range(lh):
            ch = haystack[ph]
            # print(pn + 1)
            while pn != -1 and pn < ln - 1 and ch != needle[pn + 1]:
                pn = prefix[pn]

            if ch == needle[pn + 1]:
                pn = pn + 1

            if pn + 1 == ln:
                return ph - pn

        return -1
