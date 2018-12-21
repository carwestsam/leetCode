class Trie:
    def __init__(self):
        self.val = 0
        self.children = {}

    def insert(self, word):
        node = self
        i = 0

        while i < len(word) and word[i] in node.children:
            node = node.children[word[i]]
            i += 1

        while i < len(word):
            node.children[word[i]] = Trie()
            node = node.children[word[i]]
            i += 1

        node.val += 1


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        visited = [False] * (len(s) + 10)
        visited[0] = True
        queue = [0]
        len_s = len(s)

        def expand(start_idx, v, q):
            node = trie
            for i in range(start_idx, len_s + 1):
                if node.val > 0 and v[i] is False:
                    v[i] = True
                    q.append(i)

                if i < len_s and s[i] in node.children:
                    node = node.children[s[i]]
                else:
                    break

        while len(queue) > 0 and visited[len_s] is False:
            last = queue.pop()
            expand(last, visited, queue)

        return visited[len(s)]
