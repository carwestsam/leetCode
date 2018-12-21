from unittest import TestCase

from p341.Solution import NestedIterator


class NestedInteger(object):
    def __init__(self, value):
        # self.value = value
        if type(value) == type([]):
            self.value = [NestedInteger(v) for v in value]
        else:
            self.value = value

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        if type(self.value) == type([]):
            return False
        return True

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self.value

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """

        return self.value


class TestNestedIterator(TestCase):
    def test_case(self):
        nestedList = NestedInteger([[1, 1], 2, [1, 1]]).value

        i, v = NestedIterator(nestedList), []
        while i.hasNext():
            v.append(i.next())

        self.assertEqual([1, 1, 2, 1, 1], v)
