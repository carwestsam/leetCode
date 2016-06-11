import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = re.sub('(^[ ]*)|([ ]*$)', '', s)

        if not ( re.match('^-0+([.]0+)?$', s) is None) :
            return False

        result = re.match(r'^[-]?([0-9]|([1-9]\d+))([.]\d+)?$', s)

        return not (result is None)
