class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mark = False
        self.children = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        pt = 0
        node = self
        while pt < len(word) and word[pt] in node.children:
            node = node.children[word[pt]]
            pt += 1

        while pt < len(word):
            node.children[word[pt]] = Trie()
            node = node.children[word[pt]]
            pt += 1

        node.mark = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        pt = 0
        node = self
        while pt < len(word) and word[pt] in node.children:
            node = node.children[word[pt]]
            pt += 1

        if pt == len(word) and node.mark is True:
            return True

        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        pt = 0
        node = self
        while pt < len(prefix) and prefix[pt] in node.children:
            node = node.children[prefix[pt]]
            pt += 1

        if pt == len(prefix):
            return True

        return False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)