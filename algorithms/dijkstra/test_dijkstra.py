from unittest import TestCase

from algorithms.dijkstra.dijkstra import Edge, Node, Dijkstra


class TestDijkstra(TestCase):
    def test_dijkstra(self):
        edges = [
            Edge(0, 1, 5),
            Edge(0, 2, 1),
            Edge(2, 1, 2),
            Edge(1, 3, 3),
            Edge(2, 3, 4)
        ]
        nodes = [Node() for _ in range(4)]
        nodes[0].edges = [edges[0], edges[1]]
        nodes[1].edges = [edges[3]]
        nodes[2].edges = [edges[2], edges[4]]

        self.assertEqual([0, 3, 1, 5], Dijkstra.dijkstra(edges, nodes))
