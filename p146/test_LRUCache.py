from unittest import TestCase

from p146.LRUCache import LRUCache


class TestLRUCache(TestCase):
    def test_should_set_capacity_of_one(self):
        cache = LRUCache(1)
        cache.put(1, 2)
        self.assertEqual(2, cache.get(1))
        cache.put(1, 1)
        self.assertEqual(1, cache.get(1))

    def test_should_return_negative_one_if_not_found(self):
        cache = LRUCache(1)
        cache.put(1, 2)
        self.assertEqual(-1, cache.get(2))

    def test_should_overwrite_least_recently_used_cache(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(2, cache.get(2))
        cache.put(3, 3)
        self.assertEqual(-1, cache.get(1))
        cache.put(1, 3)
        self.assertEqual(3, cache.get(1))
        self.assertEqual(-1, cache.get(2))
        self.assertEqual(3, cache.get(3))

    def test_should_check_example(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(1, cache.get(1))
        cache.put(3, 3)  # evicts key 2
        self.assertEqual(-1, cache.get(2))  # // returns - 1(not found)
        cache.put(4, 4)  # // evicts key 1
        self.assertEqual(-1, cache.get(1))  # // returns - 1(not found)
        self.assertEqual(3, cache.get(3))  # // returns 3
        self.assertEqual(4, cache.get(4))  # // returns 4
