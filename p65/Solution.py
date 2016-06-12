import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = re.sub('(^[ ]*)|([ ]*$)', '', s)

        nonZeroDigit = '[1-9]\d*'

        if not ( re.match('^-0+([.]0+)?$', s) is None) :
            return False

        float = "([.]\d+)?([e][-]?" + nonZeroDigit + ")?$"

        if not ( re.match(float, s) is None ) and not (re.match('^[.]', s) is None) :
            return True

        result = re.match("^[-]?([0-9]|(" + nonZeroDigit + "))" + float, s)

        return not (result is None)
