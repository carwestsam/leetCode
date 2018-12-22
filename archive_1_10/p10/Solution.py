class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if "*" not in p:
            if len(s) != len(p):
                return False

            for i in range(len(s)):
                if p[i] == ".":
                    continue
                elif p[i] != s[i]:
                    return False

            return True
        else:
            tokens = self.tokenize(p)
            return self.matchable(s, tokens)

    def matchable(self, origin, tokens):
        current = {0: True}
        nxt = {}
        lo = len(origin)

        for token in tokens:
            if token == ".":
                for pt in current:
                    if pt < lo:
                        nxt[pt + 1] = True

            elif len(token) == 2:
                for pt in current:
                    nxt[pt] = True
                    ipt = pt
                    ch = token[0]
                    while ipt < lo and (ch == '.' or origin[ipt] == ch):
                        nxt[ipt+1] = True
                        ipt += 1
            else:
                for pt in current:
                    if pt < lo and origin[pt] == token :
                        nxt[pt + 1] = True

            current = nxt
            nxt = {}

        return lo in current

    def tokenize(self, pattern):
        tokens = []
        i = 0
        lp = len(pattern)

        while i < lp:
            if i + 1 < lp and pattern[i + 1] == '*':
                tokens.append(pattern[i:i + 2])
                i += 1
            elif pattern[i] == '.':
                tokens.append('.')
            else:
                tokens.append(pattern[i])

            i += 1

        return tokens
