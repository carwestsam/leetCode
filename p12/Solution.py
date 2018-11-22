class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        ans = ""

        if num >= 1000:
            return "M" + self.intToRoman(num - 1000)
        elif num >= 500:
            return "D" + self.intToRoman(num - 500)
        elif num >= 100:
            return "C" + self.intToRoman(num - 100)
        elif num >= 50:
            return "L" + self.intToRoman(num - 50)
        elif num >= 10:
            return "X" + self.intToRoman(num - 10)
        elif num >= 5:
            return "V" + self.intToRoman(num - 5)
        elif 0 <= num < 4:
            return "I" * num

        return "I"
