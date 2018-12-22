class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        i = 0
        ans = 0
        symbol = 1
        is_last_symbol = False
        is_last_whitespace = True
        is_number_read = False
        valid = True

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

        while i < len(str) and valid is True:
            if str[i] in symbols and is_last_symbol is True:
                valid = False
                break
            if is_number_read is True and str[i] not in atoi_dict:
                break
            if str[i] in symbols:
                is_last_symbol = True
            elif is_last_symbol is True and str[i] not in atoi_dict:
                is_last_symbol = False
                valid = False
            elif str[i] != " " and is_last_whitespace is True and is_number_read is False and str[i] not in symbols and str[i] not in atoi_dict:
                valid = False
                break
            elif str[i] in atoi_dict:
                if is_last_symbol is True:
                    is_last_symbol = False
                    symbol = symbols[str[i-1]]
                ans = ans * 10 + atoi_dict[str[i]]
                is_number_read = True

            if str[i] == " ":
                is_last_whitespace = True
            else:
                is_last_whitespace = False
            i += 1

        if valid is False:
            return 0

        INT_MAX = 2147483647
        INT_MIN = -2147483648

        ans = ans * symbol

        if ans > INT_MAX:
            ans = INT_MAX
        if ans < INT_MIN:
            ans = INT_MIN

        return ans
