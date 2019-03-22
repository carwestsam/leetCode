from unittest import TestCase

from algorithms.dinic.Dinic import Dinic, NodeService, EdgeService


class TestDinic(TestCase):
    def test_dinic(self):
        nodeService = NodeService(6)
        edgeService = EdgeService()
        edgeService.add_edges(
            [[0, 1, 4],
             [0, 3, 9],
             [3, 1, 1],
             [3, 4, 3],
             [1, 2, 7],
             [2, 5, 9],
             [4, 2, 1],
             [4, 5, 1]
             ]
            , nodeService)
        dinic = Dinic()
        self.assertEqual(7, dinic.maxFlow(nodeService, 0, 5))
