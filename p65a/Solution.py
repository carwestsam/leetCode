import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return False


        return re.match(r"^[-+]?(([0-9])|([1-9][0-9]+))([.][0-9]+)?$", s)