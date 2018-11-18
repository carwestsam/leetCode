class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        negative = False
        if x < 0:
            negative = True
            x = -x

        ans = 0
        while x != 0:
            last = x % 10
            ans = ans * 10 + last
            x = x // 10

        if negative is True:
            ans = - ans

        return ans
