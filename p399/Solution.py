class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        conjunctions = {}
        expanded = {}

        def addConjunction(left, right, value):
            if left not in conjunctions:
                conjunctions[left] = {}

            conjunctions[left][right] = value

        def findPath(left, right):
            if left in expanded:
                return -1.0
            else:
                expanded[left] = True

            destinations = []
            visited = {left: True}

            for dest in conjunctions[left]:
                destinations.append(dest)
                visited[dest] = True

            pt = 0
            while pt != len(destinations):
                for dest in conjunctions[destinations[pt]]:
                    if dest not in visited:
                        visited[dest] = True
                        destinations.append(dest)
                        value = conjunctions[left][destinations[pt]] * conjunctions[destinations[pt]][dest]

                        if dest not in conjunctions[left]:
                            addConjunction(left, dest, value)
                            if value != 0.0:
                                addConjunction(dest, left, 1.0 / value)
                pt += 1

            if right in conjunctions[left]:
                return conjunctions[left][right]
            else:
                return -1

        for equation, value in zip(equations, values):
            addConjunction(equation[0], equation[1], value)
            if value != 0.0:
                addConjunction(equation[1], equation[0], 1.0 / value)

        results = []

        for query in queries:
            a = query[0]
            b = query[1]

            if a not in conjunctions or b not in conjunctions:
                results.append(-1.0)
                continue

            if b in conjunctions[a]:
                results.append(conjunctions[a][b])
            elif a == b and a in conjunctions:
                results.append(1.0)
            else:
                results.append(findPath(a, b))

        return results
