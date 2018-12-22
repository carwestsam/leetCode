class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        M = len(matrix)
        if M == 0:
            return False

        N = len(matrix[0])

        i = M - 1
        j = 0

        while j < N:

            while i >= 0 and matrix[i][j] > target:
                i -= 1

            if i >= 0 and matrix[i][j] == target:
                return True

            if i < M - 1:
                i += 1

            j += 1

        return False
