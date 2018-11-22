class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 1000:
            return "M"
        elif num == 500:
            return "D"
        elif num == 100:
            return "C"
        elif num == 50:
            return "L"
        elif num == 10:
            return "X"
        elif num == 5:
            return "V"
        elif num == 1:
            return "I"

        return "I"
