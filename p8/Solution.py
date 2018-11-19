class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        i = 0
        ans = 0

        atoi_dict = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0
        }

        while i < len(str):
            ans = ans * 10 + atoi_dict[str[i]]
            i += 1

        return ans
