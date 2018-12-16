import json
from unittest import TestCase

from p146.LRUCache import LRUCache
from utils import cpath


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

    def test_should_fix_error(self):
        cache = None
        with open(cpath(__file__, 'error_1.txt')) as file:
            actions = json.loads(file.readline())
            paramlist = json.loads(file.readline())
            for action, params in zip(actions, paramlist):
                if action == 'get':
                    cache.get(params[0])
                elif action == 'put':
                    cache.put(params[0], params[1])
                elif action == 'LRUCache':
                    cache = LRUCache(params[0])

    def test_should_fix_error_2(self):
        self.error_file('error_2.txt')

    def test_should_fix_error_3(self):
        self.error_file('error_3.txt')

    def error_file(self, filename):
        cache = None
        with open(cpath(__file__, filename)) as file:
            actions = json.loads(file.readline())
            param_list = json.loads(file.readline())
            expected_list = json.loads(file.readline())
            for action, params, expected in zip(actions, param_list, expected_list):
                if action == 'get':
                    self.assertEqual(expected, cache.get(params[0]))
                elif action == 'put':
                    cache.put(params[0], params[1])
                elif action == 'LRUCache':
                    cache = LRUCache(params[0])

                # cache.pr()
