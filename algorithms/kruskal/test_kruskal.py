from unittest import TestCase

from algorithms.kruskal.Kruskal import Edge, Kruskal


class TestKruskal(TestCase):
    def test_kruskal(self):
        edges = [
            Edge(0, 1, 4),
            Edge(0, 7, 8),
            Edge(1, 7, 11),
            Edge(1, 2, 8),
            Edge(7,6,1),
            Edge(7,8,7),
            Edge(2,8,2),
            Edge(2,3,7),
            Edge(2,5,4),
            Edge(8,6,6),
            Edge(6,5,2),
            Edge(3,5,14),
            Edge(3,4,9),
            Edge(5,4,10)
        ]
        self.assertEqual(37, Kruskal.kruskal(edges))
