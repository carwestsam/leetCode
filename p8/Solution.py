class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        i = 0
        ans = 0
        symbol = True
        is_last_symbol = False

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
        symbols = {
            "+": 1,
            "-": -1
        }

        while i < len(str):
            if str[i] in symbols:
                is_last_symbol = True
            elif str[i] in atoi_dict:
                if is_last_symbol is True:
                    is_last_symbol = False
                    symbol = symbols[str[i-1]]
                ans = ans * 10 + atoi_dict[str[i]]
            i += 1

        return ans * symbol
