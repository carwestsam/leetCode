import queue


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


def find(father, x):
    if father[x] == x:
        return x
    else:
        father[x] = find(father, father[x])
        return father[x]


def same(father, x, y):
    return find(father, x) == find(father, y)

def union(father, x, y):
    fx = find(father, x)
    fy = find(father, y)
    if fx == fy:
        return
    else:
        father[fx] = fy


class Kruskal:
    @staticmethod
    def kruskal(edges: [Edge]):
        father = {}
        for edge in edges:
            u = edge.u
            v = edge.v
            father[u] = u
            father[v] = v

        pq = queue.PriorityQueue(len(edges) + 1)
        for edge in edges:
            pq.put((edge.w, edge.u, edge.v))

        ans = 0
        while not pq.empty():
            w, u, v = pq.get()
            if not same(father, u, v):
                union(father, u, v)
                ans += w

        return ans
