# 146 LRU Cache

class Node(object):
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # create a hashmap to reach each node in O(1) time
        # create double linkedlist to maintain the order
        
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
        # if key is in our storage
        # change double linkedlist order
        # return value
        # else, simply return -1
        
        if key in self.hashmap:
            node = self.hashmap[key]
            
            # change order
            node.prev.next = node.next
            node.next.prev = node.prev
            
            node.next = self.head.next
            node.prev = self.head
            node.prev.next = node
            node.next.prev = node
            
            return node.val
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        nodeVal = self.get(key)
        # if key exists
        # we update if needed and change the order
        # else, we check the capacity, delete node if needed
        # and insert the new node in
        
        # if key exists
        if nodeVal != -1:
            # value of this key is not equal to the value in the storage
            # we update
            if value != nodeVal:
                self.hashmap[key].val = value
            
            # change order
            node = self.hashmap[key]
            
            node.prev.next = node.next
            node.next.prev = node.prev
            
            node.next = self.head.next
            node.prev = self.head
            
            node.prev.next = node
            node.next.prev = node
            
        else:
            # create a new node
            newNode = Node(key, value)
            
            # check capacity
            # if there is no more room
            # we need to delete the last uncommonly used node
            if self.capacity == 0:
                lastNodeKey = self.tail.prev.key
                
                # delete
                self.tail = self.tail.prev
                self.tail.key = None
                self.tail.val = None
                self.tail.next = None
                
                self.hashmap.pop(lastNodeKey)
                
                # after deleting, we need to increase capacity by 1
                self.capacity += 1
            
            # insert new node
            self.hashmap[key] = newNode
            
            newNode.next = self.head.next
            newNode.prev = self.head
            
            newNode.prev.next = newNode
            newNode.next.prev = newNode
            
            # after insert the new node
            # we need to reduce the capacity by 1
            self.capacity -= 1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)