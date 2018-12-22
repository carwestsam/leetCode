class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        elif numRows == 2:
            return s[::2] + s[1::2]
        else:
            conv = [0] * (numRows * 2)
            circle = numRows * 2 - 2
            for i in range(numRows):
                conv[i] = i
            for i in range(numRows, circle):
                conv[i] = circle - i

            buckets = []
            for i in range(numRows+1):
                buckets.append([])

            for i in range(len(s)):
                buckets[conv[i % circle]].append(s[i])

            result = ""
            for i in range(numRows):
                result += "".join(buckets[i])

            return result
