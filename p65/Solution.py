import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = re.sub('(^[ ]*)|([ ]*$)', '', s)

        nonZeroDigit = '\d+'

        if not ( re.match('^-0+([.]0+)?$', s) is None) :
            return False

        float = "([.]\d+)?([e][-]?" + nonZeroDigit + ")?$"

        if not ( re.match(float, s) is None ) and not (re.match('^[.]', s) is None) :
            return True

        result = re.match("^[-]?(" + nonZeroDigit + ")" + float, s)

        return not (result is None)
