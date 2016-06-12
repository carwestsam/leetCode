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

        result = re.match("^[-]?([0-9]|("+ nonZeroDigit + "))([.]\d+)?([e][-]?" + nonZeroDigit + ")?$", s)

        return not (result is None)
