import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = re.sub('(^[ ]*)|([ ]*$)', '', s)

        if s == "-0":
            return False

        return re.match(r'^[-]?(0|([1-9]\d+))$', s)