import queue


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


class Node:
    def __init__(self):
        self.idx = 0
        self.dist = 0x7fffffff
        self.edges = []
        self.visited = False


class Dijkstra:
    @staticmethod
    def dijkstra(edges, nodes):
        nodes[0].dist = 0
        nodes[0].visited = True
        pq = queue.PriorityQueue(len(edges) + 1)
        for e in nodes[0].edges:
            pq.put((e.w, e.v))

        while not pq.empty():
            d, u = pq.get()
            if nodes[u].visited is False:
                nodes[u].visited = True
                nodes[u].dist = d
            else:
                continue

            for e in nodes[u].edges:
                if e.w + nodes[u].dist < nodes[e.v].dist:
                    nodes[e.v].dist = e.w + nodes[u].dist
                    pq.put((nodes[e.v].dist, e.v))

        return [n.dist for n in nodes]
