class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        pt = 1

        while pt <= n:
            if pt == n:
                return True
            pt *= 2

        return False
