# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if root is None:
            return ""

        result = ""
        pt = 0
        stack = [[root, 0]]

        while pt >= 0:
            [node, state] = stack[pt]

            if state == 0:
                symbol = '^'
                if node.left is None and node.right is None:
                    symbol = '*'
                    result += symbol + str(node.val)
                    stack.pop()
                    pt -= 1
                    continue
                elif node.left is None:
                    symbol = '>'
                elif node.right is None:
                    symbol = '<'

                if node.left is None:
                    result += symbol + str(node.val)
                    stack[pt][1] = 1
                else:
                    result += symbol + str(node.val)
                    stack[pt][1] = 1
                    stack.append([node.left, 0])
                    pt += 1

            elif state == 1:
                if node.right is None:
                    stack.pop()
                    pt -= 1
                else:
                    stack[pt][1] = 2
                    stack.append([node.right, 0])
                    pt += 1

            elif state == 2:
                stack.pop()
                pt -= 1

        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if data == '':
            return None

        def read_symbol(ii):
            return data[ii], ii + 1

        def read_value(ii):
            v = 0
            sign = 1
            if data[ii] == '-':
                ii += 1
                sign = -1

            while ii < len(data) and ord('0') <= ord(data[ii]) <= ord('9'):
                v = v * 10 + ord(data[ii]) - ord('0')
                ii += 1

            return sign * v, ii

        i = 0
        result = TreeNode(0)
        stack = [[result, 0]]
        pt = 0

        while i < len(data) and pt >= 0:
            [root, state] = stack[pt]

            if state == 0:
                symbol, i = read_symbol(i)
                val, i = read_value(i)
                root.val = val

                if symbol == '*':
                    stack.pop()
                    pt -= 1
                elif symbol == '>':
                    stack[pt][1] = 1
                elif symbol == '<':
                    stack[pt][1] = 2
                    root.left = TreeNode(0)
                    stack.append([root.left, 0])
                    pt += 1
                elif symbol == '^':
                    stack[pt][1] = 1
                    root.left = TreeNode(0)
                    stack.append([root.left, 0])
                    pt += 1

            elif state == 1:
                stack[pt][1] = 2
                root.right = TreeNode(0)
                stack.append([root.right, 0])
                pt += 1

            elif state == 2:
                stack.pop()
                pt -= 1

        return result

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
