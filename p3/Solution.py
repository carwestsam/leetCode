class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        currentDict = {}
        currentStart = 0

        for i in range(len(s)):

            if s[i] in currentDict:
                newStart = currentDict[s[i]]+1
                for j in range(currentStart, newStart):
                    del currentDict[ s[j] ]
                currentStart = newStart

            currentDict[s[i]] = i

            result = i - currentStart + 1

            # result = self.lengthOfLongestSubstringIndex(s, i)
            if result > ans:
                ans = result

        return ans

    def lengthOfLongestSubstringIndex(self, seq, idx):
        currentDict = {}
        ans = 0
        for i in range(idx, len(seq)):
            if seq[i] in currentDict:
                break
            else:
                currentDict[seq[i]] = i
                ans += 1

        return ans
