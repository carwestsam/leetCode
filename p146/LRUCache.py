class ListNode:
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.__array = []
        for i in range(capacity):
            self.__array.append(ListNode(0, 0, 0, 0))
        self.__dict = {}
        self.__head = 0
        self.__capacity = capacity
        self.__size = 0

    def pr(self):

        ans = []
        cnt = 0
        ans.append([self.__array[self.__head].key, self.__array[self.__head].value])
        pt = self.__array[self.__head].right
        while pt != self.__head:
            ans.append([self.__array[pt].key, self.__array[pt].value])
            pt = self.__array[pt].right
            cnt += 1
            if cnt > self.__capacity:
                print ("!! dead loop")
                break

        print(ans)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print ('get', key)
        if self.__capacity <= 0 or key not in self.__dict:
            return -1

        target = self.__dict[key]
        tnode = self.__array[target]

        if self.__size == 1 or target == self.__head:
            return tnode.value

        if self.__size == 2:
            self.__head = target
            return tnode.value

        self.__array[tnode.left].right = tnode.right
        self.__array[tnode.right].left = tnode.left
        head = self.__head
        head_node = self.__array[head]

        tnode.right = head
        tnode.left = head_node.left
        self.__array[head_node.left].right = self.__dict[key]
        head_node.left = target
        self.__head = self.__dict[key]
        return tnode.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.__capacity <= 0:
            return

        if key in self.__dict:
            # print("put: overwrite")
            if self.__size == 1:
                self.__array[self.__head].value = value
                return

            if self.__head == self.__dict[key]:
                self.__array[self.__head].value = value
                return

            head_node = self.__array[self.__head]
            tnode = self.__array[self.__dict[key]]

            self.__array[tnode.left].right = tnode.right
            self.__array[tnode.right].left = tnode.left
            tnode.value = value
            tnode.left = head_node.left
            tnode.right = self.__head
            self.__array[head_node.left].right = self.__dict[key]
            head_node.left = self.__dict[key]
            self.__head = head_node.left
            return

        if self.__size < self.__capacity:
            # print("put insert")
            head_node = self.__array[self.__head]
            self.__array[self.__size] = ListNode(key, value, head_node.left, self.__head)
            self.__array[head_node.left].right = self.__size
            head_node.left = self.__size
            self.__dict[key] = self.__size
            self.__head = self.__size
            self.__size += 1
            return

        # print('clear and input')
        tail = self.__array[self.__head].left
        tail_node = self.__array[tail]
        del self.__dict[tail_node.key]
        tail_node.key = key
        tail_node.value = value
        self.__dict[key] = tail
        self.__head = tail

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
