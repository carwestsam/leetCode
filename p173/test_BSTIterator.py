from unittest import TestCase

from p173.Solution import BSTIterator


class T(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class TestBSTIterator(TestCase):
    def test_hasNext(self):
        iter = BSTIterator(T(2, T(1), T(4, T(3), T(5))))
        self.assertEqual(True, iter.hasNext())
        self.assertEqual(1, iter.next())
        self.assertEqual(True, iter.hasNext())
        self.assertEqual(2, iter.next())
        self.assertEqual(True, iter.hasNext())
        self.assertEqual(3, iter.next())
        self.assertEqual(True, iter.hasNext())
        self.assertEqual(4, iter.next())
        self.assertEqual(True, iter.hasNext())
        self.assertEqual(5, iter.next())
        self.assertEqual(False, iter.hasNext())
        self.assertEqual(False, iter.hasNext())
        self.assertEqual(None, iter.next())

    def test_second(self):
        iter = BSTIterator(T(2, T(1)))
        self.assertEqual(True, iter.hasNext())
        self.assertEqual(1, iter.next())
        self.assertEqual(True, iter.hasNext())
        self.assertEqual(2, iter.next())
        self.assertEqual(False, iter.hasNext())
        self.assertEqual(None, iter.next())
