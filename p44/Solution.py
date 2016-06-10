class Node(object):
    def __init__(self, value):
        self.val = value
        self.next = None

    def solve(self, target):
        if self.val == "?":
            return self.next
        elif self.val == target:
            return self.next
        else:
            return None



class Solution(object):
    def isMatch(self, s, p):

        auto = []
        terminal = Node("$terminal$")

        for char in p:
            node = Node(char)
            auto.append(node)

        auto.append(terminal)

        for idx in range(len(auto)-1):
            auto[idx].next = auto[idx+1]

        start = auto[0]

        for char in s:
            start = start.solve(char)
            if start is None:
                return False

        return start == terminal
