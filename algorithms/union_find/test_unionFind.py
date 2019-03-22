from unittest import TestCase

from algorithms.union_find.UnionFind import UnionFind


class TestUnionFind(TestCase):
    def test_union_find(self):
        uf = UnionFind(200)
        self.assertFalse(uf.find(1) == uf.find(2))
        uf.union(1, 2)
        self.assertTrue(uf.find(1) == uf.find(2))
        uf.union(3, 4)
        self.assertFalse(uf.find(3) == uf.find(2))
        uf.union(2, 3)
        self.assertTrue(uf.same(1, 4))
