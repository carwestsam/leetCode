class Solution:
    def isCompleteTree(self, root):
        if root is None:
            return True
        size_dict = set()
        self.travel(root, 1, size_dict)
        ln = len(size_dict)
        for i in range(1, ln + 1):
            if i not in size_dict:
                return False

        # print(size_dict)
        return True

    def travel(self, root, idx, d):
        d.add(idx)
        if root.left is not None:
            self.travel(root.left, idx * 2, d)
        if root.right is not None:
            self.travel(root.right, idx * 2 + 1, d)
