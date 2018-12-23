class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A) == 0:
            return []

        N = len(A[0])

        for m in range(len(A)):
            i = 0
            j = N - 1
            while i < j:
                if A[m][i] == A[m][j]:
                    A[m][i] = 1 - A[m][i]
                    A[m][j] = 1 - A[m][j]

                i += 1
                j -= 1

            if i == j:
                A[m][i] = 1 - A[m][j]

        return A
