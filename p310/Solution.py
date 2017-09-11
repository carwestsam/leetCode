class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

    def createTree(self, N, E):
        tree = {}
        for i in range(N):
            tree[i+1] = { "edges": [], "conn": 0 }

        for e in E:
            tree[e[0]]["edges"].append(e[1])
            tree[e[1]]["edges"].append(e[0])

            tree[e[0]]["conn"] += 1
            tree[e[1]]["conn"] += 1

        return tree
