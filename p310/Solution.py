MAX_NUM = 10000000000
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        tree = self.createTree(n, edges)
        self.calc_minimum_height(tree)

        maxHeight = max( tree[key]["height"] for key in tree )
        ans = [ key for key in tree if tree[key]["height"] == maxHeight ]

        return ans

    def createTree(self, N, E):
        tree = {}
        for i in range(N):
            tree[i] = { "edges": [],
                          "conn": 0,
                          "height": MAX_NUM,
                          "visit": False}

        for e in E:
            tree[e[0]]["edges"].append(e[1])
            tree[e[1]]["edges"].append(e[0])

            tree[e[0]]["conn"] += 1
            tree[e[1]]["conn"] += 1

        return tree

    def get_conn_nodes(self, tree):
        conn_nodes = []
        for k in tree:
            if tree[k]["conn"] == 1:
                conn_nodes.append(k)
                tree[k]["height"] = 1
                tree[k]["visit"] = True
        return conn_nodes

    def calc_minimum_height(self, tree):
        inhand = self.get_conn_nodes(tree)
        while len(inhand) > 0:
            uu = inhand.pop(0)
            u = tree[uu]

            for vv in u["edges"]:
                v = tree[vv]

                if v["height"] > u["height"] + 1:
                    v["height"] = u["height"] + 1

                if v["conn"] > 0:
                    v["conn"] -= 1

                if v["visit"] == False:
                    v["visit"] = True
                    inhand.append(vv)
