class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        remains = dividend
        multi = divisor
        while multi <= dividend:
            multi <<= 1
        multi >>= 1

        while remains >= divisor:
            if remains >= multi:
                remains -= multi
            multi >>= 1

        return remains
