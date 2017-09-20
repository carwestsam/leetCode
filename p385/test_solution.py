from unittest import TestCase
from p385.Solution import Solution

class TestSolution(TestCase):
  def setUp(self):
    self.sol = Solution()

  def test_parse_one_nestedInteger(self):
    self.assertEqual(self.sol.python_type_deserialize("123"), 123)
    self.assertEqual(self.sol.python_type_deserialize("-1231"), -1231)

  def test_parse_two_nestedInteger_list(self):
    self.assertEqual(self.sol.python_type_deserialize("[12,34]"), [12,34])
    self.assertEqual(self.sol.python_type_deserialize("[12,[34,-56]]"), [12,[34,-56]])

