from unittest import TestCase
from p23.Solution import Solution, ListNode

class TestSolution(TestCase):
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