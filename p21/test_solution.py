from unittest import TestCase
from p21.Solution import Solution

class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

def listLike(node):
  l = []
  pt = node
  while pt != None:
    l.append(pt.val)
    pt = pt.next
  return l

def nodeLike(l):
  next = None
  pt = None
  for x in reversed(l):
    pt = ListNode(x)
    pt.next = next
    next = pt
  return pt

class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_should_return_empty_list(self):
    result = self.sol.mergeTwoLists(None, None)
    self.assertEqual(result, None)

  def test_should_return_non_empty_list(self):
    n2 = ListNode(2)
    n1 = ListNode(1)
    n1.next = n2

    self.assertEqual(listLike(self.sol.mergeTwoLists(n1,None)), [1,2])

  def test_should_return_merged_list(self):
    l1 = nodeLike([1,3,5])
    l2 = nodeLike([2,4,6])

    self.assertEqual(listLike(self.sol.mergeTwoLists(l1, l2)), [1,2,3,4,5,6])
