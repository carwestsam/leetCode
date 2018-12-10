class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        pairs = []
        n_pairs = []
        ans = 0

        i = 0
        ls = len(s)

        while i < ls:
            if s[i] == '(':
                if i < ls - 1 and s[i + 1] == ')':
                    ans = 2
                    pairs.append((i, i + 1))
                    i += 1
            i += 1

        combined = True

        while combined is True:
            combined = False
            n_pairs = []

            i = 0
            lp = len(pairs)

            while i < lp:
                pair = pairs[i]
                left = pair[0]
                right = pair[1]

                # ( $pair )
                if left > 0 and right < ls - 1 and s[left - 1] == '(' and s[right + 1] == ')':
                    n_pairs.append((left - 1, right + 1))
                    combined = True
                # $pair1 $pair2
                elif i < lp - 1 and right + 1 == pairs[i + 1][0]:
                    n_pairs.append((left, pairs[i + 1][1]))
                    i += 1
                    combined = True
                else:
                    n_pairs.append((left, right))
                i += 1
            if combined is True:
                pairs = n_pairs

        for p in pairs:
            t = p[1] - p[0] + 1
            if t > ans:
                ans = t

        return ans
