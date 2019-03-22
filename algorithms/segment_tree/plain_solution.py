class PlainSegmentTree():
    def __init__(self, size, init):
        self.values = [init] * (size * 4)
        self.minimum = [init] * (size * 4)
        self.maximum = [init] * (size * 4)
        self.size = size

    def insert(self, pos, value):
        self.__insert(value, pos, pos, 1, self.size, 1)

    def findMin(self, targetLeft, targetRight):
        return self.__findMin(targetLeft, targetRight, 1, self.size, 1)

    def __insert(self, value, targetLeft, targetRight, left, right, pt):
        if targetRight < left or right < targetLeft:
            return 1000000, -1
        if targetLeft <= left <= right <= targetRight:
            self.values[pt] = self.minimum[pt] = self.maximum[pt] = value
            return value, value

        mid = (left + right) // 2
        lmin, lmax = self.__insert(value, targetLeft, targetRight, left, mid, pt * 2)
        rmin, rmax = self.__insert(value, targetLeft, targetRight, mid + 1, right, pt * 2 + 1)

        self.minimum[pt] = min(lmin, rmin)
        self.maximum[pt] = max(lmax, rmax)

        if self.minimum[pt] == self.maximum[pt]:
            self.values[pt] = self.minimum[pt]
        else:
            self.values[pt] = -1

        return self.minimum[pt], self.maximum[pt]

    def __findMin(self, tl, tr, l, r, pt):
        if tr < l or r < tl:
            return 1000000
        if tl <= l <= r <= tr:
            return self.minimum[pt]

        mid = (l + r) // 2
        return min(
            self.__findMin(tl, tr, l, mid, pt * 2),
            self.__findMin(tl, tr, mid + 1, r, pt * 2 + 1)
        )
