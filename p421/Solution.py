class Trie:
    def __init__(self):
        self.val = -1
        self.children = [None, None]


class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        INT_SIZE = 30

        def insert(root, num):
            node = root

            i = INT_SIZE
            while i >= 0 and node.children[(num >> i) & 1] is not None:
                node = node.children[(num >> i) & 1]
                i -= 1

            while i >= 0:
                cur = (num >> i) & 1
                node.children[cur] = Trie()
                node = node.children[cur]
                i -= 1

            node.val = num

        def findMaxValue(root, num):
            node = root
            for ii in range(INT_SIZE, -1, -1):
                cur = (num >> ii) & 1

                if node.children[cur ^1] is None:
                    node = node.children[cur]
                else:
                    node = node.children[cur ^ 1]


            # print('m', num, node.val)
            return node.val ^ num

        answer = 0
        trie = Trie()
        insert(trie, nums[0])

        for n in nums:
            v = findMaxValue(trie, n)
            insert(trie, n)
            if v > answer:
                answer = v

        return answer
