class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        bucket_secret = [0] * 11
        bucket_guess = [0] * 11

        A = 0
        B = 0

        for s, g in zip(secret, guess):
            if s == g:
                A += 1
            else:
                bucket_secret[ord(s) - ord('0')] += 1
                bucket_guess[ord(g) - ord('0')] += 1

        for i in range(10):
            B += min(bucket_secret[i], bucket_guess[i])

        return str(A) + 'A' + str(B) + 'B'

