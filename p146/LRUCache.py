class ListNode:
    def __init__(self, key, value, prev, next):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.__head = ListNode(-1, -1, None, None)
        self.__tail = ListNode(-1, -1, None, None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__keyMap = {}
        self.__size = 0
        self.__capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.__capacity <= 0:
            return -1

        if key in self.__keyMap:
            node = self.__keyMap[key]
            value = node.val
            self.__delete(node)
            self.__insert(ListNode(key, value, None, None))
            return value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if key in self.__keyMap:
            node = self.__keyMap[key]
            self.__delete(node)
        elif self.__size == self.__capacity:
            node = self.__tail.prev
            self.__delete(node)

        self.__insert(ListNode(key, value, None, None))

    def __delete(self, target):
        target.next.prev = target.prev
        target.prev.next = target.next

        self.__size -= 1
        del self.__keyMap[target.key]
        del target

    def __insert(self, target):
        target.next = self.__head.next
        self.__head.next.prev = target
        target.prev = self.__head
        self.__head.next = target
        self.__keyMap[target.key] = target
        self.__size += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
