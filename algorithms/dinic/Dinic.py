import queue


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.depth = 0
        self.edges = []


class NodeService:
    def __init__(self, size):
        self.nodes = [Node(i) for i in range(size)]
        self.size = size

    def add_edge(self, nodeIdx, edge):
        self.nodes[nodeIdx].edges.append(edge)

    def resetDepth(self):
        for node in self.nodes:
            node.depth = 0x7fffffff

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w
        self.re = None


class EdgeService:
    def __init__(self):
        self.edges = []

    def add_edge(self, u, v, w, nodeService):
        uv = Edge(u, v, w)
        self.edges.append(uv)
        vu = Edge(v, u, 0)
        self.edges.append(vu)
        uv.re = vu
        vu.re = uv
        nodeService.add_edge(u, uv)
        nodeService.add_edge(v, vu)

    def add_edges(self, eList, nodeService):
        for edgeDes in eList:
            [u, v, w] = edgeDes
            self.add_edge(u, v, w, nodeService)


class Dinic:
    def __init__(self):
        pass

    def bfs(self, nodeService: NodeService, start, end):
        nodeService.resetDepth()
        nodes = nodeService.nodes
        nq = queue.Queue(nodeService.size + 2)
        nq.put(nodes[start])
        nodes[start].depth = 0
        while not nq.empty():
            node = nq.get()
            for edge in node.edges:
                if edge.w > 0 and nodes[edge.v].depth > node.depth + 1:
                    v = nodes[edge.v]
                    v.depth = node.depth + 1
                    if v.idx != end:
                        nq.put(v)

        if nodes[end].depth <= len(nodes):
            return True
        else:
            return False

    def dfs(self, node, min_flow, nodes, end):
        if node.idx == end:
            return min_flow
        for edge in node.edges:
            if nodes[edge.v].depth == node.depth + 1 and edge.w > 0:
                cf = self.dfs(nodes[edge.v], min(edge.w, min_flow), nodes, end)
                edge.w -= cf
                edge.re.w += cf
                return cf
        return 0

    def maxFlow(self, nodeService, start, end):
        flow = 0
        while self.bfs(nodeService, start, end):
            while True:
                trans = self.dfs(nodeService.nodes[start], 0x7fffff, nodeService.nodes, end)
                if trans == 0:
                    break
                else:
                    flow += trans
        return flow
