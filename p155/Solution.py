class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.size = 0
        self.min_val = 0
        self.min_idx = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.size == 0:
            self.stack.append([x, 0])
            self.min_val = x
            self.min_idx = 0

        else:
            self.stack.append([x, self.min_idx])
            if x <= self.min_val:
                self.min_idx = self.size
                self.min_val = x

        self.size += 1

    def pop(self):
        """
        :rtype: void
        """

        [v, idx] = self.stack[-1]
        self.size -= 1
        if v == self.min_val:
            self.min_val = self.stack[idx][0]
            self.min_idx = idx
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """

        if self.size == 0:
            return 0
        else:
            return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
