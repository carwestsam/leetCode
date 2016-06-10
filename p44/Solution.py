
class Solution(object):
    def match(self, source, pattern, si):

        if len(source) < si + len(pattern):
            return -1

        for idx in range(len(pattern)):
            if pattern[idx] != '?':
                if pattern[idx] != source[si+idx]:
                    return -1

        return si

    def isMatch(self, s, p):
        s = '^' + s + '$'
        p = '^' + p + '$'
        patterns = []

        pattern = ''

        for char in p:
            if char == '*':
                if len(pattern) != 0:
                    patterns.append(pattern)
                    pattern = ''
            else :
                pattern += char

        patterns.append(pattern)

        # single part
        if len(patterns) == 1:
            return self.match(s,p,0)!=-1

        # match header and tail
        startPos = len(patterns[0])
        endPos = len(s) - len(patterns[-1])
        currentResult = (self.match(s,patterns[0], 0) != -1) and (self.match(s, patterns[-1], endPos ) != -1) and startPos <= endPos

        if currentResult == False:
            return False

        pos = startPos
        for pattern in patterns[1:-1]:
            pos = self.findMatch(s, pattern, pos)
            if pos == -1 or pos + len(pattern) > endPos:
                return False
            pos += len(pattern)

        return True

    def findMatch(self, s, pattern, pos):
        for idx in range(pos, len(s) - len(pattern) + 1):
            result = self.match(s, pattern, idx)
            if result != -1:
                return result
        return -1


