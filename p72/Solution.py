class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        l1 = len(word1)
        l2 = len(word2)
        f = []

        for i in range(l1 + 1):
            f.append([0] * (l2 + 1))

        for i in range(1, l1 + 1):
            f[i][0] = i

        for j in range(1, l2 + 1):
            f[0][j] = j

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                minimum = min(f[i][j - 1], f[i - 1][j]) + 1

                if word1[i - 1] == word2[j - 1]:
                    minimum = min(minimum, f[i - 1][j - 1])
                else:
                    minimum = min(minimum, f[i - 1][j - 1] + 1)

                f[i][j] = minimum

        return f[l1][l2]
