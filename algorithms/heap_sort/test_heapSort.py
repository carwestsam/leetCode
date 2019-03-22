from unittest import TestCase

from algorithms.heap_sort.Heap import Heap


class TestHeapSort(TestCase):
    def test_headsort(self):
        hs = Heap()
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], hs.headsort([8, 2, 4, 3, 6, 7, 1, 5]))
