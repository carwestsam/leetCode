import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = re.sub('(^[ ]*)|([ ]*$)', '', s)

        digit = '\d+'
        sign = '[+-]?'

        if not ( re.match('^-0+([.]0+)?$', s) is None) :
            return False

        powerPart = "([e]" + sign + digit + ")?"
        float = "([.]\d+)?"

        if not ( re.match(sign + float + powerPart + '$', s) is None ) and not (re.match('^' + sign + '[.]', s) is None) :
            return True

        result = re.match("^" + sign + "(" + digit + ")((" + float + ")|[.])" + powerPart + '$', s)

        return not (result is None)
