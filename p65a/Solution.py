import re

class Solution(object):

    def isFloatWithoutEpattern(self):


        return


    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return False

        intNumber = "(([0-9])|([1-9][0-9]+))"
        dotNumber = "([.][0-9]+)"
        sign = "[+-]?"
        floatwithoute = sign + "((" + dotNumber + ")|(" + intNumber + '.' + ")|(" + intNumber + dotNumber + "?" + "))"


        return re.match("^" + floatwithoute + '([e]' + sign + intNumber +  ")?$", s)
