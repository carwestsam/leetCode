class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        class Trie:
            def __init__(self):
                self.mark = -1
                self.children = {}

        root = Trie()

        def insert(r, string, value):
            node = r
            pt = 0
            while pt < len(string) and string[pt] in node.children:
                node = node.children[string[pt]]
                pt += 1

            while pt < len(string):
                node.children[string[pt]] = Trie()
                node = node.children[string[pt]]
                pt += 1

            node.mark = value

        for index, w in enumerate(wordDict):
            insert(root, w, index)

        results = []
        current = []
        visited = [False] * (len(s) + 1)
        answers = [[] for _ in range(len(s) + 1)]
        answers[0] = [[-1]]

        s += '#'
        # check avaiable
        visited[0] = True
        for i in range(len(s) - 1):
            if visited[i] != True:
                continue
            node = root
            j = i
            while j < len(s):
                if node.mark >= 0:
                    visited[j] = True
                if s[j] in node.children:
                    node = node.children[s[j]]
                    j += 1
                else:
                    break

        if visited[-1] is False:
            return []

        # combine solutions
        for i in range(len(s) - 1):
            # print(i, len(answers[i]))
            node = root
            j = i
            while j < len(s):
                if node.mark >= 0:
                    # current.append(node.mark)
                    # self.search(j, s, root, current, results, wd)
                    for ii in range(len(answers[i])):
                        answers[j].append(answers[i][ii] + [node.mark])
                    # current.pop()
                if s[j] in node.children:
                    node = node.children[s[j]]
                    j += 1
                else:
                    break

        for ans in answers[-1]:
            results.append(" ".join(wordDict[i] for i in ans[1:]))

        # self.search(0, s + "#", root, current, results, wordDict)

        return results

    def search(self, idx, s, root, current, results, wd):
        if idx == len(s) - 1:
            results.append(" ".join([wd[i] for i in current]))

        node = root
        j = idx
        while j < len(s):
            if node.mark >= 0:
                current.append(node.mark)
                self.search(j, s, root, current, results, wd)
                current.pop()
            if s[j] in node.children:
                node = node.children[s[j]]
                j += 1
            else:
                break
