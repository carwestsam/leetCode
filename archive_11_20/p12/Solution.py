class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        ans = ""

        if num >= 1000:
            x = num // 1000
            ans += "M" * x
            num -= 1000 * x

        if num >= 900:
            ans += "CM"
            num -= 900

        if num >= 500:
            ans += "D"
            num -= 500

        if num >= 400:
            ans += "CD"
            num -= 400

        if num >= 100:
            x = num // 100
            ans += "C" * x
            num -= 100 * x

        if num >= 90:
            ans += "XC"
            num -= 90

        if num >= 50:
            ans += "L"
            num -= 50

        if num >= 40:
            ans += "XL"
            num -= 40

        if num >= 10:
            x = num // 10
            ans += "X" * x
            num -= 10 * x

        if num == 9:
            ans += "IX"

        elif num >= 5:
            ans += "V"
            ans += "I" * (num - 5)

        elif num == 4:
            ans += "IV"

        elif 0 <= num < 4:
            ans += "I" * num

        return ans
