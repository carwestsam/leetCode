class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        i = 0
        j = len(s) - 1

        def vowel(ch):
            ch = ch.lower()
            if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
                return True
            return False

        while i < j:
            while i < j and not vowel(s[i]):
                i += 1
            while i < j and not vowel(s[j]):
                j -= 1

            if i < j:
                s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

            i += 1
            j -= 1

        return s
