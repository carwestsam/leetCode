
class Solution(object):
    def match(self, source, pattern, si):

        if len(source) < si + len(pattern):
            return False

        for idx in range(len(pattern)):
            if pattern[idx] != '?':
                if pattern[idx] != source[si+idx]:
                    return False

        return True

    def isMatch(self, s, p):
        s = '^' + s + '$'
        p = '^' + p + '$'
        patterns = []

        pattern = ''

        for char in p:
            if p == '*':
                if len(pattern) != 0:
                    patterns.append(pattern)
                    pattern = ''
            else :
                pattern += char

        patterns.append(pattern)

        if len(patterns) == 1:
            return self.match(s,p,0)


