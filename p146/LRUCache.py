class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.__dict = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        return self.__dict[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.__dict[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
