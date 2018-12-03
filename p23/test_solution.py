from unittest import TestCase
from p23.Solution import Solution, ListNode
from random import randint, shuffle

class TestSolution(TestCase):
    def test_should_init_and_pop_a_minimum_heap(self):
        sol = Solution()
        origin = [randint(0, 1000) for _ in range(20)]
        expected = sorted(origin)
        sol.heapInit(origin)
        self.assertEqual(min(origin), origin[0])
        actual = []
        for i in range(20):
            actual.append(sol.heapPop(origin))
        self.assertEqual(expected, actual)

    def test_should_heap_down(self):
        sol = Solution()

        origin = [randint(0, 1000) for _ in range(20)]
        shuffle(origin)

        _input = origin[:10]
        sol.heapInit(_input)
        for i in range(10, 20):
            sol.heapInsert(_input, origin[i])
        expected = sorted(origin)
        actual = []
        for i in range(20):
            actual.append(sol.heapPop(_input))
        self.assertEqual(expected, actual)

    def test_should_sort_with_func(self):
        sol = Solution()

        def mirror(x):
            return - x

        origin = [randint(0, 1000) for _ in range(20)]
        shuffle(origin)

        _input = origin[:10]
        sol.heapInit(_input, mirror)
        for i in range(10, 20):
            sol.heapInsert(_input, origin[i], mirror)

        expected = sorted(origin)
        expected.reverse()
        actual = []
        for i in range(20):
            actual.append(sol.heapPop(_input, mirror))
        self.assertEqual(expected, actual)

    def test_should_return_origin_list(self):
        sol = Solution()
        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n1.next = n2
        n2.next = n3

        ans = sol.mergeKLists([n1])

        self.assertEqual(ans, n1)

    def test_should_return_merged_list(self):
        sol = Solution()
        n11 = ListNode(1)
        n12 = ListNode(3)
        n11.next = n12

        n21 = ListNode(2)
        n22 = ListNode(6)
        n21.next = n22

        n31 = ListNode(4)
        n32 = ListNode(5)
        n31.next = n32

        ans = sol.mergeKLists([n21, n31, n11])

        self.assertEqual(ans, n11)

    def test_special(self):
        sol = Solution()
        ans = sol.mergeKLists([None])
        self.assertEqual(ans, None)
