class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pass

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

