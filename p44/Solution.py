class Node(object):
    def __init__(self, value):
        self.val = value
        self.next = None

    def solve(self, target):
        if self.val == "*":
            return [self, self.next]
        elif self.val == "?":
            if len(target) == 1:
                return [self.next]
            else :
                return []
        # elif self.val == "$terminal$":
        #     if target == "":
        #         return [self]
        #     else:
        #         return []
        elif self.val == target:
            return [self.next]
        else:
            return []

    @classmethod
    def solveBluk(cls, status, target):
        scope = []
        if target == "":
            scope.extend(status)

        for statu in status:
            scope.extend(statu.solve(target))
        return scope


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
        scope = Node.solveBluk([start], "")

        for char in s:
            scope = Node.solveBluk(scope, char)
            if len(scope) == 0:
                return False

        for statu in scope:
            if statu == terminal:
                return True

        return False
