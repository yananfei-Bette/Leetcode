# 146 LRU Cache

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):
    # double linked list with hashmap

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:
            node = self.hashmap[key]
            
            node.prev.next = node.next
            node.next.prev = node.prev
            
            node.prev = self.head
            node.next = self.head.next
            
            node.prev.next = node
            node.next.prev = node
            return node.val
        
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        nodeVal = self.get(key)
        # add new node
        if nodeVal == -1:
            newNode = Node(key, value)
            
            if self.capacity == 0:
                temp = self.tail.prev.key
                self.tail = self.tail.prev
                self.tail.key = None
                self.tail.val = None
                self.tail.next = None
                self.hashmap.pop(temp)
                self.capacity += 1
            
            self.hashmap[key] = newNode
            
            newNode.prev = self.head
            newNode.next = self.head.next
            newNode.prev.next = newNode
            newNode.next.prev = newNode
            
            self.capacity -= 1
        
        else:
            # update value
            if nodeVal != value:
                self.hashmap[key].val = value
            
            # order change
            node = self.hashmap[key]
            
            node.prev.next = node.next
            node.next.prev = node.prev
            
            node.prev = self.head
            node.next = self.head.next
            
            node.prev.next = node
            node.next.prev = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)