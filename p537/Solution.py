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

    def multiply(self, num1, num2):
        real = num1[0] * num2[0] - num1[1] * num2[1]
        imaginary = num1[0] * num2[1] + num1[1] * num2[0]
        return (real, imaginary)

    def convert(self, num):
        real, img = num
        return str(real) + "+" + str(img) + "i"
