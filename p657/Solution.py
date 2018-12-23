class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        d = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
        for m in moves:
            d[m] += 1

        return d['U'] == d['D'] and d['L'] == d['R']
