class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """

        actions = [(i, s, t) for i, s, t in zip(indexes, sources, targets)]
        actions.sort()

        len_s = len(S)
        T = ""
        i = 0
        j = 0

        for (idx, src, tar) in actions:
            if i < idx:
                T += S[i:idx]

            i = idx

            if S[i:min(i + len(src), len_s)] == src:
                # matched, need replacement
                T += tar
                i += len(src)
            else:
                # not matched, continue
                continue

        if i < len_s:
            T += S[i:len_s]

        return T
