from unittest import TestCase

from p146.LRUCache import LRUCache


class TestLRUCache(TestCase):
    def test_should_set_capacity_of_one(self):
        cache = LRUCache(1)
        cache.put(1, 2)
        self.assertEqual(2, cache.get(1))
        cache.put(1, 1)
        self.assertEqual(1, cache.get(1))
