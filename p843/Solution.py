class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def common(a, b):
            matches = 0
            for i in range(6):
                if a[i] == b[i]:
                    matches += 1
            return matches

        for t in range(10):
            hist = []

            for i in range(6):
                hist.append([0] * 26)

            for w in wordlist:
                for i in range(6):
                    hist[i][ord(w[i]) - 97] += 1

            maxscore = 0
            next_guess = wordlist[0]
            for w in wordlist:
                score = 0
                for i in range(6):
                    score += hist[i][ord(w[i]) - 97]
                if score > maxscore:
                    maxscore = score
                    next_guess = w

            result = master.guess(next_guess)
            if result == 6:
                return

            # remove not match
            next_wordlist = []
            for w in wordlist:
                if common(w, next_guess) == result:
                    next_wordlist.append(w)
            wordlist = next_wordlist

        return
