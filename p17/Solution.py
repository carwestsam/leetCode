class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        num2char = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        lnc = {}
        for k in num2char:
            lnc[k] = num2char[k].__len__()

        ans = []
        for j in range(lnc[digits[0]]):
            ans.append(num2char[digits[0]][j])
        return ans
