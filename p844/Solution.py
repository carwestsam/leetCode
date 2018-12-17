class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        ss = len(S) - 1
        tt = len(T) - 1

        while ss >= 0 or tt >= 0:
            backspace = 0
            while (S[ss] == '#' or backspace != 0) and ss >= 0:
                if S[ss] == '#':
                    backspace += 1
                elif backspace > 0:
                    backspace -= 1
                ss -= 1

            backspace = 0
            while (T[tt] == '#' or backspace != 0) and tt >= 0:
                if T[tt] == '#':
                    backspace += 1
                elif backspace > 0:
                    backspace -= 1
                tt -= 1

            if ss >= 0 and tt >= 0:
                if S[ss] != T[tt]:
                    return False
                else:
                    ss -= 1
                    tt -= 1
            else:
                break
        if ss == -1 and tt == -1:
            return True
        return False
