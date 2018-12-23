class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        pt = 1
        while pt <= n:
            if pt == n:
                return True
            pt *= 3
        return False
