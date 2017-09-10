class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        pass

    def parseComplex(self, complexString):
        cutted = complexString.split('+')
        a = int(cutted[0])
        b = int(cutted[1].split('i')[0])
        return (a, b)