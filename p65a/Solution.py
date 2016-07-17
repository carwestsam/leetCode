import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return False

        if re.match(r'^[+-]?', s):
            s = re.sub(r'^[+-]?', '',s)

        intNumber = "(([0-9])|([1-9][0-9]+))"
        dotNumber = "([.][0-9]+)"
        WS = "$"

        if re.match(dotNumber + WS, s) or re.match(intNumber + '.' + WS, s) or re.match(r"" + intNumber + dotNumber + "?" + WS, s):
            return True
        return False
