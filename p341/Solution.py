

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]]

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()
        [nestedList, i] = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while len(self.stack) > 0:
            [nestedList, i] = self.stack[-1]

            if len(nestedList) == i:
                self.stack.pop()
            else:
                if nestedList[i].isInteger() is True:
                    return True
                else:
                    self.stack[-1][1] += 1
                    self.stack.append([nestedList[i].getList(), 0])
