class UnionFind:
    def __init__(self, size):
        self.f = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if self.f[x] == x:
            return x
        else:
            self.f[x] = self.find(self.f[x])
            return self.f[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)

        if fx == fy:
            return
        else:
            if self.rank[fx] > self.rank[fy]:
                self.f[fy] = fx
                self.rank[fx] += self.rank[fy]
            else:
                self.f[fx] = fy
                self.rank[fy] += self.rank[fx]
