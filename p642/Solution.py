class Trie:
    def __init__(self):
        self.children = {}
        self.value = 0
        self.top3 = []

    def find(self, ch):
        if ch not in self.children:
            return None
        else:
            return self.children[ch]

    def insert(self, root, string, time):
        node = root
        index_last_char = None

        for index_char, char in enumerate(string):
            if char in node.children:
                node = node.children[char]
            else:
                index_last_char = index_char
                break

        if index_last_char is not None:
            for char in string[index_last_char:]:
                node.children[char] = Trie()
                node = node.children[char]

        node.value += time

        new_time = node.value
        # print('new ', string, new_time)

        node = root
        for _, char in enumerate(string):
            for i in range(len(node.top3)):
                if node.top3[i][1] == string:
                    node.top3.pop(i)
                    break
            node.top3.append((-new_time, string))
            node.top3.sort()
            if len(node.top3) > 3:
                node.top3.pop()

            node = node.children[char]

        for i in range(len(node.top3)):
            if node.top3[i][1] == string:
                node.top3.pop(i)
                break

        node.top3.append((-new_time, string))
        node.top3.sort()
        # print('sorted', node.top3)
        if len(node.top3) > 3:
            node.top3.pop()


class AutocompleteSystem:

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = Trie()
        self.cache = self.trie
        self.cacheStr = ''
        for sent, time in zip(sentences, times):
            self.trie.insert(self.trie, sent, time)

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """

        if c == '#':
            self.cache = self.trie
            self.trie.insert(self.trie, self.cacheStr, 1)
            self.cacheStr = ''
            return []
        else:
            self.cacheStr += c

        if self.cache is not None:
            self.cache = self.cache.find(c)

        if self.cache is not None:
            # print('ret', self.cache.top3)
            return [a[1] for a in self.cache.top3]
        else:
            return []

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
