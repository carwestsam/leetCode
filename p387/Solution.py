class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cha = ord('a')
        cnt = [0] * 27
        first = [0] * 27
        for i in reversed(range(len(s))):
            ch = s[i]
            pos = ord(ch) - cha
            cnt[pos] += 1
            first[pos] = i

        result = len(s) + 1

        for i in range(26):
            if cnt[i] == 1 and first[i] < result:
                result = first[i]

        if result == len(s) + 1:
            return -1

        return result
