class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n > 1:
            v = self.myPow(x, n >> 1)
            v *= v
            if n & 1 == 1:
                v *= x
            return v
        elif n == 1:
            return x
        elif n == 0:
            return 1.0
        elif n < 0:
            ans = 1.0
            ans /= self.myPow(x, -n)
            return ans

