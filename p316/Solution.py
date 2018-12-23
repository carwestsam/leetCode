class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        if s == '':
            return ''

        char_dict = {}
        i = len(s) - 1

        while i >= 0:
            char_dict[s[i]] = i
            i -= 1

        first = 27
        first_idx = len(s)
        cha = ord('a')

        visited = set()
        cnt = 0
        j = len(s) - 1
        len_cd = len(char_dict)
        while j >= 0:
            if s[j] not in visited:
                visited.add(s[j])
                cnt += 1

                if cnt == len_cd:
                    break
            j -= 1

        lastPos = j

        for j in range(26):
            ch = chr(j + cha)
            if ch in char_dict and char_dict[ch] <= lastPos:
                first_idx = char_dict[ch]
                first = ch
                break

        sub = ''
        k = first_idx + 1
        while k < len(s):
            if s[k] != first:
                sub += s[k]
            k += 1

        return first + self.removeDuplicateLetters(sub)
