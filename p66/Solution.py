class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits - 1)
        plus = 1

        while i >= 0 and plus == 1:
            digits[i] += plus
            plus = digits[i] // 10
            digits[i] %= 10
            i -= 1

        if plus == 1:
            digits.insert(0, 1)
        return digits
