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
