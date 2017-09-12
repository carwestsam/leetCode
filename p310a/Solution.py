
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        if n == 0:
            return []

        height = [0] * n
        visit = [False] * n
        father = [0] * n
        tree = []
        for ii in range(n):
            tree.append([])

        # print(height, visit, tree)

        for e in edges:
            u = e[0]
            v = e[1]
            # print(u,v)
            tree[u].append(v)
            tree[v].append(u)

        q = []
        q.append(0)
        visit[0] = True
        height[0] = 0

        maxX = 0
        maxIndex = 0


        while len(q) > 0:
            u = q.pop(0)
            if height[u] > maxX:
                maxIndex = u
                maxX = height[u]

            for v in tree[u]:
                if not visit[v]:
                    visit[v] = True
                    q.append(v)
                    height[v] = height[u] + 1



        for ii in range(n):
            visit[ii] = False
            father[ii] = -1
            height[ii] = 0

        q=[]
        q.append(maxIndex)
        visit[maxIndex] = True
        maxX = 0

        while len(q) > 0:
            u = q.pop(0)

            if height[u] > maxX:
                maxIndex = u
                maxX = height[u]

            for v in tree[u]:
                if not visit[v]:
                    visit[v] = True
                    father[v] = u
                    q.append(v)
                    height[v] = height[u] + 1



        targetHeightA = maxX//2
        targetHeightB = (maxX+1)//2

        ans = []
        pt = maxIndex
        while pt != -1:
            if height[pt] == targetHeightA or height[pt] == targetHeightB:
                ans.append(pt)

            pt = father[pt]

        return ans




