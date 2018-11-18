class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        ans = 0
        while x != 0:
            last = x % 10
            ans = ans * 10 + last
            x = x // 10

        return ans
