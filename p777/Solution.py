class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """

        length = len(start)
        x_start = []
        x_end = []

        for i in range(length):
            if start[i] == 'L':
                x_start.append((0, i))
            elif start[i] == 'R':
                x_start.append((1, i))

            if end[i] == 'L':
                x_end.append((0, i))
            elif end[i] == 'R':
                x_end.append((1, i))

        if len(x_start) != len(x_end):
            return False

        for i in range(len(x_start)):
            if x_start[i][0] != x_end[i][0]:
                return False

            if x_start[i][0] == 0 and x_start[i][1] < x_end[i][1]:
                return False

            if x_start[i][0] == 1 and x_start[i][1] > x_end[i][1]:
                return False

        return True
