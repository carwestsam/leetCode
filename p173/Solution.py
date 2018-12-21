# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        self.first = False

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.root is None:
            return False
        if self.first is False:
            return True

        node = self.stack[-1]

        if node.right is not None:
            return True

        else:
            i = len(self.stack) - 1
            while i > 0:
                if self.stack[i - 1].left == self.stack[i]:
                    return True
                i -= 1

            return False

    def next(self):
        """
        :rtype: int
        """
        if self.root is None:
            return None

        if self.first is False:
            self.first = True
            self.stack.append(self.root)
            pt = self.root
            while pt.left is not None:
                self.stack.append(pt.left)
                pt = pt.left
            return pt.val

        elif self.stack[-1].right is not None:
            node = self.stack[-1]
            target = node.right
            self.stack.append(target)
            while target.left is not None:
                self.stack.append(target.left)
                target = target.left
            return target.val
        else:
            target = self.stack.pop()
            while len(self.stack) > 0 and self.stack[-1].right == target:
                target = self.stack.pop()
            if len(self.stack) == 0:
                return None
            return self.stack[-1].val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
