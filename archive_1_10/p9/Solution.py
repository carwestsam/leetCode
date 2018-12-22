class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x == 0:
            return True
        if x < 0:
            return False

        xx = x
        y = 0

        while xx != 0:
            y = y * 10 + xx % 10
            xx //= 10

        return y == x
