class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        longestIdx = len(strs[0])
        longest = -1
        idx = 0

        for i in range(len(strs)):
            ls = len(strs[i])
            if ls < longestIdx:
                longestIdx = ls

        while idx < longestIdx:
            success = True
            current = strs[0][idx]
            for i in range(1, len(strs)):
                if strs[i][idx] != current:
                    success = False
                    break
            if success is False:
                break
            else:
                longest = idx
                idx += 1

        return strs[0][:longest + 1]
