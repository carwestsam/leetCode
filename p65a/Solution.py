import re

class Solution(object):

    def isFloatWithoutEpattern(self):
        intNumber = "(([0-9])|([1-9][0-9]+))"
        dotNumber = "([.][0-9]+)"
        WS = ""

        return "[+-]?((" + dotNumber + WS + ")|(" + intNumber + '.' + WS + ")|(" + intNumber + dotNumber + "?" + WS + "))"


    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return False

        # if re.match(r'^[+-]?', s):
        #     s = re.sub(r'^[+-]?', '',s)

        return re.match("^" + self.isFloatWithoutEpattern() + '([e]' + self.isFloatWithoutEpattern() +  ")?$", s)
