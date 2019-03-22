import unittest

from algorithms.segment_tree.plain_solution import PlainSegmentTree


def print_tree(tree, msg=''):
    arr = []
    for i in range(1, tree.size + 1):
        arr.append(tree.find(i))
    # print(msg, arr)


class TestSegmentTree(unittest.TestCase):
    def test_plain_segment_tree(self):
        tree = PlainSegmentTree(10, 1000)
        # print_tree(tree, msg='init')
        tree.insert(1, 2)
        tree.insert(5, 3)
        # print_tree(tree, msg='value')
        self.assertEqual(2, tree.findMin(1, 4))
        self.assertEqual(3, tree.findMin(3, 7))
        self.assertEqual(1000, tree.findMin(6, 9))
        tree.insert(6, 6)
        self.assertEqual(3, tree.findMin(5,6))
