from unittest import TestCase
import random

from p843.Solution import Solution


class Master:
    def __init__(self, size):
        self._wordlist = []
        for i in range(size):
            self._wordlist.append(self.random_one())
        self.picked = self._wordlist[random.randint(0, size-1)]
        self.hit = False
        self.guesses = 0

    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        self.guesses += 1
        if word == self.picked:
            self.hit = True
        result = 0
        for a, b in zip(word, self.picked):
            if a == b:
                result += 1

        return result

    def random_one(self):
        s = ""
        while True:
            for _ in range(6):
                s += chr(ord('a') + random.randint(0, 25))
            if s not in self._wordlist:
                break
        return s

    def wordlist(self):
        return list(self._wordlist)


class TestSolution(TestCase):
    def test_findSecretWord(self):
        master = Master(200)
        sol = Solution()
        sol.findSecretWord(master.wordlist(), master)
        self.assertGreater(11, master.guesses)
        self.assertEqual(True, master.hit)
