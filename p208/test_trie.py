from unittest import TestCase

from p208.Solution import Trie


class TestTrie(TestCase):
    def test_insert(self):
        trie = Trie()
        trie.insert("apple")
        self.assertEqual(True, trie.search("apple")) # returns
