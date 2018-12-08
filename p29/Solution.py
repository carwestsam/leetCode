class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        rev_dividend = False
        rev_divisor = False

        if divisor < 0:
            rev_divisor = True
            divisor = - divisor

        if dividend < 0:
            rev_dividend = True
            dividend = - dividend

        remains = dividend
        multi = divisor
        ans = 0
        multi_val = 1
        while multi <= dividend:
            multi <<= 1
            multi_val <<= 1

        multi >>= 1
        multi_val >>= 1

        while remains >= divisor:
            if remains >= multi:
                remains -= multi
                ans += multi_val

            multi_val >>= 1
            multi >>= 1

        if rev_dividend is True and rev_divisor is False and remains != 0:
            ans += 1

        if rev_divisor != rev_dividend:
            return - ans

        return ans
