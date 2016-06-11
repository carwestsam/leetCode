import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s == "-0":
            return False

        return re.match(r'^[-]?\d+$', s)